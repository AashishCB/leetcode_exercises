def can_construct_v1(ransom_note: str, magazine: str):
    ransom_note = list(ransom_note)
    for letter in magazine:
        ransom_note.remove(letter)
    if not ransom_note:
        return True
    return False


def can_construct(ransomNote: str, magazine: str):
    letters_count = {}.fromkeys(magazine, 0)
    for letter in magazine:
        letters_count[letter] += 1
    for note in ransomNote:
        if not letters_count.get(note):
            return False
        letters_count[note] -= 1
    return True


can_construct('a', 'b')
can_construct('aa', 'ab')
can_construct('aa', 'aab')
