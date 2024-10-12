from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_response import AppResponse
from openapi_server.models.beta_app_localization_create_request import BetaAppLocalizationCreateRequest
from openapi_server.models.beta_app_localization_response import BetaAppLocalizationResponse
from openapi_server.models.beta_app_localization_update_request import BetaAppLocalizationUpdateRequest
from openapi_server.models.beta_app_localizations_response import BetaAppLocalizationsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_app_localizations_app_get_to_one_related(request: web.Request, id, fields_apps=None) -> web.Response:
    """beta_app_localizations_app_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_app_localizations_create_instance(request: web.Request, body) -> web.Response:
    """beta_app_localizations_create_instance

    

    :param body: BetaAppLocalization representation
    :type body: dict | bytes

    """
    body = BetaAppLocalizationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def beta_app_localizations_delete_instance(request: web.Request, id) -> web.Response:
    """beta_app_localizations_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def beta_app_localizations_get_collection(request: web.Request, filter_locale=None, filter_app=None, fields_beta_app_localizations=None, limit=None, include=None, fields_apps=None) -> web.Response:
    """beta_app_localizations_get_collection

    

    :param filter_locale: filter by attribute &#39;locale&#39;
    :type filter_locale: List[str]
    :param filter_app: filter by id(s) of related &#39;app&#39;
    :type filter_app: List[str]
    :param fields_beta_app_localizations: the fields to include for returned resources of type betaAppLocalizations
    :type fields_beta_app_localizations: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_app_localizations_get_instance(request: web.Request, id, fields_beta_app_localizations=None, include=None, fields_apps=None) -> web.Response:
    """beta_app_localizations_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_app_localizations: the fields to include for returned resources of type betaAppLocalizations
    :type fields_beta_app_localizations: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_apps: the fields to include for returned resources of type apps
    :type fields_apps: List[str]

    """
    return web.Response(status=200)


async def beta_app_localizations_update_instance(request: web.Request, id, body) -> web.Response:
    """beta_app_localizations_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BetaAppLocalization representation
    :type body: dict | bytes

    """
    body = BetaAppLocalizationUpdateRequest.from_dict(body)
    return web.Response(status=200)
