#!/bin/bash

echo "=== Parando Jira Reports ==="

# Verificar se está rodando
if ! pgrep -f "uvicorn app.main:app" > /dev/null; then
    echo "Servidor não está rodando!"
    exit 0
fi

# Parar o processo
pkill -f "uvicorn app.main:app"

echo "Servidor parado!"
