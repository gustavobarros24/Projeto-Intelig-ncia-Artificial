from grafo import Graph
from entrega import Entrega
from estafeta import Estafeta
from veiculo import Vehicle
from veiculo import Bike
from veiculo import Car
from veiculo import Motorcycle
from listaentregas import Administrador

def main():
    g = Graph()
    g.add_edge("arentim", "tadim", 8)
    g.add_edge("arentim", "ruilhe", 4)
    g.add_edge("arentim", "tebosa", 4)
    g.add_edge("ruilhe", "priscos", 5)
    g.add_edge("ruilhe", "tadim", 5)
    g.add_edge("ruilhe", "tebosa", 2)
    g.add_edge("tebosa", "guisande", 2)
    g.add_edge("tebosa", "priscos", 1)
    g.add_edge("tadim", "priscos", 7)
    g.add_edge("tadim", "sequeira", 11)
    g.add_edge("tadim", "vilaca", 2)
    g.add_edge("tadim", "cabreiros", 7)
    g.add_edge("priscos", "guisande", 8)
    g.add_edge("priscos", "celeiros", 11)
    g.add_edge("priscos", "vilaca", 10)
    g.add_edge("guisande", "celeiros", 14)
    g.add_edge("guisande", "escudeiros", 10)
    g.add_edge("escudeiros", "figueiredo", 8)
    g.add_edge("escudeiros", "lamas", 5)
    g.add_edge("escudeiros", "morreira", 7)
    g.add_edge("cabreiros", "sequeira", 3)
    g.add_edge("cabreiros", "real", 20)
    g.add_edge("cabreiros", "mire", 17)
    g.add_edge("cabreiros", "padim", 11)
    g.add_edge("vilaca", "sequeira", 4)
    g.add_edge("vilaca", "celeiros", 5)
    g.add_edge("celeiros", "figueiredo", 2)
    g.add_edge("celeiros", "esporoes", 5)
    g.add_edge("celeiros", "lomar", 4)
    g.add_edge("celeiros", "ferreiros", 4)
    g.add_edge("celeiros", "sequeira", 5)
    g.add_edge("figueiredo", "esporoes", 7)
    g.add_edge("figueiredo", "lamas", 5)
    g.add_edge("lamas", "morreira", 5)
    g.add_edge("lamas", "esporoes", 7)
    g.add_edge("morreira", "esporoes", 4)
    g.add_edge("sequeira", "real", 10)
    g.add_edge("sequeira", "ferreiros", 4)
    g.add_edge("esporoes", "lomar", 4)
    g.add_edge("esporoes", "nogueira", 5)
    g.add_edge("padim", "mire", 7)
    g.add_edge("real", "mire", 10)
    g.add_edge("real", "merelim_spaio", 15)
    g.add_edge("real", "merelim_spedro", 4)
    g.add_edge("real", "ferreiros", 10)
    g.add_edge("real", "maximinos", 8)
    g.add_edge("real", "svicente", 2)
    g.add_edge("real", "palmeira", 7)
    g.add_edge("ferreiros", "maximinos", 4)
    g.add_edge("ferreiros", "lomar", 2)
    g.add_edge("ferreiros", "sjose_de_slazaro", 4)
    g.add_edge("lomar", "sjose_de_slazaro", 4)
    g.add_edge("lomar", "nogueira", 4)
    g.add_edge("nogueira", "sjose_de_slazaro", 4)
    g.add_edge("nogueira", "svitor", 8)
    g.add_edge("nogueira", "nogueiro", 6)
    g.add_edge("mire", "merelim_spaio", 2)
    g.add_edge("merelim_spaio", "merelim_spedro", 4)
    g.add_edge("merelim_spaio", "palmeira", 6)
    g.add_edge("merelim_spedro", "palmeira", 7)
    g.add_edge("maximinos", "svicente", 5)
    g.add_edge("maximinos", "sjose_de_slazaro", 2)
    g.add_edge("sjose_de_slazaro", "svitor", 4)
    g.add_edge("svicente", "svitor", 1)
    g.add_edge("svicente", "palmeira", 8)
    g.add_edge("svitor", "gualtar", 4)
    g.add_edge("svitor", "adaufe", 7)
    g.add_edge("svitor", "nogueiro", 3)
    g.add_edge("nogueiro", "este", 7)
    g.add_edge("nogueiro", "espinho", 5)
    g.add_edge("nogueiro", "gualtar", 4)
    g.add_edge("espinho", "este", 5)
    g.add_edge("espinho", "sobreposta", 4)
    g.add_edge("sobreposta", "pedralva", 4)
    g.add_edge("sobreposta", "este", 5)
    g.add_edge("pedralva", "este", 6)
    g.add_edge("este", "gualtar", 4)
    g.add_edge("este", "santa_lucrecia", 3)
    g.add_edge("este", "adaufe", 7)
    g.add_edge("este", "crespos", 8)
    g.add_edge("gualtar", "adaufe", 4)
    g.add_edge("palmeira", "adaufe", 8)
    g.add_edge("adaufe", "santa_lucrecia", 3)
    g.add_edge("santa_lucrecia", "crespos", 4)

    g.add_heuristica("arentim", 7)
    g.add_heuristica("ruilhe", 6)
    g.add_heuristica("tebosa", 6)
    g.add_heuristica("tadim", 5)
    g.add_heuristica("priscos", 5)
    g.add_heuristica("guisande", 6)
    g.add_heuristica("escudeiros", 5)
    g.add_heuristica("cabreiros", 3)
    g.add_heuristica("vilaca", 4)
    g.add_heuristica("celeiros", 2)
    g.add_heuristica("figueiredo", 3)
    g.add_heuristica("lamas", 3)
    g.add_heuristica("morreira", 5)
    g.add_heuristica("sequeira", 2)
    g.add_heuristica("esporoes", 3)
    g.add_heuristica("padim", 5)
    g.add_heuristica("real", 2)
    g.add_heuristica("ferreiros", 0)
    g.add_heuristica("lomar", 1)
    g.add_heuristica("nogueira", 3)
    g.add_heuristica("mire", 5)
    g.add_heuristica("merelim_spaio", 5)
    g.add_heuristica("merelim_spedro", 4)
    g.add_heuristica("maximinos", 1)
    g.add_heuristica("sjose_de_slazaro", 2)
    g.add_heuristica("svicente", 4)
    g.add_heuristica("svitor", 4)
    g.add_heuristica("nogueiro", 5)
    g.add_heuristica("espinho", 7)
    g.add_heuristica("sobreposta", 8)
    g.add_heuristica("pedralva", 10)
    g.add_heuristica("este", 7)
    g.add_heuristica("gualtar", 5)
    g.add_heuristica("palmeira", 6)
    g.add_heuristica("adaufe", 6)
    g.add_heuristica("santa_lucrecia", 8)
    g.add_heuristica("crespos", 10)
    


    armazem = "ferreiros"
    listas = Administrador(g)

    bike1 = Bike()
    bike2= Bike()
    car1 = Car()
    car2 = Car()
    mota1 = Motorcycle()
    mota2 = Motorcycle()

    estafetas = [Estafeta(1, bike1, True), Estafeta(2, bike2, True), Estafeta(3, car1, True), Estafeta(4, car2, True), Estafeta(5, mota1, True), Estafeta(6, mota2, True)]

    idsentregas = 1

    for x in estafetas:
        listas.add_estafeta(x)

    opcao = 24
    while opcao != 0:
        print("1 - Encomendar")
        print("2 - Mapa de grafos")
        print("3 - Grupo de Estafetas")
        print("0 - Sair")

        opcao = int(input("Indique a opção que pretende executar: "))
    
        if opcao == 0:
            print("Programa terminado.")
        elif opcao == 1:
            opcao2 = 24
            residencia = input("Para onde é a encomenda? ")
            peso = int(input("Qual é o peso da encomenda? "))
            prazo = int(input("Quando deseja receber a encomenda? "))
            opcao2 = int(input("Indique que algoritmo irá ser usado para executar o mapeamento: "))
            print("1 - DFS")
            print("2 - BFS")
            print("3 - A*")
            print("4 - GULOSA")
            if opcao2 == 1:
                result = g.algDFS(armazem, residencia, path=[], visited=set())
                caminho, custo = result
                listas.atribuiencomenda(custo, peso, prazo, residencia, idsentregas)
                print(result)
                result2 = listas.finalizaencomenda(custo)
                resultado1, resultado2 = result2
                resultado4 = round(resultado1,2)
                resultado3 = int(resultado2)
                print (resultado4)
                print (resultado3)
            elif opcao2 == 2:
                result = g.algBFS(armazem,residencia)
                caminho, custo = result
                listas.atribuiencomenda(custo, peso, prazo, residencia, idsentregas)
                print(result)
                result2 = listas.finalizaencomenda(custo)
                resultado1, resultado2 = result2
                resultado4 = round(resultado1,2)
                resultado3 = int(resultado2)
                print (resultado4)
                print (resultado3)
            elif opcao2 == 3:
                result = g.algestrela(armazem,residencia)
                caminho, custo = result
                listas.atribuiencomenda(custo, peso, prazo, residencia, idsentregas)
                print(result)
                result2 = listas.finalizaencomenda(custo)
                resultado1, resultado2 = result2
                resultado4 = round(resultado1,2)
                resultado3 = int(resultado2)
                print (resultado4)
                print (resultado3)
            elif opcao2 == 4:
                result = g.greedy(armazem,residencia)
                caminho, custo = result
                listas.atribuiencomenda(custo, peso, prazo, residencia, idsentregas)
                print(result)
                result2 = listas.finalizaencomenda(custo)
                resultado1, resultado2 = result2
                resultado4 = round(resultado1,2)
                resultado3 = int(resultado2)
                print (resultado4)
                print (resultado3)
        elif opcao == 2:
            g.desenha()
        elif opcao == 3:
            for estafeta in estafetas:
                estafeta_id = estafeta.getID()
                vehicle_type = estafeta.getVeiculo().__class__.__name__
                print(f"Estafeta ID: {estafeta_id}, Vehicle Type: {vehicle_type}, Rating: {estafeta.getAvaliacao()}")



if __name__ == "__main__":
    main()
