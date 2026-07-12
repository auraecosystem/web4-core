# run_all_attacks.py
import time
import math

def log_output(text, file_handle):
    """Prints text directly to the screen and saves it to a file simultaneously."""
    print(text)
    file_handle.write(text + "\n")

# Open a clean text log file in the local directory
with open("simulation_terminal_log.txt", "w") as log_file:

    log_output("====================================================", log_file)
    log_output("   WEB4 ADVERSARIAL ATTACK SIMULATION RUNTIME       ", log_file)
    log_output("====================================================\n", log_file)

    class Web4Agent:
        def __init__(self, name, profile, atp=100, t3=0.8, ci=1.0):
            self.name = name
            self.profile = profile
            self.atp = atp     # Attention Transfer Packets (Metabolic Budget)
            self.t3 = t3       # Trust Tensor average score
            self.ci = ci       # Coherence Index
            self.is_alive = True

        def calculate_metrics(self, adp_cost, atp_reward, s, c, t, r):
            # 1. Metabolic Exhaustion
            self.atp = self.atp - adp_cost + atp_reward
            
            # 2. Coherence Index (Geometric Mean Matrix calculation)
            self.ci = math.sqrt(max(0, s * c * t * r))
            
            # 3. Trust Tensor Degradation (Vector Breakdown)
            if self.ci  Reason: Metabolic Exhaustion (ATP spent with zero value returned).", file_handle)
            if attacker.t3 <= 0.5:
                log_output(" -> Reason: Trust Tensor dropped below the 0.5 Phase-Transition boundary.", file_handle)
            if attacker.ci <= 0.3:
                log_output(" -> Reason: Coherence Index broken across relational/spatial matrices.", file_handle)
        else:
            log_output(f" DEFENSE STATUS: Attack ongoing. Refining defense thresholds.", file_handle)
        log_output("-" * 60 + "\n", file_handle)

    # --- TRACK FB LOGIC: Trust Manipulation ---
    def track_fb_logic(attacker, victim, file_handle):
        log_output(" [Action] Attacker spawns Sybil identity accounts to fake cross-device witnessing.", file_handle)
        # Attacker breaks relational identity consistency
        spatial, capability, temporal, relational = 1.0, 0.9, 0.8, 0.1  
        attacker.calculate_metrics(adp_cost=15, atp_reward=0, s=spatial, c=capability, t=temporal, r=relational)
        return attacker, victim

    # --- TRACK FC LOGIC: Economic Exploits ---
    def track_fc_logic(attacker, victim, file_handle):
        log_output(" [Action] Attacker launches ATP Drain flooding against honest node.", file_handle)
        # Spam cost depletes attacker's attention packets while netting 0 token rewards
        victim.atp -= 30 
        attacker.calculate_metrics(adp_cost=85, atp_reward=0, s=0.9, c=0.9, t=0.9, r=0.9)
        return attacker, victim

    # Execute Compiled Script Orchestration
    run_simulation_track("FB", "Trust Manipulation (Sybil Identity Attack)", track_fb_logic, log_file)
    run_simulation_track("FC", "Economic Exploits (ATP Exhaustion Flood)", track_fc_logic, log_file)

    log_output("====================================================", log_file)
    log_output(" Simulation Complete. Output Saved to 'simulation_terminal_log.txt'.", log_file)
    log_output("====================================================", log_file)
