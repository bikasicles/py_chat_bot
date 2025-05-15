# This is a chat bot

# bill cosbey is the person the user is talking to.

usr_name = input("Hi! I'm Bill Cosby, What is your name?")

mood = input(f"hello {usr_name}, how are you doing? (good, bad)")

if mood.lower == good:
    drink = input(f"{usr_name}, what is your favorite drink?")
    consent = input(f"{drink} is a good choice! May I buy you a drink?")
    if consent.lower == "yes":
        print(f"Great, I'll order yo("u a {drink} while you get washed up!")
        print(f"Back already? Here is your drink!")
        print(f"Well {usr_name}, here is freedom!")
        print(f"*you toast Bill Cosby*")
        location = input(f"Well, {usr_name}, where are you from?")
        print(f"Oh, cool! I've never been.")
        print(f"You have'nt touched your {drink} yet.")
        mood = input("Are you okay?")
        if mood.lower == "yes":
        print(f"")
else:
    consent = input(f"{usr_name}, I'm sorry to hear that! can I buy you a drink?")