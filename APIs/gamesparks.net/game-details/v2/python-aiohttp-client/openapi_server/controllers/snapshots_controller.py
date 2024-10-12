from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.snapshot_creation_model import SnapshotCreationModel
from openapi_server.models.snapshot_creation_success_model import SnapshotCreationSuccessModel
from openapi_server.models.snapshot_model import SnapshotModel
from openapi_server import util


async def copy_snapshot_to_existing_game_using_post1(request: web.Request, api_key, snapshot_id, target_api_key, include_game_config=None, include_metadata=None, include_binaries=None, include_collaborators=None) -> web.Response:
    """copySnapshotToExistingGame

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str
    :param target_api_key: targetApiKey
    :type target_api_key: str
    :param include_game_config: includeGameConfig
    :type include_game_config: bool
    :param include_metadata: includeMetadata
    :type include_metadata: bool
    :param include_binaries: includeBinaries
    :type include_binaries: bool
    :param include_collaborators: includeCollaborators
    :type include_collaborators: bool

    """
    return web.Response(status=200)


async def copy_snapshot_to_new_game_using_post(request: web.Request, api_key, snapshot_id, include_game_config=None, include_metadata=None, include_binaries=None, include_collaborators=None) -> web.Response:
    """copySnapshotToNewGame

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str
    :param include_game_config: includeGameConfig
    :type include_game_config: bool
    :param include_metadata: includeMetadata
    :type include_metadata: bool
    :param include_binaries: includeBinaries
    :type include_binaries: bool
    :param include_collaborators: includeCollaborators
    :type include_collaborators: bool

    """
    return web.Response(status=200)


async def create_snapshots_using_post(request: web.Request, api_key, body) -> web.Response:
    """createSnapshots

    

    :param api_key: apiKey
    :type api_key: str
    :param body: description
    :type body: dict | bytes

    """
    body = SnapshotCreationModel.from_dict(body)
    return web.Response(status=200)


async def delete_snapshot_using_delete1(request: web.Request, api_key, snapshot_id) -> web.Response:
    """deleteSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def get_live_snapshot_id_using_get(request: web.Request, api_key) -> web.Response:
    """getLiveSnapshotId

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def get_snapshot_using_get(request: web.Request, api_key, snapshot_id) -> web.Response:
    """getSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def get_snapshots_using_get(request: web.Request, api_key, page, page_size=None) -> web.Response:
    """getSnapshots

    

    :param api_key: apiKey
    :type api_key: str
    :param page: page
    :type page: int
    :param page_size: pageSize
    :type page_size: int

    """
    return web.Response(status=200)


async def get_snapshots_using_get1(request: web.Request, api_key, page_size=None) -> web.Response:
    """getSnapshots

    

    :param api_key: apiKey
    :type api_key: str
    :param page_size: pageSize
    :type page_size: int

    """
    return web.Response(status=200)


async def publish_snapshot_using_post1(request: web.Request, api_key, snapshot_id) -> web.Response:
    """publishSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def revert_to_snapshot_using_post(request: web.Request, api_key, snapshot_id) -> web.Response:
    """revertToSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def unpublish_snapshot_using_post(request: web.Request, api_key, snapshot_id) -> web.Response:
    """unpublishSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)
