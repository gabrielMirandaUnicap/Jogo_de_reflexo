import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led = 14
led2 = 23
botao = 15
botao2 = 24
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(botao, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botao2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(led, GPIO.LOW)
GPIO.output(led2, GPIO.LOW)
time.sleep(1)

qnt = 0
lista = [led, led2]
while True:
    print("Prepare-se...")
    tempo = random.randrange(2, 7)
    op = random.choice(lista)
    time.sleep(tempo)
    GPIO.output(op, GPIO.HIGH)
    tempo_inicio = time.time()
    if op == led:
        while GPIO.input(botao) == GPIO.LOW:
            pass
    elif op == led2:
        while GPIO.input(botao2) == GPIO.LOW:
            pass
    else:
        print("ERROOUU")
        break
    tempo_fim = time.time()
    tempo_reacao = tempo_fim - tempo_inicio
    print(F"Seu tempo de reação foi: {tempo_reacao:.2f} segundos")
    GPIO.output(led, GPIO.LOW)
    GPIO.output(led2, GPIO.LOW)
    qnt += 1

    if qnt == 5:
        for i in range(0, 5):
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(led2, GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(led, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
            time.sleep(0.1)
        print("Você ganhou!!!!")
        break
    
GPIO.cleanup()