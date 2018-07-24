
import redis
import json

redis_config = {'host': 'localhost',
                'port': 6379
                }

rDb = redis.StrictRedis(host=redis_config['host'],
                        port=redis_config['port'],
                        db=0)


rDb_1 = redis.StrictRedis(host=redis_config['host'],
                          port=redis_config['port'],
                          db=1)

rDb_pool = [rDb, rDb_1]


def from_json(db=0):
    json_data=open('db.json').read()
    data = json.loads(json_data)
    for obj in data:
        set_by_location(obj['lat'], obj['lon'], {'weight': obj['weight']}, db)


def from_photosposts(db=1):
    for index in range(1,13):
        json_data = open('photospots.mwong.ch/' + str(index) + '.json').read()
        data = json.loads(json_data)
        for obj in data:
            set_by_location(obj['lat'], obj['lng'], {'weight': int(obj['c'])}, db)


def to_json(db=0):
    res = list()
    index = 0
    for key in rDb_pool[db].keys():
        lat, lon = key.split(',')
        val = rDb_pool[db].get(key)
        obj = dict()
        obj['lat'] = float(lat)
        obj['lon'] = float(lon)
        obj['weight'] = json.loads(val)['weight']
        res.insert(index, obj)
        index += 1

    with open('db.json', 'w') as outfile:
        outfile.write(json.dumps(res))


def exist(key, db=0):
    value = rDb_pool[db].get(key)
    return value


def get_by_location(lat, lon, db=0):
        key = str(lat) + ',' + str(lon)
        return rDb_pool[db].get(key)


def set_by_location(lat, lon, obj, db=0):
        key = str(lat) + ',' + str(lon)
        if not exist(key, db):
            rDb_pool[db].set(key, json.dumps(obj))


def set_by_photo_id(id, obj, db=1):
        key = id
        if not exist(key, db):
            rDb_pool[db].set(key, json.dumps(obj))

