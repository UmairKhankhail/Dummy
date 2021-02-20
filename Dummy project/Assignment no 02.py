alphabets=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number=-1
for individual in alphabets:
    number+=1
    if number%4==0:
        print()
    print(individual,end= "        ")

columns=[]

print("\nThink any word.")
length_of_word=int(input("Enter the length of word you thought: "))

if length_of_word==1:
    a = int(input("Enter the column number of the letter: "))
    columns.append(a)
else:
 for i in range(length_of_word):
    a=int(input("Enter the column number of letter no. "+str((i+1))+" : "))
    columns.append(a)

for j in range(25):
 for new_individual in alphabets:
    if (j==1 or j%3==0):
        print(alphabets[j])
