# -*- coding:utf8 -*-
import random

print "--古战抽奖--\n"
listmax = int(raw_input('最大排名数字 > '))
listarr = range(1, listmax + 1)
winnum = int(raw_input('中奖人数 > '))
listkey = int(raw_input('去除排名 > '))
listarr.pop(-(listmax - listkey + 1))

print "显示数组\n"
print (listarr)
print "抽取中奖数- %r位" % winnum
print (random.sample(listarr, winnum))
