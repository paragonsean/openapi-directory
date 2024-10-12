from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_info_localization_create_request import AppInfoLocalizationCreateRequest
from openapi_server.models.app_info_localization_response import AppInfoLocalizationResponse
from openapi_server.models.app_info_localization_update_request import AppInfoLocalizationUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_info_localizations_create_instance(request: web.Request, body) -> web.Response:
    """app_info_localizations_create_instance

    

    :param body: AppInfoLocalization representation
    :type body: dict | bytes

    """
    body = AppInfoLocalizationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def app_info_localizations_delete_instance(request: web.Request, id) -> web.Response:
    """app_info_localizations_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def app_info_localizations_get_instance(request: web.Request, id, fields_app_info_localizations=None, include=None) -> web.Response:
    """app_info_localizations_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_info_localizations: the fields to include for returned resources of type appInfoLocalizations
    :type fields_app_info_localizations: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_info_localizations_update_instance(request: web.Request, id, body) -> web.Response:
    """app_info_localizations_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppInfoLocalization representation
    :type body: dict | bytes

    """
    body = AppInfoLocalizationUpdateRequest.from_dict(body)
    return web.Response(status=200)
