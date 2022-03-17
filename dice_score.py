def score(dice):
    nums = []
    score = 0
    [nums.append(x) for x in dice if x not in nums]
    for num in nums:
        if dice.count(num) >= 3:
            if num == 1:
                score += 1000
                score += (dice.count(num) - 3) * 100
            else:
                score += num * 100
                if num == 5 and dice.count(num) > 3:
                    score += (dice.count(num) - 3) * 50
        else:
            if num == 1:
                score += dice.count(num) * 100
            elif num == 5:
                score += dice.count(num) * 50
    return score


# test
dice = [5, 3, 3, 1, 3]
print(score(dice))
