# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

# print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]

def odd_filter(number_list):
    odd_list = []
    for number in number_list:
        if number % 2 != 0:
            odd_list.append(number)
    return odd_list
def main():
    my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 123]
    print(odd_filter(my_numbers))
main()