# -*- coding: utf-8 -*-

import networkx as nx
from networkx.algorithms import bipartite as bnx
import codecs
import itertools

# the input file
rawfile = "raw_boston.txt"
#rawfile = "testp.txt"

# handles the raw file
raw_file_list = []


with codecs.open(rawfile, "r", encoding = "utf-8") as f:

# filters out some garbage from Scrapy
    for line in f:
        line = line.strip("\n")
        if "DEBUG" not in line:
    		raw_file_list.append(line)
f.close()



def make_network(raw_file_list):

# handles the individual nodes
    collect_nodes_by_source = []
    list_of_source_names = []
    node_list = []

    GB = nx.Graph()

# for all the nodes...
    for i in range(len(raw_file_list)):    
        # check whether they are name, source or else (not returned). "i" works as an index to identify the respective node when it comes back
        checker, a = my_containsAny(raw_file_list[i], i)

        # raw data starts with a source, all following non-source lines refer to names or tags. So all returned nodes should be linked to each other
        
        if checker == "source":
            GB.add_node(raw_file_list[a], bipartite = 0)
            source = raw_file_list[a]

        while source == raw_file_list[a]:
            if checker == "node":
                GB.add_node(raw_file_list[a], bipartite = 1)  
                GB.add_edge(raw_file_list[a], raw_file_list[a+1])


    G = bnx.weighted_projected_graph(GB, GB.nodes(["bipartite"]==1))

    #nx.write_graphml(GB, "abolitionists_bipartite.graphml")
    nx.write_pajek(G, "abolitionists.net")

    print "done!"




def my_containsAny(line, i):

# ":" and "[" are typically found in descriptions of sources, "," in author names. check_source will 

    a = i

    if "[" in line: 
        #print "found ["
        return "source", a

    elif ":" in line : 
        #print "found :"
        return "source", a

    elif "," in line: 
        #print "found ,"
        return "node", a

    elif "Antislavery movements" in line:
        return "None", a
    
    elif "Abolitionists" in line:
        return "None", a   

    elif "Anti-slavery " in line:
        return "None", a


    elif "An " in line:
        return "None", a

    elif "A " in line:
        return "None", a

    else:
        return "None", a




def complete_ties(L, create_using=None):


    G=nx.empty_graph(len(L),create_using)

    if G.is_directed():
        edges=itertools.permutations(L,2)
    else:
        edges=itertools.combinations(L,2)
    G.add_edges_from(edges)
    return G


make_network(raw_file_list)

