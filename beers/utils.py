from statistics import mean, stdev


def calculate_rating_data(reviews):
    avg = None
    sd = None

    if reviews:
        avg = mean(r.rating for r in reviews)

        if len(reviews) > 1:
            sd = stdev(r.rating for r in reviews)

    return {
        'avg': avg,
        'stdev': sd,
        'count': len(reviews),
    }
