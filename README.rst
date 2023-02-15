Thumbor Cloud Storage 2
=======================

This is a for of Thumbor Cloud Storage to make it work with new version of Thumbor.
As the original Thumbor Coud Storage seems like it's no longer maintained.

Installation
------------

.. code:: bash

        pip install thumbor-cloud-storage2

Authentication
~~~~~~~~~~~~~~

Authentication is handled by the Google Cloud SDK, see `gcloud
documentation <http://gcloud-python.readthedocs.io/en/latest/gcloud-auth.html>`__.

Contribution
------------

TODO

Features
--------

-  *thumbor\_cloud\_storage.loaders.cloud\_storage\_loader* - takes a
   bucket object path and downloads the file through the gcloud
   S3-compatible API.
-  *thumbor\_cloud\_storage.result\_storages.cloud\_storage*

Configuration
-------------

Loader settings
~~~~~~~~~~~~~~~

When using ``thumbor_cloud_storage2.loaders.cloud_storage_loader``:

.. code:: python

    LOADER = 'thumbor_cloud_storage.loaders.cloud_storage_loader'
    CLOUD_STORAGE_BUCKET_ID = ''
    CLOUD_STORAGE_PROJECT_ID = ''

Result storage settings
~~~~~~~~~~~~~~~~~~~~~~~

When ``thumbor_cloud_storage2.result_storages.cloud_storage`` is enabled:

.. code:: python

    RESULT_STORAGE = 'thumbor_cloud_storage.result_storages.cloud_storage'
    RESULT_STORAGE_CLOUD_STORAGE_PROJECT_ID = ''
    RESULT_STORAGE_CLOUD_STORAGE_BUCKET_ID = ''

