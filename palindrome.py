def is_palindrome(str):
    letters = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    start = 0
    end = len(str) - 1

    while start < end:
        while str[start].upper() not in letters:
            start += 1
        while str[end].upper() not in letters:
            end -= 1
        if str[start].lower() != str[end].lower():
            return False
        else:
            start += 1
            end -= 1

        return True

print is_palindrome('A man, a plan, a canal, Panama')
