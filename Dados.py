import random
import matplotlib.pyplot as plot



def lanzarDados(numero_veces, resultados):
    for i in range(numero_veces):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        resultado = dado1 + dado2;
        resultados.append(resultado);
        
    intervalos = range(2,14)
    plot.hist(x=resultados, bins=intervalos, color='#F2AB6D', rwidth=0.85)
    plot.title('Resultados')
    plot.xlabel('Suma de dados')
    plot.ylabel('Repeticiones')
    plot.xticks(intervalos)

vector = [];
lanzarDados(10000, vector);
#lanzarDados(1000, vector);
#lanzarDados(10000, vector);

