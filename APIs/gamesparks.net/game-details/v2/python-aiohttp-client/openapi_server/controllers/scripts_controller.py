from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_model import MessageModel
from openapi_server.models.scripts_difference_list_model import ScriptsDifferenceListModel
from openapi_server.models.snapshot_script_version_list_model import SnapshotScriptVersionListModel
from openapi_server import util


async def export_zip_using_get(request: web.Request, api_key) -> web.Response:
    """exportZip

    

    :param api_key: apiKey
    :type api_key: str

    """
    return web.Response(status=200)


async def get_script_differences_using_get(request: web.Request, api_key, snapshot_id1, snapshot_id2) -> web.Response:
    """getScriptDifferences

    

    :param api_key: apiKey
    :type api_key: str
    :param snapshot_id1: snapshotId1
    :type snapshot_id1: str
    :param snapshot_id2: snapshotId2
    :type snapshot_id2: str

    """
    return web.Response(status=200)


async def get_script_versions_using_get(request: web.Request, api_key, page, page_size=None) -> web.Response:
    """getScriptVersions

    

    :param api_key: apiKey
    :type api_key: str
    :param page: page
    :type page: int
    :param page_size: pageSize
    :type page_size: int

    """
    return web.Response(status=200)


async def get_script_versions_using_get1(request: web.Request, api_key, page_size=None) -> web.Response:
    """getScriptVersions

    

    :param api_key: apiKey
    :type api_key: str
    :param page_size: pageSize
    :type page_size: int

    """
    return web.Response(status=200)


async def import_accept_using_post(request: web.Request, api_key, body, file) -> web.Response:
    """importAccept

    

    :param api_key: apiKey
    :type api_key: str
    :param body: body
    :type body: str
    :param file: file
    :type file: str

    """
    return web.Response(status=200)


async def import_zip_using_post(request: web.Request, api_key, file) -> web.Response:
    """importZip

    

    :param api_key: apiKey
    :type api_key: str
    :param file: file
    :type file: str

    """
    return web.Response(status=200)
