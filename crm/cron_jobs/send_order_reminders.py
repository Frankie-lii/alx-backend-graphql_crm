#!/usr/bin/env python3
import datetime
import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Setup logging
LOG_FILE = "/tmp/order_reminders_log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

# GraphQL endpoint
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=True,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Calculate date range (last 7 days)
today = datetime.date.today()
week_ago = today - datetime.timedelta(days=7)

query = gql(
    """
    query GetPendingOrders($startDate: Date!, $endDate: Date!) {
        orders(orderDate_Gte: $startDate, orderDate_Lte: $endDate, status: "pending") {
            id
            customer {
                email
            }
        }
    }
    """
)

params = {
    "startDate": week_ago.isoformat(),
    "endDate": today.isoformat()
}

try:
    result = client.execute(query, variable_values=params)
    orders = result.get("orders", [])

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for order in orders:
        log_msg = f"{timestamp} - Order ID: {order['id']}, Customer Email: {order['customer']['email']}"
        logging.info(log_msg)

    print("Order reminders processed!")
except Exception as e:
    logging.error(f"Error processing order reminders: {e}")

