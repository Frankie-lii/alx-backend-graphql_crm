#!/usr/bin/env python3
import datetime
import logging
import requests

LOG_FILE = "/tmp/low_stock_updates_log.txt"

def update_low_stock():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mutation = """
    mutation {
        updateLowStockProducts {
            updatedProducts {
                name
                stock
            }
            message
        }
    }
    """

    try:
        response = requests.post(
            "http://localhost:8000/graphql",
            json={"query": mutation},
            timeout=10
        )
        data = response.json().get("data", {}).get("updateLowStockProducts", {})
        updated_products = data.get("updatedProducts", [])
        message = data.get("message", "No response message")

        with open(LOG_FILE, "a") as f:
            f.write(f"{timestamp} - {message}\n")
            for product in updated_products:
                f.write(f"Product: {product['name']}, Stock: {product['stock']}\n")

    except Exception as e:
        logging.error(f"{timestamp} - Error updating low stock: {e}\n")

