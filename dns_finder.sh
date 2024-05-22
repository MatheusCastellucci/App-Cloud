#!/bin/bash
# dns_finder.sh
# Example script to get the DNS
# Replace this with the actual command to retrieve your DNS

aws cloudformation describe-stacks --stack-name yobama --query "Stacks[0].Outputs[?OutputKey=='ALBDNSName'].OutputValue" --output text