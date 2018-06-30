import matplotlib.pyplot as plt
import networkx as nx
import csv_func as csv_func
import matplotlib.patches as mpatches
import matplotlib as mplt
from itertools import count

hschool_list=['LICEUL TEORETIC""GRIGORE MOISIL"" MUN.TIMISOARA','COLEGIUL NATIONAL "CONSTANTIN DIACONOVICI LOGA" MUN.TIMISOARA','COLEGIUL NATIONAL BANATEAN MUN.TIMISOARA','LICEUL PEDAGOGIC "CARMEN SYLVA" MUN.TIMISOARA','COLEGIUL NATIONAL "ANA ASLAN" MUN.TIMISOARA']
school_list=['COLEGIUL NATIONAL "CONSTANTIN DIACONOVICI LOGA" MUN.TIMISOARA','COLEGIUL NATIONAL BANATEAN MUN.TIMISOARA','LICEUL PEDAGOGIC "CARMEN SYLVA" MUN.TIMISOARA','COLEGIUL NATIONAL "ANA ASLAN" MUN.TIMISOARA','LICEUL TEORETIC "GRIGORE MOISIL" MUN.TIMISOARA']
mapping={}


def normalize(x):
    if x>0:
        normal=x/0.5
    else:
        normal = -x /0.5
    return normal


def create_graph(file):
    data_list=csv_func.get_data_from_file(file)
    G = nx.Graph()
    for i in range(0,11):
        G.add_node(i)

    for touple in data_list:
        if touple[1] in school_list:
            G.add_node(touple[0],label=touple[1])
            G.node[touple[0]]['school']=touple[1]
            grade=float(touple[2])
            label = '\n\n\n'+str(grade)#+'\n\n\n'+touple[1]
            ppl_labels[touple[0]]=label
            length = grade - int(grade)
            if grade !=0:
                if grade - int(grade)<0.5:
                    G.add_edge(touple[0],int(grade),weight=1-length)
                else:
                    length=int(grade)+1-grade
                    G.add_edge(touple[0],int(grade)+1,weight=1-length)
            else:
                G.add_edge(touple[0], int(grade))
    return G

def draw_graph(G):

    color_nodelist_touple=color_for_each_attribute(G,'school')
    colors=color_nodelist_touple[0]
    nlist=color_nodelist_touple[1]
    labels={}
    for i in range(0,11):
        labels[i]=i

    pos=nx.spring_layout(G)
    print(pos)
    label_pos=pos
    for posl in label_pos.values():
        posl[1]+=0.1

    print(nx.info(G))
    # nx.draw_networkx_nodes(G,pos=pos,nodelist=nlist,node_size=400,node_color=colors,with_labels=True,cmap=plt.cm.jet)
    # nx.draw_networkx_nodes(G,pos=pos,nodelist=[i for i in range(0,11)],node_size=100,with_labels=True)
    # nx.draw_networkx_edges(G,pos=pos)
    # nx.draw_networkx_labels(G,pos=pos,labels=labels,font_size=16)
    plt.show()
    nx.draw_networkx_nodes(G, pos=pos, nodelist=nlist, node_size=400, node_color=colors, with_labels=True,
                           cmap=plt.cm.jet)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[i for i in range(0, 11)], node_size=300, with_labels=True)
    nx.draw_networkx_edges(G, pos=pos)
    nx.draw_networkx_labels(G, pos=pos, labels=labels, font_size=16)
    nx.draw_networkx_labels(G, pos=label_pos, labels=ppl_labels, font_size=8)


    legend_color_map=color_nodelist_touple[2]
    handle_list=create_handle_for_legend(legend_color_map)
    plt.legend(handles=handle_list)
    plt.show()

def color_for_each_attribute(Graph,attribute):
    schools = set(nx.get_node_attributes(Graph,attribute).values())
    print(schools)
    mapping = dict(zip(sorted(schools), count()))
    print(mapping)
    nodes = Graph.nodes()
    colors=[]
    nlist=[]
    for n in nodes:
        if n not in range(0,11):
            colors.append(mapping[Graph.node[n][attribute]])
            nlist.append(n)
    print(colors)
    return (colors,nlist,mapping)

def create_handle_for_legend(legend_color_map):
    handle_list = []
    norm = mplt.colors.Normalize(vmin=0, vmax=4)
    for school in legend_color_map.keys():
        color = legend_color_map[school]
        cmap = plt.cm.jet
        m = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        print(school + str(color))
        color = m.to_rgba(color)
        patch = mpatches.Patch(color=color, label=school)
        handle_list.append(patch)
    return handle_list

def degree_of_grades_by_school(G):
    print('the degree of node 9 is '+str(G.degree[8]))

ppl_labels = {}
G1=create_graph('BAC.csv')
print(degree_of_grades_by_school(G1))
draw_graph(G1)


school_list=hschool_list
ppl_labels = {}
mapping={}
G2=create_graph('ADM.csv')
print(degree_of_grades_by_school(G2))
draw_graph(G2)
