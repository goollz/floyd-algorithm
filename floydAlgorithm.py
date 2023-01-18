# %% [markdown]
# # Algoritmo Floyd

# %%
from tarfile import SOLARIS_XHDTYPE
from typing import List
import numpy as np
Vector = List[int]
Matrix = List[List[int]]
import time

# %%
def make_vertice_list():
    """[this function creates a list with contain all the vertices]

    Returns:
        lista[list]: [list with contain all the vertices in the graph]
    """
    lista = []
    vertices = input("insira todos os vertices de uma vez: ")
    for i in range(len(vertices)):
        lista.append(vertices[i])
    return lista

# %%
def make_values_matrix(lista):
    """[this function receive a list as input, initializes the matrix of solution and completes with the edge's value inputs the matrix of distance]

    Args:
        lista ([list]): [the list of vertices of the graph]

    Returns:
        far_matrix [list of list]: [matrix that contains the values of the edges]
        solution_matrix [list of list]: [matrix inmatrix of connections between the vertices]
    """
    tamanho = len(lista)
    far_matrix = [["-"]*tamanho for i in range(tamanho)]
    solution_matrix = [[0]*tamanho for i in range(tamanho)]
    print(solution_matrix)
    for j in range(tamanho):
        far_matrix[j][j] = int(0)
    for y in range(tamanho):
        for x in range(tamanho):
            if y!=x:
                #print(y,x)
                var = input(f"informe o valor da aresta {lista[x]}->{lista[y]} se não tiver valor coloque - : ")
                if var == "-":
                    far_matrix[y][x] = var 
                else:
                    far_matrix[y][x] = int(var)
    return (far_matrix, solution_matrix)

# %%
def floydAlgorithm():
    """[summarythis function recalculates the values of the edges and puts the better value on the place,
        and put the responsible for this recalc on the matrix of solution]

    Returns:
        far_matrix [list of list]: [returns the recalculated matrix of edges values]
        solution_matrix [list of list]: [returns the returns the matrix of solution that
                                         contains the returns the recalculated matrix of edges values for the recalculated matrix of edges values]
    """
    lista = make_vertice_list()
    far_matrix,solution_matrix = make_values_matrix(lista)
    for i in range(len(lista)):
        if i == 0:
            y = 1
            x = 1
            while y < len(lista):
                x = 1
                while x < len(lista):
                    if far_matrix[0][x]!='-' and far_matrix[y][0] != '-':
                        number = far_matrix[0][x]+far_matrix[y][0]
                        if far_matrix[y][x] == '-':
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                        elif number<far_matrix[y][x]:
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                    x+=1
                y+=1
                
        elif i == len(lista)-1:
            y = i-1
            x = i-1
            while y>=0:
                x = i-1
                while x>=0:
                    if far_matrix[i][x] != '-' and far_matrix[y][i] != '-':
                        number = far_matrix[i][x]+far_matrix[y][i]
                        if far_matrix[y][x] == '-':
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                        elif number<far_matrix[y][x]:
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                    x-=1
                y-=1
                
        else:
            y = i+1
            x = i+1
            while y < len(lista):
                x=i+1
                while x < len(lista):
                    if far_matrix[i][x]!='-' and far_matrix[y][i] != '-':
                        number = far_matrix[i][x]+far_matrix[y][i]
                        if far_matrix[y][x] == '-':
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                        elif number<far_matrix[y][x]:
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                    x+=1
                y+=1
                
            y = i-1
            x = i-1
            while y>=0:
                x = i-1
                while x>=0:
                    if far_matrix[i][x] != '-' and far_matrix[y][i] != '-':
                        number = far_matrix[i][x]+far_matrix[y][i]
                        if far_matrix[y][x] == '-':
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                        elif number<far_matrix[y][x]:
                            far_matrix[y][x]=number
                            solution_matrix[y][x]=i+1
                    x-=1
                y-=1
                
            y=i-1
            y2 = i+1
            x = i-1
            x2 = i+1
            while y >=0:
                x2 = i+1
                while x2 < len(lista):
                    if far_matrix[i][x2] != '-' and far_matrix[y][i] != '-':
                        number = far_matrix[i][x2] + far_matrix[y][i]
                        if far_matrix[y][x2] == '-':
                            far_matrix[y][x2] = number
                            solution_matrix[y][x2]=i+1
                        elif number<far_matrix[y][x2]:
                            far_matrix[y][x2]=number
                            solution_matrix[y][x2] = i+1
                    x2+=1
                y-=1
            while y2<len(lista):
                x = i-1
                while x >= 0:
                    if far_matrix[i][x] != '-' and far_matrix[y2][i] != '-':
                        number = far_matrix[i][x]+far_matrix[y2][i]
                        if far_matrix[y2][x]== '-':
                            far_matrix[y2][x] = number
                            solution_matrix[y2][x] = i+1
                        elif number<far_matrix[y2][x]:
                            far_matrix[y2][x] = number
                            solution_matrix[y2][x]=i+1
                    x-=1
                y2+=1
                            
                       
    return far_matrix, solution_matrix,lista   
            

def minimun_path(origem,destino,lista,far_matrix,solution_matrix):
    origens = []
    destinos = []
    vertices = []
    vertices.append(destino)
    arestas = []
    origem_number = lista.index(origem)
    destino_number = lista.index(destino)
    origens.append(origem_number)
    if origem!=destino:
        while len(origens) > 0:
            origem2 = origens.pop(0)
            var = solution_matrix[origem2][destino_number]-1
            if var == -1:
                if origem2 == origem_number:
                    vertices.append(lista[origem2])
                    arestas.append(far_matrix[origem_number][destino_number])
                else:
                    destinos.append(origem2)
                    arestas.append(far_matrix[origem2][destino_number])
            else:
                origens.append(var)
                if origem2 != origem_number:
                    vertices.append(lista[origem2])
                    arestas.append(far_matrix[origem2][destino_number])
        while len(destinos) > 0:
            origem2 = destinos.pop(0)
            var = solution_matrix[origem_number][origem2] -1
            if var == -1:
                vertices.append(lista[origem2])
                arestas.append(far_matrix[origem_number][origem2])
            else:
                destinos.append(var)
                vertices.append(lista[origem2])
                arestas.append(far_matrix[origem_number][origem2])
        vertices.append(lista[origem_number])
        return vertices, arestas
    else:
        arestas.append(0)
        return vertices,arestas
        
            
def main_loop():
    far_matrix,solution_matrix,lista = floydAlgorithm()
    print(f"lista de vertices: {lista}")
    print("Matrz de distancias:")
    for i in range(len(far_matrix)):
        print(far_matrix[i])
        
    print("Matrz de solucao:")
    for i in range(len(solution_matrix)):
        print(solution_matrix[i])
    flag = True
    vertices = []
    arestas = []
    while flag==True:
        try:
            origim, destiny = input("informe os vertices de origem e destino: ")
            vertices,arestas = minimun_path(origim,destiny,lista,far_matrix,solution_matrix)
            var = len(vertices)
            var = var-1
            var2 = var-1
            while var > 0:
                while var > 0:
                    print(f" {vertices[var]}")
                    print(f" |\n {arestas[var2]}\n |\n\ /")
                    var-=1
                    var2-=1
                print(f" {vertices[var]}")
            total_cost=0
            for i in range(len(arestas)):
                total_cost += arestas[i]
            print(f"o custo toal foi: {total_cost}")         
        except ValueError:
            print("paramos")
            flag = False
    
    
    
# %%
if __name__ == "__main__":
    main_loop()

# %%



