# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

# print(name_from_email("elek.viz@exam.com"))

def name_from_email(email_address):
    first_name = ""
    full_name =""
    i = 0
    while email_address[i] != ".":
        if i == 0:
            first_name += email_address[i].upper()
        else:
            first_name += email_address[i]
        i += 1
    i += 1
    while email_address[i] != "@":
        if email_address[i-1] == ".":
            full_name += email_address[i].upper()
        else:
            full_name += email_address[i]
        i += 1
    # first_name[0] = first_name[0].upper()
    full_name += " " + first_name
    return full_name
def main():
    my_email = "attila.kezer@gmail.com"
    print(name_from_email(my_email))
main()
