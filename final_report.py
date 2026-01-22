import datetime

class ProjectReporter:
    def __init__(self, architecture, threat_results, budget_left, systemic_score):
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.architecture = architecture
        self.threat_results = threat_results
        self.budget_left = budget_left
        self.systemic_score = systemic_score

    def generate_txt_report(self):
        filename = "Zetheta_Cyber_Defense_Report.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write("====================================================\n")
            f.write(f"     BANKING CYBER DEFENSE SIMULATION REPORT\n")
            f.write(f"     Generated on: {self.timestamp}\n")
            f.write("====================================================\n\n")

            f.write("1. ARCHITECTURE STATUS\n")
            for name, info in self.architecture.items():
                f.write(f"- {name}: Status: {info['status']} | Security: Lvl {info['security_level']}\n")

            f.write("\n2. FINANCIAL OVERVIEW\n")
            f.write(f"- Remaining Defense Budget: {self.budget_left} Credits\n")
            f.write(f"- Systemic Health Score: {self.systemic_score}%\n\n")

            f.write("3. RISK ASSESSMENT\n")
            if self.systemic_score < 60:
                f.write("CRITICAL: High risk of financial contagion detected.\n")
            else:
                f.write("STABLE: Defenses are sufficient for current threat levels.\n")

        print(f"✅ Final Report successfully saved as '{filename}'")

# --- FINAL INTEGRATION ---
if __name__ == "__main__":
    # Sample data representing outcomes from Parts 1-5
    final_nodes = {
        "Core_DB": {"status": "Healthy", "security_level": 11},
        "ATM_1": {"status": "⚠️ BREACHED", "security_level": 6}
    }
    
    reporter = ProjectReporter(
        architecture=final_nodes,
        threat_results="Success/Fail Log",
        budget_left=400,
        systemic_score=75.0
    )
    
    reporter.generate_txt_report()