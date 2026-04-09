# =================================================================
# PROJECT: Private Blockchain Implementation
# DESCRIPTION: Permissioned Ledger with Membership Service Provider (MSP).
# DELIVERABLE: Blockchain config logic, Chaincode simulation, and DApp.
# =================================================================

import hashlib
import json
from datetime import datetime

class PrivateBlockchain:
    def __init__(self):
        self.chain = []
        self.authorized_peers = ["Org1_Admin", "Org2_Admin"] # MSP Logic
        self.pending_transactions = []
        # Create Genesis Block
        self.create_block(previous_hash="0"*64, proof=100)
        print("⛓️ Private Enterprise Blockchain Initialized.")

    def authorize_peer(self, identity):
        """Membership Service Provider (MSP) check."""
        return identity in self.authorized_peers

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.now()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def execute_chaincode(self, sender, receiver, asset_id, identity):
        """Simulating Hyperledger Chaincode (Smart Contract)."""
        if not self.authorize_peer(identity):
            print(f"🚫 Access Denied: Peer {identity} is not authorized on this network!")
            return False

        transaction = {
            'sender': sender,
            'receiver': receiver,
            'asset': asset_id,
            'status': 'COMMITTED'
        }
        self.pending_transactions.append(transaction)
        print(f"📦 Chaincode Executed: Asset {asset_id} transferred to {receiver}.")
        return True

    def get_last_block(self):
        return self.chain[-1]

# --- MAIN EXECUTION (Private Network Simulation) ---
if __name__ == "__main__":
    hyperledger = PrivateBlockchain()

    # 1. Authorized Transaction (Org1 Admin)
    print("\n--- Transaction 1: Authorized ---")
    hyperledger.execute_chaincode("SupplyChain_Dept", "Logistics_Dept", "Asset_ID_9901", "Org1_Admin")
    
    # 2. Mining/Committing the block
    last_hash = hashlib.sha256(json.dumps(hyperledger.get_last_block(), sort_keys=True).encode()).hexdigest()
    hyperledger.create_block(proof=200, previous_hash=last_hash)

    # 3. Unauthorized Transaction Attempt (Hacker/Guest)
    print("\n--- Transaction 2: Unauthorized ---")
    hyperledger.execute_chaincode
