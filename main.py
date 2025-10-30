import os
import requests
import pandas as pd

# --- CONFIGURAÇÃO ---
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("⚠️ GITHUB_TOKEN não definido nas variáveis de ambiente!")

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# --- FUNÇÃO PARA PEGAR REPOSITÓRIOS DO USUÁRIO AUTENTICADO ---
def list_my_repos():
    url = "https://api.github.com/user/repos"
    params = {"per_page": 100, "page": 1}
    repos = []

    while True:
        r = requests.get(url, headers=headers, params=params)
        print(f"Status {r.status_code} | Página {params['page']}")
        r.raise_for_status()

        data = r.json()
        if not data:
            break

        repos.extend(data)
        params["page"] += 1

    return repos

# --- EXECUÇÃO ---
repos = list_my_repos()

# --- CONVERTE PARA DATAFRAME E EXPORTA ---
dados = [{
    "Nome": repo["name"],
    "Descrição": repo["description"],
    "Linguagem": repo["language"],
    "Estrelas": repo["stargazers_count"],
    "Forks": repo["forks_count"],
    "Atualizado em": repo["updated_at"],
    "Privado": repo["private"],
    "URL": repo["html_url"]
} for repo in repos]

df = pd.DataFrame(dados)
df.to_csv("meus_repos.csv", index=False, encoding="utf-8-sig")

print(f"✅ Exportado com sucesso! Total: {len(df)} repositórios.")
