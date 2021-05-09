from __future__ import unicode_literals
import json
import matplotlib.pyplot as plt
import numpy as np
#
#
#
# f = open('usersjson2.txt', 'r')
# users = json.loads(f.read())
# retweets = []
# for usr in users:
#     retweets.append(users[usr]["retweets"])
#
# N_points = 100000
# n_bins = 200
#
# plt.rcParams['mathtext.fontset'] = 'stix'
# plt.rcParams['font.family'] = 'STIXGeneral'
#
# # Generate a normal distribution, center at x=0 and y=5
# x = retweets
# print(np.min(x), np.max(x))
# # plt.rc('text', usetex=True)
# # plt.rc('font', family='serif')
#
# # plt.rc('font', family='')
#
# fig = plt.figure(figsize=(9,5))
# ax = fig.add_subplot(111)
# # ax2 = fig.add_subplot(111)
#
# a=np.arange(6)
# b = np.arange(1, 300, 1)
#
# # We can set the number of bins with the `bins` kwarg
# ax.hist(x, bins=b, histtype='step', color='k', linewidth=1.1, label = 'aktywność użytkowników')
# # ax2.hist(x, bins=a, histtype='step', color='k', linewidth=1.1, label = 'aktywność użytkowników')
# ax.set_xlabel("liczba tweeetów", fontsize=12)
# ax.set_ylabel("liczba użytkowników", fontsize=12)
#
# # ax2.set_xlabel("liczba tweeetów")
# # ax2.set_ylabel("liczba użytkowników")
#
# # ax.set_ylim(ymin=0, ymax=100)
#
#
# ax.set_yscale('log')
# ax.set_xscale('log')
# # ax2.set_yscale('log')
# # ax2.set_xscale('log')
# plt.legend()
#
# plt.savefig('wykres1log.pdf')
#
#
#
# plt.show()


########################################################
#ITERACJE
########################################################

# fig = plt.figure(figsize=(9,5))
# # ax = fig.add_subplot(111)
# ax2 = fig.add_subplot(111)
#
# yy    = [5042, 5104, 5184, 5401, 6024, 6469, 6782]
# xx = [2, 5, 10, 20, 50, 100, 200]
#
# yy2 = [63958, 63920, 63866, 63361, 60558, 56680, 55233, 54900]
#
# # We can set the number of bins with the `bins` kwarg
# # ax.hist(x, bins=b, histtype='step', color='k', linewidth=1.1, label = 'aktywność użytkowników')
# ax2.scatter(xx, yy, color='k', linewidth=1.1, label = 'średnie przystosowanie grupy')
# # ax.set_xlabel("ilość tweeetów", fontsize=12)
# # ax.set_ylabel("ilość użytkowników", fontsize=12)
#
# ax2.set_xlabel("liczba iteracji")
# ax2.set_ylabel("przystosowanie")
#
#
# # ax.set_yscale('log')
# # ax.set_xscale('log')
# # ax2.set_yscale('log')
# # ax2.set_xscale('log')
# plt.legend()
#
# plt.savefig('przystIter.pdf')
# plt.show()


########################################################
#KOLONIA
########################################################


fig = plt.figure(figsize=(9,5))
# ax = fig.add_subplot(111)
ax2 = fig.add_subplot(111)

yy1 = [5158, 6960, 8484, 8598, 8921, 8945]
xx = [10, 12, 15, 20, 30, 50]

yy2 = [28668, 39695, 48221, 51658, 57445, 53467]

ax2.scatter(xx, yy2, color='k', linewidth=1.1, label = 'średnie przystosowanie użytkownika')


ax2.set_xlabel("liczba pszczół")
ax2.set_ylabel("przystosowanie")

# ax.set_ylim(ymin=0, ymax=100)


# ax.set_yscale('log')
# ax.set_xscale('log')
# ax2.set_yscale('log')
# ax2.set_xscale('log')
plt.legend(loc=4)

plt.savefig('przystKolGlob.pdf')

plt.show()