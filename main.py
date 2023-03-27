def romanToInt(s: str) -> int:
    # dictionary to hold the values of Roman numerals
    # e.g. 'I' is the key, 1 is the value.
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000}

    # this is a variable to hold the result
    result = 0

    # this loop is iterating through the string from left to right
    for i in range(len(s)):
        # if the current Roman numeral is less than the next one, subtract its value
        if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i+1]]:
            result -= roman_dict[s[i]]
        # if the current Roman numeral is MORE than the next one, add its value
        else:
            result += roman_dict[s[i]]
    return result


# calling the result
result = romanToInt('Z')
print(result)


