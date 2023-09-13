### Tutorial de Raspagem Web com Python: Capturando Dados de Pokémon com BeautifulSoup4

#### Pré-requisitos:

1. Python instalado no seu sistema.
2. pip (Instalador de pacotes Python).

#### Passo 1: Instalando os Pacotes Necessários


```bash 
pip install requests beautifulsoup4
```

#### Passo 2: Importando as Bibliotecas

Inicie seu script importando as bibliotecas necessárias:

```pyton
import requests
from bs4 import BeautifulSoup
```

#### Passo 3: Definindo a URL da Página a Ser Raspada

```python
URL = 'https://pokemondb.net/pokedex/all'
```
#### Passo 4: Obtendo o Conteúdo HTML da Página

Nós usaremos a biblioteca `requests` para obter o conteúdo HTML da página:

```python
response = requests.get(URL)
response.raise_for_status()  # Isso lançará uma exceção para erros HTTP
```

Quando você faz uma requisição com a biblioteca `requests` em Python, você recebe uma resposta, e essa resposta possui várias propriedades. Duas propriedades comuns que são usadas para acessar o corpo da resposta são:

- `response.text`: Retorna o conteúdo da resposta, em formato Unicode. É útil quando você está lidando com páginas web que retornam texto.
    
- `response.content`: Retorna o conteúdo da resposta em bytes. Isso é particularmente útil se você estiver fazendo o download de conteúdo não-textual, como imagens ou arquivos binários. No entanto, também pode ser usado para conteúdo textual para garantir que nada seja perdido na conversão para Unicode.

Em muitos casos de raspagem web, `response.text` e `response.content` podem ser usados de forma intercambiável. No entanto, usar `response.content` é uma maneira segura de garantir que você está capturando todo o conteúdo exatamente como ele foi enviado pelo servidor.
#### Passo 5: Analisando o Conteúdo com BeautifulSoup

Uma vez que você tem o conteúdo da página, você pode analisá-lo usando BeautifulSoup:

```python
soup = BeautifulSoup(response.content, 'html.parser')
```

O `BeautifulSoup` precisa de um parser para interpretar e navegar no documento HTML ou XML que você passou para ele. Existem vários parsers que o BeautifulSoup suporta:

- `'html.parser'`: É um parser incluído na biblioteca padrão do Python. É decentemente rápido e requer poucas dependências externas.
    
- `'lxml'`: É um parser externo que é muito mais rápido que o `'html.parser'`. Para usar o lxml com BeautifulSoup, você precisa instalar o lxml separadamente.
    
- `'html5lib'`: É outro parser externo que é útil se você precisa analisar páginas que são escritas em HTML5, mas é geralmente mais lento que os outros.
    

O argumento `'html.parser'` está dizendo ao BeautifulSoup para usar o parser incluído no Python para interpretar o documento HTML. Se você estiver raspando um grande volume de páginas ou precisar de uma velocidade extra, pode considerar a instalação e utilização do lxml, que é geralmente mais rápido.

Em resumo, a linha `soup = BeautifulSoup(response.content, 'html.parser')` está criando um objeto BeautifulSoup a partir do conteúdo da resposta da página web, usando o parser padrão do Python para interpretar o documento HTML.
#### Passo 6: Localizando a Tabela de Dados dos Pokémon

A página possui uma tabela que contém os dados dos Pokémon. Precisamos localizar essa tabela:

```python
pokemon_table = soup.find('table', id='pokedex')
```

#### Passo 7: Extraindo as Linhas da Tabela

Cada linha (`tr`) da tabela representa um Pokémon:

```python
pokemon_rows = pokemon_table.tbody.find_all('tr')
```

#### Passo 8: Capturando os Dados de Cada Pokémon

Itere sobre cada linha, extraia os detalhes e armazene-os em uma lista:

```python
pokemons = []

for row in pokemon_rows:
    columns = row.find_all('td')
    
    number = columns[0].text.strip()
    name = columns[1].text.strip()
    type_ = columns[2].text.strip()
    total = columns[3].text.strip()
    hp = columns[4].text.strip()
    attack = columns[5].text.strip()
    defense = columns[6].text.strip()
    sp_atk = columns[7].text.strip()
    sp_def = columns[8].text.strip()
    speed = columns[9].text.strip()
    
    pokemon_data = {
        'Número': number,
        'Nome': name,
        'Tipo': type_,
        'Total': total,
        'HP': hp,
        'Ataque': attack,
        'Defesa': defense,
        'Ataque Especial': sp_atk,
        'Defesa Especial': sp_def,
        'Velocidade': speed
    }
    
    pokemons.append(pokemon_data)

```


#### Passo 9: Testando a Raspagem

Para verificar se tudo está funcionando como esperado, imprima os dados dos primeiros cinco Pokémon:

```python
for pokemon in pokemons[:5]:
    print(pokemon)

```

#### Passo 10: Executando o Script

```bash
python poke_scrapper.py
```

Você deve ver os dados dos primeiros cinco Pokémon impressos no console.