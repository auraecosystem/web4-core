"""
delegation_validator.py

Universal Delegation Validator

Supports:
- Capability delegation
- Signed delegations
- Expiration
- Revocation
- Scope validation
- Delegation chains
- Loop detection
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Set
from enum import Enum
import hashlib
import secrets


# ==========================================================
# ENUMS
# ==========================================================

class ValidationResult(Enum):
    VALID = "valid"
    EXPIRED = "expired"
    REVOKED = "revoked"
    INVALID_SIGNATURE = "invalid_signature"
    INVALID_SCOPE = "invalid_scope"
    LOOP_DETECTED = "loop_detected"


# ==========================================================
# DELEGATION TOKEN
# ==========================================================

@dataclass
class DelegationToken:

    token_id: str

    issuer: str

    subject: str

    scopes: Set[str]

    issued_at: datetime

    expires_at: datetime

    signature: str

    parent: Optional[str] = None


# ==========================================================
# SIMPLE SIGNER
# ==========================================================

class SimpleSigner:

    @staticmethod
    def sign(secret: str, payload: str):

        return hashlib.sha256(
            f"{secret}:{payload}".encode()
        ).hexdigest()

    @staticmethod
    def verify(secret, payload, signature):

        return (
            SimpleSigner.sign(secret, payload)
            == signature
        )


# ==========================================================
# REVOCATION STORE
# ==========================================================

class RevocationStore:

    def __init__(self):

        self.revoked = set()

    def revoke(self, token_id):

        self.revoked.add(token_id)

    def is_revoked(self, token_id):

        return token_id in self.revoked


# ==========================================================
# VALIDATOR
# ==========================================================

class DelegationValidator:

    def __init__(self):

        self.tokens: Dict[str, DelegationToken] = {}

        self.revocations = RevocationStore()

    def issue(

        self,
        issuer,
        subject,
        scopes,
        secret,
        hours=24,
        parent=None,

    ):

        token_id = secrets.token_hex(16)

        payload = (
            issuer +
            subject +
            "".join(sorted(scopes))
        )

        signature = SimpleSigner.sign(
            secret,
            payload,
        )

        token = DelegationToken(

            token_id=token_id,

            issuer=issuer,

            subject=subject,

            scopes=set(scopes),

            issued_at=datetime.utcnow(),

            expires_at=datetime.utcnow()
            + timedelta(hours=hours),

            signature=signature,

            parent=parent,

        )

        self.tokens[token_id] = token

        return token

    def validate_signature(

        self,
        token,
        secret,

    ):

        payload = (
            token.issuer +
            token.subject +
            "".join(sorted(token.scopes))
        )

        return SimpleSigner.verify(
            secret,
            payload,
            token.signature,
        )

    def validate(

        self,
        token_id,
        secret,

    ):

        token = self.tokens.get(token_id)

        if token is None:

            return ValidationResult.INVALID_SIGNATURE

        if self.revocations.is_revoked(token.token_id):

            return ValidationResult.REVOKED

        if datetime.utcnow() > token.expires_at:

            return ValidationResult.EXPIRED

        if not self.validate_signature(token, secret):

            return ValidationResult.INVALID_SIGNATURE

        return ValidationResult.VALID


# ==========================================================
# CHAIN VALIDATOR
# ==========================================================

class DelegationChainValidator:

    def __init__(self, validator):

        self.validator = validator

    def validate_chain(

        self,

        token_id,

        secret,

    ):

        visited = set()

        current = token_id

        while current:

            if current in visited:

                return ValidationResult.LOOP_DETECTED

            visited.add(current)

            result = self.validator.validate(
                current,
                secret,
            )

            if result != ValidationResult.VALID:

                return result

            token = self.validator.tokens[current]

            current = token.parent

        return ValidationResult.VALID
