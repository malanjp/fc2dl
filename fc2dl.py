#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os, sys, re, commands, argparse, hashlib, requests

FC2magick = '_gGddgPfeaf_gzyr'  #updated FC2 2011.7


""" argments setting
"""
parser = argparse.ArgumentParser(description='FC2 video download script.')
parser.add_argument('target_url',
                   help='fc2 video page url.')
parser.add_argument('-o', '-O', '--outfile',
                   help='output filename.')


args = parser.parse_args()
match = re.search(r'http:\/\/video\.fc2\.com\/content\/(\w+)/?$', args.target_url)
print args

if match is None:
  match = re.search(r'http:\/\/video\.fc2\.com\/a\/content\/(\w+)/?$', args.target_url)
  if match is None:
    print "doesn't match"
    quit()

target = match.group(1)
print 'target:', target

mini = hashlib.md5(target + FC2magick).hexdigest()
ginfo_url = 'http://video.fc2.com/ginfo.php?mimi=' + mini + '&v=' + target + '&upid=' + target + '&otag=1'
#print ginfo_url
filepath = commands.getoutput("curl -L -R '%s'" % ginfo_url)
#print filepath
title = filepath.split('&')[15].split('=')[1]  # title(need encode)
url =  filepath.split('&')[0].split('=')[1] + '?' + filepath.split('&')[1]
print title
print 'flv url:', url

print args.outfile
if args.outfile:
  title = args.outfile

command = "curl -L -R -o '%s.flv' '%s'" % (title, url)
print command
os.system(command)


