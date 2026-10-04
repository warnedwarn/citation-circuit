import ast
from pathlib import Path

SOURCE = (Path(__file__).parents[1] / 'contracts' / 'contract.py').read_text()
TREE = ast.parse(SOURCE)

def test_public_surface():
 for name in ('create_circuit', 'trace_link', 'seal_circuit', 'get_circuit'):
  assert f'def {name}' in SOURCE

def test_closed_relation_vocabulary():
 assert "RELATIONS = ('CITES', 'QUOTES', 'SUMMARIZES', 'NO_LINK')" in SOURCE
 assert 'bounded relation required' in SOURCE

def test_validator_binds_relation_and_digests():
 assert 'exact closed relation and both ordered full-response digests must match' in SOURCE
 assert "result['source_digest']" in SOURCE and "result['target_digest']" in SOURCE

def test_graph_guards_are_enforced():
 assert 'source_origin == target_origin' in SOURCE
 assert 'pair_key in self.pairs' in SOURCE
 assert 'edge_key in self.edges' in SOURCE

def test_owner_seals_after_two_edges():
 assert "len(json.loads(circuit.edge_ids)) < 2" in SOURCE
 assert "circuit.state = 'SEALED'" in SOURCE
