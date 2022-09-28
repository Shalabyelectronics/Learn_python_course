# Practice number 1
# Covert the fellowing code to list comprehension way

odd_number = []
for n in range(6):
    if n % 3 == 0 and n != 0:
        odd_number.append(n)

#_________________________________________
#Solution 
odd_number = [n for n in range(6) if n % 3 == 0 and n != 0]

# Practice number 2
# Covert the fellowing code to list comprehension way
vowels = ["u", "a", "e", "i", "o"]
sentence = "Hi Shalaby lets plaly."
highlight_vowels = []
for l in sentence:
    if l in vowels:
        highlight_vowels.append(f"({l})")
    else:
        highlight_vowels.append(l)
else:
    sentence = "".join(highlight_vowels)

#_________________________________________
#Solution 
sentence = "Hi Shalaby lets plaly."
sentence = "".join([f"({l})" if l in vowels else l for l in sentence])


# Practice number 3
# Covert the fellowing code to list comprehension way
colors = ["red", "orange", "green"]
sentence = ""
color_meaning = []
for c in colors:
    if c == "red":
        color_meaning.append((c,"Stop"))
    elif c == "orange":
        color_meaning.append((c,"Steady"))
    else:
        color_meaning.append((c,"Go"))
else:
    for c,m in color_meaning:
        if c == "red":
            sentence += f"First {m} for {c}, "
        elif c == "orange":
            sentence += f"Then be {m} for {c}, "
        else:
            sentence += f"Finally {m} for {c}."
#_________________________________________
#Solution 
sentence_c = "".join([f"First {m} for {c}, "if c == "red"
    else f"Then be {m} for {c}, " if c == "orange"
    else f"Finally, {m} fo {c}." for c,m in [(c, "Stop") if c == "red"
        else (c, "Steady") if c == "orange" else (c, "Go") for c in colors]])

# Practice number 4
# Covert the fellowing code to list comprehension way
students_marks = {11:75, 22:55, 33:40, 44:89, 55:90}
students_rating = {}
for s_id, marks in students_marks.items():
    if marks < 50:
        students_rating[s_id] = "Faild"
    elif marks <= 60:
        students_rating[s_id] = "Average"
    elif marks <= 80:
        students_rating[s_id] = "Good"
    else:
        students_rating[s_id] = "Excellent"
 #_________________________________________
#Solution 
st_rating = {s_id:("Faild" if marks < 50
    else "Average" if marks <= 60 
    else "Good" if marks <= 80
    else "Excellent") for s_id,marks in students_marks.items()} 
