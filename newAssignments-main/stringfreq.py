def max_frequency_char(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    max_char = max(freq, key=freq.get)
    return max_char, freq[max_char]
input_string = "strawberry"
max_char, max_freq = max_frequency_char(input_string)
print(
    f"The character '{max_char}' has the maximum frequency of {max_freq} times in the string '{input_string}'.")
