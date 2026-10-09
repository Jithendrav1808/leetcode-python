words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = "".join(sorted(word))

    if key in groups:
        groups[key].append(word)

    else:
        groups[key] = [word]


print(list(groups.values()))