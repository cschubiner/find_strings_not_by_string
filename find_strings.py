#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Find strings that are not around other strings')
parser.add_argument('string_to_find', metavar='string_to_find', type=str,
                    help='the string you want to find')
parser.add_argument('string_to_not_find', metavar='string_to_not_find', type=str,
                    help='the string you don\'t want to find near it')
parser.add_argument('-c', metavar='num_lines', type=int, default=10,
                    help='number of lines to search around string_to_find')
parser.add_argument('-t', metavar='file_type', type=str, nargs='+',
                    help='include this file type (separate multiple file types with spaces)')

args = parser.parse_args()
print(args)
import subprocess

to_include = ''
if args.t is not None:
  for file_type in args.t:
    to_include += ' --include *.' + file_type

grep_str = 'grep -Hnri' + to_include + ' -C ' + str(args.c) + ' "' + args.string_to_find + '" *'
print(grep_str)

stdout = subprocess.Popen(['-c', grep_str], shell=True, stdout=subprocess.PIPE).stdout
grep_result = stdout.read().decode('utf-8')
for res in grep_result.split('\n--\n'):
  if args.string_to_not_find in res:
    continue
  print(res)
  print('\n ------------------ \n')
