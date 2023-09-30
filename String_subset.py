def word_subset(word1,word2):
    final_set = set(word1)
    letters = {}

    for i in word1:
        for j in i:
            count= i.count(j)
    if j not in letters and count > letters[j]:
        letters[j] = count


    for i in word2:
        for j in letters:
            if i.count(j) < letters[j]:
                final_set.remove(i)
                break
    return list(final_set)