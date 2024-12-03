def get_probability(dataset : dict, feature : str, value=None, given=None) -> float:
    total = 1
    len_all = 0
    for target, data in dataset.items():
        len_all += len(data)
        if given and target != given:
            continue
        for case in data:
            try:
                if str(case[feature]) == str(value):
                    total += 1
            except:
                continue
    return total / len_all

def get_prior_probability(dataset: list, target) -> float:
    len_all = 0
    for _ ,data in dataset.items():
        len_all += len(data)
    return len(dataset[target]) / len_all

def do_naive_bayes(dataset: list, features : dict) -> dict:
    probabilities = {}
    for target in dataset:
        probabilities[target] = get_prior_probability(dataset, target)
        for feature, value in features.items():
            probabilities[target] *= get_probability(dataset, feature, value, target)
    tot = 0
    for i, j in probabilities.items():
        tot += j
    for i in probabilities.keys():
        probabilities[i] /= tot

    return probabilities