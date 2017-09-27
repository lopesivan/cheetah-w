"""Classe de template."""
from .factory import Factory


class TDb_127(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.ip = data_model['ip']
        self.tmpl.dns = data_model['dns']
        self.tmpl.machines = data_model['machines']

        self.tmpl.name = "db.%s" % self.tmpl.dns['reverse']

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

