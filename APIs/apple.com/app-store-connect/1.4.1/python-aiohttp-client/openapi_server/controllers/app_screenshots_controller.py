from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_screenshot_create_request import AppScreenshotCreateRequest
from openapi_server.models.app_screenshot_response import AppScreenshotResponse
from openapi_server.models.app_screenshot_update_request import AppScreenshotUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_screenshots_create_instance(request: web.Request, body) -> web.Response:
    """app_screenshots_create_instance

    

    :param body: AppScreenshot representation
    :type body: dict | bytes

    """
    body = AppScreenshotCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_screenshots_delete_instance(request: web.Request, id) -> web.Response:
    """app_screenshots_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_screenshots_get_instance(request: web.Request, id, fields_app_screenshots=None, include=None) -> web.Response:
    """app_screenshots_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_screenshots: the fields to include for returned resources of type appScreenshots
    :type fields_app_screenshots: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_screenshots_update_instance(request: web.Request, id, body) -> web.Response:
    """app_screenshots_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppScreenshot representation
    :type body: dict | bytes

    """
    body = AppScreenshotUpdateRequest.from_dict(body)
    return web.Response(status=200)
