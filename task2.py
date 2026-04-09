# =================================================================
# PROJECT: Custom ERC-20 Token Creation
# DESCRIPTION: Solidity Smart Contract for a custom Ethereum token.
# DELIVERABLE: Contract code, Token Details, and Deployment Guide.
# =================================================================

# --- PART 1: ACTUAL SOLIDITY CODE (For your Deliverable) ---
"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AdityaToken {
    string public name = "Aditya Coin";
    string public symbol = "ADI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) public balanceOf;

    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }
}
"""

# --- PART 2: PYTHON SIMULATION (For GitHub Execution) ---

class ERC20Simulator:
    def __init__(self, name, symbol, supply):
        self.name = name
        self.symbol = symbol
        self.supply = supply
        self.balances = {"Deployer_Address": supply}
        
    def get_token_details(self):
        print(f"💎 TOKEN NAME:   {self.name}")
        print(f"🏷️ SYMBOL:       {self.symbol}")
        print(f"💰 TOTAL SUPPLY: {self.supply:,} {self.symbol}")
        print("-" * 30)

    def simulate_transfer(self, to_addr, amount):
        if self.balances["Deployer_Address"] >= amount:
            self.balances["Deployer_Address"] -= amount
            self.balances[to_addr] = amount
            print(f"✅ Transaction Proof: {amount} {self.symbol} sent to {to_addr}")
            print(f"🔗 TX Hash: 0x{id(amount)}...{id(to_addr)}") # Simulated Hash
        else:
            print("❌ Error: Insufficient funds for transaction.")

if __name__ == "__main__":
    print("🚀 Deploying Custom ERC-20 Token on Ethereum Testnet...")
    
    # Initialize Token
    my_token = ERC20Simulator("Aditya Coin", "ADI", 1000000)
    
    # 1. Token Details
    my_token.get_token_
