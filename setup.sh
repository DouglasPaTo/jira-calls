#!/bin/bash

echo "=== Jira Reports - Setup ==="

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "Instalando Python..."
    sudo apt update && sudo apt install -y python3 python3-pip python3-venv
fi

# Verificar e remover banco de dados existente
if [ -f "app/jira_reports.db" ]; then
    echo "Removendo banco de dados existente..."
    rm -f app/jira_reports.db
    echo "Banco de dados antigo removido!"
fi

# Criar pastas necessárias
echo "Criando pastas..."
mkdir -p logs
mkdir -p app/static/favicon

# Criar ambiente virtual
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências Python
echo "Instalando dependências Python..."
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy aiosqlite asyncpg psycopg2-binary python-dotenv requests passlib bcrypt==4.0.1 jinja2 python-multipart itsdangerous

echo ""
echo "=== Setup concluído! ==="
echo ""
echo "Para rodar o servidor:"
echo "  source venv/bin/activate"
echo "  uvicorn app.main:app --reload"
echo ""
echo "Acesse: http://127.0.0.1:8000"
echo "Login: usrking / MortySeiya!"
echo ""
echo "O banco de dados SQLite será criado automaticamente na pasta do projeto."
