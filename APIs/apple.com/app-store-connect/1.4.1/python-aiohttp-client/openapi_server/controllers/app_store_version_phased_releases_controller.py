from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_store_version_phased_release_create_request import AppStoreVersionPhasedReleaseCreateRequest
from openapi_server.models.app_store_version_phased_release_response import AppStoreVersionPhasedReleaseResponse
from openapi_server.models.app_store_version_phased_release_update_request import AppStoreVersionPhasedReleaseUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_store_version_phased_releases_create_instance(request: web.Request, body) -> web.Response:
    """app_store_version_phased_releases_create_instance

    

    :param body: AppStoreVersionPhasedRelease representation
    :type body: dict | bytes

    """
    body = AppStoreVersionPhasedReleaseCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_store_version_phased_releases_delete_instance(request: web.Request, id) -> web.Response:
    """app_store_version_phased_releases_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_store_version_phased_releases_update_instance(request: web.Request, id, body) -> web.Response:
    """app_store_version_phased_releases_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppStoreVersionPhasedRelease representation
    :type body: dict | bytes

    """
    body = AppStoreVersionPhasedReleaseUpdateRequest.from_dict(body)
    return web.Response(status=200)
