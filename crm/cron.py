#!/usr/bin/env python3
import datetime
import logging
import requests

HEARTBEAT_LOG = "/tmp/crmheartbeatlog.txt"  # Correct file name

def logcrmheartbeat():
    """Logs heartbeat message every 5 minutes."""
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Append to log file
    with open(HEARTBEAT_LOG, "a") as f:
        f.write(message + "\n")

    # Optional GraphQL health check
    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": "{ hello }"},
            timeout=5
        )
        if response.status_code == 200:
            print("GraphQL endpoint is responsive.")
    except requests.RequestException as e:
        logging.error(f"GraphQL health check failed: {e}")

