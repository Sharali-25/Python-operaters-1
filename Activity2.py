Amount=int(input("Plz enter amount for withdraw"))
note_1=Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10
print("Note of 100 rupee",note_1)
print("Note of 50 rupee",note_2)
print("Note of 10 rupee",note_3)