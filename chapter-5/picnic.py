# find how much of each item was brough to the picnic

import pprint

guests = {
        "jorge": {"apples": 1, "oranges": 3, "peaches": 4},
        "alice": {"apples": 4, "oranges": 1, "peaches": 5, "bread": 7},
        "carlos": {"soft-drinks": 4, "ham": 5, "cheese": 7},
        "maria": {"desert": 4, "water": 4, "bread": 5, "apple-juice": 7},
}

def total_amount(guests):

    amount_per_item = {}

    for k in guests.keys():
        for item, amount in guests[k].items():
            if item not in amount_per_item:
                amount_per_item.setdefault(item, amount)
            else:
                amount_per_item[item] += amount

    pprint.pprint(amount_per_item)


total_amount(guests)
