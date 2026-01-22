import random
import time

class ThreatModelSimulation:
    def __init__(self):
        # PART 1: Architecture (The Bank)
        self.nodes = {
            "ATM_1": {"status": "Healthy", "security_level": 3, "zone": "Edge"},
            "Mobile_Gateway": {"status": "Healthy", "security_level": 5, "zone": "Edge"},
            "Teller_Sys": {"status": "Healthy", "security_level": 6, "zone": "Internal"},
            "Core_DB": {"status": "Healthy", "security_level": 10, "zone": "Core"},
            "SWIFT_Node": {"status": "Healthy", "security_level": 9, "zone": "Core"}
        }

        # PART 2: Threat Library (The Attack Vectors)
        # Power Bonus: How much "extra strength" the attack has
        self.threat_library = {
            "DDoS": {"power_bonus": 2, "target_zone": "Edge", "impact": "Service Down"},
            "SQL_Injection": {"power_bonus": 4, "target_zone": "Internal", "impact": "Data Leak"},
            "Ransomware": {"power_bonus": 7, "target_zone": "Core", "impact": "System Lock"},
            "Insider_Threat": {"power_bonus": 5, "target_zone": "Core", "impact": "Funds Theft"}
        }

    def launch_attack(self, threat_name):
        """Simulates a specific threat hitting a random node in its target zone."""
        if threat_name not in self.threat_library:
            print("Threat type unknown.")
            return

        threat = self.threat_library[threat_name]
        
        # Identify valid targets for this specific threat
        targets = [name for name, info in self.nodes.items() if info["zone"] == threat["target_zone"]]
        target_node = random.choice(targets)

        print(f"\n⚠️  THREAT DETECTED: {threat_name} targeting {target_node}")
        time.sleep(1)

        # PART 2 LOGIC: Threat Power + Skill vs. Node Defense
        hacker_skill = random.randint(1, 10)
        total_attack_power = hacker_skill + threat["power_bonus"]
        node_defense = self.nodes[target_node]["security_level"]

        if total_attack_power > node_defense:
            self.nodes[target_node]["status"] = f"⚠️ BREACHED ({threat_name})"
            print(f"💥 CRITICAL: {threat_name} bypasses security! Result: {threat['impact']}")
        else:
            print(f"🛡️  DEFENSE SECURE: {target_node} successfully mitigated {threat_name}.")

    def display_soc_dashboard(self):
        """Displays the Security Operations Center (SOC) view."""
        print(f"\n{'BANKING NODE':<20} | {'ZONE':<10} | {'STATUS':<20} | {'DEFENSE'}")
        print("-" * 75)
        for name, info in self.nodes.items():
            print(f"{name:<20} | {info['zone']:<10} | {info['status']:<20} | Lvl {info['security_level']}")

# --- EXECUTION ---
if __name__ == "__main__":
    sim = ThreatModelSimulation()
    
    print("Initializing Banking Threat Model...")
    sim.display_soc_dashboard()

    # Launching a series of diverse attack vectors
    sim.launch_attack("DDoS")
    sim.launch_attack("SQL_Injection")
    sim.launch_attack("Ransomware")

    # Final Security Audit
    print("\n" + "="*25 + " FINAL AUDIT REPORT " + "="*25)
    sim.display_soc_dashboard()