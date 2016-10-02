#!/usr/bin/python
# -*- coding: UTF-8, tab-width: 4 -*-


from random import randint


def charsets():
    c = {
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'digit': '0123456789',
        'lchex': '0123456789abcdef',
        'uchex': '0123456789ABCDEF',
        }
    c['base64'] = c['upper'] + c['lower'] + c['digit'] + '+/'
    return c
charsets = charsets()


def introspect(idmaker):
    return idmaker(introspect)


def makeidmaker(opts = None):
    if not isinstance(opts, dict):
        opts = {}
    charset = opts.get('chars', '')
    if (len(charset) > 1) and (charset[0] == '.'):
        charset = charsets[charset[1:]]
    else:
        if opts.get('AZ', opts.get('upper', False)):
            charset += charsets['upper']
        if opts.get('az', opts.get('lower', True)):
            charset += charsets['lower']
        if opts.get('09', opts.get('digit', True)):
            charset += charsets['digit']
    randmax = len(charset) - 1

    state = {
        'idlen': int(opts.get('len', 3)),
        'dupes': int(opts.get('dupes', 0)),
        }
    dupemax = int(opts.get('dupemax', 100))
    undupe  = int(opts.get('undupe', 10))
            # ^-- decay for dupe counter. set to zero or positive depending
            #     on how lucky you feel.

    def dbg(*ignored): pass
    debuglv = int(opts.get('debug', 0))
    if debuglv > 0:
        from sys import stderr
        def dbg(minlv, *msg):
            if (debuglv >= minlv):
                print >>stderr, ' '.join(map(str, msg))


    def idmaker(wasdupe = False):
        dupes = state['dupes']
        idlen = state['idlen']
        if wasdupe:
            if wasdupe is introspect:
                return state
            dupes += 1
            state['dupes'] = dupes
        if dupes > 0:
            if not wasdupe:
                dupes = max(dupes - undupe, 0)
                dbg(2, 'dupe counter decayed to', dupes)
                state['dupes'] = dupes
            if dupes >= dupemax:
                idlen += 1
                state['idlen'] = idlen
                dbg(1, 'reached', dupes, '>=', dupemax,
                    'dupes -> id length was increased to', idlen)
                state['dupes'] = 0
        id = ''
        haslen = 0
        while haslen < idlen:
            id += charset[randint(0, randmax)]
            haslen += 1
        return id

    return idmaker
