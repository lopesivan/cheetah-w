# encoding: utf-8
"""Criação de iarquivos de configuração para ip estático."""

import sys
import os
import os.path
import yaml

import models


def main():
    """Método principal de criação de arquivos."""
    path = sys.argv[1]

    if os.path.isfile(path) and os.access(path, os.R_OK):
        # Load YAML file
        config_file = file(path, 'r')
        data_model = yaml.load(config_file)
        config_file.close()

        t = models.TKnife(data_model, 'chef.conf.knife')
        t.put()
        t.save()

        t = models.TJuca(data_model, 'chef.conf.juca')
        t.put()
        t.save()

        t = models.TInterface(data_model, 'chef.conf.interface')
        t.put()
        t.save()

        t = models.TMakefile(data_model, 'chef.conf.makefile')
        t.put()
        t.save()

    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
