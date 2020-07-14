#  Without using loops: 
# * symbol is use to print the list elements in a single line with space. 
# To print all elements in new lines or separated by space use sep=”\n” or sep=”, ” respectively.

# a = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]

# print(*a, sep = "\n")


# Print out each element of the following array on a separate line, 
# but this time the input array can contain arrays nested to an arbitrarily deep level:

a = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# For the above input, the expected output is:
# Bob
# Slack
# reddit
# 89
# 101
# alacritty
# (brackets)
# 5
# 375
# 0
# {slice, owned}
# 22

print(*a, sep = "\n")
