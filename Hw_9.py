def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
            
        except KeyError:
            print(f'Please enter your name')
        except ValueError:
            print(f'Please enter your phone number')
        except IndexError:
            print(f"Please enter your name and your phone number divided by space")
            
    return inner

@input_error
def func_hello():
    return "Hello, how can I help you?"

@input_error
def  add_contact():
    add_input = input("Please enter your name and your phone number: ")
    list = add_input.split()
    dict[list[0]]=list[1]
    return "Contact saved"
    
@input_error
def change_contact():
    add_input = input("Please enter your name and your phone number: ")
    list = add_input.split()
    dict[list[0]]=list[1]
    return "Contact changed"
 
@input_error
def show_phone():
    add_input = input("Please enter your phone number: ")
    for n, ph in dict.items():
        if add_input == ph:
            return n


@input_error
def showall_func():
    return dict

@input_error    
def func_good_bye():
    return "good bye!"    
    

COMMANDS = {
    func_hello: "hello",
    add_contact: "add",
    change_contact: "change",
    show_phone: "phone",
    showall_func: "show all",
    func_good_bye: "good bye. close. exist. bye"  
    
}
 
dict = {}

def main():
    while True:
        user_input = input(">>>")
        for k,v in COMMANDS.items():
            if v == user_input.lower():
                print(k())
        if user_input == '.':
            break
            

if __name__ == "__main__":
    main()