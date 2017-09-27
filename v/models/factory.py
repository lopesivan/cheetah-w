# encoding: utf-8
"""Criação de arquivos de configuração para ip estático."""
from abc import ABCMeta, abstractmethod

from chef.conf.enp1s0 import enp1s0
from chef.conf.interface import interface
from chef.conf.named_conf_options import named_conf_options
from chef.conf.db_127 import db_127
from chef.conf.db_local import db_local
from chef.conf.named_conf_local import named_conf_local
from chef.conf.hosts import hosts


template = {
    'chef.conf.enp1s0': enp1s0(),
    'chef.conf.interface': interface(),
    'chef.conf.named_conf_options': named_conf_options(),
    'chef.conf.db_127': db_127(),
    'chef.conf.db_local': db_local(),
    'chef.conf.named_conf_local': named_conf_local(),
    'chef.conf.hosts': hosts(),
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

