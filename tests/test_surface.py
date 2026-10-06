from pathlib import Path

HTML = (Path(__file__).parents[1] / 'docs' / 'index.html').read_text()

def test_complete_browser_surface():
 for item in ('id="connect"', 'id="create"', 'id="trace"', 'id="settle"', 'id="consume"', 'id="load"', 'id="demo"', 'FINALIZED', 'get_circuit', 'settle_circuit', 'consume_action', 'sourceAuthority', 'targetAuthority', 'beneficiary', 'consequence'):
  assert item in HTML

def test_graph_identity():
 assert 'class="map-stage"' in HTML
 assert 'class="composer"' in HTML
 assert 'AUTHORITY-BOUND PROTOCOL GATE' in HTML
