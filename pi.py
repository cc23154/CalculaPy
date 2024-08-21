def Calcula_pi(quaoPreciso : int = 100):
    from random import uniform
    baixo = 0
    cima = 0
    for _ in range(quaoPreciso):
        ponto = (uniform(0, 1), uniform(0, 1))
        if 1 >= ponto[0] ** 2 + ponto[1] ** 2:
            cima += 1
        baixo += 1
    return 4 * (cima / baixo)