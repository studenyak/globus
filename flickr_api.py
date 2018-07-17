
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


# bbox - see description https://www.flickr.com/services/api/flickr.photos.search.html
def get_photos_by_bbox(bbox):
    if not isinstance(bbox, list):
        return {'error': 'bbox should be a list'}

    str_bbox = ','.join(map(str, bbox))
    response = flickr.photos.search(bbox=str_bbox)
    return response


def get_photo_info(photo_id, secret=''):
    response = flickr.photos.getInfo(photo_id=photo_id,
                                     secret=secret)
    return response
