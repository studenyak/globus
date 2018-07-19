# This script gets data from the FlickrAPI server and builds data structures that we need
# {lon, lat, total}
# Depending on the zoomLevel the data is stored to the specific Redis db
# db=0 - World wide
# db=1
# ...
# db=20 - Street wide

import flickr_api
import logging
import geo_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_worldwide_data():
    for lon in range(81, 179):
        for lat in range(-90, 89):
            res = flickr_api.get_photos_by_bbox([lon, lat, lon + 1, lat + 1])
            weight = int(res['photos']['total'])
            logger.info(str(lat) + ',' + str(lon))
            if weight > 0:
                geo_db.write(lat, lon, {"weight": weight}, 0)
