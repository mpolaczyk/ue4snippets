#!/usr/bin/env python

from string import Template


class Delegate:

    paramSuffix = ['', '_OneParam', '_TwoParams', '_ThreeParams', '_FourParams', '_FiveParams', '_SixParams', '_SevenParams', '_EightParams']
    
    def __init__(self, kind, name, owningType, paramTypes, paramNames):
        self.kind = kind
        self.name = name
        self.owningType = owningType
        self.paramTypes = paramTypes
        self.paramNames = paramNames
        

    def Generate(self):
        a =  'DECLARE_${kind}'
        b = self.paramSuffix[len(self.paramNames)]
        c = '(${name}' if self.owningType == '' else ''.join(['({0}'.format(self.owningType), ', ${name}']) 
        d = ''
        if len(self.paramNames) > 0:
            d = ''.join([', {0}, {1}'.format(str(pt), str(pn)) for pt, pn in zip(self.paramTypes, self.paramNames)])
        else:
            d = ''.join([', {0}'.format(str(pn)) for pn in self.paramTypes])
        e = ')'
        return Template(''.join([a,b,c,d,e])).substitute(kind = self.kind, name = self.name)


class DelegateGeneratorTest:

    def __init__(self, maxParams):
        self.maxParams = maxParams
    
    def TestEvents(self):
        for n in range(1, self.maxParams + 2):
            print(Delegate('EVENT', '$name$', '$owning_type$', ['$$type{0}$$'.format(p) for p in range(1,n)], []).Generate())

    
    def TestDelegates(self):
        for n in range(1, self.maxParams + 2):
            print(Delegate('DELEGATE', '$name$', '', ['$$type{0}$$'.format(p) for p in range(1,n)], []).Generate())

    
    def TestMulticastDeleates(self):
        for n in range(1, self.maxParams + 2):
            print(Delegate('MULTICAST_DELEGATE', '$name$', '', ['$$type{0}$$'.format(p) for p in range(1,n)], []).Generate())

    
    def TestDynamicDelegates(self):
        for n in range(1, self.maxParams + 2):
            print(Delegate('DYNAMIC_DELEGATE', '$name$', '', ['$$type{0}$$'.format(p) for p in range(1,n)], ['$$name{0}$$'.format(p) for p in range(1,n)]).Generate())

    
    def TestDynamicMulticastDelegates(self):
        for n in range(1, self.maxParams + 2):
            print(Delegate('DYNAMIC_MULTICAST_DELEGATE', '$name$', '', ['$$type{0}$$'.format(p) for p in range(1,n)], ['$$name{0}$$'.format(p) for p in range(1,n)]).Generate())