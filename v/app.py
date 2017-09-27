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

        t = models.TEnp1s0(data_model, 'chef.conf.enp1s0')
        t.put()
        t.save()

        t = models.TInterface(data_model, 'chef.conf.interface')
        t.put()
        t.save()

        t = models.TNamed_conf_options(data_model, 'chef.conf.named_conf_options')
        t.put()
        t.save()

        t = models.TDb_127(data_model, 'chef.conf.db_127')
        t.put()
        t.save()

        t = models.TDb_local(data_model, 'chef.conf.db_local')
        t.put()
        t.save()

        t = models.TNamed_conf_local(data_model, 'chef.conf.named_conf_local')
        t.put()
        t.save()

        t = models.THosts(data_model, 'chef.conf.hosts')
        t.put()
        t.save()

    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
