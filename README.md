# 🚀 Jira Reports

Sistema completo e profissional para geração de relatórios de tickets do Jira com filtros avançados e exportação HTML.

## ✨ Por que usar o Jira Reports?

- **🔒 Seguro**: Desenvolvido com FastAPI, um dos frameworks mais modernos e seguros do Python. Autenticação robusta com senhas criptografadas.
- **⚡ Rápido**: Python é sinônimo de velocidade. O sistema processa milhares de tickets em segundos.
- **💾 Robusto**: Banco de dados SQLite significa zero complexidade, mas com poder de crescer, você pode começar simples e escalar quando precisar.
- **🎯 Flexível**: Filtros por projeto, status, organização, responsável, data e muito mais.
- **📊 Profissional**: Relatórios HTML limpos e prontos para impressão ou envio.

## 🎯 Para quem é?

Perfeito para gestores, líderes de equipe e analistas que precisam de relatórios claros e rápidos dos tickets de suporte ou projetos no Jira.

## 📋 Como Configurar

### 1. Credenciais do Jira

Edite o arquivo `.env` com seus dados:

```env
JIRA_URL=https://suaempresa.atlassian.net
JIRA_EMAIL=seu@email.com
JIRA_API_TOKEN=seu_token_aqui
```

### 2. Gerando o Token API

1. Acesse: https://id.atlassian.com/manage-profile/security/api-tokens
2. Clique em "Create API token"
3. Dê um nome (ex: "Jira Reports")
4. Copie o token gerado e cole no `.env`

### 3. Pronto!

Execute `./setup.sh` uma vez e `./restart.sh` para iniciar.

## 💡 Como Usar

1. **Acesse** o sistema pelo navegador
2. **Faça login** com suas credenciais
3. **Atualize** os tickets com os botões "Atualizar Tudo" ou "Atualizar Recentes"
4. **Filtre** pelos campos desejados (projeto, status, organização, responsável, datas)
5. **Exporte** para HTML com um clique

## 🛠️ Stack Tecnológica

| Componente | Tecnologia | Por que? |
|------------|-----------|-----------|
| **Backend** | FastAPI (Python) | Moderno, ultra-rápido, segurança nativa |
| **Banco de Dados** | SQLite | Simples, confiável, não precisa de complexidade |
| **Frontend** | HTML + TailwindCSS | Limpo e responsivo |
| **Servidor** | Uvicorn | Performance industrial-grade |

**Python**: Linguagem mais popular do mundo, conhecida por sua confiabilidade e vasto ecossistema de bibliotecas.

## 📁 Estrutura do Projeto

```
jira-calls/
├── app/
│   ├── main.py              # Entrada do servidor
│   ├── routers/             # Rotas da aplicação
│   │   ├── web.py          # Dashboard e relatórios
│   │   └── auth.py         # Autenticação
│   ├── services/            # Integração com Jira
│   ├── db/                  # Modelos do banco
│   ├── templates/           # Páginas HTML
│   └── static/              # CSS, logo, favicon
├── .env                     # Suas credenciais
├── setup.sh                 # Configuração inicial
├── restart.sh               # Iniciar/reiniciar
└── README.md               # Este arquivo
```

## ⚙️ Scripts Disponíveis

| Comando | O que faz |
|---------|-----------|
| `./setup.sh` | Instala tudo que precisa (Python, dependências) |
| `./start.sh` | Inicia o servidor |
| `./stop.sh` | Para o servidor |
| `./restart.sh` | Reinicia o servidor |

## 🎨 Customização

### Logo do Relatório
Coloque sua logo em: `app/static/logo.png` (200x50px recomendado)

### Favicon
Coloque seu ícone em: `app/static/favicon/favicon.ico` (32x32px recomendado)

O sistema detecta automaticamente!

## 🔐 Segurança

- Senhas criptografadas com BCrypt
- Sessões seguras com chave secreta
- Proteção contra ataques comuns
- Credenciais em arquivo separado

## 📝 Requisitos

- Linux (testado no Ubuntu)
- Python 3.10+
- Acesso à internet (para API do Jira)

## 📄 Licença

MIT License - Use, modifique e distribua à vontade!
