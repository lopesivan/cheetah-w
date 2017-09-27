"""Classe de template."""
from .factory import Factory


class THosts(Factory):
    """Classe de template."""
    def __init__(self, data_model, template_name):

        Factory.__init__(self, template_name)

        self.data_model = data_model

        self.tmpl.name = "hosts"

        self.tmpl.ip = data_model['ip']
        self.tmpl.servers = data_model['servers']
        self.tmpl.dns = data_model['dns']

    def put(self):
        fileName = "%s" % self.tmpl.name
        print ("File: %s" % fileName)
        print self.tmpl

    def save(self):
        fileName = "%s" % self.tmpl.name
        print ("Save File: %s" % fileName)
        open(fileName, 'w').write(str(self.tmpl))

