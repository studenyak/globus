import flickr_api
import logging
logger = logging.getLogger(__name__)

RADIUS_LIMIT_KM = 32

def rome():
    geo = {'lat': 41.766923,
           'lon': 12.349517}

    y_dist = 35
    x_dist = 35

    pass


def count_per_km():
    geo = {'lat': 41.902685,
           'lon': 12.506292}

    for i in range(1, RADIUS_LIMIT_KM, 1):
        result = flickr_api.get_photo_by_geo(geo, i)
        logger.info('%d km: %s photos', i, result['total'])