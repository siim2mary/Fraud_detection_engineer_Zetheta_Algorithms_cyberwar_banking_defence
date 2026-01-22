import streamlit as st
import random
import json
import pandas as pd
from datetime import datetime

class ZethetaDefenseSystem:
    def __init__(self):
        # --- 1. INITIALIZE DATA STRUCTURES FIRST ---
        if 'logs' not in st.session_state:
            st.session_state.logs = []
        
        if 'budget' not in st.session_state:
            st.session_state.budget = 2000
            
        if 'budget_history' not in st.session_state:
            st.session_state.budget_history = [2000]

        # --- 2. INITIALIZE NODES ---
        if 'nodes' not in st.session_state:
            self.reset_system()

    def reset_system(self):
        """Restores nodes and logs the event."""
        st.session_state.nodes = {
            "ATM_1": {"status": "Healthy", "security": 5, "zone": "Edge"},
            "Mobile_Gateway": {"status": "Healthy", "security": 5, "zone": "Edge"},
            "Teller_Sys": {"status": "Healthy", "security": 6, "zone": "Internal"},
            "Core_DB": {"status": "Healthy", "security": 10, "zone": "Core"},
            "SWIFT_Node": {"status": "Healthy", "security": 9, "zone": "Core"}
        }
        self.log_event("RECOVERY", "System", "All nodes restored to Healthy state.")

    def log_event(self, event_type, target, detail):
        """Adds entry to the audit trail."""
        entry = {
            "time": datetime.now().strftime("%H:%M:%S"), 
            "event": event_type, 
            "target": target, 
            "detail": detail
        }
        st.session_state.logs.insert(0, entry)

    def attack(self, threat_name, power_bonus):
        """Logic for Part 2 & Part 7 analytics."""
        target = random.choice(list(st.session_state.nodes.keys()))
        node = st.session_state.nodes[target]
        attack_roll = random.randint(1, 10) + power_bonus
        
        if attack_roll > node["security"]:
            node["status"] = f"⚠️ BREACHED ({threat_name})"
            self.log_event("CRITICAL", target, f"Successful {threat_name} attack.")
        else:
            self.log_event("INFO", target, f"Blocked {threat_name} attempt.")

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="Zetheta Analytics SOC", layout="wide")
sim = ZethetaDefenseSystem()

st.title("🛡️ Zetheta Bank: Security Operations & Analytics")

# --- SIDEBAR ---
st.sidebar.header("Command Center")
st.sidebar.metric("Remaining Budget", f"${st.session_state.budget}")

if st.sidebar.button("♻️ Reset & Recover System"):
    sim.reset_system()
    st.session_state.budget = 2000
    st.session_state.budget_history = [2000]
    st.rerun()

if st.sidebar.button("📦 Export Final Audit"):
    with open("final_audit.json", "w") as f:
        json.dump(st.session_state.logs, f, indent=4)
    st.sidebar.success("Audit Log Exported!")

# --- ANALYTICS SECTION ---
st.subheader("📊 Live Security Analytics")
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.write("**Defense Levels by Node**")
    chart_data = pd.DataFrame([
        {"Node": k, "Security": v["security"]} for k, v in st.session_state.nodes.items()
    ])
    st.bar_chart(chart_data.set_index("Node"))

with col_chart2:
    st.write("**Budget Depletion (Defense Spending)**")
    st.line_chart(st.session_state.budget_history)

st.divider()

# --- SOC REAL-TIME MONITOR ---
st.subheader("🌐 Network Health Monitor")
node_cols = st.columns(len(st.session_state.nodes))
for i, (name, info) in enumerate(st.session_state.nodes.items()):
    node_cols[i].metric(name, f"Lvl {info['security']}", info['status'], delta_color="inverse")

# --- INTERACTIVE TABS ---
tab_ops, tab_audit = st.tabs(["🎮 Field Operations", "📜 Compliance Logs"])

with tab_ops:
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Threat Simulation")
        if st.button("🚀 Launch DDoS"):
            sim.attack("DDoS", 2)
            st.rerun()
        if st.button("🔥 Launch Ransomware"):
            sim.attack("Ransomware", 7)
            st.rerun()
    with c2:
        st.write("### Defense Allocation")
        target_node = st.selectbox("Select Node to Harden", list(st.session_state.nodes.keys()))
        if st.button("🔧 Upgrade Security ($200)"):
            if st.session_state.budget >= 200:
                st.session_state.nodes[target_node]["security"] += 1
                st.session_state.budget -= 200
                st.session_state.budget_history.append(st.session_state.budget)
                sim.log_event("DEFENSE", target_node, "Security level hardened.")
                st.rerun()
            else:
                st.error("Insufficient Funds!")

with tab_audit:
    st.write("### Official Audit Trail")
    st.table(st.session_state.logs)