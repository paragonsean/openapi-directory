from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.css_template_get200_response import CssTemplateGet200Response
from openapi_server.models.css_template_pk_get200_response import CssTemplatePkGet200Response
from openapi_server.models.css_template_pk_put200_response import CssTemplatePkPut200Response
from openapi_server.models.css_template_post201_response import CssTemplatePost201Response
from openapi_server.models.css_template_rest_api_post import CssTemplateRestApiPost
from openapi_server.models.css_template_rest_api_put import CssTemplateRestApiPut
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server import util


async def css_template_delete(request: web.Request, q=None) -> web.Response:
    """css_template_delete

    Deletes multiple css templates in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def css_template_get(request: web.Request, q=None) -> web.Response:
    """css_template_get

    Get a list of CSS templates, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def css_template_info_get(request: web.Request, q=None) -> web.Response:
    """css_template_info_get

    Get metadata information about this API resource

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def css_template_pk_delete(request: web.Request, pk) -> web.Response:
    """css_template_pk_delete

    Delete CSS template

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def css_template_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """css_template_pk_get

    Get a CSS template

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def css_template_pk_put(request: web.Request, pk, body) -> web.Response:
    """css_template_pk_put

    Update a CSS template

    :param pk: 
    :type pk: int
    :param body: Model schema
    :type body: dict | bytes

    """
    body = CssTemplateRestApiPut.from_dict(body)
    return web.Response(status=200)


async def css_template_post(request: web.Request, body) -> web.Response:
    """css_template_post

    Create a CSS template

    :param body: Model schema
    :type body: dict | bytes

    """
    body = CssTemplateRestApiPost.from_dict(body)
    return web.Response(status=200)


async def css_template_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """css_template_related_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
