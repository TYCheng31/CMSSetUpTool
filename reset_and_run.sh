#!/bin/bash

echo "=================================================="
echo "🚀 Starting fully automated CMS reset and setup process"
echo "=================================================="

echo "⚠️ WARNING: This will erase ALL CMS databases and files!"
echo "Starting in 3 seconds... (Press Ctrl+C to abort)"
sleep 3

echo -e "\n[1/5] Clearing old database and files..."
sudo rm -rf /var/local/lib/cms
yes | sudo cmsDropDB  

echo -e "\n[2/5] Initializing a fresh CMS database..."
sudo cmsInitDB

echo -e "\n[3/5] Creating default admin account (admin/admin)..."
cmsAddAdmin admin -p admin

echo -e "\n[4/5] Running Integrated Python Script (Creates & Configures)..."
source tool_env/bin/activate
python Auto.py
deactivate

echo -e "\n[5/5] Batch creating user accounts and adding to contest (Default Contest ID: 1)..."
while IFS=, read -r username password; do
    [ -z "$username" ] && continue
    username=$(echo "$username" | xargs)
    password=$(echo "$password" | xargs)
    
    echo "  -> Adding user: $username"
    cmsAddUser "$username" "$username" "$username" -p "$password"
    cmsAddParticipation -c 1 "$username"

done <<EOF
S01,tsqpmd5p99
S02,kkciy9nx4f
S03,g3rgapug7v
EOF

echo "=================================================="
echo "🎉 All processes completed! The CMS system is ready."
echo "=================================================="