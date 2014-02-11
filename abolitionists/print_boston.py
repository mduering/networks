import codecs
rawfile = "raw_boston.txt"
net_file = []

with codecs.open(rawfile, "r", encoding = "utf-8") as f:
	for line in f:
		net_file.append(line)
f.close()



sort_out = set(net_file)

print sort_out