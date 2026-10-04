import json, re, time
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet
from genlayer_py.types import TransactionStatus

ROOT = Path(__file__).parents[1]
ENV = (ROOT.parents[3] / 'accounts.env').read_text()
ADDRESS = json.loads((ROOT / 'deployment.json').read_text())['contractAddress']
def account(number):
 key = re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', ENV, re.M).group(1).strip()
 return create_account(account_private_key=key)
def client(number): return create_client(chain=studionet, account=account(number))
def write(number, name, args):
 c = client(number); tx = c.write_contract(address=ADDRESS, function_name=name, args=args); print(name + '_tx=' + str(tx), flush=True)
 receipt = c.wait_for_transaction_receipt(transaction_hash=tx, status=TransactionStatus.FINALIZED, retries=180, interval=5000, full_transaction=True)
 leader = (receipt.get('consensus_data', {}).get('leader_receipt') or [{}])[0]
 assert receipt.get('result_name') == 'MAJORITY_AGREE' and leader.get('execution_result') == 'SUCCESS'
 return str(tx)
circuit_id = 'CIRCUIT-' + str(int(time.time()))
source = 'https://raw.githubusercontent.com/warnedwarn/citation-circuit/main/docs/evidence/source-note.md'
target = 'https://cdn.jsdelivr.net/gh/warnedwarn/citation-circuit@main/docs/evidence/target-handbook.md'
transactions = {}
transactions['create'] = write(2, 'create_circuit', [circuit_id, 'Harbor access references'])
transactions['first'] = write(3, 'trace_link', [circuit_id, 'EDGE-A-' + str(int(time.time())), source, target])
transactions['second'] = write(3, 'trace_link', [circuit_id, 'EDGE-B-' + str(int(time.time())), target, source])
transactions['seal'] = write(2, 'seal_circuit', [circuit_id])
state = client(2).read_contract(address=ADDRESS, function_name='get_circuit', args=[circuit_id])
assert state['state'] == 'SEALED' and len(state['edges']) == 2
proof = {'circuitId':circuit_id,'transactions':transactions,'state':state,'fixtureDisclosure':'Wallets and evidence pages are operator-controlled fixtures.'}
(ROOT / 'evidence').mkdir(exist_ok=True); (ROOT / 'evidence' / 'live-run.json').write_text(json.dumps(proof, indent=2) + '\n')
print(json.dumps(proof, indent=2), flush=True)
