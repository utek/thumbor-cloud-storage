from collections import defaultdict

from google.cloud import storage
from tornado.concurrent import return_future

buckets = defaultdict(dict)


async def load(context, path):
    result = LoaderResult()
    project_id = context.config.get("CLOUD_STORAGE_PROJECT_ID")
    bucket_id = context.config.get("CLOUD_STORAGE_BUCKET_ID")

    logger.debug("[CLOUD_STORAGE_LOADER] Bucket Path %s" % bucket_path)
    logger.debug("[CLOUD_STORAGE_LOADER] Bucket ID %s" % bucket_id)

    bucket = buckets[project_id].get(bucket_id, None)
    if bucket is None:
        client = storage.Client(project_id)
        bucket = client.get_bucket(bucket_id)
        buckets[project_id][bucket_id] = bucket

    logger.debug("[CLOUD_STORAGE_LOADER] Looking for %s" % path)
    blob = bucket.get_blob(path)

    if blob:
        result.successful = True
        result.buffer = blob.download_as_string()
    else:
        result.error = LoaderResult.ERROR_NOT_FOUND
        result.successful = False
    return result
