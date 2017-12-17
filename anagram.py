def anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    print(sorted(s1))
    return sorted(s1) == sorted(s2)

print(anagram1('ace','cea'))

# or

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    print(sorted(s1))
    if sorted(s1) == sorted(s2):
        print("yo it is anagram")
anagram('ace','cea')

def anagram3(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1)==len(s2):
        print('its anagram')

anagram3('ace','aec')

    