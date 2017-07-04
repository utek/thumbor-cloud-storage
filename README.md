# Thumbor Cloud Storage

## Installation

```bash
    pip install thumbor-cloud-storage
```

### Authentication

Authentication is handled by the Google Cloud SDK, see [gcloud documentation](http://gcloud-python.readthedocs.io/en/latest/gcloud-auth.html).

## Contribution

TODO

## Features

 * *thumbor_cloud_storage.loaders.cloud_storage_loader* - takes a bucket object path and downloads the file through the gcloud S3-compatible API.
 * *thumbor_cloud_storage.result_storages.cloud_storage*

## Configuration

### Loader settings

When using ``thumbor_cloud_storage.loaders.cloud_storage_loader``:

```python
LOADER = 'thumbor_cloud_storage.loaders.cloud_storage_loader'
CLOUD_STORAGE_BUCKET_ID = ''
CLOUD_STORAGE_PROJECT_ID = ''
```

### Result storage settings

When ``thumbor_cloud_storage.result_storages.cloud_storage`` is enabled:

```python
RESULT_STORAGE = 'thumbor_cloud_storage.result_storages.cloud_storage'
RESULT_STORAGE_CLOUD_STORAGE_PROJECT_ID = ''
RESULT_STORAGE_CLOUD_STORAGE_BUCKET_ID = ''
```

