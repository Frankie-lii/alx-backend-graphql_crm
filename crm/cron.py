#!/usr/bin/env python3
import datetime
import logging
import requests

LOG_FILE = "/tmp/crm_heartbeat_log.txt"

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Log to file (append mode)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

    # Optional: Check GraphQL endpoint
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

