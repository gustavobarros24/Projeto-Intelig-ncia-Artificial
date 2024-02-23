from estafeta import Estafeta
from entrega import Entrega
import random

class Administrador:
    def __init__(self,grafo):
        self.estafetas = []
        self.entregas = []
        self.grafo = grafo

    def get_estafetas(self):
        return self.estafetas

    def print_estafetas_disponibilidades(self):
        for estafeta in self.estafetas:
            print(f"Estafeta {estafeta.getID()}: Disponibilidade - {estafeta.getDisponibilidade()}")

    def add_estafeta(self, estafeta):
        self.estafetas.append(estafeta)

    def add_entrega(self, entrega):
        self.entregas.append(entrega)
    
    def seleciona_entafeta(self, x,):
        estafetaselecionado = None
        for estafeta in self.estafetas:
            if estafeta.id_estafeta == x:
                return estafetaselecionado
    
    def atribuiencomenda(self, custo, peso, prazo, residencia,idsentregas):
        
        entregador = None
        entrega = Entrega(idsentregas, prazo,residencia,"ferreiros","Em processo")

        idsentregas = idsentregas + 1
        


        if peso > 100:
            print("Peso superior a 100, impossível de fornecer transporte")


        if custo < 30 and 5 >= peso > 0 :
            entregador
            for estafeta in self.estafetas:
                if estafeta.getDisponibilidade() == True and estafeta.getVeiculo().__class__.__name__ == "Bike":
                    entregador = estafeta
                    break
            
            entregador.setDisponibilidade(False)
            entregador.setPesoatual(peso)
            entrega.setCusto(custo)
            entrega.setEstafetaDeServico(entregador.getID())

        if 110 > custo and 20 > peso > 5 :
            entregador
            for estafeta in self.estafetas:
                if estafeta.getDisponibilidade() == True and estafeta.getVeiculo().__class__.__name__ == "Motorcycle":
                    entregador = estafeta
                    break
            
            entregador.setDisponibilidade(False)
            entregador.setPesoatual(peso)
            entrega.setCusto(custo*1.6*0.02)
            entrega.setEstafetaDeServico(entregador.getID())

        if custo >= 110 and 100 >= peso > 20:
            for estafeta in self.estafetas:
                if estafeta.getDisponibilidade() == True and estafeta.getVeiculo().__class__.__name__ == "Carro":
                    entregador = estafeta
                    break
            
            entregador.setDisponibilidade(False)
            entregador.setPesoatual(peso)
            entrega.setCusto(custo*1.6*0.07)
            entrega.setEstafetaDeServico(entregador.getID())

        print(entrega)
        self.add_entrega(entrega)
    
    def finalizaencomenda(self, custo):
        estafetaaficar = None
        fimentrega = None
        for entrega in self.entregas:
            if entrega.getestado() == "Em processo":
                fimentrega = entrega
                entrega.setEstado("Concluída")
                break

        for estafeta in self.estafetas:
            if estafeta.getID() == fimentrega.getEstafetaDeServico():
                estafetaaficar = estafeta
                estafeta.setDisponibilidade(True)


        tempoquedemorou = custo/estafetaaficar.getVeiculo().getSpeed()

        custototal = fimentrega.getPreco()

        if(fimentrega.getPrazo() < 24):
            custototal = custototal + 50
        
        if(fimentrega.getPrazo() > 24):
            custototal = custototal + 10

        if fimentrega.getPrazo() >= tempoquedemorou:
            fimentrega.setRating(random.randint(4, 5))
        
        if fimentrega.getPrazo() < tempoquedemorou:
            fimentrega.setRating(random.randint(1,2,3))
        
        estafetaaficar.setAvaliacao((fimentrega.getRating()+estafetaaficar.getAvaliacao())/2)

        return (tempoquedemorou,custototal)