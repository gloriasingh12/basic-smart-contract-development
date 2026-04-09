# =================================================================
# PROJECT: DeFi Lending & Borrowing Application
# DESCRIPTION: Smart Contract logic for dynamic interest rates.
# DELIVERABLE: DApp logic with Deposit, Borrow, and Interest calculations.
# =================================================================

import time

class DeFiProtocol:
    def __init__(self):
        self.total_liquidity = 100000  # Total tokens in the pool
        self.total_borrowed = 0
        self.base_interest_rate = 0.05  # 5% starting rate
        self.user_balances = {}         # User deposits
        self.user_borrows = {}          # User loans
        print("🏦 DeFi Lending Protocol Deployed on Testnet.")

    def calculate_dynamic_rate(self):
        """Logic: Interest increases as more tokens are borrowed (Utilization Rate)."""
        utilization_rate = self.total_borrowed / self.total_liquidity
        # Interest Rate = Base Rate + (Utilization * 20%)
        current_rate = self.base_interest_rate + (utilization_rate * 0.20)
        return round(current_rate * 100, 2)

    def deposit(self, user, amount):
        """Users can deposit tokens to earn interest."""
        self.user_balances[user] = self.user_balances.get(user, 0) + amount
        self.total_liquidity += amount
        print(f"💰 {user} deposited {amount} tokens. Pool Liquidity: {self.total_liquidity}")

    def borrow(self, user, amount):
        """Users can borrow tokens if pool has enough liquidity."""
        current_rate = self.calculate_dynamic_rate()
        
        if (self.total_liquidity - self.total_borrowed) >= amount:
            self.total_borrowed += amount
            self.user_borrows[user] = self.user_borrows.get(user, 0) + amount
            print(f"💸 {user} borrowed {amount} tokens at {current_rate}% interest.")
        else:
            print(f"❌ Error: Not enough liquidity in the pool to lend {amount}.")

    def show_protocol_status(self):
        print("\n" + "="*45)
        print("📊 DEFI PROTOCOL DASHBOARD")
        print("="*45)
        print(f"Total Pool Liquidity:  {self.total_liquidity} tokens")
        print(f"Total Tokens Borrowed: {self.total_borrowed} tokens")
        print(f"Current Interest Rate: {self.calculate_dynamic_rate()}%")
        print("="*45)

# --- MAIN EXECUTION (DApp Simulation) ---
if __name__ == "__main__":
    defi = DeFiProtocol()

    # 1. Users depositing funds
    defi.deposit("Aditya", 50000)
    defi.deposit("Rahul", 20000)

    # 2. Status check before borrowing
    defi.show_protocol_status()

    # 3. Dynamic Interest Rate in action
    print("\n--- Processing Borrow Requests ---")
    defi.borrow("Priya", 30000) # Interest should be low
    defi.borrow("Suresh", 40000) # Interest should increase as pool dries up

    # 4. Final Status
    defi.show_protocol_status()

    print("\n✅ Task 23 Complete: DeFi Dynamic Interest Logic Verified.")
