minas = 3
casilla_cerrada="."
numeros="123456"
letras="ABCDEF"
columna=int(input())
niveles=""

match niveles:
    case "facil":
        minas=3
        filas=6
        columnas=6
    case "medio":
        minas=6
        filas=8
        columnas=8
    case "dificil":
        minas=10
        filas=10
        columnas=10

