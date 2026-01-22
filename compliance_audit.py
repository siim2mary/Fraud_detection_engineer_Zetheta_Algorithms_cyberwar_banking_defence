import json
import os
from datetime import datetime

class ComplianceManager:
    def __init__(self):
        self.log_filename = "bank_audit_trail.json"
        # Create the file if it doesn't exist
        if not os.path.exists(self.log_filename):
            with open(self.log_filename, 'w') as f:
                json.dump([], f)

    def record_event(self, event_type, target, detail, status="Logged"):
        """
        Records a specific event into the audit trail.
        event_type: 'ATTACK', 'DEFENSE', 'SYSTEMIC_RISK'
        """
        new_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": event_type,
            "target_node": target,
            "description": detail,
            "compliance_status": status
        }

        # Read existing logs
        with open(self.log_filename, 'r') as f:
            logs = json.load(f)

        # Add new entry
        logs.append(new_entry)

        # Write back to file
        with open(self.log_filename, 'w') as f:
            json.dump(logs, f, indent=4)
        
        print(f"📄 Audit Log Updated: {event_type} on {target}")

    def generate_audit_summary(self):
        """Displays a summary of the audit trail for a compliance officer."""
        with open(self.log_filename, 'r') as f:
            logs = json.load(f)
            
        print("\n" + "="*20 + " COMPLIANCE AUDIT SUMMARY " + "="*20)
        print(f"{'TIMESTAMP':<20} | {'EVENT':<10} | {'TARGET':<15} | {'STATUS'}")
        print("-" * 65)
        
        for entry in logs[-5:]:  # Show last 5 events
            print(f"{entry['timestamp']:<20} | {entry['event_type']:<10} | {entry['target_node']:<15} | {entry['compliance_status']}")

# --- EXECUTION ---
if __name__ == "__main__":
    auditor = ComplianceManager()

    # Simulating events to log
    auditor.record_event("ATTACK", "ATM_1", "Brute force attempt detected", "FAILED")
    auditor.record_event("DEFENSE", "Core_DB", "Upgraded security to Lvl 12", "SUCCESS")
    auditor.record_event("COMPLIANCE", "System", "Quarterly risk assessment completed", "VERIFIED")

    # Display the last few entries
    auditor.generate_audit_summary()