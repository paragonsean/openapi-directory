from typing import List, Dict
from aiohttp import web

from openapi_server.models.manage_item_summary import ManageItemSummary
from openapi_server.models.manage_query import ManageQuery
from openapi_server.models.manage_result import ManageResult
from openapi_server.models.manage_screen import ManageScreen
from openapi_server.models.manage_snapshot import ManageSnapshot
from openapi_server.models.manage_snippet import ManageSnippet
from openapi_server.models.message_model import MessageModel
from openapi_server.models.snapshot_creation_model import SnapshotCreationModel
from openapi_server import util


async def copy_snapshot_to_existing_game_using_post(request: web.Request, api_key, snapshot_id, target_api_key) -> web.Response:
    """copySnapshotToExistingGame

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str
    :param target_api_key: targetApiKey
    :type target_api_key: str

    """
    return web.Response(status=200)


async def create_query_using_post(request: web.Request, api_key, body) -> web.Response:
    """createQuery

    

    :param api_key: apiKey
    :type api_key: str
    :param body: query
    :type body: dict | bytes

    """
    body = ManageQuery.from_dict(body)
    return web.Response(status=200)


async def create_screen_using_post(request: web.Request, api_key, body) -> web.Response:
    """createScreen

    

    :param api_key: apiKey
    :type api_key: str
    :param body: screen
    :type body: dict | bytes

    """
    body = ManageScreen.from_dict(body)
    return web.Response(status=200)


async def create_snapshot_using_post(request: web.Request, api_key, body) -> web.Response:
    """createSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param body: model
    :type body: dict | bytes

    """
    body = SnapshotCreationModel.from_dict(body)
    return web.Response(status=200)


async def create_snippet_using_post(request: web.Request, api_key, body) -> web.Response:
    """createSnippet

    

    :param api_key: apiKey
    :type api_key: str
    :param body: snippet
    :type body: dict | bytes

    """
    body = ManageSnippet.from_dict(body)
    return web.Response(status=200)


async def delete_query_using_delete(request: web.Request, api_key, short_code) -> web.Response:
    """deleteQuery

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str

    """
    return web.Response(status=200)


async def delete_screen_using_delete(request: web.Request, api_key, short_code) -> web.Response:
    """deleteScreen

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str

    """
    return web.Response(status=200)


async def delete_snapshot_using_delete(request: web.Request, api_key, snapshot_id) -> web.Response:
    """deleteSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def delete_snippet_using_delete(request: web.Request, api_key, short_code) -> web.Response:
    """deleteSnippet

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str

    """
    return web.Response(status=200)


async def get_query_using_get(request: web.Request, api_key, short_code) -> web.Response:
    """getQuery

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str

    """
    return web.Response(status=200)


async def get_screen_using_get(request: web.Request, api_key, short_code) -> web.Response:
    """getScreen

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str

    """
    return web.Response(status=200)


async def get_snippet_using_get(request: web.Request, api_key, short_code) -> web.Response:
    """getSnippet

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str

    """
    return web.Response(status=200)


async def list_executable_screens_using_get(request: web.Request, api_key) -> web.Response:
    """listExecutableScreens

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def list_queries_using_get(request: web.Request, api_key) -> web.Response:
    """listQueries

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def list_screens_using_get(request: web.Request, api_key) -> web.Response:
    """listScreens

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def list_snapshots_using_get(request: web.Request, api_key) -> web.Response:
    """listSnapshots

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def list_snippets_using_get(request: web.Request, api_key) -> web.Response:
    """listSnippets

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def publish_snapshot_using_post(request: web.Request, api_key, snapshot_id) -> web.Response:
    """publishSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def revert_snapshot_using_post(request: web.Request, api_key, snapshot_id) -> web.Response:
    """revertSnapshot

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id: snapshotId
    :type snapshot_id: str

    """
    return web.Response(status=200)


async def update_query_using_put(request: web.Request, api_key, short_code, body) -> web.Response:
    """updateQuery

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str
    :param body: query
    :type body: dict | bytes

    """
    body = ManageQuery.from_dict(body)
    return web.Response(status=200)


async def update_screen_using_put(request: web.Request, api_key, short_code, body) -> web.Response:
    """updateScreen

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str
    :param body: screen
    :type body: dict | bytes

    """
    body = ManageScreen.from_dict(body)
    return web.Response(status=200)


async def update_snippet_using_put(request: web.Request, api_key, short_code, body) -> web.Response:
    """updateSnippet

    

    :param api_key: apiKey
    :type api_key: str
    :param short_code: shortCode
    :type short_code: str
    :param body: snippet
    :type body: dict | bytes

    """
    body = ManageSnippet.from_dict(body)
    return web.Response(status=200)
