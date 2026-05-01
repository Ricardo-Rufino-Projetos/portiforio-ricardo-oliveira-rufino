# 🎨 Desenhando Emojis com Dados

## 📝 Descrição do Projeto

Este projeto explora a representação visual de emojis e imagens por meio de estruturas de dados em Python. O objetivo principal é entender como matrizes, dicionários e listas podem ser utilizados para armazenar, manipular e renderizar informações visuais baseadas em pixels RGB.

Desenvolvido como parte de estudos em **Python e Estrutura de Dados**, o projeto utiliza conceitos de iteração sobre coleções aninhadas para aplicar transformações em imagens pixel a pixel — como escurecimento de cores, inversão de canal RGB e transposição de matrizes — culminando na renderização visual com a biblioteca Matplotlib.

## 🚀 Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Biblioteca:** Matplotlib

## 📁 Estrutura do Projeto

```
projeto-desenhando-emojis-com-dados/
├── criador-de-emojis-(pixels-rgb).py       # Criação e transformação de emojis via grade de pixels RGB
├── integrador-(criação-livre).py           # Manipulação de playlists de imagens com inversão de cores
└── matrizes-musicais-(transposição).py     # Transposição de matrizes musicais e transformação de pixels
```

## 🔍 Detalhes dos Módulos

**`criador-de-emojis-(pixels-rgb).py`**
Define um emoji "Smile" como uma grade 5×5 de tuplas RGB. Percorre cada pixel e aplica uma transformação de escurecimento (divisão por 2 nos canais amarelos), exibindo o resultado com `plt.imshow()`.

**`integrador-(criação-livre).py`**
Itera sobre uma playlist de imagens armazenadas em dicionários. Remove o último pixel de cada imagem, inverte os canais RGB de todos os pixels restantes (`255 - valor`) e insere um pixel cinza neutro no início da lista.

**`matrizes-musicais-(transposição).py`**
Transpõe matrizes de frequências musicais (linhas → colunas) e aplica a mesma lógica de inversão de pixels RGB em uma playlist de imagens que representa cenas como "Sol" e "Noite".

## 📊 Conceitos Trabalhados

- Representação de imagens como matrizes de tuplas RGB
- Iteração sobre estruturas de dados aninhadas (dicionários, listas, tuplas)
- Transformações pixel a pixel: escurecimento, inversão de cor, inserção e remoção
- Transposição de matrizes usando índices
- Renderização de imagens com `matplotlib.pyplot.imshow()`

## 🔧 Como Executar

1. Clone o repositório.
2. Instale a dependência necessária:
   ```bash
   pip install matplotlib
   ```
3. Execute o arquivo desejado:
   ```bash
   python "criador-de-emojis-(pixels-rgb).py"
   ```

---

[Voltar ao início](https://github.com/seu-usuario/seu-usuario)
