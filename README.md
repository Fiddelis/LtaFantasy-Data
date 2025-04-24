# 🧙‍♂️ LtaFantasy-Data

Um coletor de dados para a Fantasy da LTA (Liga de Torneios Amadores), que consome dados via API e exporta as informações em arquivos CSV organizados por tipo de dado.

## 📦 Sobre o projeto

Este script permite a coleta de:

- Pontuações dos jogadores (`scores`)
- Dados individuais por jogador (`individual`)
- Estatísticas gerais do mercado (`markets`)

Ideal para análises personalizadas, históricos e visualizações com ferramentas externas (como Excel, Power BI ou notebooks Python).

---

## ⚙️ Requisitos

- Python 3.10+
- Instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

### Comando base

```bash
python src/main.py [--data <tipo>] [--player_id <id1> <id2> ...] [--path <caminho>]
```

### Argumentos

| Argumento       | Tipo       | Descrição                                                                                  |
|-----------------|------------|--------------------------------------------------------------------------------------------|
| `--data`        | `str`      | Tipo de dado a ser coletado: `scores`, `individual` ou `markets`. Se omitido, executa todos. |
| `--player_id`   | `str`      | Um ou mais IDs de jogadores. Somente se `--data` for `individual`.                    |
| `--path`        | `str`      | Caminho onde os arquivos CSV serão salvos. Padrão: `./data`                                |

---

### Exemplos

✅ Coletar tudo:
```bash
python src/main.py
```

✅ Coletar apenas pontuações:
```bash
python src/main.py --data scores
```

✅ Coletar dados individuais de jogadores específicos:
```bash
python src/main.py --data individual --player_id d3034265-e29a-4ba3-91cc-a69f20af0cb0 ...
```

✅ Salvar os arquivos em outro diretório:
```bash
python src/main.py --path output/
```

---

## 📂 Estrutura de diretórios

Após a execução, os dados serão salvos organizados assim:

```
data/
├── market/
│   └── round_name/
│       ├── infos.csv
│       ├── teams.csv
│       └── players.csv
├── players/
│   └── role/
│       └── player_name/
│           ├── infos.csv
│           ├── games.csv
│           ├── recentMatches.csv
│           └── upcomingMatches.csv
├── score_split_name.csv
```