from typing import List, Dict
from aiohttp import web

from openapi_server.models.age_rating_declaration_response import AgeRatingDeclarationResponse
from openapi_server.models.app_category_response import AppCategoryResponse
from openapi_server.models.app_info_localizations_response import AppInfoLocalizationsResponse
from openapi_server.models.app_info_response import AppInfoResponse
from openapi_server.models.app_info_update_request import AppInfoUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_infos_age_rating_declaration_get_to_one_related(request: web.Request, id, fields_age_rating_declarations=None) -> web.Response:
    """app_infos_age_rating_declaration_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_age_rating_declarations: the fields to include for returned resources of type ageRatingDeclarations
    :type fields_age_rating_declarations: List[str]

    """
    return web.Response(status=200)


async def app_infos_app_info_localizations_get_to_many_related(request: web.Request, id, filter_locale=None, fields_app_infos=None, fields_app_info_localizations=None, limit=None, include=None) -> web.Response:
    """app_infos_app_info_localizations_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param filter_locale: filter by attribute &#39;locale&#39;
    :type filter_locale: List[str]
    :param fields_app_infos: the fields to include for returned resources of type appInfos
    :type fields_app_infos: List[str]
    :param fields_app_info_localizations: the fields to include for returned resources of type appInfoLocalizations
    :type fields_app_info_localizations: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def app_infos_get_instance(request: web.Request, id, fields_app_infos=None, include=None, fields_age_rating_declarations=None, fields_app_categories=None, fields_app_info_localizations=None, limit_app_info_localizations=None) -> web.Response:
    """app_infos_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_infos: the fields to include for returned resources of type appInfos
    :type fields_app_infos: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param fields_age_rating_declarations: the fields to include for returned resources of type ageRatingDeclarations
    :type fields_age_rating_declarations: List[str]
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]
    :param fields_app_info_localizations: the fields to include for returned resources of type appInfoLocalizations
    :type fields_app_info_localizations: List[str]
    :param limit_app_info_localizations: maximum number of related appInfoLocalizations returned (when they are included)
    :type limit_app_info_localizations: int

    """
    return web.Response(status=200)


async def app_infos_primary_category_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_infos_primary_category_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_infos_primary_subcategory_one_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_infos_primary_subcategory_one_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_infos_primary_subcategory_two_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_infos_primary_subcategory_two_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_infos_secondary_category_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_infos_secondary_category_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_infos_secondary_subcategory_one_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_infos_secondary_subcategory_one_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_infos_secondary_subcategory_two_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_infos_secondary_subcategory_two_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_infos_update_instance(request: web.Request, id, body) -> web.Response:
    """app_infos_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: AppInfo representation
    :type body: dict | bytes

    """
    body = AppInfoUpdateRequest.from_dict(body)
    return web.Response(status=200)
