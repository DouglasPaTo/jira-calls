#!/bin/bash

echo "=== Reiniciando Jira Reports ==="

# Parar servidor existente
if pgrep -f "uvicorn app.main:app" > /dev/null; then
    echo "Parando servidor..."
    pkill -f "uvicorn app.main:app"
    sleep 1
fi

# Iniciar servidor
source venv/bin/activate
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > logs/server.log 2>&1 &
PID=$!

echo "Servidor reiniciado com PID: $PID"
echo "Acesse: http://localhost:8000"
echo "Logs: logs/server.log"