def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:    # stop the loop when count equals counter
            return
        counter += 1
        yield item              # while running,  output the item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue            # skip the item when item exists in the set, seen
        yield item              # while running, output the item
        seen.add(item)          # add item in the set when it is not exist yet


def run_pipeline():
    items = [3, 8, 8, 2, 2, 3, 5, 1, 7, 9, 1]
    for item in take(3, distinct(items)):       # loop over the sequence of distinct items
        print(item)                             # prints item in 3 cycle
                                                # this is how we control the cycle of loops


run_pipeline()
