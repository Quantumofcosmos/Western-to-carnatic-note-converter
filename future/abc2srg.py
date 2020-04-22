# takes in.txt with abc in strightlines without lyrics
# gives out.txt with srg

##ToDo:
# implement transpose that can come around

western = open("in.txt","r")
carnatic = open("out.txt","w", encoding='utf-16')

#ASD={"e":"1","f":"2","f#":"3","g":"4","g#":"5","a":"6","a#":"7","b":"8","c":"9","c#":"10","d":"11","d#":"12","E":"13","F":"14","F#":"15","G":"16","G#":"17","A":"18","A#":"19","B":"20","C":"21","C#":"22","D":"23","D#":"24"}
SRG={"1":"Ṣ","2":"Ṛ1","3":"Ṛ2","4":"G̣1","5":"G̣2","6":"Ṃ1","7":"Ṃ2","8":"P̣","9":"Ḍ1","10":"Ḍ2","11":"Ṇ1","12":"Ṇ2","13":"S","14":"R1","15":"R2","16":"G1","17":"G2","18":"M1","19":"M2","20":"P","21":"D1","22":"D2","23":"N1","24":"N2","25":"Ṡ","26":"Ṙ1",
 			"27":"Ṙ2","28":"Ġ1","29":"Ġ2","30":"Ṁ1","31":"Ṁ2","32":"Ṗ","33":"Ḋ1","34":"Ḋ2","35":"Ṅ1","36":"Ṅ2"}

ASD={"E3":"1","F3":"2","F3#":"3","G3":"4","G3#":"5","A3":"6","A3#":"7","B3":"8","C4":"9","C4#":"10","D4":"11","D4#":"12","E4":"13","F4":"14","F4#":"15","G4":"16","G4#":"17","A4":"18","A4#":"19","B4":"20","C5":"21","C5#":"22","D5":"23","D5#":"24",
			"E5":"25","F5":"26","F5#":"27","G5":"28","G5#":"29","A5":"30","A5#":"31","B5":"32","C6":"33","C6#":"34","D6":"35","D6#":"36"}

TEST={"E3":"Ṣ","F3":"Ṛ1","F3#":"Ṛ2","G3":"G̣1","G3#":"G̣2","A3":"Ṃ1","A3#":"Ṃ2","B3":"P̣","C4":"Ḍ1","C4#":"Ḍ","D4":"11","D4#":"12","E4":"13","F4":"14","F4#":"15","G4":"16","G4#":"17","A4":"18","A4#":"19","B4":"20","C5":"21","C5#":"22","D5":"23","D5#":"24"}

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


#S	R1	R2/G1	R3/G2	    G3	  M1	M2	 P	D1	D2/N1	D3/N2	N3
#E      F	  F#	  G	    G#	  A	A#	 B      C	 C#	  D	D#
