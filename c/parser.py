# encoding: utf-8

import sys
import os
import os.path
import yaml


# Director
class Director(object):

    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# Abstract Builder
class Builder(object):

    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


# Concrete Builder
class BuilderHouse(Builder):

    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'


class BuilderFlat(Builder):

    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# Product
class Building(object):

    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | Size: {0.size}'.format(self)



def uncapitalize(s):
    """TODO: Docstring for uncapitalize.

    :s: TODO
    :returns: TODO

    """
    if len(s) == 0:
        return s
    else:
        return s[0].lower() + s[1:]


def main():

    PATH = sys.argv[1]

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        # Load YAML file
        config_file = file(PATH, 'r')
        dataModel = yaml.load(config_file)
        config_file.close()

        # Class:
        print "<Interface>"
        print 'Class: {}Factory.java'\
            .format(dataModel['Abstract Factory'].capitalize())

        print '{}Factory'\
            .format(dataModel['Abstract Factory'].capitalize())

        for t in dataModel['Family']:
            print '{}{}Factory'\
                .format(t.capitalize(),
                        dataModel['Abstract Factory'].capitalize())

        print ""
        for key, value in dataModel['Products'].iteritems():
            print '{} criar{}'.format(key.capitalize(),
                                      key.capitalize())

        print "<concrete>"
        for t in dataModel['Family']:
            print ""
            print 'Class: {}{}Factory.java'\
                .format(t.capitalize(),
                        dataModel['Abstract Factory'].capitalize())
            print '{}{}Factory'\
                .format(t.capitalize(),
                        dataModel['Abstract Factory'].capitalize())
            print "%sFactory" % \
                dataModel['Abstract Factory'].capitalize()

            for key, value in dataModel['Products'].iteritems():
                print '{} criar{} {}{}'.format(key.capitalize(),
                                               key.capitalize(),
                                               key.capitalize(),
                                               t.capitalize())

        for key, value in dataModel['Products'].iteritems():
            print ""
            print "<Interface>"
            print "Class: {}.java".format(key.capitalize())
            print "{}".format(key.capitalize())
            for v in value:
                print v

        print "<concrete>"
        for key, value in dataModel['Products'].iteritems():
            for t in dataModel['Family']:
                print 'Class: {}{}.java'.format(key.capitalize(),
                                                t.capitalize())
                print '{}{}'.format(key.capitalize(),
                                    t.capitalize())
                print '{}'.format(key.capitalize())
                for v in value:
                    print v

        print "<client>"
        print 'Class: {}.java'.format("client".capitalize())
        print '{}Factory'\
            .format(dataModel['Abstract Factory'].capitalize())
        print '{}'.format(uncapitalize("factory"))
        print '{}Factory.{}()'\
            .format(dataModel['Abstract Factory'].capitalize(),
                    "getFactory")

        for t in dataModel['Family']:
            for key, value in dataModel['Products'].iteritems():
                print '{}'.format(key.capitalize())
                print '{}'.format(uncapitalize(key))
                print '{}.criar{}'\
                    .format(uncapitalize("factory"),
                            key.capitalize())
                for v in value:
                    print '{}.{}()'.format(uncapitalize(key),
                                           v)
        director = Director()
        director.builder = BuilderHouse()
        director.construct_building()
        building = director.get_building()
        print(building)
        director.builder = BuilderFlat()
        director.construct_building()
        building = director.get_building()
        print(building)
    else:
        print "Either file is missing or is not readable"


if __name__ == "__main__":
    main()
