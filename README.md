# REST-API
"""
Script para integração com a API do GitHub, utilizando autenticação via token pessoal.

Este código realiza uma conexão autenticada com a API oficial do GitHub,
faz uma varredura em todas as páginas de repositórios do usuário logado
e exporta as informações principais de cada repositório para um arquivo CSV.

📌 Funcionalidades principais:
1. Lê o token de autenticação armazenado na variável de ambiente `GITHUB_TOKEN`.
2. Estabelece comunicação segura com a API do GitHub utilizando a biblioteca `requests`.
3. Realiza requisições paginadas para coletar todos os repositórios do usuário autenticado.
4. Extrai e organiza dados relevantes de cada repositório, incluindo:
   - Nome do repositório
   - Descrição
   - Linguagem principal
   - Número de estrelas (stargazers)
   - Número de forks
   - Data da última atualização
   - Status de privacidade (público/privado)
   - URL do repositório no GitHub
5. Converte os dados obtidos em um DataFrame (`pandas`) e exporta para o arquivo:
   `meus_repos.csv`, localizado na mesma pasta do script.

💡 Dependências:
- requests → para chamadas HTTP à API do GitHub
- pandas → para manipulação e exportação dos dados em formato tabular

✅ Saída:
Um arquivo `meus_repos.csv` contendo todos os repositórios do usuário autenticado
e suas respectivas informações.

Autor: Guilherme Jatobá
"""
