#!/bin/bash

echo "=== Iniciando Jira Reports ==="

# Ativar ambiente virtual
if [ ! -d "venv" ]; then
    echo "Erro: Ambiente virtual não encontrado. Execute ./setup.sh primeiro."
    exit 1
fi

source venv/bin/activate

# Verificar se já está rodando
if pgrep -f "uvicorn app.main:app" > /dev/null; then
    echo "Servidor já está rodando!"
    exit 0
fi

# Iniciar servidor em background
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > logs/server.log 2>&1 &
PID=$!

echo "Servidor iniciado com PID: $PID"
echo "Acesse: http://localhost:8000"
echo "Logs: logs/server.log"
