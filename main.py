import logging
import flickr_api


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



if __name__ == "__main__":
    geo = {'lat': 41.902685,
           'lon': 12.506292}

    result = flickr_api.get_photo_by_geo(geo, 0.025)
    logger.info(result['total'])

