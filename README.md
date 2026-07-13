# Sistema de Gerenciamento de Tarefas - TechFlow Solutions

## Objetivo e Escopo
Sistema de gerenciamento de tarefas para acompanhar o fluxo de trabalho em tempo real, desenvolvido para a TechFlow Solutions.

## Metodologia
Utilizei o Kanban no GitHub Projects para organização das tarefas nas colunas A Fazer, Em Progresso e Concluído.

## Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Rode o servidor: `python app.py`
3. Execute os testes: `pytest`

## Gestão de Mudanças
**Alteração de Escopo:** O cliente solicitou a capacidade de priorizar tarefas críticas. 
**Ação:** Foi adicionado o campo "Prioridade" no modelo de tarefas e atualizado o quadro Kanban para refletir o esforço dessa nova funcionalidade. Os testes unitários também foram ajustados para cobrir essa regra de negócio.