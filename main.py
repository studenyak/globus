import logging
import flickr_api
import tests
import utils
import redis
import json

redis_config = {'host': 'localhost',
                'port': 6379,
                'db': 0}

rDb = redis.StrictRedis(host=redis_config['host'],
                        port=redis_config['port'],
                        db=redis_config['db'])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def dump_redis_to_json(db=0):
    res = list()
    index = 0
    for key in rDb.keys():
        lat,lon = key.split(',')
        val = rDb.get(key)
        obj = dict()
        obj['lat'] = float(lat)
        obj['lon'] = float(lon)
        obj['weight'] = json.loads(val)['weight']
        res.insert(index, obj)
        index += 1

    with open('db.json', 'w') as outfile:
        outfile.write(json.dumps(res))


if __name__ == "__main__":
    # dump_redis_to_json()

    area = tests.get_orvietto_area()
    response = flickr_api.get_photos_by_bbox([area['start']['lon'], area['start']['lat'],
                                              area['end']['lon'], area['end']['lat']])

    total = response['photos']['total']
    perpage = response['photos']['perpage']
    photo = response['photos']['photo']

    for index in range(0, perpage):
        info = flickr_api.get_photo_info(photo[index]['id'])
        key = str(info['photo']['location']['latitude']+','+info['photo']['location']['longitude'])
        value = rDb.get(key)
        if not value:
            value = dict()
            value['weight'] = 1
            # value['photo'] = [info]
        else:
            value = json.loads(value)
            value['weight'] += 1
            # value['photo'].insert(int(value['weight']) - 1, info)
        rDb.set(key, json.dumps(value))


