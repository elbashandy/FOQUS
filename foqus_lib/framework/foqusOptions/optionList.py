"""optionList.py

This is an option list class for FOQUS, mainly used for optimization and
surrogate model plugins.

John Eslick, Carnegie Mellon University, 2014
See LICENSE.md for license and copyright details.
"""

from option import *

class optionList(dict):
    def __init__(self):
        '''
            Initalize an option list
        '''
        dict.__init__(self)
        self.order = [] # display order for options

    def clear(self):
        dict.clear(self)
        self.order=[]

    def loadValues(self, sd):
        '''
            Save a dictornary with only option names and values.  Good
            for fixed sets of options, where nothing but the values
            change.
        '''
        if sd == None: return
        for k, v in sd.iteritems():
            if k in self:
                self[k].value = v

    def saveValues(self):
        '''
            Load the option values from a dictionary.
        '''
        sd = {}
        for k, v in self.iteritems():
            sd[k] = v.value
        return sd

    def saveDict(self):
        '''
            Save all of the option attributes to a dictionary.  This is
            good for things like node that have varying sets of options.
        '''
        sd = {'order':self.order, 'options':{}}
        for key in self:
            sd['options'][key] = self[key].saveDict()
        return sd

    def loadDict(self, sd):
        '''
            Load an entire option list from a dictionary.  For things
            with varying sets of options.
        '''
        for opt in sd['options']:
            self[opt] = option()
            self[opt].loadDict(sd['options'][opt])
        self.order = sd.get(
            'order',
            sorted(self.keys(), key=lambda s: s.lower()))

    def addIfNew(
        self,
        name,
        default=0.0,
        value=None,
        desc="An option",
        vmin=None,
        vmax=None,
        dtype=None,
        validValues=[],
        optSet=0,
        disable=False,
        section = "",
        hint = ""):
        '''
            Add an option only if it does not already exist.  Otherwise
            same as add.
        '''
        if name not in self:
            self.add(
                name,
                default=default,
                value=value,
                desc=desc,
                vmin=vmin,
                vmax=vmax,
                dtype=dtype,
                validValues=validValues,
                optSet=optSet,
                disable=disable)

    def add(
        self,
        name,
        default=0.0,
        value=None,
        desc="An option",
        vmin=None,
        vmax=None,
        dtype=None,
        validValues=[],
        optSet=0,
        disable=False,
        section = "",
        hint = ""):
        '''
            Add an option to the list.
        '''
        self[name] = option(
            default=default,
            value=value,
            desc=desc,
            vmin=vmin,
            vmax=vmax,
            dtype=dtype,
            validValues=validValues,
            optSet=optSet,
            disable=disable)
        if name not in self.order:
            self.order.append(name)

    def delete(self, key):
        '''
            delete an option from the list
        '''
        del self[key]
        self.order.remove(key)
