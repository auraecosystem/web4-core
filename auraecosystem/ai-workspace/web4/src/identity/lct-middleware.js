// auraecosystem/ai-workspace/web4/src/identity/lct-middleware.js
const { LctParser } = require('./lct-parser');

const parser = new LctParser({ strictMode: true, minTrustBoundary: 0.5 });

/**
 * Web4 Network Gatekeeper Middleware
 * Intercepts incoming requests and evaluates trust/metabolic thresholds.
 */
function protectWeb4Route(req, res, next) {
  // 1. Extract token from Authorization header or custom Web4 field
  const authHeader = req.headers['authorization'] || req.headers['x-web4-lct'];
  
  if (!authHeader) {
    return res.status(401).json({
      error: "Missing Identity Vector",
      message: "Requests to trust-native routes require a valid Linked Context Token (LCT)."
    });
  }

  // Handle standard "Bearer <token>" formatting if present
  const token = authHeader.startsWith('Bearer ') ? authHeader.split(' ')[1] : authHeader;

  try {
    // 2. High-Performance Fast Extract to check for immediate metabolic exhaustion
    const baselineMetabolism = parser.fastExtractMetabolism(token);
    if (baselineMetabolism.atp <= 0) {
      return res.status(402).json({
        error: "Metabolic Exhaustion",
        message: "Your agent's ATP budget is depleted. Transaction dropped via economic physics constraint."
      });
    }

    // 3. Perform deep multidimensional decoding and verification checks
    const parsedLCT = parser.parse(token);

    if (!parsedLCT.isValid) {
      return res.status(403).json({
        error: "Identity Structural Fracture",
        message: "Geometric coherence check failed. Relational or spatial validation broke threshold rules."
      });
    }

    if (!parsedLCT.isAlive) {
      return res.status(403).json({
        error: "Phase Transition Lockdown",
        message: "Agent Trust Tensor (T3) average has crossed below the critical 0.5 operational boundary."
      });
    }

    // 4. Attach verified trust-native identity state parameters to the request context
    req.web4Agent = parsedLCT;
    
    // Process request cleanly
    next();
  } catch (error) {
    return res.status(400).json({
      error: "Malformed Token Packet",
      message: error.message
    });
  }
}

module.exports = { protectWeb4Route };
