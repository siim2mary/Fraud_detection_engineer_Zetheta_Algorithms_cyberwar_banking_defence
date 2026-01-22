import time

class IncidentResponseTrainer:
    def __init__(self):
        # PART 4: Scenario Library
        self.scenarios = [
            {
                "id": 1,
                "title": "🚨 RANSOMWARE BREACH",
                "description": "Encryption is spreading on the SWIFT Node. Payments are failing.",
                "options": {
                    "1": {"text": "Isolate the Node (Cut Network)", "impact": "Prevents spread; stops payments.", "correct": True},
                    "2": {"text": "Pay the Ransom (20 BTC)", "impact": "High cost; no guarantee of data.", "correct": False},
                    "3": {"text": "Reboot the Servers", "impact": "Corruption spreads faster.", "correct": False}
                }
            },
            {
                "id": 2,
                "title": "🌐 VOLUMETRIC DDoS",
                "description": "Mobile Banking is offline. 50,000 customers cannot login.",
                "options": {
                    "1": {"text": "Ignore and Wait", "impact": "Reputational collapse.", "correct": False},
                    "2": {"text": "Activate Cloud Scrubbing", "impact": "Filters bad traffic; restores app.", "correct": True},
                    "3": {"text": "Shut down the API Gateway", "impact": "Attacker succeeds in Denial of Service.", "correct": False}
                }
            }
        ]

    def start_session(self):
        print("--- 🛡️ ZETHETA INCIDENT RESPONSE SIMULATOR ---")
        score = 0
        
        for scene in self.scenarios:
            print(f"\nSCENARIO {scene['id']}: {scene['title']}")
            print(f"SITUATION: {scene['description']}")
            
            for key, opt in scene['options'].items():
                print(f"  [{key}] {opt['text']}")
            
            choice = input("\nSELECT ACTION (1/2/3): ")
            
            if choice in scene['options']:
                action = scene['options'][choice]
                print(f"RESULT: {action['impact']}")
                if action['correct']:
                    print("✅ STATUS: SUCCESSFUL CONTAINMENT")
                    score += 1
                else:
                    print("❌ STATUS: CRITICAL FAILURE")
            else:
                print("⚠️ HESITATION: You waited too long. Attack succeeded.")
            
            time.sleep(1)

        print(f"\n🏁 TRAINING COMPLETE. Final Score: {score}/{len(self.scenarios)}")

# --- RUNNING THE TRAINER ---
if __name__ == "__main__":
    trainer = IncidentResponseTrainer()
    trainer.start_session()
