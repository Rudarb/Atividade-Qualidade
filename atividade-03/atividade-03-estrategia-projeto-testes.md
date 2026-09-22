# Atividade 3: Estratégia e Projeto de Testes do LocalEats

> Substituam os campos entre colchetes pelas respostas da equipe e removam as instruções antes da entrega.

## 1. Identificação

**Turma:** [Qualidade de software noite]  
**Equipe:** []  
**Data:** [dd/mm/aaaa]

### Integrantes

| Nome | Usuário no GitHub |
|---|---|
| [Rudá] | [@Rudarb] |

**Elemento de Competência:** Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

---

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

[Verificar se quando o usuário realiza um pedido os itens sao calculados corretamente, se o pedido é registrado uma única vez, se é apresentado na conta do usuário e pode ser visto]

### 2.2 Escopo

#### Funcionalidades incluídas

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| [Ruda] | [Fazer pedido] | [carrinho, confirmação e consulta] |




#### Funcionalidade não incluída

| Funcionalidade não incluída | Justificativa |
|---|---|
| [Favoritar restaurantes] | [a personalização, não interfere diretamente na transação de compra] |

### 2.3 Abordagem

| Item | Decisão da equipe | Justificativa |
|---|---|---|
| Níveis de teste | [Integração, Sistema e Aceitação] | [ pedido depende da comunicação entre frontend, backend e persistência.] |
| Tipos de teste | [Funcional e Não funcional.] | [Priorizar testes funcionais como as regras do pedido e complementar com não funcionais como tempo de confirmação e segurança.] |
| Perspectiva caixa-preta ou caixa-branca | [Caixa-preta e Caixa-branca] | [Caixa-preta para validar entradas e saídas visíveis ao usuário; caixa-branca para testar as falhas críticasa ] |
| Técnicas de teste | [Aplicar partição de equivalência, valor limite e teste de estado] | [O pedido envolve combinações de itens disponíveis, autenticação, formas de pagamento] |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | [navegador com acesso a internet e um login na aplicação] |
| Responsáveis pelo planejamento | [QA, PO, Dev] |
| Responsáveis pela especificação dos casos | [QA, PO, Dev] |
| Responsáveis pela futura execução | [Qa, Dev, PO, DevOps] |

### 2.5 Critérios

| Critério | Definição da equipe |
|---|---|
| Entrada | [Restaurantes cadastrados, funcionalidade fazer pedido, formas de pagamento configuradas e conta de teste criada] |
| Saída | [ Nenhum defeito crítico ou alto estiver aberto, defeitos médios e baixos avaliados e aceitos pelo PO, consultas funcionando e aprovação do DevOps] |
| Suspensão | [o ambiente estiver indisponível ou instável] |

---

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos


| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|:---:|:---:|:---:|---|
| R01 | [Ruda] | [Fazer pedido] | [Pedido duplicado] | [Cliente cobrado duas vezes] | [Média] | [Alto] | [Baixa/Média/Alta] | [Critica ] |[Impacto financeiro e reputacional direto para cliente]|
| R02 | [Ruda] | [Fazer pedido] | [Cálculo incorreto no total] | [Cliente paga o valor errado] | [Média] | [Alto] | [Alta] | [Erros de cálculo são frequentes e afetam tanto o comercio quanto o cliente] |


### 3.2 Aplicação das técnicas


#### Análise do integrante

**Integrante:** [Ruda]  
**Funcionalidade:** [Fazer pedido]  
**Risco relacionado:** [R01]  
**Técnica escolhida:** [tabela de decisão]

**Por que a técnica foi escolhida:**  
[Tabela de decisão permite mapear as combinações de condições.]

**Aplicação da técnica:**  
| Usuário clicou em "finalizar pedido"? | Existe requisição de pedido em andamento?| Última requisição retornou sucesso? |
| [sim] | [não] | [Não se aplica] | [Enviar novo pedido] |
| [sim] | [Sim] | [Não se aplica] | [Bloquear novo envio e desabilitar botão] |
| [sim] | [não] | [sim] | [Bloquear novo envio e desabilitar botão e redirecionar para consulta do pedido] |

**Casos derivados:** [CT01: Clique único, sem requisição em andamento, pedido enviado uma única vez.

CT02: Duplo clique rápido, apenas um pedido enviado; segundo clique bloqueado.

CT03: Clique após confirmação de sucesso, nenhum novo pedido; redireciona para consulta]

---

## 4. Tarefa 3: Casos de teste e rastreabilidade

### 4.1 Casos de teste


### CT01: [ Realizar pedido com clique único]

**Integrante responsável:** [Ruda]  
**Funcionalidade:** [Fazer pedido]  
**Risco ou requisito relacionado:** [R01]  
**Técnica utilizada:** [tabela de decisão]

**Pré-condição:**  
[Usuário com conta válida, carrinho com pelo menos um item, usuário na tela de rivisão]

**Dados de entrada:**  
[Restaurante: “Exemplo”. Item: “Prato Executivo” – R$ 25,00. Forma de pagamento: Cartão de crédito. Endereço de entrega preenchido]

**Passos:**

1. [Acessar o carrinho e conferir os itens selecionados.]
2. [Clicar uma única vez no botão “Finalizar Pedido”.]
3. [Aguardar o processamento e observar a resposta do sistema.]

**Resultado esperado:**  
[O sistema exibe o indicador de carregamento durante o processamento e o pedido é registrado uma única vez no banco de dados. O usuário é redirecionado para a tela de confirmação]

---

### CT02: [Impedir pedido duplicado]

**Integrante responsável:** [Ruda]  
**Funcionalidade:** [Fazer pedido]  
**Risco ou requisito relacionado:** [R02]  
**Técnica utilizada:** [tabela de decisão]

**Pré-condição:**  
[Usuário com conta válida, carrinho com itens válidos e restaurante selecionado.]

**Dados de entrada:**  
[Restaurante: “Exemplo”. Item: “Prato Executivo” – R$ 25,00. Forma de pagamento: Cartão de crédito. Endereço de entrega preenchido]

**Passos:**

1. [Clicar rapidamente duas vezes seguidas no botão “Finalizar Pedido”.]
2. [Observar o comportamento do botão e do sistema durante o processamento.]
3. [Verificar no banco de dados ou na tela de pedidos quantos pedidos foram registrados.]

**Resultado esperado:**  
[O botão é desabilitado imediatamente após o primeiro clique. Apenas uma requisição é enviada ao backend e somente um pedido é registrado no banco de dados.]

---

### CT03: [Validar cálculo do total do pedido]

**Integrante responsável:** [nome]  
**Funcionalidade:** [Fazer pedido]  
**Risco ou requisito relacionado:** [R03]  
**Técnica utilizada:** [Partição de equivalência]

**Pré-condição:**  
[Usuário com conta válida, Taxa de entrega configurada  e restaurante selecionado]

**Dados de entrada:**  
[tre itens do menu item A (R$10), item B (R$20), item C (R$30), taxa de entrega de R$5 e cupom de desconto de 10%]

**Passos:**

1. [Adicionar o Item A ao carrinho e verificar o subtotal, Total esperado: R$ 15,00.]
2. [Adicionar o Item B ao carrinho, Total esperado: R$ 30,00.]
3. [Adicionar o Item C ao carrinho, Total esperado:R$ 60,00 aplicando cupom total R$54,00]

**Resultado esperado:**  
[O sistema calcula corretamente o subtotal, a taxa de entrega e o desconto em cada combinação,o usuário visualiza o detalhamento dos valores antes de finalizar o pedid]

---



### 4.2 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| [Ruda] | [Fazer pedido] | [R01:Realizar pedido com clique único] | [Tabela de decisão] | [CT01 e CT02] |


---

## 5. Uso de inteligência artificial

**Ferramenta utilizada:**  
[Informar a ferramenta ou registrar “não utilizada”.]

**Como foi utilizada:**  
[Descrever brevemente.]

**Uma sugestão que precisou ser alterada ou rejeitada:**  
[Descrever brevemente. Caso nenhuma sugestão tenha sido rejeitada, expliquem como as sugestões foram analisadas criticamente.]

**Como as respostas foram verificadas:**  
[Descrever brevemente.]
