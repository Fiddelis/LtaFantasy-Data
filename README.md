# 🧙‍♂️ LtaFantasy-Data

Um coletor de dados para o [LTA Fantasy](https://ltafantasy.com), que consome dados via API e exporta as informações em arquivos CSV organizados por tipo de dado.

## 📂 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Recomendação de Equipe Fantasy](#-recomendação-de-equipe-fantasy)
- [Requisitos](#-requisitos)
- [Como Usar](#-como-usar)
- [Estrutura de Diretórios](#-estrutura-de-diretórios)

---

## 📦 Sobre o projeto

Este script permite a coleta de:

- Pontuações dos jogadores (`scores`)
- Dados individuais por jogador (`individual`)
- Estatísticas gerais do mercado (`markets`)

Ideal para análises personalizadas, históricos e visualizações com ferramentas externas (como Excel, Power BI ou notebooks Python).

---

## ⚡ Recomendação de Equipe Fantasy

Esse script também permite gerar a **melhor equipe de Fantasy** com base nas prioridades das roles e no **orçamento disponível**.

### Como utilizar

O arquivo `src/recommendation.py` permite gerar uma equipe de jogadores, selecionando um de cada role, sem ultrapassar o orçamento determinado.

### Exemplo de uso

1. **Rodar o script para gerar a melhor equipe**:
   
   ```bash
   python src/recommendation.py --top 1 --jungle 2 --mid 3 --bottom 2 --support 1 --budget 50
   ```

   Esse comando gera a melhor equipe dentro de um orçamento de 50, levando em consideração as prioridades de cada role.

### Argumentos

| Argumento       | Tipo       | Descrição                                                   |
|-----------------|------------|-------------------------------------------------------------|
| `--top`         | `int`      | Prioridade para o jogador da role `top` (padrão: 1)         |
| `--jungle`      | `int`      | Prioridade para o jogador da role `jungle` (padrão: 1)      |
| `--mid`         | `int`      | Prioridade para o jogador da role `mid` (padrão: 1)         |
| `--bottom`      | `int`      | Prioridade para o jogador da role `bottom` (padrão: 1)      |
| `--support`     | `int`      | Prioridade para o jogador da role `support` (padrão: 1)     |
| `--budget`      | `float`    | Orçamento máximo para a seleção dos jogadores (padrão: 50)  |

### Exemplo de saída

Ao rodar o comando, o script irá exibir a melhor equipe encontrada:

```
Best team (budget ≤ 50):

    Role   | Name             | Price   | Priority
   -----------------------------------------------------
    Top    | PlayerTop        | 12.50   | 1
    Jungle | PlayerJungle     | 15.00   | 1
    Mid    | PlayerMid        | 18.00   | 1
    Bottom | PlayerBottom     | 10.00   | 1
    Support| PlayerSupport    | 8.00    | 1

Total price: 50.00
```

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
src/
├── main.py
├── recommendation.py   # Novo script para recomendação de equipe
``` 

---

Essa versão mais simples e direta do README tem a explicação concisa de como usar a funcionalidade de recomendação de time e como executar o script com exemplos claros. Você pode adicionar diretamente essa seção no seu arquivo README para fornecer informações claras aos usuários do seu projeto.

Se precisar de mais algo, é só avisar!
