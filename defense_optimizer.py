import random

class DefenseOptimizer:
    def __init__(self):
        # Initial Bank State (Part 1 & 2)
        self.nodes = {
            "ATM_1": {"security": 3, "criticality": 5, "zone": "Edge"},
            "Mobile_Gateway": {"security": 5, "criticality": 7, "zone": "Edge"},
            "Teller_Sys": {"security": 6, "criticality": 6, "zone": "Internal"},
            "Core_DB": {"security": 10, "criticality": 10, "zone": "Core"},
            "SWIFT_Node": {"security": 9, "criticality": 10, "zone": "Core"}
        }
        self.budget = 1000  # Total Defense Credits
        self.upgrade_cost = 100 # Cost to increase security by 1 level

    def optimize_defenses(self):
        """
        Algorithm: Allocates budget based on 'Risk Score' 
        Risk Score = Criticality / Security
        """
        print(f"💰 Starting Budget: {self.budget} Credits")
        print("🤖 Running Optimization Algorithm...")

        # Keep spending until budget is gone or security is maxed
        while self.budget >= self.upgrade_cost:
            # Calculate Risk for each node
            # We want to upgrade nodes with HIGH criticality but LOW security
            target_node = None
            highest_risk = -1

            for name, info in self.nodes.items():
                risk_score = info["criticality"] - info["security"]
                if risk_score > highest_risk and info["security"] < 15:
                    highest_risk = risk_score
                    target_node = name

            if target_node:
                self.nodes[target_node]["security"] += 1
                self.budget -= self.upgrade_cost
                print(f"🛡️ Upgraded {target_node} to Level {self.nodes[target_node]['security']}")
            else:
                break

        print(f"✅ Optimization Complete. Remaining Budget: {self.budget}")

    def display_finances(self):
        print(f"\n{'NODE':<20} | {'CRITICALITY':<12} | {'SECURITY LEVEL'}")
        print("-" * 50)
        for name, info in self.nodes.items():
            print(f"{name:<20} | {info['criticality']:<12} | Lvl {info['security']}")

# --- EXECUTION ---
if __name__ == "__main__":
    bank_admin = DefenseOptimizer()
    
    print("--- PRE-OPTIMIZATION STATUS ---")
    bank_admin.display_finances()

    bank_admin.optimize_defenses()

    print("\n--- POST-OPTIMIZATION STATUS ---")
    bank_admin.display_finances()