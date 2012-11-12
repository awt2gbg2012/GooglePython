#!/usr/local/bin/python

# import modules
import sys

# main function
def main():
  print repeat('Yay', False)
  print repeat('Woo Hoo', True)

# repeat function
def repeat(s, exclaim):
  result = s + s + s
  if exclaim:
    result = result + '!!!'
  return result    

# boilerplate
if __name__ == '__main__':
  main()
