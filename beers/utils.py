from statistics import mean, stdev


def calculate_rating_data(reviews):
    if reviews:
        avg = mean(r.rating for r in reviews)
        sd = stdev(r.rating for r in reviews)
    else:
        avg = None
        sd = None

    return {
        'avg': avg,
        'stdev': sd
    }
