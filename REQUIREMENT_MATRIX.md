# Readiness matrix

| Requirement | Proof target | Status |
|---|---|---|
| Neutral authority boundary | Governor registry plus origin and path-prefix binding for both distinct endpoints | PASS source + live |
| Auditable settled relationship | Relation, authority IDs, ordered URLs, and ordered full-response digests are stored per edge | PASS tests |
| Concrete downstream necessity | Frozen relation threshold determines `AUTHORIZED` or `DENIED`; only beneficiary can consume once | PASS tests + live |
| Unique graph edges | Authority-pair and edge replay guards | PASS tests |
| Complete lifecycle | approve authorities, create gate, trace, settle, consume, and read | PASS (`CIRCUIT-1791257575`) |
| Deployed source match | new manifest and fetched-source digest | PASS |
| Public browser workflow | canonical Cloudflare flow against corrected deployment, with complete controls and no console errors | PASS |
