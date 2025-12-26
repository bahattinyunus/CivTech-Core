import time
import sys
import random

def type_effect(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def boot_sequence():
    print("\033[96m")
    print("╔════════════════════════════════════════════════════╗")
    print("║   CIVTECH-CORE GENESIS PROTOCOL v1.0               ║")
    print("╚════════════════════════════════════════════════════╝")
    print("\033[0m")
    
    steps = [
        "Allocating memory blocks...",
        "Connecting to Satellite Grid...",
        "Syncing with City Sensors...",
        "Loading Governance Modules...",
        "Decrypting Admin Keys..."
    ]
    
    for step in steps:
        time.sleep(random.uniform(0.3, 0.8))
        print(f"\033[92m[OK]\033[0m {step}")
    
    type_effect("\n> SYSTEM READY. AWAITING COMMAND...", 0.05)

if __name__ == "__main__":
    boot_sequence()
