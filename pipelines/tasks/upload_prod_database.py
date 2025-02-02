import logging
import os

from utils.storage_client import (
    ObjectStorageClient,  # Assurez-vous que le chemin est correct
)

import pipelines.config.config

logger = logging.getLogger(__name__)


def upload():
    try:
        # Utilisation de ObjectStorageClient pour interagir avec Scaleway Object Storage
        storage_client = ObjectStorageClient()
        db_path = "database/data.duckdb"  # Fichier local
        s3_key = f"{os.getenv('ENV')}/database.duckdb"  # Destination sur S3

        storage_client.upload_object(db_path, s3_key)
        logger.info(f"✅ Base uploadée sur s3://{storage_client.bucket_name}/{s3_key}")

    except Exception as e:
        logger.error(f"Erreur lors de l'upload: {e}")


def execute():
    upload()
