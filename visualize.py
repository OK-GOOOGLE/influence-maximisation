import json

import matplotlib.pyplot as plt
import networkx as nx

graph = nx.DiGraph()
f = open('usersjson2.txt', 'r')
users = json.loads(f.read())
graph.add_nodes_from(users.keys())

for user in users:
    for retweet in users[user]["RetweetedBy"]:
        graph.add_edge(user, retweet)

graph.remove_nodes_from(list(nx.isolates(graph)))
f = nx.Graph()
deg1 = 10
deg2 = 10
fedges = filter(lambda x: graph.degree()[x[0]] > deg1 and graph.degree()[x[1]] > deg2, graph.edges())
f.add_edges_from(fedges)
print(f.number_of_nodes())
print(f.number_of_edges())
pos = nx.spring_layout(f)
deg = 500
subnodes = [node for node,degree in graph.degree() if degree > deg]
allnodes = f.nodes()
subnodes = list(set (subnodes) - (set(subnodes) - set(allnodes)))
nx.draw_networkx_nodes(f, pos, node_size=5, with_labels=True)
nx.draw_networkx_nodes(f, pos, nodelist=subnodes, with_labels=True, node_color='c',  node_size=10)
nx.draw_networkx_edges(f, pos )
labels = {}
for node in subnodes:
    labels[node] = node
nx.draw_networkx_labels(f,pos, labels, font_color='w',font_size=18)


# plt.subplot(122)
plt.axis('off')
plt.show()
#
# plt.axis('off')
# plt.show()

# for user in users:
#     graph.add_node(user)
#
# retweets = []
# i = 0
# users_map = {}
#
# for usr in users:
#     users_map[usr] = i
#     i+=1
#
# k = 0
# for usr in users:
#     # users_map[usr] = i
#     graph.add_node(users_map[usr])
#     # print("added")
#     for retw in users[usr]["RetweetedBy"]:
#         if users_map[retw] not in graph.nodes:
#             graph.add_node(users_map[usr])
#         graph.add_edge(users_map[usr], users_map[retw])
#     k += 1
#     if k >= 3:
#         break
#     #     print(usr, users[usr])
#
#
#
#
#     # retweets.append(users[usr]["retweets"])
#
#
#
#
# # G = nx.random_geometric_graph(5, 1)
# # print(G.nodes)
# # position is stored as node attribute data for random_geometric_graph
# pos = nx.get_node_attributes(graph, 'pos')
#
# # find node near center (0.5,0.5)
# dmin = 1
# ncenter = 0
# for n in pos:
#     x, y = pos[n]
#     d = (x - 0.5)**2 + (y - 0.5)**2
#     if d < dmin:
#         ncenter = n
#         dmin = d
#
# # color by path length from node near center
# p = dict(nx.single_source_shortest_path_length(graph, ncenter))
# # print(graph.nodes)
# plt.figure(figsize=(8, 8))
# nx.draw_networkx_edges(graph, nx.spring_layout(graph))#,  alpha=0.4)
# nx.draw_networkx_nodes(graph, nx.spring_layout(graph),
#                        node_size=80,
#                        node_color='c',
#                        cmap=plt.cm.Reds_r)
# # j =0
# # for i in p:
# #     j+=1
# #     print(i)
# #     if j > 10:
# #         break
# # print(graph.nodes)
# plt.xlim(-0.05, 1.05)
# plt.ylim(-0.05, 1.05)
# plt.axis('off')
# plt.show()