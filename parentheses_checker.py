def checker(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(' and char != ")":
                return False
            if current_char == '{' and char != "}":
                return False
            if current_char == '[' and char != "]":
                return False

    # If stack isn't empty yet then return false
    if stack:
        return False
    return True

string_seq=input('Enter a seq of parentheses::::')
res=checker(string_seq)
if res==True:
    print('Balanced')
else:
    print('Unbalanced')