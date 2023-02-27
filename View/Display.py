class Display:
    def flash(self, message):
        print(message+'\n')

    def promt(self, message):
        return input(message)

    def greet(self):
        print('Good day!\n'
              'Welcome to NoteApp\n')
    def say_bye(self):
        print('Let me save your notes...\n'
              'And good bye!')
    def show_all(self, note_list):
        print_notes = lambda lst: [print(str(n)) for n in lst]
        print_notes(note_list)

    def commands(self):
        com_list = ['create', 'update', 'delete', 'find', 'list', 'exit']
        print('Command list:')
        for i, com in enumerate(com_list, start = 1):
            print(f'{i}. {com}')

    def oopsie(self):
        print('Something went wrong... Awkward...')

    def format_picker(self):
        inp_value = input('Choose file format:').lower()
        formats = ['txt', 'json', 'csv', 'xml']
        for i, fmt in enumerate(formats, start = 1):
            print(f'{i}. {fmt}')
        if inp_value == '1' or 'txt':
            return 1
        elif inp_value == '2' or 'json':
            return 2
        elif inp_value == '3' or 'csv':
            return 3
        elif inp_value == '4' or 'xml':
            return 4
        else:
            print('Error: Incorrect input value')
            return 'Incorrect input'