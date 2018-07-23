# This script grabs data from the flickr server for specific area and builds following data structures:
# db=0: key: "lon,lat"; value: {total, photo_ids[]}
# db=1: key: photo_id; value: {lon, lat}
# Depending on the zoomLevel the data is stored to the specific Redis db
# db=100 - World wide
# db=101
# ...
# db=120 - Street wide

import flickr_api
import logging
import geo_db
import sys
import json


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('flickr_grabber.log')
logger.addHandler(handler)


def get_worldwide_data():
    for lon in range(143, 180):
        for lat in range(-90, 90):
            res = flickr_api.get_photos_by_bbox([lon, lat, lon + 1, lat + 1])
            weight = int(res['photos']['total'])
            logger.info(str(lat) + ',' + str(lon))
            if weight > 0:
                geo_db.set_by_location(lat, lon, {"weight": weight}, 0)


if __name__ == "__main__":
    FLICKR_PUBLIC, FLICKR_SECRET, str_bbox = sys.argv[1:4]
    index = int(sys.argv[4])
    pages_per_grabber = int(sys.argv[5])
    logger.info("grabber %s: %s", index, sys.argv)

    flickr_api.init(FLICKR_PUBLIC, FLICKR_SECRET)

    start_page = index * pages_per_grabber + 1
    end_page = index * pages_per_grabber + pages_per_grabber
    for page in range(start_page, end_page):
        logger.info("grabber %s: %s -> %s", index, start_page, end_page)
        response = flickr_api.get_photos_by_bbox(str_bbox, page)
        perpage = int(response['photos']['perpage'])
        photo = response['photos']['photo']
        for index in range(0, perpage):
            info = flickr_api.get_photo_info(photo[index]['id'])
            lat = float(info['photo']['location']['latitude'])
            lon = float(info['photo']['location']['longitude'])
            value = geo_db.get_by_location(lat, lon)
            if not value:
                value = dict()
                value['weight'] = 1
                # value['photo'] = [info]
            else:
                value = json.loads(value)
                value['weight'] += 1
                # value['photo'].insert(int(value['weight']) - 1, info)
            geo_db.set_by_location(lat, lon, value)
            geo_db.set_by_photo_id(photo[index]['id'], info)
