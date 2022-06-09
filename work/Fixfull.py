import requests, sys, re


#try catch valid file name
while True:
    try:
        filename = input("Enter File name: ")
        fastafile = open(filename, "r")
        break   
    except FileNotFoundError:
        print("File not found")
name = open("filename.txt","w")
foldername = filename.split(".", 1)[0]
name.write(foldername)
name.close()

#turn file in array
fastalines = fastafile.readlines()


        
newlines = []
for i in range(len(fastalines)):
    if fastalines[i][0] == ">":
        uniprotid = (str(fastalines[i][1:]).rstrip("\n").split("/", 1)[0])
        try:
            requestURL = str("https://www.uniprot.org/uniprot/"+uniprotid)
            r = requests.get(requestURL, headers={ "Accept" : "application/xml"})
            try:
                #try catch loop add
                responseBody = r.text
                result = re.search('OS=(.*)OX=', responseBody)
                newlines.append("\n>"+result.group(1).rstrip().replace(" ", "_")+"\n")
            except:
                print("error")
        except:
            print("error")
    else:
        newlines.append(fastalines[i])
newname = "fixed"+filename
f = open(newname,"w")
f.close()
f = open(newname,"a")

f.writelines(newlines)
f.close()