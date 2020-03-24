def readnet(filename):
    f = open(filename, "r", encoding="utf-8-sig")
    net = {}
    elem = f.readline()
    n = int(elem)
    net["noNodes"] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[i].append(float(elems[j]))
    net["mat"] = mat
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] >= 1):
                d += 1
                if (i > j):
                    noEdges += 1
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net


def writerez(rez, filename):
    f = open(filename, "w", encoding="utf-8-sig")
    f.write(str(len(rez.repres)))
    f.write("\n")
    for i in rez.repres:
        f.write(str(i) + ",")
    f.write("\n")
    f.write(str(rez.fitness))
    f.close()