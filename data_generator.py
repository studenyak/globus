# This script gets data from the FlickrAPI server and builds data structures that we need
# {lon, lat, total}
# Depending on the zoomLevel the data is stored to the specific Redis db
# db=0 - World wide
# db=1
# ...
# db=20 - Street wide

import flickr_api
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_worldwide_data():
    for lon in range (-180, -175):
        for lat in range(-90, -85):
            res = flickr_api.get_photos_by_bbox([lon, lat, lon + 1, lat + 1])
            obj = dict()
            obj['lon'] = lon
            obj['lat'] = lat
            obj['weight'] = res['photos']['total']
            logging.info(obj)
