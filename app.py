import random

# Definir la baraja de cartas de Uno
colores = ['Rojo', 'Amarillo', 'Verde', 'Azul']
valores = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Saltar', 'Reversa', 'Roba_Dos']
baraja = [f"{color} {valor}" for color in colores for valor in valores] * 2

# Barajar la baraja
random.shuffle(baraja)

# Repartir cartas a los jugadores
def repartir_cartas(num_jugadores, num_cartas=7):
    manos = {f"Jugador {i+1}": [baraja.pop() for _ in range(num_cartas)] for i in range(num_jugadores)}
    cartas_sobrantes = baraja[:]
    return manos, cartas_sobrantes


# Mostrar manos
def mostrar_manos(manos):
    for jugador, mano in manos.items():
        print(f"Mano de {jugador}: {', '.join(mano)}")

# Bucle principal del juego
def main():
    num_jugadores = 3
    manos, cartas_sobrantes = repartir_cartas(num_jugadores)
    mostrar_manos(manos)

    # Simular un bucle de juego simple
    jugador_actual = 0

    # Carta inicial de la baraja
    carta_actual = cartas_sobrantes.pop()
    print(f"Carta inicial: {carta_actual}")
    direccion = 1
    final_juego = 0

    while True:
        nombre_jugador = f"Jugador {jugador_actual + 1}"
        print("\n" + "=" * 20 + f"{nombre_jugador} y Carta actual en el juego: {carta_actual}")
        print(f"Mano actual: {', '.join(manos[nombre_jugador])}")

        # Buscar una carta válida para jugar
        carta_jugada = None
        poder = None
        for carta in manos[nombre_jugador]:
            color, valor = carta.split()
            color_actual, valor_actual = carta_actual.split()
            if color == color_actual or valor == valor_actual:
                carta_jugada = carta
                if valor == 'Saltar' or valor == 'Reversa' or valor == 'Roba_Dos':
                    poder = valor
                break

        if carta_jugada:
            manos[nombre_jugador].remove(carta_jugada)
            carta_actual = carta_jugada
            print(f"{nombre_jugador} juega {carta_jugada}")

            # Aplicar el poder de la carta si es necesario
            if poder == 'Reversa':
                direccion *= -1
                print("Dirección del juego invertida")
            elif poder == 'Saltar':
                jugador_actual = (jugador_actual + direccion) % num_jugadores
                print(f"el siguiente jugador se salta el turno")
            elif poder == 'Roba_Dos':
                if len(cartas_sobrantes) != 0:
                    siguiente_jugador = (jugador_actual + direccion) % num_jugadores
                    manos[f"Jugador {siguiente_jugador + 1}"].extend([cartas_sobrantes.pop() for _ in range(2)])
                    print(f"El siguiente jugador roba dos cartas: {', '.join(manos[f'Jugador {siguiente_jugador + 1}'][-2:])}")
        else:
            if cartas_sobrantes:
                nueva_carta = cartas_sobrantes.pop()
                manos[nombre_jugador].append(nueva_carta)
                print(f"{nombre_jugador} no tiene una carta válida. Roba {nueva_carta}")
            else:
                print(f"¡{nombre_jugador} no tiene cartas válidas y no hay más cartas para robar!")
                final_juego += 1


        # Actualizar el jugador actual
        jugador_actual = (jugador_actual + direccion) % num_jugadores
        
        # Verificar si el juego ha terminado
        if final_juego == num_jugadores:
            print("Fin del juego")
            break
        if len(manos[nombre_jugador]) == 0:
            print(f"{nombre_jugador} ha ganado!")
            break

if __name__ == "__main__":
    main()