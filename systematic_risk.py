class SystemicRiskTool:
    def __init__(self):
        # PART 5: Multiple Banks in the ecosystem
        self.ecosystem = {
            "Zetheta_Bank": {"health": 100, "connected_to": ["Global_Trust", "Retail_Bank"]},
            "Global_Trust": {"health": 100, "connected_to": ["Zetheta_Bank", "Central_Reserve"]},
            "Retail_Bank":  {"health": 100, "connected_to": ["Zetheta_Bank"]},
            "Central_Reserve": {"health": 100, "connected_to": ["Global_Trust"]}
        }
        self.fragility_threshold = 60 # Below this, a market crash occurs

    def simulate_contagion(self, failed_bank):
        """If one bank fails, it damages its neighbors."""
        print(f"💥 INITIAL FAILURE: {failed_bank} has been breached!")
        
        # Damage the failed bank
        self.ecosystem[failed_bank]["health"] = 0
        
        # Spread the 'infection' to connected banks
        for neighbor in self.ecosystem[failed_bank]["connected_to"]:
            damage = 40  # Risk spillover amount
            self.ecosystem[neighbor]["health"] -= damage
            print(f"⚠️ CONTAGION: Risk spreading to {neighbor}. Health dropped by {damage}%.")

    def calculate_systemic_score(self):
        """Calculates the average health of the entire ecosystem."""
        total_health = sum(bank["health"] for bank in self.ecosystem.values())
        avg_health = total_health / len(self.ecosystem)
        
        print(f"\n🌍 SYSTEMIC HEALTH SCORE: {avg_health:.2f}%")
        
        if avg_health < self.fragility_threshold:
            print("🚨 CRITICAL: Systemic Collapse Imminent. Economic instability detected.")
        else:
            print("✅ STABLE: The ecosystem remains resilient.")

# --- EXECUTION ---
if __name__ == "__main__":
    risk_analyst = SystemicRiskTool()
    
    # 1. Start with one failure
    risk_analyst.simulate_contagion("Zetheta_Bank")
    
    # 2. Assess the market impact
    risk_analyst.calculate_systemic_score()