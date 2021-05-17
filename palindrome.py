def is_palindrome(a):
    a = str(a)
    b = a[::-1]
    if a == b:
        return True
    else:
        return False

#test
print(is_palindrome(23431))
