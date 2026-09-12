
## Validador de Senha com Testes Automatizados

Validação de senha em Python com suíte de testes em pytest. Projeto de estudo em qualidade de software.

### Regras de validação

Mínimo de 8 caracteres, ao menos uma letra maiúscula, uma minúscula e um número.

### Testes

A suíte cobre 13 casos, construídos a partir de partição de equivalência (classes de entrada válida e inválidas por critério) e análise de valor limite (fronteira entre 7 e 8 caracteres), além de casos de borda (string vazia e None).

### Como rodar

```
pip install -r requirements.txt
pytest
```
