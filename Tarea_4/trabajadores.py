class Trabajadores:
    def __init__(self, num, nom, pat, mat, he, sb, adi):
        self.__no_cuenta = num
        self.__nombre = nom
        self.__paterno = pat
        self.__materno = mat
        self.__horas_extras = he
        self.__salario_base = sb
        self.__año_ingreso = adi

    def set_no_cuenta(self,num):
        self.__no_cuenta = num

    def get_no_cuenta(self):
        return self.__no_cuenta

    def set_nombre(self, nom):
        self.__nombre = nom

    def get_nombre(self):
        return self.__nombre

    def set_paterno(self,pat):
        self.__paterno = pat

    def get_paterno(self):
        return self.__paterno

    def set_materno(self,mat):
        self.__materno = mat

    def get_materno(self):
        return self.__materno

    def set_horas_extras(self,he):
        self.__horas_extras = he

    def get_horas_extras(self):
        return self.__horas_extras

    def set_salario_base(self,sb):
        self.__salario_base = sb

    def get_salario_base(self):
        return self.__salario_base

    def set_año_ingreso(self,adi):
        self.__año_ingreso = adi

    def get_año_ingreso(self):
        return self.__año_ingreso

    def to_string( self ):
        return f"No. de trabajador: {self.__no_cuenta}, Nombre: {self.__nombre}, Paterno: {self.__paterno}, Materno: {self.__materno}, Horas extra: {self.__horas_extras}, Salario base: {self.__salario_base}, Año de ingreso: {self.__año_ingreso}."
