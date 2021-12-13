import re, argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--fileName', default='example-dns-logs.txt',
                    help='Enter the name of DNS log file you would like to parse and sort through - default is example-dns-logs.txt')
args = parser.parse_args()
if args.fileName: fileName = str(args.fileName)
freq = {}
regex = '\(\d.*'
with open(fileName, 'r') as f:    #read DNS log
    log = f.readlines()
for i in range(len(log)):               #finds all elems
    log[i] = re.findall(regex,log[i])
for item in log:                        #calculates freqs
    if tuple(item) in freq:
        freq[tuple(item)] += 1
    else:
        freq[tuple(item)] = 1
sortFreq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))   #sort freqs
for key, value in sortFreq.items():     #outputs sorted DNS log freqs
    try:print(value, key[0])
    except:pass
