#!/usr/bin/env python3
import datetime
import logging
import requests  # Using requests for optional GraphQL check

HEARTBEAT_LOG = "/tmp/crmheartbeatlog.txt"  # No underscore

def logcrmheartbeat():
    """Logs heartbeat message every 5 minutes."""
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Append to heartbeat log
    with open(HEARTBEAT_LOG, "a") as f:
        f.write(message + "\n")

    # Optional GraphQL hello field check
    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.status_code == 200:
            print("GraphQL endpoint responded to heartbeat check.")
    except requests.RequestException as e:
        logging.error(f"GraphQL health check failed: {e}")

