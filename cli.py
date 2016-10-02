#!/usr/bin/python
# -*- coding: UTF-8, tab-width: 4 -*-

import mkrandid
from sys import argv, stdin, stdout


config = {  # CLI defaults:
    'chars':    '.lchex',   # startswith('.') => pre-defined: lower case hex
    'len':      2,          # ID length: start really short
    'debug':    8,          # verbosity level
    'dupemax':  4,          # quite impatient so you actually see it in action
    'undupe':   1,          # how far to decreases the counter on each non-dupe

    # You can modify all options via CLI args (see the "for" loop below),
    # including these:
    #   dupes:  (number) initial value for the dupe counter.
    # Charset options (see below):
    #   upper:  (bool; alias: AZ) append uppercase letters A-Z
    #   lower:  (bool; alias: az) append lowercase letters a-z
    #   digit:  (bool; alias: 09) append digits 0-9
    #
    # Notes on charset options:
    #   * unavailable (ignored) for pre-defined charsets.
    #   * az and 09 default to True.
    #   => CLI options for using only AZ: chars= 09= az= AZ
    }

for opt in argv[1:]:
    opt = opt.split('=', 1) + [True]
    # ^-- Boolean values: omit the = for True, and set to
    #     empty string for False.
    print 'cli config:', repr(opt[0]), '=', repr(opt[1])
    config[opt[0]] = opt[1]

idm = mkrandid.makeidmaker(config)

dupe = False
print 'Commands: empty line = claim dupe, "q" = quit, anything else: ID was ok'
while True:
    id = idm(dupe)
    print repr(id), repr(mkrandid.introspect(idm))
    stdout.flush()
    ln = stdin.readline()
    if ln == '': break
    ln = ln.rstrip()
    if ln == 'q': break
    dupe = (ln == '')
