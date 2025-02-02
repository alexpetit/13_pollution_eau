import logging
import os

from utils.storage_client import ObjectStorageClient

import pipelines.config.config

logger = logging.getLogger(__name__)


def download():
    try:
        # Utilisation de ObjectStorageClient pour interagir avec Scaleway Object Storage
        storage_client = ObjectStorageClient()
        env = os.getenv("ENV")
        s3_key = f"{env}/database.duckdb"
        local_path = "database/database_downloaded.duckdb"

        storage_client.download_object(s3_key, local_path)
        logger.info(
            f"✅ Base téléchargée depuis s3://{storage_client.bucket_name}/{s3_key} -> {local_path}"
        )
    except Exception as e:
        logger.error(f"Erreur lors du téléchargement: {e}")


def execute():
    download()
