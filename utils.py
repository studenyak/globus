
import json
import logging
logger = logging.getLogger(__name__)


def print_json(obj):
    logger.info("%s", json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))


def write_json_to_file(jsonData):
    with open('db.json', 'a') as outfile:
        # json.dump(jsonData, outfile, sort_keys=True, indent=4)
        outfile.write(json.dumps(jsonData))
        outfile.write(",\n")
        outfile.close()

