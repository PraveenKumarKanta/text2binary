def encoder(message = ''):
        message = input("Enter your message: ")
        sandesam = ''
        for letter in message:
                sandesam = sandesam + (bin(ord(letter))[2:]) + ' '
        
        return print(sandesam[:-1])

def decoder(binary_code = ''):
        binary_code = input("Enter the binary code: ")
        separated_values = binary_code.split()
        final_message = ''
        for value in separated_values:
                final_message = final_message + chr(int(value,2))
        
        return print(final_message)

limiter = 0
while(limiter < 1):
        option = input("Enter E to encode or D to decode and 'Q' to quit the program: ")
        if option == 'E':
                encoder()
                
        elif option == 'D':
                decoder()
                
        elif option == 'Q':
                limiter = 1
        else:
                print("Option input is case sensitive!")
