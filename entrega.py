class Entrega:
    def __init__(self, id_entrega, prazo, destino, pontodepartida,estado):
        self.id_entrega = id_entrega
        self.prazo = prazo
        self.destino = destino
        self.pontodepartida = pontodepartida
        self.rating = 5
        self.estafetadeservico = None
        self.custo = None
        self.estado = estado
    
    #### GETTERS ####
    def getestado(self):
        return self.estado

    def getID(self):
        return self.id_entrega
    
    def getPrazo(self):
        return self.prazo
    
    def getDestino(self):
        return self.destino
    
    def getPontoDePartida(self):
        return self.pontodepartida
    
    def getRating(self):
        return self.rating
    
    def getEstafetaDeServico(self):
        return self.estafetadeservico
    
    def getPreco(self):
        return self.custo
    
    #### SETTERS ####
    def setEstado(self, estado):
        self.estado = estado

    def setID(self, id_entrega):
        self.id_entrega = id_entrega
        
    def setPrazo(self, prazo):
        self.prazo = prazo
        
    def setDestino(self, destino):
        self.destino = destino
        
    def setPontoDePartida(self, pontodepartida):
        self.pontodepartida = pontodepartida
        
    def setRating(self, rating):
        self.rating = rating
    
    def setEstafetaDeServico(self, estafetadeservico):
        self.estafetadeservico = estafetadeservico
    
    def setCusto(self, custo):
        self.custo = custo
