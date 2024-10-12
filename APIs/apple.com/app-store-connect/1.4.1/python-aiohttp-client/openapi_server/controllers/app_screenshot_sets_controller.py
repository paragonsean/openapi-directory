from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_screenshot_set_app_screenshots_linkages_request import AppScreenshotSetAppScreenshotsLinkagesRequest
from openapi_server.models.app_screenshot_set_app_screenshots_linkages_response import AppScreenshotSetAppScreenshotsLinkagesResponse
from openapi_server.models.app_screenshot_set_create_request import AppScreenshotSetCreateRequest
from openapi_server.models.app_screenshot_set_response import AppScreenshotSetResponse
from openapi_server.models.app_screenshots_response import AppScreenshotsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_screenshot_sets_app_screenshots_get_to_many_related(request: web.Request, id, fields_app_screenshot_sets=None, fields_app_screenshots=None, limit=None, include=None) -> web.Response:
    """app_screenshot_sets_app_screenshots_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_screenshot_sets: the fields to include for returned resources of type appScreenshotSets
    :type fields_app_screenshot_sets: List[str]
    :param fields_app_screenshots: the fields to include for returned resources of type appScreenshots
    :type fields_app_screenshots: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_screenshot_sets_app_screenshots_get_to_many_relationship(request: web.Request, id, limit=None) -> web.Response:
    """app_screenshot_sets_app_screenshots_get_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)


async def app_screenshot_sets_app_screenshots_replace_to_many_relationship(request: web.Request, id, body) -> web.Response:
    """app_screenshot_sets_app_screenshots_replace_to_many_relationship

    

    :param id: the id of the requested resource
    :type id: str
    :param body: List of related linkages
    :type body: dict | bytes

    """
    body = AppScreenshotSetAppScreenshotsLinkagesRequest.from_dict(body)
    return web.Response(status=200)


async def app_screenshot_sets_create_instance(request: web.Request, body) -> web.Response:
    """app_screenshot_sets_create_instance

    

    :param body: AppScreenshotSet representation
    :type body: dict | bytes

    """
    body = AppScreenshotSetCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_screenshot_sets_delete_instance(request: web.Request, id) -> web.Response:
    """app_screenshot_sets_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_screenshot_sets_get_instance(request: web.Request, id, fields_app_screenshot_sets=None, include=None, fields_app_screenshots=None, limit_app_screenshots=None) -> web.Response:
    """app_screenshot_sets_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_screenshot_sets: the fields to include for returned resources of type appScreenshotSets
    :type fields_app_screenshot_sets: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_app_screenshots: the fields to include for returned resources of type appScreenshots
    :type fields_app_screenshots: List[str]
    :param limit_app_screenshots: maximum number of related appScreenshots returned (when they are included)
    :type limit_app_screenshots: int

    """
    return web.Response(status=200)
