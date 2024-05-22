#!/bin/bash

echo "Destruindo a stack..."

# Deletar a stack
aws cloudformation delete-stack --stack-name Yobama

# Verificar se o comando delete-stack foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Esperando a stack ser destruída..."

    # Esperar até que a stack seja completamente deletada
    aws cloudformation wait stack-delete-complete --stack-name Yobama

    # Verificar se a espera foi bem-sucedida
    if [ $? -eq 0 ]; then
        echo "Stack destruída com sucesso."
        echo "Como você pôde, Demay."
    else
        echo "Erro ao esperar a destruição da stack."
    fi
else
    echo "Erro ao deletar a stack."
fi
