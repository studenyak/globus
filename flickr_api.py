
from flickrapi import FlickrAPI
import logging

FLICKR_PUBLIC = '0a0aa19115f64849d8481a442cb46346'
FLICKR_SECRET = '01acb8879d01d906'
flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')

logger = logging.getLogger(__name__)


def get_photo_by_geo(geo, radius=5):
    if not geo.get('lat') or not geo.get('lon'):
        return {'error': 'wrong params'}

    response = flickr.photos.search(lat=geo['lat'],
                                    lon=geo['lon'],
                                    radius=radius,
                                    radius_units='km')
    return response['photos']