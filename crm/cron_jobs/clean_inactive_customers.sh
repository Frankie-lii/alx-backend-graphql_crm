#!/bin/bash
# Shell script to delete customers with no orders since a year ago

LOG_FILE="/tmp/customercleanuplog.txt"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Navigate to project root (adjust path if needed)
cd "$(dirname "$0")/../.." || exit 1

# Run Django shell command to delete inactive customers
python3 manage.py shell <<EOF
from datetime import datetime, timedelta
from crm.models import Customer

cutoff = datetime.now() - timedelta(days=365)
deleted_customers = Customer.objects.filter(last_order_date__lt=cutoff)
deleted_customers.delete()
EOF

# Log execution
echo "$TIMESTAMP - Inactive customers cleanup executed" >> "$LOG_FILE"

