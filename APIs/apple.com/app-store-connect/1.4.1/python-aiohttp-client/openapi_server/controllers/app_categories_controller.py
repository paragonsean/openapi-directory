from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_categories_response import AppCategoriesResponse
from openapi_server.models.app_category_response import AppCategoryResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def app_categories_get_collection(request: web.Request, filter_platforms=None, exists_parent=None, fields_app_categories=None, limit=None, include=None, limit_subcategories=None) -> web.Response:
    """app_categories_get_collection

    

    :param filter_platforms: filter by attribute &#39;platforms&#39;
    :type filter_platforms: List[str]
    :param exists_parent: filter by existence or non-existence of related &#39;parent&#39;
    :type exists_parent: List[str]
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]
    :param limit: maximum resources per page
    :type limit: int
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param limit_subcategories: maximum number of related subcategories returned (when they are included)
    :type limit_subcategories: int

    """
    return web.Response(status=200)


async def app_categories_get_instance(request: web.Request, id, fields_app_categories=None, include=None, limit_subcategories=None) -> web.Response:
    """app_categories_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]
    :param limit_subcategories: maximum number of related subcategories returned (when they are included)
    :type limit_subcategories: int

    """
    return web.Response(status=200)


async def app_categories_parent_get_to_one_related(request: web.Request, id, fields_app_categories=None) -> web.Response:
    """app_categories_parent_get_to_one_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]

    """
    return web.Response(status=200)


async def app_categories_subcategories_get_to_many_related(request: web.Request, id, fields_app_categories=None, limit=None) -> web.Response:
    """app_categories_subcategories_get_to_many_related

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_app_categories: the fields to include for returned resources of type appCategories
    :type fields_app_categories: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)
