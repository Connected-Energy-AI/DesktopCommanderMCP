#!/usr/bin/env python3
"""
Rapid Start Workflow - 90 Minute Executive Cleanup
For Robert Bailey - Connected Energy Services / Talian Technologies

Usage:
    python scripts/rapid-start.py --phase inventory
    python scripts/rapid-start.py --phase stabilize
    python scripts/rapid-start.py --phase recover
    python scripts/rapid-start.py --phase consolidate
    python scripts/rapid-start.py --phase operate
    python scripts/rapid-start.py --all
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "rapid-start-output"
OUTPUT_DIR.mkdir(exist_ok=True)

def phase_inventory():
    """Phase 1: Inventory (20 min) - Gather all accounts, tools, debts, disputes"""
    print("\n" + "="*60)
    print("PHASE 1: INVENTORY (20 minutes)")
    print("="*60)
    
    inventory = {
        "timestamp": datetime.now().isoformat(),
        "accounts": {
            "banking": [],
            "credit_cards": [],
            "loans": [],
            "saas_subscriptions": [],
            "utilities": [],
            "investment": [],
            "retirement": []
        },
        "tools": {
            "software": [],
            "hardware": [],
            "services": []
        },
        "debts": {
            "business": [],
            "personal": []
        },
        "disputes": {
            "active": [],
            "potential": []
        },
        "customers": {
            "outstanding_invoices": [],
            "follow_up_required": []
        }
    }
    
    # Prompt for input
    print("\n📋 ACCOUNT INVENTORY")
    print("List all accounts you can recall (banking, credit, loans, SaaS, utilities):")
    print("  Format: name,type,balance,status (press Enter twice when done)")
    
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 2:
            account = {
                "name": parts[0].strip(),
                "type": parts[1].strip(),
                "balance": parts[2].strip() if len(parts) > 2 else "unknown",
                "status": parts[3].strip() if len(parts) > 3 else "active"
            }
            
            # Categorize
            acc_type = account["type"].lower()
            if "bank" in acc_type or "checking" in acc_type or "savings" in acc_type:
                inventory["accounts"]["banking"].append(account)
            elif "credit" in acc_type or "card" in acc_type:
                inventory["accounts"]["credit_cards"].append(account)
            elif "loan" in acc_type or "mortgage" in acc_type:
                inventory["accounts"]["loans"].append(account)
            elif "saas" in acc_type or "software" in acc_type or "subscription" in acc_type:
                inventory["tools"]["software"].append(account)
            else:
                inventory["accounts"]["utilities"].append(account)
    
    # Save inventory
    output_file = OUTPUT_DIR / "inventory.json"
    with open(output_file, 'w') as f:
        json.dump(inventory, f, indent=2)
    
    print(f"\n✅ Inventory saved to: {output_file}")
    print(f"   Total accounts: {sum(len(v) for v in inventory['accounts'].values())}")
    print(f"   Total tools: {sum(len(v) for v in inventory['tools'].values())}")
    
    return inventory


def phase_stabilize():
    """Phase 2: Stabilize (20 min) - Freeze spend, enable MFA, set follow-ups"""
    print("\n" + "="*60)
    print("PHASE 2: STABILIZE (20 minutes)")
    print("="*60)
    
    actions = {
        "timestamp": datetime.now().isoformat(),
        "freeze_non_essential": [],
        "enable_mfa": [],
        "set_follow_ups": [],
        "password_changes": [],
        "account_locks": []
    }
    
    print("\n🔒 SECURITY STABILIZATION")
    print("List accounts needing immediate security attention:")
    print("  Format: account,action (freeze|mfa|password|lock) (press Enter twice when done)")
    
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 2:
            action = {
                "account": parts[0].strip(),
                "action": parts[1].strip(),
                "completed": False,
                "timestamp": datetime.now().isoformat()
            }
            
            if action["action"] == "freeze":
                actions["freeze_non_essential"].append(action)
            elif action["action"] == "mfa":
                actions["enable_mfa"].append(action)
            elif action["action"] == "password":
                actions["password_changes"].append(action)
            elif action["action"] == "lock":
                actions["account_locks"].append(action)
            else:
                actions["set_follow_ups"].append(action)
    
    # Save actions
    output_file = OUTPUT_DIR / "stabilize-actions.json"
    with open(output_file, 'w') as f:
        json.dump(actions, f, indent=2)
    
    print(f"\n✅ Stabilization actions saved to: {output_file}")
    print(f"   Total actions: {sum(len(v) for v in actions.values()) - 1}")  # -1 for timestamp
    
    # Print checklist
    print("\n📋 IMMEDIATE ACTION CHECKLIST:")
    for action_type, items in actions.items():
        if action_type == "timestamp":
            continue
        print(f"\n  {action_type.replace('_', ' ').title()}:")
        for item in items:
            print(f"    ☐ {item['account']}")
    
    return actions


def phase_recover():
    """Phase 3: Recover (20 min) - Open disputes, reconcile, send updates"""
    print("\n" + "="*60)
    print("PHASE 3: RECOVER (20 minutes)")
    print("="*60)
    
    recover = {
        "timestamp": datetime.now().isoformat(),
        "disputes_to_open": [],
        "transactions_to_reconcile": [],
        "customer_updates": [],
        "chargebacks": []
    }
    
    print("\n💰 RECOVERY ACTIONS")
    print("List disputes, reconciliations, and customer updates needed:")
    print("  Format: item,type,amount,notes (press Enter twice when done)")
    
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 2:
            item = {
                "description": parts[0].strip(),
                "type": parts[1].strip(),
                "amount": parts[2].strip() if len(parts) > 2 else "0",
                "notes": parts[3].strip() if len(parts) > 3 else "",
                "status": "pending"
            }
            
            if "dispute" in item["type"].lower():
                recover["disputes_to_open"].append(item)
            elif "reconcile" in item["type"].lower() or "transaction" in item["type"].lower():
                recover["transactions_to_reconcile"].append(item)
            elif "customer" in item["type"].lower() or "update" in item["type"].lower():
                recover["customer_updates"].append(item)
            elif "chargeback" in item["type"].lower():
                recover["chargebacks"].append(item)
    
    # Save recovery items
    output_file = OUTPUT_DIR / "recovery-items.json"
    with open(output_file, 'w') as f:
        json.dump(recover, f, indent=2)
    
    print(f"\n✅ Recovery items saved to: {output_file}")
    
    # Calculate total recovery potential
    total = 0
    for item in recover["disputes_to_open"] + recover["chargebacks"]:
        try:
            total += float(item["amount"].replace('$', '').replace(',', ''))
        except:
            pass
    
    print(f"   Potential recovery: ${total:,.2f}")
    
    return recover


def phase_consolidate():
    """Phase 4: Consolidate (20 min) - Pick targets, schedule migrations"""
    print("\n" + "="*60)
    print("PHASE 4: CONSOLIDATE (20 minutes)")
    print("="*60)
    
    consolidate = {
        "timestamp": datetime.now().isoformat(),
        "accounts_to_close": [],
        "accounts_to_merge": [],
        "accounts_to_keep": [],
        "migration_schedule": []
    }
    
    print("\n🔄 CONSOLIDATION PLAN")
    print("List accounts to close, merge, or keep:")
    print("  Format: account,action,destination (press Enter twice when done)")
    
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    for line in lines:
        parts = line.split(',')
        if len(parts) >= 2:
            item = {
                "account": parts[0].strip(),
                "action": parts[1].strip(),
                "destination": parts[2].strip() if len(parts) > 2 else "",
                "scheduled_date": "",
                "completed": False
            }
            
            if item["action"].lower() == "close":
                consolidate["accounts_to_close"].append(item)
            elif item["action"].lower() == "merge":
                consolidate["accounts_to_merge"].append(item)
            elif item["action"].lower() == "keep":
                consolidate["accounts_to_keep"].append(item)
    
    # Save consolidation plan
    output_file = OUTPUT_DIR / "consolidation-plan.json"
    with open(output_file, 'w') as f:
        json.dump(consolidate, f, indent=2)
    
    print(f"\n✅ Consolidation plan saved to: {output_file}")
    print(f"   To close: {len(consolidate['accounts_to_close'])}")
    print(f"   To merge: {len(consolidate['accounts_to_merge'])}")
    print(f"   To keep: {len(consolidate['accounts_to_keep'])}")
    
    return consolidate


def phase_operate():
    """Phase 5: Operate (10 min) - Build tomorrow's top-3 and message queue"""
    print("\n" + "="*60)
    print("PHASE 5: OPERATE (10 minutes)")
    print("="*60)
    
    operate = {
        "timestamp": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "top_3_priorities": [],
        "messages_to_send": [],
        "follow_ups": [],
        "blocked_by": []
    }
    
    print("\n📅 TOMORROW'S PRIORITIES")
    print("What are your top 3 priorities for tomorrow?")
    
    for i in range(3):
        priority = input(f"  Priority {i+1}: ")
        if priority:
            operate["top_3_priorities"].append({
                "priority": i + 1,
                "task": priority,
                "completed": False
            })
    
    print("\n📧 MESSAGES TO SEND")
    print("List messages/emails to send (press Enter twice when done):")
    
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    for line in lines:
        operate["messages_to_send"].append({
            "to": line.split(',')[0].strip() if ',' in line else line,
            "subject": line.split(',')[1].strip() if ',' in line else "",
            "sent": False
        })
    
    print("\n⏰ FOLLOW-UPS")
    print("List follow-ups needed (press Enter twice when done):")
    
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except EOFError:
            break
    
    for line in lines:
        operate["follow_ups"].append({
            "task": line,
            "completed": False
        })
    
    # Save operating plan
    output_file = OUTPUT_DIR / f"operating-plan-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output_file, 'w') as f:
        json.dump(operate, f, indent=2)
    
    print(f"\n✅ Operating plan saved to: {output_file}")
    print(f"   Top 3 priorities set: {len(operate['top_3_priorities'])}")
    print(f"   Messages to send: {len(operate['messages_to_send'])}")
    print(f"   Follow-ups: {len(operate['follow_ups'])}")
    
    return operate


def run_all_phases():
    """Run all 5 phases sequentially"""
    print("\n" + "="*60)
    print("🚀 90-MINUTE RAPID START WORKFLOW")
    print("   For Robert Bailey - Executive Multi-Role Operations")
    print("="*60)
    
    results = {
        "started": datetime.now().isoformat(),
        "phases": {}
    }
    
    # Phase 1: Inventory
    results["phases"]["inventory"] = phase_inventory()
    
    # Phase 2: Stabilize
    results["phases"]["stabilize"] = phase_stabilize()
    
    # Phase 3: Recover
    results["phases"]["recover"] = phase_recover()
    
    # Phase 4: Consolidate
    results["phases"]["consolidate"] = phase_consolidate()
    
    # Phase 5: Operate
    results["phases"]["operate"] = phase_operate()
    
    # Save complete results
    results["completed"] = datetime.now().isoformat()
    output_file = OUTPUT_DIR / "rapid-start-complete.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    
    print("\n" + "="*60)
    print("✅ RAPID START WORKFLOW COMPLETE!")
    print("="*60)
    print(f"\n📁 All outputs saved to: {OUTPUT_DIR}")
    print(f"   - inventory.json")
    print(f"   - stabilize-actions.json")
    print(f"   - recovery-items.json")
    print(f"   - consolidation-plan.json")
    print(f"   - operating-plan-{datetime.now().strftime('%Y-%m-%d')}.json")
    print(f"\n⏱️  Total time: {results['completed']}")
    print("\n🎯 Next: Review outputs and begin execution!")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="90-Minute Rapid Start Workflow for Executive Cleanup"
    )
    parser.add_argument(
        "--phase",
        choices=["inventory", "stabilize", "recover", "consolidate", "operate"],
        help="Run a specific phase"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all phases sequentially"
    )
    
    args = parser.parse_args()
    
    if args.all:
        run_all_phases()
    elif args.phase:
        phase_func = {
            "inventory": phase_inventory,
            "stabilize": phase_stabilize,
            "recover": phase_recover,
            "consolidate": phase_consolidate,
            "operate": phase_operate
        }
        phase_func[args.phase]()
    else:
        parser.print_help()
        print("\nExample usage:")
        print("  python scripts/rapid-start.py --all")
        print("  python scripts/rapid-start.py --phase inventory")


if __name__ == "__main__":
    main()
