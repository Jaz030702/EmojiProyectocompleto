from symbols import tabla_simbolos, sujetos, reglas_semanticas


def analizar(texto):
    tokens = texto.lower().split()

    if not tokens:
        return "ERROR: entrada vacía"

    if tokens[0] not in sujetos:
        return "ERROR SINTÁCTICO"

    sujeto = tokens[0]

    for token in tokens[1:]:

        if token not in tabla_simbolos:
            return "ERROR SEMÁNTICO"

        tipo = tabla_simbolos[token][0]

        if tipo not in reglas_semanticas[sujeto]:
            return "ERROR SEMÁNTICO"

    emojis = []

    for token in tokens:
        if token in tabla_simbolos:
            emojis.append(tabla_simbolos[token][1])

    return " ".join(emojis)