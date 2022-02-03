
def rec_brute(weight_left, items, items_amount, iteration_count):
    #iteration_count - counts all the iterations that happened
    if items_amount == 0 or weight_left == 0:
        return [iteration_count, 0,[]]

    iteration_count[0] += 1

    if items[items_amount-1][1] > weight_left :
        return rec_brute(weight_left, items, items_amount-1, iteration_count)

    else:
        left = rec_brute(weight_left, items, items_amount - 1, iteration_count)
        right =  rec_brute(weight_left - items[items_amount-1][1], items, items_amount -1, iteration_count)
        right[1] += items[items_amount-1][0]
        if left >= right:
            return left
        else:
            right[2].append(items[items_amount-1])
            return right

#The method to call the brute algorithm
def brute(weight_max, items):
    return rec_brute(weight_max, items, len(items), iteration_count = [0])
