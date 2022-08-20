def is_palindrome(teststr) -> bool:
    return teststr == teststr[::-1]

while (run := True):
    teststr = input("Enter string to test for palindrome, or 'exit': ").lower()
    if teststr == 'exit':
        break

    newstr = ''.join(i for i in teststr if i.isalnum())
    print("Palindrome test:", is_palindrome(newstr))
