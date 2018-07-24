import pymongo
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mongo = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo["globus"]
collection = db["flickr"]


def exist(id):
    if not isinstance(id, int):
        id = int(id)
    doc = collection.find({"_id": id})
    return doc.count() > 0


def get_by_location(lat, lon):
    doc = collection.find({"latitude": lat, "longitute": lon})
    return doc


def set_by_location(lat, lon, obj):
        pass


# Note: this function does not check if the doc already exists
def set_by_photo_id(id, obj):
    if not isinstance(id, int):
        id = int(id)

    doc = {"_id": id}
    doc.update(obj)
    collection.insert_one(doc)


def update(id, info):
    if not isinstance(id, int):
        id = int(id)
    try:
        set_by_photo_id(id, info)
    except pymongo.errors.DuplicateKeyError as er:
        logger.error("%s, id: %s", er, id)

