# Projeto Jira Reports - Estrutura de Arquivos

## Visão Geral
- **Frontend**: Jinja2 + Tailwind CSS (CDN) + vanilla JS
- **Backend**: FastAPI + SQLite
- **Database**: `app/jira_reports.db`

## Estrutura de Diretórios

```
new-jreport/
├── app/                          # Aplicação principal
│   ├── main.py                   # Entry point FastAPI
│   ├── routers/                  # Rotas da aplicação
│   │   ├── web.py                # Dashboard, filtros, export
│   │   └── auth.py               # Login, usuários
│   ├── services/                 # Integração Jira
│   │   └── jira_service.py       # API Jira
│   ├── db/                       # Banco de dados
│   │   ├── session.py            # Config SQLite
│   │   └── models.py             # Modelos (Ticket, User)
│   ├── templates/                # Templates HTML
│   │   ├── base.html             # Layout base
│   │   ├── login.html            # Login
│   │   ├── dashboard.html        # Dashboard + filtros
│   │   ├── usuarios.html         # Gerenciamento usuários
│   │   └── report.html           # Template exportação HTML
│   ├── static/                   # Arquivos estáticos
│   │   ├── logo.png              # Logo do relatório
│   │   └── favicon/              # Favicon
│   └── config/
│       └── settings.py           # Configurações .env
├── logs/                         # Logs do servidor
├── .env                          # Variáveis de ambiente
├── start.sh                      # Iniciar servidor
├── stop.sh                       # Parar servidor
├── restart.sh                    # Reiniciar servidor
├── setup.sh                      # Setup inicial
├── README.md                     # Documentação
└── requirements.txt              # Dependências Python
```

## Descrição dos Arquivos Principais

### app/main.py
- Configuração do FastAPI
- Middleware de sessão
- Template Jinja2
- Static files

### app/routers/web.py
- Dashboard principal (`/`)
- Filtros por data, organização, label, responsável
- Atualização de tickets do Jira (`/atualizar`)
- Exportação HTML (`/exportar`)

### app/routers/auth.py
- Login (`/login`)
- Logout (`/logout`)
- Gerenciamento usuários (`/usuarios`)

### app/services/jira_service.py
- `get_jira_auth()` - Autenticação
- `fetch_done_tickets()` - Busca tickets done do Jira
- `extract_ticket_data()` - Extrai dados do ticket

### app/templates/report.html
- Template de exportação HTML
- Estatísticas, resumo de horas, detalhamento de tickets
- JavaScript para cálculo de valores

## Rotas Web

| Rota | Descrição |
|------|-----------|
| `/` | Dashboard com filtros e lista de tickets |
| `/login` | Página de login |
| `/logout` | Logout |
| `/usuarios` | Gerenciar usuários |
| `/atualizar` | Atualizar tickets do Jira |
| `/exportar` | Exportar relatório HTML |

## Variáveis de Ambiente (.env)

| Variável | Descrição |
|----------|-----------|
| JIRA_URL | URL do Jira |
| JIRA_EMAIL | Email de acesso |
| JIRA_API_TOKEN | Token API do Jira |
| SECRET_KEY | Chave para sessões |