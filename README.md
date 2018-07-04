# Flappy Bird versão Canarinho pistola

Reimplementação do jogo Flappy Bird em Python com Pygame. Por enquanto só foi implementado uma física básica e controle de botões. Espaço faz o Canarinho pular e escape abandona o jogo.


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
Também é possível usar o Virtualenv para instalar pygame se você não quiser instalar coisas como root. O código do jogo detecta automaticamente se Virtualenv foi usado ou não. Basta entrar no diretório raiz do projeto e executar:
```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
deactivate
```
Depois de instalado, basta entrar no diretório raiz do projeto e executar:
```
./jogo
```

## Melhorias para as próximas versões

Em ordem de prioridade:

* ~~Interação com obstáculos;~~
* Contagem de pontuação;
* Texturas para plano de fundo e obstáculos;
* Sons;
* Animação do Canarinho morrendo quando ele bate no obstáculo ou cai no buraco;
* Animação do Canarinho girando ao pular, tal como se encontra em outras implementações de Flappy Bird.
* Desenhar sprite do Canarinho pistola mais parecido com o original;
* Seleção de dificuldade com parâmetros da física e/ou dimensões do obstáculo parametrizáveis?
