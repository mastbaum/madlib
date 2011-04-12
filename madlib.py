#!/usr/bin/env python

#
# madlib.py
#
# A little madlib maker. Reads original text from a file and makes
# substitutions based on rules in an imported module. Note that this does a
# search-and-replace on the original, not a key-based replacement.
#
# atm, amastbaum@gmail.com
#

import string

class Word:
  '''a mad lib word, consisting of the word itself, a 'part of speech,' and 
     optionally a usage example.
  '''
  def __init__(self, word, pos, usage=''):
    self.word = word
    self.pos = pos
    self.usage = usage

def frequency_count(s, n=0):
  '''returns a sorted list of word frequencies, optionally the first n only'''
  d = {}
  for i in s:
    word = string.lower(i.strip(string.punctuation))
    try:
      d[word] += 1
    except KeyError:
      d[word] = 1

  l = sorted(d.items(), key = lambda item: -item[1])

  if n:
    return l[:n]
  return l

def main(t, wl):
  '''prints a mad-lib-ified of t based on the substitution patterns in wl'''
  for w in wl.wordlist:
    prompt = 'Please enter a ' + w.pos
    if w.usage: prompt += ' (e.g. ' + w.usage + ')'
    prompt += ': '

    s = raw_input(prompt)
    if(w.pos == 'verb' and s[-1] == 'e'):
      s = s[:-1]
    t = string.replace(t, w.word, s)

  print '\n' + '-' * 40 
  print string.capitalize(sys.argv[1])
  print '-' * 40 
  print t

if __name__ == '__main__':
  import sys
  wl = __import__(sys.argv[1])
  f = open(sys.argv[1] + '.txt')
  t = f.read()

  main(t, wl)

