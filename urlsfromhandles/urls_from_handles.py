# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2", "hellobello"]

def urls_from_handles(handle_names):
    greenfox_url = "https://github.com/greenfox-academy/"
    urls_list = []
    for handle in handle_names:
        full_url = greenfox_url + handle
        urls_list.append(full_url)
    return urls_list

def main():
    print(urls_from_handles(names))
main()