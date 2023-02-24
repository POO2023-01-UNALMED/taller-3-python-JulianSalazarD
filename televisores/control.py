class Control:
    #atributos
    def __init__(self):
        self._tv = None

    #metodos
    def getTv(self):
        return self._tv
    
    def setTv(self, _tv):
        self._tv = _tv

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def enlazar(self,_tv):
        self._tv = _tv
        self._tv.setControl(self)

    def setCanal(self,_canal):
        self._canal = _canal
