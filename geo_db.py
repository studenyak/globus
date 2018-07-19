
import redis
import json

redis_config = {'host': 'localhost',
                'port': 6379,
                'db': 0}

rDb = redis.StrictRedis(host=redis_config['host'],
                        port=redis_config['port'],
                        db=redis_config['db'])


def to_json(db=0):
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


def exist(key, db=0):
    value = rDb.get(key)
    return value


def write(lat, lon, obj, db=0):
        key = str(lat) + ',' + str(lon)
        if not exist(key, db):
            rDb.set(key, json.dumps(obj))
