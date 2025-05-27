from blockchain import Block, Blockchain
import time

def audit_events_example():
    # Create a new blockchain for audit logs with difficulty 8
    audit_chain = Blockchain(difficulty=16)

    # Add some audit events
    audit_chain.add_block({
        "event_type": "login",
        "user_id": "user123",
        "timestamp": time.time(),
        "ip_address": "192.168.1.1",
        "success": True
    })

    audit_chain.add_block({
        "event_type": "data_access",
        "user_id": "user123",
        "timestamp": time.time(),
        "resource": "customer_database",
        "action": "read"
    })

    audit_chain.add_block({
        "event_type": "login",
        "user_id": "user456",
        "timestamp": time.time(),
        "ip_address": "192.168.1.2",
        "success": False
    })

    audit_chain.add_block({
        "event_type": "data_modification",
        "user_id": "admin001",
        "timestamp": time.time(),
        "resource": "user_settings",
        "action": "update"
    })

    # Save the blockchain to a file
    audit_chain.save_to_file("audit_chain.json")

    # Demonstrate querying - find all login events
    login_events = audit_chain.find_blocks_by_criteria("event_type", "login")
    print("\nLogin Events:")
    for block in login_events:
        print(f"Block #{block.index} - User: {block.data['user_id']}, Success: {block.data['success']}")

    # Demonstrate attempt to tamper with data
    print("\nAttempting to tamper with block 2:")
    tampered_data = audit_chain.chain[2].data.copy()
    tampered_data["success"] = True  # Try to change a failed login to successful
    success, message = audit_chain.attempt_tamper(2, tampered_data)
    print(message)

    # Verify the chain is still valid
    print(f"\nIs blockchain valid? {audit_chain.is_chain_valid()}")

if __name__ == "__main__":
    audit_events_example()