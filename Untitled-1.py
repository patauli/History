from setuptools import Command


Command=''
while Command !="quit":
    command=input(">")
    if command=="start":
        print("started")
    elif command=="stop":
        print("stopped")
    else:
        print("I dont undstand")

