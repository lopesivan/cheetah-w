"""Classe de template."""
from .factory import Factory


class TEnp3s0f5(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.name = "enp3s0f5"

        self.tmpl.ip = data_model['ip']

    def put(self):
        fileName = "%s.rb" % self.tmpl.name
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%s.rb" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

