from tornado.concurrent import return_future
from gcloud import storage

def load(context, path, callback):
    bucket_id  = context.config.get("CLOUD_STORAGE_BUCKET_ID")
    project_id = context.config.get("CLOUD_STORAGE_PROJECT_ID")
    client = storage.Client(project_id)
    bucket = client.get_bucket(bucket_id, project_id)
    blob = bucket.get_blob(path)

    if blob is None:
      return callback(None)

    callback(blob.download_as_string())
