# Proyecto_Navidad_Python

**Buscaminas & Hundir la Flota**
- Este repositorio contiene dos juegos clásicos desarrollados en Python. El proyecto se centra en la lógica de matrices, recursividad y gestión de estados en juegos por turnos.

## BUSCAMINAS:

- Algoritmo de Expansión Recursiva: La función revelar_vacias utiliza recursividad para abrir automáticamente todas las celdas adyacentes que no tengan minas alrededor.

- Cálculo de Proximidad: La función contar_minas_alrededor escanea un área de $3 \times 3$ alrededor de una coordenada para determinar el número de peligros adyacentes.

- Validación Robusta: Implementación de bloques try-except para capturar errores de valor (ValueError) cuando el usuario introduce caracteres no numéricos.

## HUNDIR LA FLOTA

- Diccionario de Estado: Cada jugador se gestiona a través de un diccionario que contiene su tablero propio, su historial de disparos y la lista de coordenadas de sus barcos.

- Inteligencia Artificial Progresiva:
Fácil: Disparos aleatorios puros.
Medio: Disparos aleatorios pero evitando repetir coordenadas ya atacadas.
Difícil: Si la IA detecta un impacto ("Tocado"), su siguiente movimiento prioriza las casillas vecinas (norte, sur, este, oeste) para hundir el barco.

- Sistema de Coordenadas Alfanumérico: Transformación de entrada de usuario (ej: "A5") a índices de matriz mediante la función ord() para letras y conversión entera para números.

- Validación de Colocación (Reglas Propias): El código verifica que los barcos no se solapen y que se respete un margen de seguridad entre ellos mediante la función se_puede_colocar.
