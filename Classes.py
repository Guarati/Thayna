from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nome, senha, area, periodo):
        self._nome = nome
        self._senha = senha
        self._area = area
        self._periodo = periodo


    # Getters
    def get_nome(self):
        return self._nome

    def get_senha(self):
        return self._senha

    def get_area(self):
        return self._area

    def get_periodo(self):
        return self._periodo

    # Setters
    def set_nome(self, nome):
        self._nome = nome

    def set_senha(self, senha):
        self._senha = senha

    def set_area(self, area):
        self._area = area

    def set_periodo(self, periodo):
        self._periodo = periodo


class Aluno(Usuario):
    def __init__(self, nome, senha, area, periodo, diasdisponiveis):
        super().__init__(nome, senha, area, periodo)
        self.diasdisponiveis = diasdisponiveis

    def get_info(self):
        return f'Aluno: {self._nome}, Área: {self._area}, Período: {self._periodo}, Dias Disponíveis: {self.diasdisponiveis}'


class Empresa(Usuario):
    def __init__(self, nome, senha, area, periodo, salario):
        super().__init__(nome, senha, area, periodo)
        self.salario = salario

    def get_info(self):
        return f'Empresa: {self._nome}, Área: {self._area}, Período: {self._periodo}, Salário Oferecido: {self.salario}'


