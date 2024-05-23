#!/bin/bash

echo "Iniciando a stack..."
# Start the cloud server
aws cloudformation create-stack --stack-name yobama --template-body file://projeto_aws.yaml --capabilities CAPABILITY_IAM

echo "Esperando a stack ser criada..."
# Print the output of the command if it is not "none"
output=""
while [[ -z $output || $output == "None" ]]; do
    output=$(aws cloudformation describe-stacks --stack-name yobama --query "Stacks[0].Outputs[?OutputKey=='ALBDNSName'].OutputValue" --output text)
    sleep 1
done
echo "Link para o DNS da Stack: $output"
