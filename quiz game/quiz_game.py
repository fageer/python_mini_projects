print("Welcome to Fager Quiz🥳.")
playing = input("Do You want to Play? ").lower()
while playing not in ['y', 'yes']:
        print("You Should Enter 'Y' or 'YES' to Play")
        playing = input("Do You want to Play? ").lower()
    
print("Let's playing 🥳.")
success = 0
fail = 0

q1 = input("How much Player In Soccer Team?\n").lower()
if q1 == '11':
    print(f"{q1} is Correct answer ✅.")
    success += 1
else:
    print(f"{q1}is Incorrect answer ❌.")
    fail += 1


q2 = input("What is The Name of the play that won golden ball 8 time?\n").lower()
if q2 == 'messi':
    print(f"{q2} is Correct answer ✅.")
    success += 1
else:
    print(f"{q2}is Incorrect answer ❌.")
    fail += 1


q3 = input("where neymar currently playin?\n").lower()
if q3 == 'psg':
    print(f"{q3} is Correct answer ✅.")
    success += 1
else:
    print(f"{q3}is Incorrect answer ❌.")
    fail += 1


q4 = input("where rodrygo currently playin?\n").lower()
if q4 == 'real madrid':
    print(f"{q4} is Correct answer ✅.")
    success += 1
else:
    print(f"{q4}is Incorrect answer ❌.")
    fail += 1


q5 = input("where joaoflex currently playing?\n").lower()
if q5 == 'barcelona':
    print(f"{q5} is Correct answer ✅.")
    success += 1
else:
    print(f"{q5}is Incorrect answer ❌.")
    fail += 1



print("You got {} answer Correct.\nand got {} answers Incorrect.".format(success,fail))
print("You got {}%.".format((success / 5) * 100))
print("Thanks for Playing 🙏.")


