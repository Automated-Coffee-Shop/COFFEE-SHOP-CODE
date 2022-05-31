import random
cream = random.randint(1,10)
print ("Cream Score:",cream)
taste = random.randint(1,10)
print ("Taste Score:",taste)
smell = random.randint(1,10)
print ("Smell Score:",smell)
avg = ((cream + taste + smell)/3)
formatted_string = "{:.2f}".format(avg)
float_value = float(formatted_string)
print("Average Score:",float_value)

if float_value<=7:
    print("Do not serve")
if float_value>7:
    print("Ready to serve")