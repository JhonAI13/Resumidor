# Resumidor de Texto em Python Puro

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 📖 Descrição

Este projeto é uma implementação de um resumidor de textos em Português, desenvolvido inteiramente em **Python puro**, sem a necessidade de instalar qualquer biblioteca ou dependência externa. A ideia foi criar, do zero, um algoritmo de sumarização extrativa, que identifica e seleciona as frases mais relevantes de um texto para compor um resumo coeso.

Fiz questão de não utilizar bibliotecas como NLTK, SpaCy ou qualquer outra ferramenta de NLP, para demonstrar a lógica fundamental por trás do processo de sumarização, utilizando apenas as funcionalidades nativas do Python.

## ✨ Funcionalidades

*   **Sumarização Extrativa**: O resumo é criado pela extração das frases mais significativas do texto original.
*   **Zero Dependências**: O script roda em qualquer ambiente que tenha Python 3 instalado, sem a necessidade de `pip install`.
*   **Processamento de Texto**: Inclui funções para limpeza de texto, como remoção de pontuação e *stopwords* (palavras comuns como 'a', 'de', 'o').
*   **Cálculo de Relevância**: A importância de cada frase é calculada com base na frequência das palavras que ela contém.

## 🚀 Como Usar

Para utilizar este resumidor, basta seguir os passos abaixo:

1.  **Clone o repositório ou copie o código** para um arquivo Python (`.py`) em sua máquina.

2.  **Abra o arquivo** em um editor de texto ou IDE de sua preferência.

3.  **Substitua o conteúdo da variável `texto`** pelo texto que você deseja resumir.


```python
# Seu texto de entrada
texto = """O que é Python?
Python é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica, projetada 
para enfatizar o esforço do programador. A linguagem, lançada por Guido van Rossum em 1991, destaca 
a importância da eficiência do programador sobre a do computador. Sua sintaxe é simples, clara e 
legível, tornando-a uma excelente linguagem de programação para iniciantes. A tipagem dinâmica e o 
alto nível de abstração são características essenciais da linguagem.
"""
# Gera e imprime o resumo
resumo = gerar_resumo(texto)
print(resumo)
```
5.  O resumo gerado será impresso no console.

```dash
Python é uma linguagem de programação de alto nível, interpretada e de tipagem dinâmica, projetada 
para enfatizar o esforço do programador.
```

## ⚙️ Como Funciona

O algoritmo segue uma abordagem clássica de sumarização extrativa, dividida nas seguintes etapas:

1.  **Divisão em Frases**: O texto de entrada é primeiramente segmentado em uma lista de frases.
2.  **Limpeza e Tokenização**: O texto completo é processado para remover toda a pontuação e as *stopwords* (palavras de parada).
3.  **Cálculo de Frequência de Palavras**: O script conta a frequência de cada palavra significativa no texto. Palavras mais frequentes são consideradas mais importantes.
4.  **Pontuação de Frases**: Cada frase recebe uma pontuação. Essa pontuação é a soma das frequências das palavras que a compõem.
5.  **Seleção do Resumo**: As frases com as maiores pontuações são selecionadas para formar o resumo final. A quantidade de frases no resumo é definida dinamicamente com base no tamanho do texto original.

## 👨‍💻 Autor
Trabalho realizado por **Jonathas Martins da Rocha**.
Conecte-se comigo e explore mais projetos:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jonathas-rocha/)
[![Portfólio](https://img.shields.io/badge/Portf%C3%B3lio-000000?style=for-the-badge&logo=linkedin&logoColor=white)](https://jonathasmartinsdata.my.canva.site/)

