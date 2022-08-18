import decorators
from collections import UserDict


class Field:
    def __init__(self, value: str):
        self.value = value


class Name(Field):
    def __init__(self, *args):
        super().__init__(*args)


class Phone(Field):
    def __init__(self, *args):
        super().__init__(*args)


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name: Name = name
        self.phone: list[Phone] = [phone] if phone is not None else []

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        try:
            self.phone.remove(old_phone)
            self.phone.append(new_phone)
        except ValueError:
            return f'Old_phone: {old_phone} has not existed to change'

    def remove_phone(self, phone: Phone):
        try:
            self.phone.remove(phone)
        except ValueError:
            return f'Phone: {phone} has not existed to delete'

    def __repr__(self):
        return f"{self.name.value}:{[phone.value for phone in self.phone]}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


phone_book = AddressBook()


def hello_handler():
    return 'How can I help you?'


@decorators.add_error_decorator
def add_handler(*args):
    phone_book.update({args[0]: args[1]})
    return 'Telephone number has beem added'


@decorators.change_error_decorator
def change_handler(*args):
    phone_book[args[0]] = args[1]
    return 'Telephone number has beem changed'


@decorators.phone_error_decorator
def phone_handler(*args):
    return phone_book[args[0]]


def show_all_handler():
    title = 'Telephone Book\n'
    contacts = '\n'.join(f'{name} - {phone_number}' for name, phone_number in phone_book.items())
    f_contacts = 'Number does not  exist' if contacts == '' else contacts
    return title + f_contacts


def exit1_handler():
    return 'Good bye!'


def exit2_handler():
    return 'Good bye!'


def exit3_handler():
    return 'Good bye!'


commands = {
            hello_handler: 'hello',
            add_handler: 'add',
            change_handler: 'change',
            phone_handler: 'phone',
            show_all_handler: 'show all',
            exit1_handler: 'exit',
            exit2_handler: 'close',
            exit3_handler: 'good bye',
        }


def user_input_parser(user_input):
    arguments = []
    command = ""
    for k, v in commands.items():
        if user_input.startswith(v):
            command = k
            arguments = user_input.replace(v, "").split()
    return command, arguments


@decorators.input_error_decorator
def main():
    while True:
        user_input = input('Command: ').lower()
        command, arguments = user_input_parser(user_input)
        print(command(*arguments))
        if command == exit1_handler or command == exit2_handler or command == exit3_handler:
            break


if __name__ == '__main__':
    main()

