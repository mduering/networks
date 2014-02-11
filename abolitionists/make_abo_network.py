# -*- coding: utf-8 -*-

import networkx as nx
import codecs

# the input file
rawfile = "raw_boston.txt"

# handles the raw file
net_file = []


with codecs.open(rawfile, "r", encoding = "utf-8") as f:

# filters out some garbage from Scrapy
    for line in f:
        line = line.strip("\n")
        if "DEBUG" not in line:
    		net_file.append(line)
f.close()



def make_network(net_file):

# handles the individual nodes
    add_nodes = []

    G = nx.Graph()

# for all the nodes...
    for i in range(len(net_file)):    
        # check whether they are name, source or else (not returned). "i" works as an index to identify the respective node when it comes back
        checker, a = my_containsAny(net_file[i], i)

        # raw data starts with a source, all following non-source lines refer to names or tags. So all returned nodes should be linked to each other
        if checker == "node":
            add_nodes.append(net_file[i])

            G.add_node(net_file[a])

            # for all the lines which have been indentified as nodes within this section, i.e. before the next "source" comes up
            
            w = 0

            for c in range(len(add_nodes)):
                try:
                    # make a complete network of all nodes
                    for b in range(len(add_nodes)):

                        if (add_nodes[c],add_nodes[c+b]) in G.edges():
                            w += 1
                        G.add_edge(add_nodes[c],add_nodes[c+b])
                        G.edge[add_nodes[c]] [add_nodes[c+b]] ['weight'] = w 


                except IndexError:
                    pass


        if checker == "source":
            add_nodes = []



    nx.write_graphml(G, "abolitionists.graphml")
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



make_network(net_file)

