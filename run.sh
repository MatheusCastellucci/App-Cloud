#!/bin/bash

echo "Iniciando a stack..."

# Start the cloud server
aws cloudformation create-stack --stack-name Yobama --template-body file://projeto_aws.yaml --capabilities CAPABILITY_IAM

echo "Cloud server started"

# Print the output of the command if it is not "none"
output="None"
while [[ $output == "None" ]]; do
    output=$(aws cloudformation describe-stacks --stack-name Yobama --query "Stacks[0].Outputs[?OutputKey=='ALBDNSName'].OutputValue" --output text)
    sleep 1
done

echo "DNS da Stack: $output"

echo "para acessar a aplicação, use o link acima"
    