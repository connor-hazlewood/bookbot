def get_num_words(text):    
    number = len(text.split())
    return number
def character_count(text):
    counts = {}
    for tex in text:
        char = tex.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort(counts):
    my_list = []
    for character, count in counts.items():
        my_dict = {"char": character, "num": count}
        my_list.append(my_dict)
    my_list.sort(reverse = True, key=sort_on)
    return my_list

def sort_on(my_dict):
    return my_dict["num"]
