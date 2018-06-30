#!/bin/env python3

from os import path, getcwd

# Carregar ambiente virtual
if path.exists(path.join('.', 'venv')):
	activate_this = path.join(getcwd(), 'venv/bin/activate_this.py')
	with open(activate_this) as file_:
		exec(file_.read(), dict(__file__ = activate_this))

import pygame
pygame.init()

# Variáveis
local = getcwd()
tela = pygame.display.set_mode((700, 497))
pygame.display.set_caption('Canarinho Pistola')
relogio = pygame.time.Clock()
done = False
print(local)


def pulou(jogador, frame):
	jogador['frame'] = frame
	jogador['forca'] = -.010
	jogador['velocidade'] = 0
	print('Pulou em ' + str(jogador['frame']))


def atualiza_altura(jogador, frame):
	t = frame - jogador['frame']
	jogador['frame'] = frame

	# Equações de movimento, entrem em ação!
	g = G + jogador['forca']
	v = jogador['velocidade'] + (g * t);
	h = jogador['posicao'][Y] + (v * t) + (0.5 * g * t * t);

	jogador['forca'] = 0
	jogador['posicao'][Y] = h
	jogador['velocidade'] = v


G = 0.001; X = 0; Y = 1

def criar_jogador():
	jogador = {
		'imagem': pygame.image.load(path.join(local, 'jogador-pequeno.png')).convert_alpha(),
		'posicao': [100, 200],
		'frame': 0,
		'velocidade': 0,
		'forca': -.002, 
	}

	jogador['tamanho'] = jogador['imagem'].get_size()
	return jogador

jogador = criar_jogador()

while not done:
	# Atualiza tela.
	frame = pygame.time.get_ticks()

	# Limpa tela
	sujo0 = pygame.Rect(jogador['posicao'], jogador['tamanho'])
	pygame.draw.rect(tela, (0, 0, 0), sujo0)

	# Atualiza posição
	atualiza_altura(jogador, frame)

	# Desenha jogador
	sujo1 = pygame.Rect(jogador['posicao'], jogador['tamanho'])
	tela.blit(jogador['imagem'], jogador['posicao'])
	pygame.display.update([sujo0, sujo1])
	#print('altura = ' + str(jogador['posicao'][Y]))

	# Processa teclado
	pressed_keys = pygame.key.get_pressed()

	for event in pygame.event.get(pygame.KEYUP) :
		if event.key == pygame.K_SPACE:
			pulou(jogador, frame)

		if event.key == pygame.K_ESCAPE:
			done = True

	for event in pygame.event.get(pygame.QUIT) :
		exit()

	relogio.tick(30)


