from televisores.marca import Marca
from televisores.control import Control

class TV:
    #atributos de clase
    _numTV = 0

    #atributos de instancia
    def __init__(self, _marca, _estado):
        self._marca = _marca
        self._canal = 1
        self._precio = 500
        self._estado = _estado
        self._volumen = 1
        self._control = None

    #metodos
    @classmethod
    def getNumTV(cls):
        return TV._numTV
    
    @classmethod
    def setNumTV(cls,i):
        TV._numTV += 1

    def getEstado(self):
        return self._estado

    def getMarca(self):
        return self._marca
    
    def setMarca(self, _marca):
        self._marca = _marca

    def getCanal(self):
        return self._canal
    
    def setCanal(self, _canal):
        if (_canal >= 0 and _canal <= 120 and self.getEstado()):
            self._canal = _canal

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, _precio):
        self._precio = _precio

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, _volumen):
        self._volumen = _volumen

    def getControl(self):
        return self._control
    
    def setControl(self, _control):
        self._control = _control

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if(self.getEstado() and self._canal < 120):
            self._canal += 1

    def canalDown(self):
        if(self.getEstado() and self._canal > 0):
            self._canal -= 1
    
    def volumenUp(self):
        if(self.getEstado() and self._volumen < 7):
            self._volumen += 1

    def volumenDown(self):
        if(self.getEstado() and self._volumen > 0):
            self._volumen -= 1


