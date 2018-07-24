import logging
import flickr_api
import tests
import json
import subprocess


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_flickr_grabbers(keys, str_bbox, pages_per_grabber):
    process_pool = list()
    for index in range(0, len(keys)):
        process = subprocess.Popen(['python',
                         'flickr_grabber.py',
                         keys[index]["FLICKR_PUBLIC"],
                         keys[index]["FLICKR_SECRET"],
                         str_bbox,
                         str(index),
                         str(pages_per_grabber)])
        process_pool.insert(index, process)
    return process_pool


if __name__ == "__main__":
    json_data = open("flickr_keys.json").read()
    keys = json.loads(json_data)
    flickr_api.init(keys[0]["FLICKR_PUBLIC"],
                    keys[0]["FLICKR_SECRET"])

    area = tests.get_rome_area()
    str_bbox = ','.join(map(str, [area['start']['lon'], area['start']['lat'],
                                  area['end']['lon'], area['end']['lat']]))
    response = flickr_api.get_photos_by_bbox(str_bbox)

    total = int(response['photos']['total'])
    perpage = int(response['photos']['perpage'])
    pages = int(response['photos']['pages'])
    photo = response['photos']['photo']
    pages_per_grabber = total / len(keys)
    process_pool = run_flickr_grabbers(keys, str_bbox, pages_per_grabber)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        for process in process_pool:
            process.kill()

