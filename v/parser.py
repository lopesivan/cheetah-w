# encoding: utf-8

import sys
import os
import os.path
import yaml

from java.af.model_abstract_factory import model_abstract_factory


def main():

    PATH = sys.argv[1]

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        # Load YAML file
        config_file = file(PATH, 'r')
        dataModel = yaml.load(config_file)
        config_file.close()

        # Class:
        print("<Interface>")
        print('Class: {}Factory.java'\
            .format(dataModel['Abstract Factory'].capitalize()))

        print('{}Factory'\
            .format(dataModel['Abstract Factory'].capitalize()))

        for t in dataModel['Family']:
            print('{}{}Factory'\
                .format(t.capitalize(),
                        dataModel['Abstract Factory'].capitalize()))

        print("")
        for key, value in dataModel['Products'].iteritems():
            print('{} criar{}'.format(key.capitalize(),
                                      key.capitalize()))

        t = model_abstract_factory()
        t.metodo = "wwww"

        print(t)
    else:
        print("Either file is missing or is not readable")


if __name__ == "__main__":
    main()
