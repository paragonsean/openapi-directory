from typing import List, Dict
from aiohttp import web

from openapi_server.models.beta_build_localization_create_request import BetaBuildLocalizationCreateRequest
from openapi_server.models.beta_build_localization_response import BetaBuildLocalizationResponse
from openapi_server.models.beta_build_localization_update_request import BetaBuildLocalizationUpdateRequest
from openapi_server.models.beta_build_localizations_response import BetaBuildLocalizationsResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def beta_build_localizations_build_get_to_one_related(request: web.Request, id, fields_builds=None) -> web.Response:
    """beta_build_localizations_build_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def beta_build_localizations_create_instance(request: web.Request, body) -> web.Response:
    """beta_build_localizations_create_instance

    

    :param body: BetaBuildLocalization representation
    :type body: dict | bytes

    """
    body = BetaBuildLocalizationCreateRequest.from_dict(body)
    return web.Response(status=200)


async def beta_build_localizations_delete_instance(request: web.Request, id) -> web.Response:
    """beta_build_localizations_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def beta_build_localizations_get_collection(request: web.Request, filter_locale=None, filter_build=None, fields_beta_build_localizations=None, limit=None, include=None, fields_builds=None) -> web.Response:
    """beta_build_localizations_get_collection

    

    :param filter_locale: filter by attribute &#39;locale&#39;
    :type filter_locale: List[str]
    :param filter_build: filter by id(s) of related &#39;build&#39;
    :type filter_build: List[str]
    :param fields_beta_build_localizations: the fields to include for returned resources of type betaBuildLocalizations
    :type fields_beta_build_localizations: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def beta_build_localizations_get_instance(request: web.Request, id, fields_beta_build_localizations=None, include=None, fields_builds=None) -> web.Response:
    """beta_build_localizations_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_beta_build_localizations: the fields to include for returned resources of type betaBuildLocalizations
    :type fields_beta_build_localizations: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_builds: the fields to include for returned resources of type builds
    :type fields_builds: List[str]

    """
    return web.Response(status=200)


async def beta_build_localizations_update_instance(request: web.Request, id, body) -> web.Response:
    """beta_build_localizations_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: BetaBuildLocalization representation
    :type body: dict | bytes

    """
    body = BetaBuildLocalizationUpdateRequest.from_dict(body)
    return web.Response(status=200)
