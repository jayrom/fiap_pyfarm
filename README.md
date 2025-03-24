# fiap_pyfarm
A simple python application for farmers.

## Descrição

**FIAP PyFarm** é uma prposta de aplicação desenvolvida como desafio para o curso de Inteligência Artificial da FIAP, turma 1TIAOB, pela **Tião FarmTech Solutions** para impulsionar os recentes esforços de inovação tecnológica da **Fazenda Esperança**, em Ribeirão Preto, SP. 
Inicialmente, FIAP PyFarm oferece as seguintes funcionalidades:

- Cadastro de até duas culturas, sendo uma de amendoim e uma de milho e cálculo da área disponível para plantio a partir dde suas dimensões nominais. 
- Cálculo da quantidade dos insumos necessários à produção de um ano para esas culturas, a partir da área de plantio.

## Premissas

Algumas premissas forma adotadas para a execução do trabalho, a saber:

### Fazenda Esperança

Para caracterizarmos melhor o contexto de uso da aplicação, foi concebida uma propriedade fictícia, a Fazenda Esperança. Localizada na região de Ribeirão Preto, dedica-se atualmente às culturas de amendoim e milho, atendendo a diretrizes estratégicas do negócio. Também as características da propriedade, como o tipo de solo, clima, relevo plano, distribuição de chuvas e estações bem definidas favorecem o plantio dessas culturas.
Dispõe de um bom grau de mecanização e se aproveita da proximidade de artérias importantes, como a Via Anhanguera, para escoamento das safras.

#### Área total e área de plantio

A fazenda possui duas grandes áreas retangulares distintas, separadas por um córrego, utilizado para irrigação.
Devido à disponibilidade de equipamentos modernos para mecanização da lavoura, foi possível minimizar a quantidade de ruas internas, áreas de manobras e movimentação de pessoal, equipamento, insumos e colheita, mantendo a redução de terreno útil historicamente em apenas 10%.

#### Irrigação

Devido ao formato do terreno, os proprietários optaram por utilizar um sistema combinado de gotejamento subterrâneo e aspersão de baixa pressão, que confere maior eficiência no uso da água, assim como distribuição mais eficiente, minimizando perdas por evaporação. O abastecimento de água provém de um córrego que corta a propriedade e divide as duas áreas de plantio.

### Insumos

Os insumos considerados são os mais comuns para as culturas selecionadas. As quantidades definidas são valores médios reais e já consideram as safras de um ano (safras de verão para amendoim e milho e safrinha para milho).

#### Estatísticas de consumo de insumos

Essa seção foi incluída na aplicação Python como um exemplo de funcionalidade a ser mais adequadamente desenvolvida, mas que poderia agregar um valor efetivo ao uso da aplicação.
A partir de dados históricos sobre o consumo de insumos da fazenda, fictícios no Python, informações estatísticas, como as exemplificadas no script R, poderiam ser de grande valia para o agricultor, permitindo estender o levantamento de dados para análises mais acertadas, como cruzamento com dados meteorológicos, análise localizada do solo etc.
Dado o nível limitado de conhecimento sobre as linguagens e o tempo para entrega, a comunicação entre as duas aplicações não foi feita, limitando-se à cópia manual de dados.

### Uso das linguagens

Sem dúvida, muito da solução desenvolvida poderia ser desenvolvida deforma mais simples e eficiente. Por outro lado, devido ao nosso conhecimento limitado das duas linguagens, optamos por empregar apenas os recursos que pudemos praticar nas aulas e alguns poucos desafios adicionais. 

## Requisitos do sistema

As aplicações foram desenvolvidas e testadas utilizando-se os seguintes requisitos:
- Python 3.12.2
- R 4.4.3
- RStudio 2024.12.1 - Build 563

## Como usar

### Aplicação Python

- Em um terminal Python, na pasta onde se encontram os arquivos da solução, rodar:

    `> python.exe pyfarm.py` ou, simplesmente, `> py pyfarm.py`

### Script R

- No RStudio, abrir o arquivo pyfarm.R, pressionar `CTRL + A` e `CTRL + ENTER`. 

## Problemas conhecidos

Alguns problems conhecidos:
- Não há consistência para todas as entradas de dados.

## Integrantes do grupo

- [Edmilson Marciano](https://github.com/marciano64)
- [Jayro Mazzi Junior](https://github.com/jayrom)
- [Leonardo Camacho](leonardocamacho1983)
- [Lucas Arcanjo](https://github.com/ArcanjoLucas00)



