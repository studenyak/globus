import logging
import flickr_api
import tests
import utils
import json
import data_generator


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    data_generator.get_worldwide_data()
    # area = tests.get_orvietto_area()
    # response = flickr_api.get_photos_by_bbox([area['start']['lon'], area['start']['lat'],
    #                                           area['end']['lon'], area['end']['lat']])
    #
    # total = response['photos']['total']
    # perpage = response['photos']['perpage']
    # photo = response['photos']['photo']
    #
    # for index in range(0, perpage):
    #     info = flickr_api.get_photo_info(photo[index]['id'])
    #     key = str(info['photo']['location']['latitude']+','+info['photo']['location']['longitude'])
    #     value = rDb.get(key)
    #     if not value:
    #         value = dict()
    #         value['weight'] = 1
    #         # value['photo'] = [info]
    #     else:
    #         value = json.loads(value)
    #         value['weight'] += 1
    #         # value['photo'].insert(int(value['weight']) - 1, info)
    #     rDb.set(key, json.dumps(value))


