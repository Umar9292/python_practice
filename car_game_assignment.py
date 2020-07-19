command = ''
stored_command = ''
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit the car
        ''')
    elif command == 'start' and stored_command != 'start':
        stored_command = 'start'
        print('Car has been started')
    elif command == 'start' and stored_command == 'start':
        print('Car has already been started')
    elif command == 'stop' and stored_command != 'stop':
        stored_command = 'stop'
        print('Car has been stopped')
    elif command == 'stop' and stored_command == 'stop':
        print('Car has already been stopped')
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
