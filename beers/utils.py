from statistics import mean

def calculate_rating_data(reviews):
    if reviews:
        avg = mean(r.rating for r in reviews)
        stddev = 5
    else:
        avg = None
        stddev = None

    return {
        'avg': avg,
        'stddev': stddev
    }
