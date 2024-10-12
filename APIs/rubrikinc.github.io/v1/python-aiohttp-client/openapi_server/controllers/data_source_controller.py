from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_delete_object_snapshots_config import BulkDeleteObjectSnapshotsConfig
from openapi_server.models.bulk_delete_snapshots_config import BulkDeleteSnapshotsConfig
from openapi_server.models.expired_custom_retention_snapshots import ExpiredCustomRetentionSnapshots
from openapi_server.models.request_failed_exception import RequestFailedException
from openapi_server import util


async def bulk_delete_snapshots(request: web.Request, body) -> web.Response:
    """Bulk delete all snapshots for the given objects

    This endpoint deletes all snapshots from all locations for the objects with the IDs specified by the &#39;objectIds&#39; parameter. API returning success does not guarantee that the snapshots will be expired. 

    :param body: A list of object IDs. 
    :type body: dict | bytes

    """
    body = BulkDeleteSnapshotsConfig.from_dict(body)
    return web.Response(status=200)


async def bulk_delete_snapshots_for_object(request: web.Request, id, body) -> web.Response:
    """Bulk delete specified snapshots for the given object

    Bulk deletion of the snapshots specified by a list of snapshot IDs for a given object. Object type is required. Location ID is optional. API returning success does not guarantee that the snapshot will be expired. 

    :param id: ID of the object.
    :type id: str
    :param body: A list of snapshot IDs specifying snapshots to delete. Optionally specifies a location ID. Snapshot deletion is global when the location ID is absent. 
    :type body: dict | bytes

    """
    body = BulkDeleteObjectSnapshotsConfig.from_dict(body)
    return web.Response(status=200)


async def expired_custom_retention_snapshots(request: web.Request, id) -> web.Response:
    """Returns a list of snapshots that have expired according to their snapshot-level SLA Domain assignments 

    Gets a list of the snapshots of a specified data source that have expired according to the snapshot-level SLA Domain assignments. This list does not include remote snapshots. 

    :param id: The object ID.
    :type id: str

    """
    return web.Response(status=200)
