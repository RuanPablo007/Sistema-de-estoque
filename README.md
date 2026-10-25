
# Sistema de Estoque em Python

## Sobre o projeto

Este projeto consiste no desenvolvimento de um sistema de estoque utilizando a linguagem de programação Python. Seu objetivo é colocar em prática os conhecimentos adquiridos durante os estudos de programação, por meio da construção de uma aplicação que permita cadastrar produtos, validar informações e, futuramente, gerenciar diferentes operações relacionadas ao controle de estoque.

O projeto está sendo desenvolvido de forma progressiva, dividido em etapas que aumentam gradualmente em complexidade. Dessa maneira, cada funcionalidade é implementada à medida que novos conceitos são estudados e compreendidos.

Além de servir como uma ferramenta de aprendizado, este projeto tem como finalidade desenvolver habilidades importantes para a programação, como raciocínio lógico, resolução de problemas, organização de código e compreensão das estruturas fundamentais da linguagem Python.

## Objetivos

Os principais objetivos deste projeto são:

- Praticar os fundamentos da linguagem Python.
- Desenvolver o raciocínio lógico por meio de problemas práticos.
- Aprender a receber, processar e apresentar informações.
- Implementar validações para evitar dados inválidos.
- Aprender a organizar e manipular informações de produtos.
- Desenvolver gradualmente um sistema de gerenciamento de estoque.
- Aplicar novos conceitos de programação conforme o avanço dos estudos.
- Construir um projeto prático para acompanhar a evolução no aprendizado.

## Funcionalidades atuais

Até o momento, o sistema permite:

- Receber o nome de um produto.
- Solicitar o preço unitário.
- Informar a quantidade disponível em estoque.
- Calcular o valor total do estoque de um produto.
- Validar o nome do produto, impedindo que fique vazio.
- Verificar se o preço informado é maior que zero.
- Impedir o cadastro de quantidades negativas.
- Exibir as informações do produto quando os dados são válidos.

O sistema ainda se encontra em fase inicial de desenvolvimento. Novas funcionalidades serão adicionadas conforme o aprendizado de novos conceitos de Python.

## Tecnologias utilizadas

### Python

A linguagem Python é utilizada para desenvolver toda a lógica do sistema. Sua sintaxe permite trabalhar com variáveis, estruturas condicionais, operações matemáticas e manipulação de dados.

### Visual Studio Code

O Visual Studio Code é utilizado como ambiente de desenvolvimento para escrever, executar, testar e modificar o código-fonte do projeto.

## Conceitos de programação aplicados

### 1. Variáveis

As variáveis são utilizadas para armazenar as informações recebidas pelo programa, como o nome, o preço e a quantidade de cada produto.

### 2. Entrada de dados

A função `input()` permite que o usuário informe os dados necessários para o funcionamento do sistema.

### 3. Tipos de dados

O projeto utiliza diferentes tipos de dados de acordo com a informação armazenada:

- `str`: utilizado para armazenar o nome do produto.
- `float`: utilizado para representar o preço unitário.
- `int`: utilizado para representar a quantidade de unidades.

### 4. Operações matemáticas

O sistema realiza uma multiplicação entre o preço unitário e a quantidade disponível para calcular o valor total do estoque.

### 5. Estruturas condicionais

As estruturas `if`, `elif` e `else` são utilizadas para verificar as informações fornecidas pelo usuário e determinar quais ações devem ser executadas.

### 6. Validação de dados

As validações impedem que informações básicas inválidas sejam aceitas pelo sistema. Entre elas estão a verificação de nomes vazios, preços iguais ou inferiores a zero e quantidades negativas.

### 7. Formatação de saída

As f-strings são utilizadas para apresentar os dados de maneira organizada. A formatação numérica também permite exibir preços com duas casas decimais.

## Exemplo de funcionamento

Durante a execução, o programa solicita as informações de um produto, calcula o valor total em estoque e apresenta os dados ao usuário.

Exemplo de entrada:

```text
Qual é o seu produto? Teclado
Qual é o preço do produto? 80
Qual a quantidade? 5
```

Exemplo de saída:

```text
===== DADOS DO PRODUTO =====
O nome do seu produto é: Teclado
O preço do seu produto é: 80.00
A quantidade é: 5
O valor do estoque é de: 400.00
```

O valor total é calculado multiplicando o preço unitário pela quantidade disponível.

## Etapas de desenvolvimento

O desenvolvimento foi planejado em dez etapas, começando pelos fundamentos da programação e avançando gradualmente para recursos mais complexos.

### Etapa 1 — Cadastro de produtos

Receber o nome, o preço unitário e a quantidade de um produto.

### Etapa 2 — Consulta de informações

Apresentar os dados cadastrados e calcular o valor total correspondente ao estoque do produto.

### Etapa 3 — Validação de dados

Verificar as informações fornecidas pelo usuário e impedir que dados básicos inválidos sejam aceitos.

### Etapa 4 — Cadastro de múltiplos produtos

Estudar listas, dicionários e o método append() para armazenar vários produtos.

### Etapa 5 — Menu interativo

Implementar um menu de opções que permita navegar pelas funcionalidades do sistema e executar diferentes operações.

### Etapa 6 — Entrada e saída de estoque

Adicionar funcionalidades para registrar a entrada de mercadorias e a retirada de unidades, respeitando as quantidades disponíveis.

### Etapa 7 — Edição e exclusão de produtos

Permitir localizar produtos, atualizar suas informações e removê-los do cadastro.

### Etapa 8 — Persistência de dados

Estudar arquivos e JSON para salvar as informações e recuperá-las quando o programa for executado novamente.

### Etapa 9 — Relatórios e alertas

Desenvolver relatórios sobre o estoque, identificar produtos com poucas unidades e calcular o valor total dos produtos armazenados.

### Etapa 10 — Banco de dados e organização

Estudar SQLite, comandos SQL, tratamento de exceções e organização do código em módulos para tornar a aplicação mais estruturada e confiável.

As etapas representam o planejamento do projeto. As funcionalidades serão consideradas concluídas à medida que forem implementadas e testadas.

## Aprendizados

O desenvolvimento deste projeto proporciona a oportunidade de aprender programação por meio da prática, permitindo observar como conceitos individuais podem ser combinados para resolver um problema concreto.

Durante o processo, o foco está em compreender a lógica de cada funcionalidade, identificar erros, testar diferentes situações e melhorar o código de forma gradual.

O projeto também serve como registro da evolução dos estudos em Python e como base para aplicações mais complexas no futuro.

## Status do projeto

**Em desenvolvimento.**

O sistema está em sua fase inicial, com funcionalidades básicas de cadastro, cálculo e validação de dados. O desenvolvimento continuará conforme o avanço nos estudos de Python.

## Próximos passos

- Aprimorar as validações de entrada.
- Estudar listas e dicionários.
- Implementar o armazenamento de múltiplos produtos.
- Criar um menu interativo.
- Adicionar funcionalidades de movimentação de estoque.
- Implementar persistência de dados.
- Desenvolver relatórios.
- Integrar um banco de dados.

## Autor

Desenvolvido por **Ruan Pablo** como projeto prático de estudos em Python.

O objetivo é aprimorar continuamente os conhecimentos em programação por meio da construção de projetos e da implementação gradual de novas funcionalidades.
