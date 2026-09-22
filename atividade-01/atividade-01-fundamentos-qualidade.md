# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** [Qualidade de software noite]  
**Equipe:** []  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [Rudá] | [@Rudarb] |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | [Autenticação de usuário] | [Cliente] | [sem a autenticação o usuário não consegue acessar nenhuma funcionalidade interna ] |
| Explícita | [Realizar e Consultar pedidos] | [Cliente] | [cliente nao consegue comprar e o restaurante não vende] |
| Implícita | [Segurança] | [Cliente] | [Vazamentos de dados, acessos indevidos e fraudes] |
| Implícita | [Retorno claro] | [Cliente] | [sem o retorno claro da finalização do pedido podem ocorrer pedidos duplicados e cobranças a mais ao cliente] |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade? Justifiquem utilizando pelo menos uma necessidade implícita identificada pela equipe.**

[ Um sistema pode implementar todas as funcionalidades explícitas e ainda ter baixa qualidade.
Isso porque os requisitos explícitos dizem “o quê” fazer, mas não garantem “como” será feito. Usando de exemplo o retorno claro para o cliente mesmo que implementado se por exemplo no momento do pagamendo o retorno somente levar o usuário para a uma página de continuar pedindo ao invés de uma tela de pagamento realizado.]

---

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| [Rudá] | [Realizando pedido] | [Realizando um login e um pedido] | [Rapido e intuitivo sem muita verificação] | [ver evidência](img/Realizando_pedido.png) |

---

## 4. Tarefa 3: Requisitos e características de qualidade


| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| [Rudá] | [Garantir que cada pedido seja registrado uma vez por tentativa de compra] | [mitigar erro] | [Pedidos duplicados geram cobranças indevidas] | [análise de logs e do banco de dados e monitoramento da taxa de pedidos duplicados.] |


---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Informar a ferramenta ou registrar “não utilizada”.]

**Como foi utilizada:**  
[Descrever brevemente.]

**Como as respostas foram verificadas:**  
[Descrever brevemente.]
