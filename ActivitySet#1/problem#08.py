# Files

filename = input("dataset/mbox-short.txt")
try:
    fname=open("dataset/mbox-short.txt")
except:
    print("File name cannot be opened",filename)
    exit()
count=0
for line in fname:
    if line.startswith("X-DSPAM-Confidence:"):
        count=count+1
        print('there where',count,'X-DSPAM-Confidence',fname)
