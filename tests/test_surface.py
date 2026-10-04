from pathlib import Path

HTML = (Path(__file__).parents[1] / 'docs' / 'index.html').read_text()

def test_complete_browser_surface():
 for item in ('id="connect"', 'id="create"', 'id="trace"', 'id="seal"', 'id="load"', 'id="demo"', 'FINALIZED', 'get_circuit'):
  assert item in HTML

def test_graph_identity():
 assert 'class="map-stage"' in HTML
 assert 'class="composer"' in HTML
 assert 'VERIFIED REFERENCE GRAPH' in HTML
