import ast
from pathlib import Path

SOURCE = (Path(__file__).parents[1] / 'contracts' / 'contract.py').read_text()
TREE = ast.parse(SOURCE)

def test_public_surface():
 for name in ('approve_authority', 'create_circuit', 'trace_link', 'settle_circuit', 'consume_action', 'get_authority', 'get_circuit'):
  assert f'def {name}' in SOURCE

def test_closed_relation_vocabulary():
 assert "RELATIONS = ('CITES','QUOTES','SUMMARIZES','NO_LINK')" in SOURCE
 assert 'bounded relation required' in SOURCE

def test_validator_binds_relation_and_digests():
 assert 'exact closed relation and both ordered full-response digests must match' in SOURCE
 assert "result['source_digest']" in SOURCE and "result['target_digest']" in SOURCE

def test_graph_guards_are_enforced():
 assert 'source_origin==target_origin' in SOURCE
 assert 'pair_key in self.pairs' in SOURCE
 assert 'edge_key in self.edges' in SOURCE

def test_authority_registry_binds_each_endpoint():
 assert 'governor authority required' in SOURCE
 assert 'source must match its approved authority' in SOURCE
 assert 'source_id==target_id' in SOURCE

def test_neutral_relation_settles_concrete_protocol_action():
 assert "matched=sum(1 for edge_id in edge_ids if self.edges[edge_id].relation==circuit.required_relation)" in SOURCE
 assert "circuit.decision='AUTHORIZED' if matched>=int(circuit.required_count) else 'DENIED'" in SOURCE
 consume = SOURCE[SOURCE.index('def consume_action'):SOURCE.index('def get_authority')]
 assert 'beneficiary required' in consume and "circuit.state!='SETTLED'" in consume
 assert "circuit.state='CONSUMED'" in consume
