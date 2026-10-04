# CITATION CIRCUIT / FIELD ATLAS

Documents do not live alone. One quotes another, a bulletin summarizes a handbook, and a policy cites an earlier decision. Citation Circuit makes those relationships inspectable as a growing public graph.

## Graph law

Anyone may propose a directed link between documents on distinct HTTPS origins. Validators retrieve both complete responses and agree on exactly one closed relationship: `CITES`, `QUOTES`, `SUMMARIZES`, or `NO_LINK`. The contract stores the ordered source digests, normalized origins, contributor, and result. A reused origin pair cannot be replayed inside the same circuit.

The graph has no artificial winner. It stays `ACTIVE` while contributors trace edges. After at least two edges, only the creator may seal the map. Existing edges remain readable after sealing.

## Cartographic interface

The browser is a spatial map, not a contract argument grid. A composer attaches a source node to a target node, while the map renders finalized edges as labeled routes. The full demo creates one circuit, traces two different origin pairs, waits for each transaction to reach `FINALIZED`, and seals the resulting graph.

## Local checks

```text
python -m pytest -q
genvm-lint check contracts/contract.py
```

The included web records and temporary wallets are operator-controlled technical fixtures.
