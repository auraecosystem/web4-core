createdb gucs && \
pg_restore -d gucs -x -O -U postgres gucs.pgdump && \
node script.odp
