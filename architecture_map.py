import random
import time

class BankArchitecture:
    def __init__(self):
        # PART 1: Nodes and Connections
        self.nodes = {
            "ATM_1": {"status": "Healthy", "security_level": 3, "zone": "Edge"},
            "Mobile_Gateway": {"status": "Healthy", "security_level": 5, "zone": "Edge"},
            "Teller_Sys": {"status": "Healthy", "security_level": 6, "zone": "Internal"},
            "Core_DB": {"status": "Healthy", "security_level": 10, "zone": "Core"},
            "SWIFT_Node": {"status": "Healthy", "security_level": 9, "zone": "Core"}
        }

        # PART 1 ADDITION: Connectivity/Lateral Movement paths
        self.paths = {
            "ATM_1": ["Teller_Sys"],
            "Mobile_Gateway": ["Teller_Sys"],
            "Teller_Sys": ["Core_DB"],
            "Internal_Admin": ["SWIFT_Node"]
        }

    def simulate_chain_attack(self, entry_point):
        """Simulates an attacker trying to move deeper into the bank."""
        current_node = entry_point
        
        while current_node:
            print(f"\n📍 CURRENT POSITION: {current_node}")
            success = self.attack_node(current_node)
            
            if success:
                # If breached, find the next nodes in the path
                next_options = self.paths.get(current_node, [])
                if next_options:
                    print(f"🔓 PATH UNLOCKED: Attacker is moving toward {next_options}...")
                    current_node = next_options[0] # Move to the next connected node
                    time.sleep(1)
                else:
                    print("🏁 TARGET REACHED: No further paths available.")
                    break
            else:
                print(f"🛑 STOPPED: Attacker could not bypass {current_node}. Chain broken.")
                break

    def attack_node(self, node_name):
        node = self.nodes[node_name]
        attacker_skill = random.randint(1, 15)
        
        if attacker_skill > node['security_level']:
            node['status'] = "⚠️ BREACHED"
            print(f"💥 {node_name} BYPASSED! (Skill {attacker_skill} > Defense {node['security_level']})")
            return True
        return False

    def display_status(self):
        print(f"\n{'NODE':<20} | {'STATUS':<12} | {'SECURITY'}")
        print("-" * 50)
        for name, info in self.nodes.items():
            print(f"{name:<20} | {info['status']:<12} | Lvl {info['security_level']}")

# --- RUNNING THE CHAIN ATTACK ---
my_bank = BankArchitecture()
print("--- STARTING LATERAL MOVEMENT SIMULATION ---")

# Attacker starts at the ATM and tries to reach the Core Database
my_bank.simulate_chain_attack("ATM_1")

my_bank.display_status()