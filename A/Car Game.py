
# while True:
#     command = input('> ').lower()
#     if command == 'help':
#         print('''
# start - to start the car
# stop - to stop the car
# quit - to exit''')
#     elif command == 'start':
#         print('Car Started... Ready to go!')
#     elif command == 'stop':
#         print('Car Stopped.')
#     elif command == 'quit':
#         break
#     else:
#         print("I don't understand that...")


started = False
while True:
    command = input('> ').lower()
    if command == 'help' :
        print('''
start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print('Car Started... Ready to go!')
    elif command == 'stop':
        if not started:
            print('Car is already stopped')
        else:
            started = False
            print('Car Stopped.')
    elif command == 'quit':
        break
    else:
        print("I don't understand that... Type 'help' to see command ")