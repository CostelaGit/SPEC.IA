# Agente de Padronização OpenAPI para B3

Este projeto implementa um protótipo de agente inteligente capaz de comparar e adaptar a documentação OpenAPI Specification (OAS) de uma API local aos padrões da B3.

## Funcionalidades

- **Parsing de OAS:** Carrega especificações OpenAPI em formatos JSON ou YAML.
- **Comparação de OAS:** Identifica divergências e similaridades em paths, schemas e esquemas de segurança entre duas especificações OpenAPI.
- **Adaptação de OAS:** Aplica adaptações básicas, como a inclusão de esquemas de segurança da B3 e a renomeação de paths (ex: `/cotacoes` para `/v1/market-data/quotes`).
- **Geração de OAS:** Gera uma nova especificação OpenAPI adaptada.

## Como usar

1.  **Prepare seus arquivos:**
    *   `local_swagger.json` (ou `.yaml`): O arquivo OpenAPI da sua API local.
    *   `b3_swagger.json` (ou `.yaml`): O arquivo OpenAPI da B3 (obtido da URL `https://b3api.brytsoftware.com/swagger/v1/swagger.json`).

2.  **Execute o agente:**
    ```bash
    python3.11 main.py
    ```

3.  **Verifique os resultados:**
    *   `Comparison Report:` Será exibido no console, detalhando as divergências e similaridades encontradas.
    *   `adapted_swagger.json`: Um novo arquivo OpenAPI será gerado com as adaptações aplicadas.

## Estrutura do Projeto

-   `main.py`: Contém a lógica principal do agente, incluindo funções para carregar, comparar, adaptar e gerar especificações OpenAPI.
-   `b3_swagger.json`: O arquivo OpenAPI da B3 utilizado como referência.
-   `local_swagger.json`: Um arquivo OpenAPI de exemplo para simular a API local (gerado temporariamente pelo `main.py` para testes).
-   `adapted_swagger.json`: O arquivo OpenAPI de saída, com as adaptações aplicadas.

## Próximos Passos (Melhorias Futuras)

-   Implementar lógica de adaptação mais sofisticada para schemas, incluindo mapeamento de campos e transformações de tipos de dados.
-   Adicionar suporte para versionamento de API mais robusto.
-   Desenvolver uma interface de usuário (CLI ou Web) para facilitar a interação com o agente.
-   Integrar com ferramentas de CI/CD para automação da padronização da documentação.
-   Gerar um relatório comparativo mais detalhado e formatado (ex: HTML, PDF).


