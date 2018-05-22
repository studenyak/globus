
import json
import logging
logger = logging.getLogger(__name__)


def print_json(obj):
    logger.info("%s", json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': ')))

