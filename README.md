# Flappy Bird versão canarinho pistola

Por enquanto só foi implementado uma física básica e controle de botões.


## Dependências

* Python 3.x
* Pygame
* Virtualenv (opcional)

## Instalação

Em ambiente Debian e derivados, execute:
```
sudo apt-get update
sudo apt-get install python3 python3-pygame
```
Também é possível usar o virtualenv para instalar pygame se você não quiser instalar coisas como root:
```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
deactivate
```
Depois de instalado, basta executar:
```
./jogo
```
