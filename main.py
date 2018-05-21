__author__ = 'mac'

import logging
from flickrapi import FlickrAPI
import json

FLICKR_PUBLIC = '0a0aa19115f64849d8481a442cb46346'
FLICKR_SECRET = '01acb8879d01d906'
RADIUS_LIMIT_KM = 32
flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('globus')


def print_json(obj):
    logger.info("%s", json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))


def get_photo_by_geo(geo, radius=5):
    if not geo.get('lat') or not geo.get('lon'):
        return {'error': 'wrong params'}

    response = flickr.photos.search(lat=geo['lat'],
                                    lon=geo['lon'],
                                    radius=radius,
                                    radius_units='km')
    return response['photos']


def test_rome():
    geo = {'lat': 41.766923,
           'lon': 12.349517}

    y_dist = 35
    x_dist = 35

    pass


def test_count_per_km():
    geo = {'lat': 41.902685,
           'lon': 12.506292}

    for i in range(1, RADIUS_LIMIT_KM, 1):
        result = get_photo_by_geo(geo, i)
        logger.info('%d km: %s photos', i, result['total'])

if __name__ == "__main__":
    geo = {'lat': 41.902685,
           'lon': 12.506292}

    result = get_photo_by_geo(geo, 0.025)
    logger.info(result['total'])

