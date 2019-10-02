# takes in.txt with abc in strightlines without lyrics
# gives out.txt with srg

##ToDo:
# implement transpose that can come around

western = open("in.txt","r")
carnatic = open("out.txt","w")

ASD={"e":"1","f":"2","f#":"3","g":"4","g#":"5","a":"6","a#":"7","b":"8","c":"9","c#":"10","d":"11","d#":"12","E":"13","F":"14","F#":"15","G":"16","G#":"17","A":"18","A#":"19","B":"20","C":"21","C#":"22","D":"23","D#":"24"}
SRG={"0":"n2-","1":"s","2":"r1","3":"r2","4":"g1","5":"g2","6":"m1","7":"m2","8":"p","9":"d1","10":"d2","11":"n1","12":"n2","13":"S","14":"R1","15":"R2","16":"G1","17":"G2","18":"M1","19":"M2","20":"P","21":"D1","22":"D2","23":"N1","24":"N2","25":"S+"}

def convertor(note):
    sharp="F"
    final=""
    transpose = 0
    for index,alpha in enumerate(note):
        if sharp=="T":
            sharp="F"
        else:
            try:
                if(note[index+1]=="#"):
#                     print(SRG[ASD[alpha+"#"]])
#                    print(str(int(ASD[alpha+"#"])+transpose))
                    final=final+str(SRG[str(int(ASD[alpha+"#"])+transpose)])+" "
                    sharp="T"
                else:
#                     print(SRG[ASD[alpha]])
                    final=final+SRG[str(int(ASD[alpha])+transpose)]+" "
            except:
                continue
    return(final)

for line in western:
    thisline = convertor(line)
    carnatic.write(thisline + '\n')
western.close()
carnatic.close()


#S	R1	R2/G1	R3/G2	G3	M1	M2	 P	D1	D2/N1	D3/N2	N3
#E    F	  F#	  G	    G#	 A	A#	 B  C	 C#	      D	    D#
