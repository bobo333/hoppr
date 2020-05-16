from statistics import mean, stdev


CATEGORY_WEIGHTS = {
    'Brewery': .4,
    'Hops': .4,
    'Style': .2,
    'ABV': .3,
}


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


def add_overall_prediction(category_data):
    denominator = 0
    total_score = 0

    for cat_name, cat_ratings in category_data['categories'].items():
        if len(cat_ratings):

            if any(c['rating']['avg'] != None for c in cat_ratings):
                cat_avg = mean(cat_val['rating']['avg'] for cat_val in cat_ratings if cat_val['rating']['avg'])
                cat_weight = CATEGORY_WEIGHTS[cat_name]
                denominator += cat_weight
                total_score += cat_avg * cat_weight

    prediction = None
    if denominator != 0:
        prediction = total_score / denominator

    category_data['overall'] = prediction
