# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from chef.conf.enp3s0f5 import enp3s0f5
from chef.conf.interface import interface


template = {
    'chef.conf.enp3s0f5': enp3s0f5(),
    'chef.conf.interface': interface(),
}


class Factory(object):
    """Metodo fabrica."""
    __metaclass__ = ABCMeta

    def __init__(self, template_name):
        self.tmpl = template[template_name]

    @abstractmethod
    def put(self):
        """Imprime mensagem na tela."""
        pass

    @abstractmethod
    def save(self):
        """Salva em arquivo."""
        pass

