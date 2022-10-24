steps = {}

def join(moves):
    return "".join(moves)
    
# the strategy is similar to abbey, but we look backs harder than her.
# she only look back 2 steps, find most frequently pattern of all 2 moves,
#
# Other strategies:
#
# - quincy repeat 5 moves
# - kris always counter our last moves, hence, once we establed a patterns, he
# is not a problem
# - mrugresh look for our top pick in last 10 moves, hence, similar to kris,
# once we establed a pattern, we're in control.
def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Interestingly, 3 to 6 works best, as in we win more than 60%.
    # If n is larger than 6, we start to get terrible result.
    # I guess it's becauase we don't have enough data to predict once n get that
    # larger, we only play 1000 games.
    n = 5

    hist = opponent_history

    guess = "R"
    if len(hist) > n:
        pattern = join(hist[-n:])

        if join(hist[-(n + 1):]) in steps.keys():
            steps[join(hist[-(n + 1):])] += 1
        else:
            steps[join(hist[-(n + 1):])] = 1

        possible = [pattern + "R", pattern + "P", pattern + "S"]

        for i in possible:
            if not i in steps.keys():
                steps[i] = 0

        predict = max(possible, key=lambda key: steps[key])

        if predict[-1] == "P":
            guess = "S"
        if predict[-1] == "R":
            guess = "P"
        if predict[-1] == "S":
            guess = "R"

    return guess