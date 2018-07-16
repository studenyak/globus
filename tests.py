import flickr_api
import logging
import utils
import time
logger = logging.getLogger(__name__)

RADIUS_LIMIT_KM = 32
KM_IN_DEGREE = 111
DEGREE_IN_KM = 0.009
DEGREE_IN_METER = 0.009009


def get_orvietto_area():
    start = {'lat': 42.713566,
             'lon': 12.099742}

    end = {'lat': 42.724611,
           'lon': 12.122237}

    return {'start': start, 'end': end}


def get_vatican_area():
    start = {'lat': 41.898513,
             'lon': 12.442947}

    end = {'lat': 41.908240,
           'lon': 12.459730}

    return {'start': start, 'end': end}


def get_rome_area():
    start = {'lat': 41.766760,
             'lon': 12.328421}

    end = {'lat': 42.036925,
           'lon': 12.749842}

    return {'start': start, 'end': end}


def get_photos(rome_area):
    cur_lat = rome_area['start']['lat']
    index = 0
    step_km = 0.005
    db = []
    db_json = {}
    db_json['step_km'] = step_km
    db_json['data'] = {}
    while cur_lat < rome_area['end']['lat']:
        cur_lon = rome_area['start']['lon']
        while cur_lon < rome_area['end']['lon']:
            index += 1
            #response = flickr_api.get_photo_by_geo({'lat': cur_lat, 'lon': cur_lon}, step_km)
            weight = 0#response['total']
            logger.info('%s:\tlat: %s\tlon: %s\ttotal photos: %s', index, cur_lat, cur_lon, weight)
            db_json[str(cur_lat)+":"+str(cur_lon)] = weight
            db.insert(index, {'lat': cur_lat, 'lon':cur_lon, 'weight': weight})
            #utils.write_json_to_file({'lat': float("{0:.6f}".format(cur_lat)), 'lon': float("{0:.6f}".format(cur_lon)), 'weight': int(weight)})
            cur_lon += DEGREE_IN_KM * step_km
        cur_lat += DEGREE_IN_KM * step_km

    logger.info(db)


def count_per_km():
    geo = {'lat': 41.902685,
           'lon': 12.506292}

    for i in range(1, RADIUS_LIMIT_KM, 1):
        result = flickr_api.get_photo_by_geo(geo, i)
        logger.info('%d km: %s photos', i, result['total'])