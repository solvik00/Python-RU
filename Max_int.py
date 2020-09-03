#Algorithmi sem biður um jákvæða tölu frá notanda endurtekið þangað til notandinn
#setur inn neikvæða tölu, þá finnur algorithminn stærstu töluna.
num_int = int(input("Input a number: "))
max_int = 0
while num_int>=0: #inntakið þarf að vera jákvætt
    if num_int>max_int:
        max_int = num_int #max_int breytist ef inntakið er stærra en max_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)    