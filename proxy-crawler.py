import urllib

urls = ['http://www.cnproxy.com/proxy%d.html'%x for x in xrange(1,11)]+['http://www.cnproxy.com/proxyedu%d.html'%x for x in xrange(1,3)]

def handle(url):
    text = []
    for line in urllib.urlopen(url):
        if line.find("SCRIPT")>0:
            text.append(line.decode('gbk').strip())
    change = text[1]
    text = [x for x in text[2:] if x.find("HTTP")>0]

    changedict = dict([tuple(x.replace('\"','').split("=")) for x in change.split(';')][:-1])
    ret = []
    for t in text:
        ta = [x.replace("</td>","") for x in t[4:-5].split('<td>') if x]
        idx0 = ta[0].find("\":\"+")
        idx1 = ta[0].find(")</SCRIPT>")
        idx2 = ta[0].find("<SCRIPT")
        port_orig = ta[0][idx0+4:idx1].replace("+","")
        port = ''.join([changedict[p] for p in port_orig])
        ret.append(([ta[0][:idx2],port,ta[1],ta[2],ta[3]]))
    return ret

res = []
for url in urls:
    ret = handle(url)
    res.extend(ret)
out = [x[0]+" "+x[1] for x in res]
out = list(set(out))

f = open("ip1.txt","w")
for ret in out:
    f.write(ret+"\n")
f.close()

