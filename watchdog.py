# watchdog.py
import random

# Battery and mission settings
battery = 100.0
TOTAL_WAYPOINTS = 10

# Loop through navigation waypoints (same range pattern as the retry example)
for waypoint in range(1, TOTAL_WAYPOINTS + 1):

    # Simulated battery drain: random float between 1.5 and 3.5
    drain = random.uniform(1.5, 3.5)
    battery = battery - drain

    # f-string formatting for telemetry logs
    print(f"[NAV] Waypoint {waypoint} reached. Battery: {battery:.1f}%")

    # Decision logic: check the most critical condition first (if / elif)
    if battery < 75.0:
        print("[EMERGENCY RETURN TRIGGERED]")
        break
    elif battery < 80.0:
        print(f"[CAUTION] Low battery: {battery:.1f}%")