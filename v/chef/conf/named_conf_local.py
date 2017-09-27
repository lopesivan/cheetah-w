#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1506526474.53384
__CHEETAH_genTimestamp__ = 'Wed Sep 27 12:34:34 2017'
__CHEETAH_src__ = '../m/named_conf_local.tmpl'
__CHEETAH_srcLastModified__ = 'Wed Sep 27 11:36:31 2017'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class named_conf_local(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(named_conf_local, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";

// Zona de pesquisa direta.
zone "''')
        _v = VFFSL(SL,"dns.domain",True) # u'${dns.domain}' on line 10, col 7
        if _v is not None: write(_filter(_v, rawExpr=u'${dns.domain}')) # from line 10, col 7.
        write(u'''" {
  type master;
  file "/etc/bind/''')
        _v = VFN(VFFSL(SL,"dns.domain",True),"split",False)('.')[0] # u"${dns.domain.split('.')[0]}" on line 12, col 19
        if _v is not None: write(_filter(_v, rawExpr=u"${dns.domain.split('.')[0]}")) # from line 12, col 19.
        write(u'''/db.''')
        _v = VFFSL(SL,"dns.domain",True) # u'${dns.domain}' on line 12, col 50
        if _v is not None: write(_filter(_v, rawExpr=u'${dns.domain}')) # from line 12, col 50.
        write(u'''";
};

// Zona de pesquisa reversa.
zone "''')
        _v = VFN(VFFSL(SL,"ip.address",True),"split",False)('.')[2] # u"${ip.address.split('.')[2]}" on line 16, col 7
        if _v is not None: write(_filter(_v, rawExpr=u"${ip.address.split('.')[2]}")) # from line 16, col 7.
        write(u'''.''')
        _v = VFN(VFFSL(SL,"ip.address",True),"split",False)('.')[1] # u"${ip.address.split('.')[1]}" on line 16, col 35
        if _v is not None: write(_filter(_v, rawExpr=u"${ip.address.split('.')[1]}")) # from line 16, col 35.
        write(u'''.''')
        _v = VFN(VFFSL(SL,"ip.address",True),"split",False)('.')[0] # u"${ip.address.split('.')[0]}" on line 16, col 63
        if _v is not None: write(_filter(_v, rawExpr=u"${ip.address.split('.')[0]}")) # from line 16, col 63.
        write(u'''.in-addr-arpa" {
  type master;
  file "/etc/bind/''')
        _v = VFN(VFFSL(SL,"dns.domain",True),"split",False)('.')[0] # u"${dns.domain.split('.')[0]}" on line 18, col 19
        if _v is not None: write(_filter(_v, rawExpr=u"${dns.domain.split('.')[0]}")) # from line 18, col 19.
        write(u'''/db.''')
        _v = VFFSL(SL,"dns.reverse",True) # u'${dns.reverse}' on line 18, col 50
        if _v is not None: write(_filter(_v, rawExpr=u'${dns.reverse}')) # from line 18, col 50.
        write(u'''";
};


''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_named_conf_local= 'respond'

## END CLASS DEFINITION

if not hasattr(named_conf_local, '_initCheetahAttributes'):
    templateAPIClass = getattr(named_conf_local, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(named_conf_local)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=named_conf_local()).run()

