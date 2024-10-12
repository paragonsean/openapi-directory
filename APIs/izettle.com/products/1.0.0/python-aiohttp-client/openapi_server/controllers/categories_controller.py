from typing import List, Dict
from aiohttp import web

from openapi_server.models.category_response import CategoryResponse
from openapi_server.models.create_categories_request import CreateCategoriesRequest
from openapi_server.models.rename_category_request import RenameCategoryRequest
from openapi_server import util


async def create_categories(request: web.Request, organization_uuid, body) -> web.Response:
    """Create a new category

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def delete_category(request: web.Request, organization_uuid, category_uuid) -> web.Response:
    """Delete a category

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param category_uuid: 
    :type category_uuid: str
    :type category_uuid: str

    """
    return web.Response(status=200)


async def get_product_types(request: web.Request, organization_uuid) -> web.Response:
    """Retrieve all categories

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)


async def rename_category(request: web.Request, organization_uuid, category_uuid, body) -> web.Response:
    """Rename a category

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param category_uuid: 
    :type category_uuid: str
    :type category_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenameCategoryRequest.from_dict(body)
    return web.Response(status=200)
