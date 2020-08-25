#cada linha do arquivo de entrada deve contart 6 digitos no formato tempo (3 digitos), comando ligar (2), comando desligar (2) ex:"120a+m-", "056__m+"

import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
import pyglet
from multiprocessing import Process

arduino = serial.Serial('/dev/ttyUSB0', 9600) # your Serial port should be different!

time.sleep(2) #waiting the initialization...

def initmotor():
	
	f = open("textoinputMOTOR.txt", "r") # texto de entrada no modo de leitura
	tempo = 0 #declaração da variável de tempo
	i = 0 #variavel de contagem de tempo
	aux = f.readline()
	
	while True:
	
		time.sleep(1)#deixa 1 seg passar
		tempo += 1
		if tempo == int(aux[0:3]): #ler os 3 primeiros numeros da linha do arquivo e transforma em inteiro para comparar com o tempo
			
			string_to_int = int(aux[3:6])
			arduino.write(bytes([string_to_int])) #decodificação de string para byte
				
		elif tempo != int(aux[0:3]): #caso o tempo nao seja o mesmo do arquivo
			continue 
		aux = f.readline() #apos encontrar o tempo compativel busca o proximo
		if aux == None:
			f.close()
			break
	
		
if __name__ == "__main__":
	
	motor_thread = Process(target=initmotor)
	
	
	vidPath = 'video.mp4'
	window= pyglet.window.Window(640, 360)
	player = pyglet.media.Player()
	source = pyglet.media.StreamingSource()
	MediaLoad = pyglet.media.load(vidPath)
 
	player.queue(MediaLoad)
	player.play()
	@window.event
	def on_draw():
		if player.source and player.source.video_format:
			player.get_texture().blit(0,0)
	motor_thread.start()
	
	pyglet.app.run()
	motor_thread.join()

	
