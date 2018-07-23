
from flickrapi import FlickrAPI
import logging

logger = logging.getLogger(__name__)


def init(flickr_public, flickr_secret):
    global flickr
    flickr = FlickrAPI(flickr_public, flickr_secret, format='parsed-json')


def get_photo_by_geo(geo, radius=5):
    if not geo.get('lat') or not geo.get('lon'):
        return {'error': 'wrong params'}

    response = flickr.photos.search(lat=geo['lat'],
                                    lon=geo['lon'],
                                    radius=radius,
                                    radius_units='km')
    return response['photos']


# bbox - see description https://www.flickr.com/services/api/flickr.photos.search.html
def get_photos_by_bbox(bbox, page=1):
    # if not isinstance(bbox, list):
    #     return {'error': 'bbox should be a list'}

    response = flickr.photos.search(bbox=bbox, page='34')
    return response


def get_photo_info(photo_id, secret=''):
    response = flickr.photos.getInfo(photo_id=photo_id,
                                     secret=secret)
    return response
