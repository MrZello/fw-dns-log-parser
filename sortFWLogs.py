import re, argparse
parser = argparse.ArgumentParser()
parser.add_argument('-e','--exclude', default='0.0.0',
                    help='Enter the first three octets for the subnet you would like to exclude, e.i. 192.168.0 - default is 0.0.0')
parser.add_argument('-f', '--fileName', default='example-fw-logs.txt',
                    help='Enter the name of FW log file you would like to parse and sort through - default is example-fw-logs.txt')
args = parser.parse_args()
if args.exclude: exclude = str(args.exclude)
if args.fileName: fileName = str(args.fileName)
ipv4 = '\d+\.\d+\.\d+\.\d+'
ipv6 = '[a-fA-F0-9]+\::[a-fA-F0-9:]+'
src, dst = [],[]
srcF, dstF = {},{}
with open(fileName, 'r') as f: #read log file
    log = f.read()
tmp = re.findall(ipv4, log)                 #parse for IPs
tmp += re.findall(ipv6, log)
for each in range(len(tmp)):                #create src and dst lists
    if each%2 == 0 : src.append(tmp[each])
    else : dst.append(tmp[each])
for i in src:                               #calc src IP freqs
    if i in srcF: srcF[i] += 1
    else: srcF[i] = 1
for i in dst:                               #calc dst IP freqs
    if i in dstF: dstF[i] += 1
    else: dstF[i] = 1
sortSrc = dict(sorted(srcF.items(), key=lambda x: x[1], reverse=True))
sortDst = dict(sorted(dstF.items(), key=lambda x: x[1], reverse=True))
for key, value in sortSrc.items():          #output sorted src IPs
    if key[:-2] == exclude or key[:-3] == exclude or key[:-4] == exclude: pass
    else: print('src', value, key)          #if stmnt is for the IP exclusion
print()
for key, value in sortDst.items():          #output sorted dst IPs
    if key[:-2] == exclude or key[:-3] == exclude or key[:-4] == exclude: pass
    else: print('dst', value, key)          #if stmnt is for the IP exclusion
