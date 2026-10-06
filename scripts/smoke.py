import json, os, re, time
from pathlib import Path
from genlayer_py import create_account, create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions

def calldata_compat(method=None, args=None, kwargs=None):
 out = {}
 if method is not None: out['method'] = method
 if args: out['args'] = args
 if kwargs: out['kwargs'] = kwargs
 return out

contract_actions.make_calldata_object = calldata_compat
ROOT = Path(__file__).parents[1]
ENV = (ROOT.parents[3] / 'accounts.env').read_text()
ADDRESS = json.loads((ROOT / 'deployment.json').read_text())['contractAddress']
def account(number):
 key = re.search(rf'^ACCOUNT_{number}_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)', ENV, re.M).group(1).strip()
 return create_account(account_private_key=key)
def client(number): return create_client(chain=studionet, account=account(number))
def write(number, name, args):
 c = client(number); tx = c.write_contract(address=ADDRESS, function_name=name, args=args); print(name + '_tx=' + str(tx), flush=True)
 receipt = c.wait_for_transaction_receipt(transaction_hash=tx, wait_until='finalized', retries=180, interval=5000, full_transaction=True)
 leader = (receipt.get('consensus_data', {}).get('leader_receipt') or [{}])[0]
 assert receipt.get('result_name') == 'MAJORITY_AGREE' and leader.get('execution_result') == 'SUCCESS'
 return str(tx)
circuit_id = os.environ.get('CIRCUIT_ID') or 'CIRCUIT-' + str(int(time.time()))
source = 'https://raw.githubusercontent.com/warnedwarn/citation-circuit/main/docs/evidence/source-note.md'
target = 'https://cdn.jsdelivr.net/gh/warnedwarn/citation-circuit@main/docs/evidence/target-handbook.md'
beneficiary = account(2).address
transactions = {
 'approveSource': write(2, 'approve_authority', ['RAW_NOTE','Repository source note','https://raw.githubusercontent.com/warnedwarn/citation-circuit/']),
 'approveTarget': write(2, 'approve_authority', ['CDN_HANDBOOK','Repository target handbook','https://cdn.jsdelivr.net/gh/warnedwarn/citation-circuit@main/docs/evidence/']),
 'create': write(2, 'create_circuit', [circuit_id,'Harbor handbook release gate','SUMMARIZES',1,beneficiary,'Release the approved handbook package to the named beneficiary']),
 'trace': write(2, 'trace_link', [circuit_id,'EDGE-'+str(int(time.time())),'RAW_NOTE',source,'CDN_HANDBOOK',target]),
 'settle': write(2, 'settle_circuit', [circuit_id]),
 'consume': write(2, 'consume_action', [circuit_id])
}
state = client(2).read_contract(address=ADDRESS, function_name='get_circuit', args=[circuit_id])
assert state['state'] == 'CONSUMED' and state['decision'] == 'AUTHORIZED' and state['matched_count'] == 1
proof = {'circuitId':circuit_id,'transactions':transactions,'state':state,'fixtureDisclosure':'The approved authorities, wallet, and evidence pages are operator-controlled fixtures used to prove neutral relation settlement and one-time action consumption.'}
(ROOT / 'evidence').mkdir(exist_ok=True); (ROOT / 'evidence' / 'live-run.json').write_text(json.dumps(proof, indent=2) + '\n')
print(json.dumps(proof, indent=2), flush=True)
