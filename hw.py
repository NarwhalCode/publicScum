def reverse(reverseMe):
    return reverseMe[::-1]


def space(spaceMe):
    
    spaced = ''

    for x in range(len(spaceMe)):
        spaced = spaced + spaceMe[x] + ' '

    return spaced


def isPallindrome(isPal):
    if isPal == reverse(isPal):
        return True
    else:
        return False



text = "hello world"
text_reversed = reverse(text)

print( text_reversed )

#print(space(text))
#print(isPallindrome(text))

print(text[::-1])
