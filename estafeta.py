class Estafeta:
    def __init__(self, id_estafeta, veiculo, disponibilidade = True):
        self.id_estafeta = id_estafeta
        self.disponibilidade = disponibilidade
        self.veiculo = veiculo
        self.pesoatual = 0
        self.avaliacao = 5
    
    #### GETTERS ####
    
    def getID(self):
        return self.id_estafeta
    
    def getDisponibilidade(self):
        return self.disponibilidade
    
    def getVeiculo(self):
        return self.veiculo
    
    def getPesoAtual(self):
        return self.pesoatual
    
    def getAvaliacao(self):
        return self.avaliacao

    #### SETTERS ####
    
    def setID(self, id_estafeta):
        self.id_estafeta = id_estafeta
         
    def setDisponibilidade(self, disponibilidade):
        self.disponibilidade = disponibilidade
        return self.disponibilidade
    
    def setVeiculo(self, veiculo):
        self.veiculo = veiculo
             
    def setPesoatual(self, pesoatual):
        self.pesoatual = pesoatual
    
    def setAvaliacao(self, avaliacao):
        self.avaliacao = avaliacao