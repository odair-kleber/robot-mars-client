# Robôs em Marte Client

Implementação Python de uma aplicação _client_ para a API [**RobosEmMarte**](https://github.com/lesvasconcelos/RobosEmMarte).

## Dependências
- https://pypi.org/project/requests/
- https://pypi.org/project/keyboard/

## Requisitos
- Python 3.7

## Configuração
Antes de iniciar a aplicação é necessário executar os seguintes comandos para configuração das dependências:

```
pip install --upgrade pip
pip install keyboard
pip install requests
```

## Como executar?
No diretório raiz, executar o comando abaixo:

```
python main.py
```

## Inscruções de uso
Há 4 possíveis comandos que podemos enviar para o robô em Marte, representados por quatro teclas do teclado.

Sendo elas:
* `ARROW UP`: Direciona o robô para o norte
* `ARROW RIGHT`: Direciona o robô para o leste
* `ARROW DOWN`: Direciona o robô para o sul
* `ARROW LEFT`: Direciona o robô para o oeste
* `SHIFT`: Movimento o robô na direção atual
