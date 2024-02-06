velocidade = 70
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_ultrapassada = velocidade > RADAR_1
local_carro_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
local_carro_radar_2 = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = local_carro_radar_1 and local_carro_radar_2
carro_multado = carro_passou_radar_1 and velocidade_ultrapassada

if velocidade_ultrapassada:
    print("Velocidade ultrapassada.")

if carro_passou_radar_1:
    print("Carro passou pelo Radar 1.")

if carro_passou_radar_1 and \
    velocidade_ultrapassada:
    print("Carro multado")
