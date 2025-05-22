def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        low_c = c.lower()
        if low_c in chars:
            chars[low_c] += 1
        else:
            chars[low_c] = 1
    return chars

def sort_chars_dict(chars_dict):
    sorted_list = []
    for char, count in chars_dict.items():
        sorted_list.append({"char": char, "num": count})

    # Sort the list in descending order based on the 'num' key
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list

