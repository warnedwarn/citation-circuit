# Readiness matrix

| Requirement | Proof target | Status |
|---|---|---|
| Neutral authority boundary | Governor registry plus origin and path-prefix binding for both distinct endpoints | PASS source, deployment pending |
| Auditable settled relationship | Relation, authority IDs, ordered URLs, and ordered full-response digests are stored per edge | PASS tests |
| Concrete downstream necessity | Frozen relation threshold determines `AUTHORIZED` or `DENIED`; only beneficiary can consume once | PASS tests, deployment pending |
| Unique graph edges | Authority-pair and edge replay guards | PASS tests |
| Complete lifecycle | approve authorities, create gate, trace, settle, consume, and read | UNVERIFIED |
| Deployed source match | new manifest and fetched-source digest | UNVERIFIED |
| Public browser workflow | canonical Cloudflare flow against corrected deployment | UNVERIFIED |
