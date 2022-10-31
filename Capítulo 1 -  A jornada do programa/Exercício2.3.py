
"""
Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio
(tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?
"""

milhas = 10 / 1.61
tempo_minutos = 42.7
tempo_segundos = 42 * 60 + 42
tempo_hora = tempo_minutos/60

print(f"Ele faz cerca de {milhas/tempo_minutos} por minuto")
print(f"Ele faz cerca de {milhas/tempo_segundos} por segundos")
print(f"Ele faz cerca de {milhas/tempo_hora} por hora")

