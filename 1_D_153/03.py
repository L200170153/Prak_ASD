def hitungVokal(x):
    vokal = "aiueoAIUEO"
    a=0
    for i in x:
        if i in vokal:
            a+=1
    return "("+str(len(x))+", "+str(a)+")"

def hitungKonso(x):
    vokal = "aiueoAIUEO"
    a=0
    for i in x:
        if not i in vokal:
            a+=1
    return "("+str(len(x))+", "+str(a)+")"

print(hitungVokal("Surakarta"))
print(hitungKonso("Surakarta"))
