#!/bin/bash
# dns_finder.sh
# Example script to get the DNS

dns_name=$(aws cloudformation describe-stacks --stack-name yobama --query "Stacks[0].Outputs[?OutputKey=='ALBDNSName'].OutputValue" --output text)

if [ $? -eq 0 ]; then
    echo "ALB DNS Name: $dns_name"
else
    echo "Failed to get ALB DNS Name."
fi
