# Atividade 4: Testes Automatizados do LocalEats

---

## 1. Identificação

- **Turma:** Qualidade de software noite
- **Modalidade:** Individual
- **Repositório:** [https://github.com/Rudarb/Atividade-Qualidade]
- **Diretório da atividade:** [https://github.com/Rudarb/Atividade-Qualidade/tree/main/atividade-04]
- **Data da última execução:** [dd/mm/aaaa — preencher ao rodar o comando da seção 6]

### Integrantes

1. Rudá Rosa

---

## 2. Integrantes e responsabilidades

| ID | Integrante responsável | Tipo | Comportamento verificado | Arquivo e função de teste |
|---|---|---|---|---|
| TU01 | Rudá Rosa | Unitário | Quantidade válida (3 itens) retorna `True` | `atividade-4/test_regras_localeats.py::test_qnt_valida_1_e_10` |
| TU02 | Rudá Rosa | Unitário | Quantidade acima de 10  retorna `False` | `atividade-4/test_regras_localeats.py::test_qnt_acima_de_10_retorna_false` |
| TU03 | Rudá Rosa | Unitário | Quantidade negativa gera `ValueError` | `atividade-4/test_regras_localeats.py::test_qnt_negativa_gera_value_error` |
| TU04 | Rudá Rosa | Unitário | Limites 0, 1, 10 e 11 | `atividade-4/test_regras_localeats.py::test_limites_da_quantidade_de_itens` |
| TF01 | Rudá Rosa | Funcional | Página inicial e navegação para "Meus Pedidos" | `atividade-4/test_localeats.py::test_pagina_inicial_e_navegacao_para_meus_pedidos` |


## 3. Testes unitários

### Registro das regras implementadas

#### Regra de Rudá Rosa

- **Regra escolhida:** Regra 3, quantidade de itens
- **Função implementada:** `quantidade_itens_valida(quantidade)`
- **Arquivo da implementação:** `src/regras_localeats.py`
- **Testes criados:** `test_qnt_valida_1_e_10`; `test_qnt_acima_de_10_retorna_false`; `test_qnt_negativa_gera_value_error`; `test_limites_da_quantidade_de_itens`
- **Comportamentos verificados:** quantidades de 1 a 10 retornam `True`; zero e quantidades acima de 10 retornam `False`; quantidades negativas geram `ValueError`.

---

## 4. Aplicação do TDD

### TDD de Rudá Rosa

- **Regra escolhida:** Regra 3, quantidade de itens
- **Primeiro teste escrito:** `test_qnt_valida_1_e_10`
- **Por que o teste falhou inicialmente:** a função e o módulo `src/regras_localeats.py` ainda não existiam; o pytest acusou `ModuleNotFoundError` na coleta dos testes.
- **Implementação mínima realizada:** criada a `quantidade_itens_valida` retornando apenas `True`, o suficiente para o primeiro teste passar.
- **Segundo teste escrito:** `test_qnt_acima_de_10_retorna_false`. Junto com os demais testes, ele fez 4 casos falharem com a implementação mínima. Ajustei a função para validar a faixa de 1 a 10 e levantar `ValueError` para negativos.
- **Melhoria ou refatoração realizada:** substituí os números fixos por constantes (`QNT_MIN` e `QNT_MAX`).

---

## 5. Testes funcionais com Playwright

**Sistema:** https://local-eats-unisenac.vercel.app/

### Teste funcional de Rudá Rosa

- **ID:** `TF01`
- **Fluxo automatizado:** verificar a apresentação da página inicial e navegar para a página de pedidos.
- **Interação realizada:** clique no link "Meus Pedidos" do menu.
- **Primeira assertion:** o título "Descubra sabores incríveis na sua cidade" está visível na página inicial.
- **Segunda assertion:** a URL após o clique contém `orders.html`.
- **Terceira assertion:** o link "Explorar" continua visível no menu da página de pedidos.
- **Arquivo e função:** `atividade-04/test_localeats.py::test_pagina_inicial_e_navegacao_para_meus_pedidos`
- **Resultado final:** [failed]

---

## 6. Resultado da execução

Instalação :

```powershell
pip install -r requirements.txt
python -m playwright install
```

Execução:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

- **Quantidade total de testes:** 8 coletados esperados (7 unitários, contando os 4 casos do teste parametrizado, e 1 funcional)
- **Testes aprovados:** [7]
- **Testes reprovados:** [1]
- **Link para o relatório:** [relatorio-pytest.txt](relatorio-pytest.txt)
- **Observações:** [uma falha encontrada no momento de realizar o teste, possivelmente pela falta de login]

---

## 7. Explicações individuais

### Explicação do teste de Rudá Rosa

- **Teste escolhido:** `test_qnt_acima_de_10_retorna_false`
- **Comportamento verificado:** que um pedido com mais de 10 itens é considerado inválido.
- **Dados ou estado inicial:** nenhuma preparação; a função é chamada diretamente com o valor `11`.
- **Resultado esperado:** `False`.
- **O que faria o teste falhar:** se a função deixasse de checar o limite superior `quantidade >= 1` apenas ou usasse `< 11` trocado por `<= 11`.

---

## 8. Uso de inteligência artificial

- **Ferramenta utilizada:** Claude
- **Como a ferramenta foi utilizada:** apoio para estruturar e formatação do texto README
- **Uma sugestão que precisou ser alterada ou rejeitada:** []
- **Motivo da alteração ou rejeição:** [informar]
- **Como o código sugerido foi verificado:** []

---

## 9. Diferenciais opcionais

- [] Terceiro teste unitário para caso de borda: `test_limites_da_quantidade_de_itens`
- [] Uso de `pytest.raises` para verificar exceção: `test_qnt_negativa_gera_value_error`
- [] Parametrização com `pytest.mark.parametrize`: `test_limites_da_quantidade_de_itens`
- [ ] Cenário BDD em Gherkin.
- [ ] Automação com `pytest-bdd`.
- [ ] Organização com Page Object Model.
- [ ] Segundo teste funcional pelo mesmo integrante.
- [ ] Execução em mais de um navegador.
- [ ] Screenshot, vídeo ou trace do Playwright.
- [ ] Registro de uma falha encontrada e corrigida.

### Descrição dos diferenciais
