#!/usr/bin/python

import math

el = int(raw_input("Enter e lower bound (inclusive): "))
eh = int(raw_input("Enter e upper bound (inclusive): "))
e = [el,eh]
n = int(raw_input("Enter the precision (num bits of mantissa): "))
base = int(raw_input("Enter the base: "))
explicit = raw_input("Explicit 1? (y/n)").lower() == 'y'
latex = raw_input("LaTeX? (y/n)").lower() == 'y'

def add_prefixes(array, prefixes):
  return map(lambda x: map(lambda y: str(y) + x, prefixes), array)

def generate_base(num, base, baseTen=True):
  if num <= 0:
    return []
  elif num == 1:
    return map(lambda x: str(x), range(0, base))
  else:
    sub_soln = generate_base(n - 1, base, False)
    this_soln = add_prefixes(sub_soln, range(0, base))
    flat = sorted(reduce(lambda x, y: x + y, this_soln))
    if baseTen:
      return map(lambda x: int(x, base), flat)
    else:
      return flat

if explicit:
  mantissas = map(lambda x: int('1' + x, base), generate_base(n - 1, base, False))
else:
  mantissas = generate_base(n, base)

if latex:
  print "\\begin{tabular}{>{$}c<{$} >{$}c<{$} >{$}c<{$} >{$}c<{$} >{$}c<{$}}"

for exponent in range(e[0], e[1] + 1):
  for mantissa in mantissas:
    data = (mantissa, base, exponent, mantissa * math.pow(2, exponent))
    if latex:
      print "  %s & \\times & %d^{%d} & = & %f\\\\" % data
    else:
      print "%s x %d^{%d} = %f" % data

if latex:
  print "\\end{tabular}"