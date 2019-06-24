# takes in.txt with abc in strightlines without lyrics
# gives out.txt with srg

##ToDo:
# implement transpose that can come around

western = open("in.txt","r")
carnatic = open("out.txt","w")

ASD={"E":"1","F":"2","F#":"3","G":"4","G#":"5","A":"6","A#":"7","B":"8","C":"9","C#":"10","D":"11","D#":"12"}
SRG={"1":"S","2":"R1","3":"R2","4":"G1","5":"G2","6":"M1","7":"M2","8":"P","9":"D1","10":"D2","11":"N1","12":"N2"}

def convertor(note):
    sharp="F"
    final=""
    for index,alpha in enumerate(note):
        if sharp=="T":
            sharp="F"
        else:
            try:
                if(note[index+1]=="#"):
#                     print(SRG[ASD[alpha+"#"]])
                    final=final+str(SRG[ASD[alpha+"#"]])+" "
                    sharp="T"
                else:
#                     print(SRG[ASD[alpha]])
                    final=final+SRG[ASD[alpha]]+" "
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
