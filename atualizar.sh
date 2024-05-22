#!/bin/bash

echo "Atualizando stack ..."

# Atualizar a stack
aws cloudformation update-stack --stack-name Yobama --template-body file://projeto_aws.yaml --capabilities CAPABILITY_IAM

# Verificar se o comando anterior foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Aguardando atualização..."
    # Aguardar até a atualização estar completa
    aws cloudformation wait stack-update-complete --stack-name Yobama

    # Verificar se a espera foi bem-sucedida
    if [ $? -eq 0 ]; then
        echo "Stack atualizada com sucesso."
    else
        echo "Erro ao aguardar a atualização da stack."
    fi
else
    echo "Erro ao atualizar a stack."
fi
