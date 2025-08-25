#!/bin/bash
# Script to clean inactive customers

LOG_FILE="/tmp/customer_cleanup_log.txt"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Navigate to project directory
cd "$(dirname "$0")/../.." || exit 1

# Run Django shell command to delete inactive customers
DELETED_COUNT=$(python3 manage.py shell <<EOF
from datetime import datetime, timedelta
from crm.models import Customer

cutoff = datetime.now() - timedelta(days=365)
deleted, _ = Customer.objects.filter(last_order_date__lt=cutoff).delete()
print(deleted)
EOF
)

# Log result
echo "\$TIMESTAMP - Deleted \$DELETED_COUNT inactive customers" >> "\$LOG_FILE"

