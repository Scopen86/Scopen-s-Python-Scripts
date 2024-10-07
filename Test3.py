from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

final_ans = 'Phép Lai ở Thế hệ p là AAXBY x AaXBXb'
Test = 'Phép lai ở thế hệ P là AaXbY × AaXBXb.'
print(similar(final_ans, Test))

