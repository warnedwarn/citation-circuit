# CITATION CIRCUIT / FIELD ATLAS

Document relationships now operate a protocol gate. Citation Circuit asks validators to settle how one approved authority record relates to another, then deterministic policy code uses that result to authorize or deny a named downstream action.

## Graph law

Only the deployment governor can register source authorities. Every document URL must match its authority's normalized HTTPS origin and directory prefix. Anyone may trace a directed link between two distinct approved authorities. Validators retrieve both complete responses and agree on exactly one closed relationship: `CITES`, `QUOTES`, `SUMMARIZES`, or `NO_LINK`. The contract stores the authority IDs, ordered source digests, contributor, and result.

At creation, the caller freezes a required relationship, required match count, beneficiary, and concrete consequence. Permissionless settlement counts the audited edges that match the frozen relationship and stores `AUTHORIZED` or `DENIED`. Only the beneficiary can consume an authorized action, and only once. Relationship consensus is therefore necessary to a concrete state transition rather than decorative metadata.

## Cartographic interface

The browser remains a spatial map. A composer attaches approved source and target authorities, while the map renders the finalized relation beside the frozen policy. The complete flow opens a gate, traces a link, waits for `FINALIZED`, settles the policy, and consumes the authorized action.

## Local checks

```text
python -m pytest -q
genvm-lint check contracts/contract.py
```

The included authorities, records, and wallets are operator-controlled technical fixtures. They demonstrate enforcement and are not represented as independent publishers.

## Survey coordinates

- Public atlas: https://citation-circuit.pages.dev/
- Source repository: https://github.com/warnedwarn/citation-circuit
- StudioNet contract: `0xF44145fE227e268437dCbfA49B9FC05E92A0Ce1E`
- Verified live circuit: `CIRCUIT-1791084135` — `SEALED`, two independently finalized edges
- Canonical-site replay: `CIRCUIT-1791085026062` — `SEALED`, relations `SUMMARIZES` and `CITES`

Exact deployment, lifecycle, browser-run, and digest records live in `deployment.json` and `evidence/`.
