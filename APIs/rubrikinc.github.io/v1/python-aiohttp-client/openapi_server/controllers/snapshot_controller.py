from typing import List, Dict
from aiohttp import web

from openapi_server.models.snapshot_storage_stats import SnapshotStorageStats
from openapi_server import util


async def get_snapshot_storage_stats_v1(request: web.Request, id) -> web.Response:
    """Returns storage stats for a snapshot

    Returns the storage statistics for a snapshot.

    :param id: ID assigned to a snapshot object.
    :type id: str

    """
    return web.Response(status=200)
