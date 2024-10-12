from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.distinc_response_schema import DistincResponseSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.query_get200_response import QueryGet200Response
from openapi_server.models.query_pk_get200_response import QueryPkGet200Response
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server.models.saved_query_get200_response import SavedQueryGet200Response
from openapi_server.models.saved_query_pk_get200_response import SavedQueryPkGet200Response
from openapi_server.models.saved_query_pk_put200_response import SavedQueryPkPut200Response
from openapi_server.models.saved_query_post201_response import SavedQueryPost201Response
from openapi_server.models.saved_query_rest_api_post import SavedQueryRestApiPost
from openapi_server.models.saved_query_rest_api_put import SavedQueryRestApiPut
from openapi_server import util


async def query_distinct_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """query_distinct_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def query_get(request: web.Request, q=None) -> web.Response:
    """query_get

    Get a list of queries, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def query_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """query_pk_get

    Get query detail information.

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def query_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """query_related_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def saved_query_delete(request: web.Request, q=None) -> web.Response:
    """saved_query_delete

    Deletes multiple saved queries in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def saved_query_distinct_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """saved_query_distinct_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def saved_query_export_get(request: web.Request, q=None) -> web.Response:
    """saved_query_export_get

    Exports multiple saved queries and downloads them as YAML files

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def saved_query_get(request: web.Request, q=None) -> web.Response:
    """saved_query_get

    Get a list of saved queries, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def saved_query_import_post(request: web.Request, form_data=None, overwrite=None, passwords=None) -> web.Response:
    """saved_query_import_post

    

    :param form_data: upload file (ZIP)
    :type form_data: str
    :param overwrite: overwrite existing saved queries?
    :type overwrite: bool
    :param passwords: JSON map of passwords for each file
    :type passwords: str

    """
    return web.Response(status=200)


async def saved_query_info_get(request: web.Request, q=None) -> web.Response:
    """saved_query_info_get

    Get metadata information about this API resource

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def saved_query_pk_delete(request: web.Request, pk) -> web.Response:
    """saved_query_pk_delete

    Delete saved query

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def saved_query_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """saved_query_pk_get

    Get a saved query

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def saved_query_pk_put(request: web.Request, pk, body) -> web.Response:
    """saved_query_pk_put

    Update a saved query

    :param pk: 
    :type pk: int
    :param body: Model schema
    :type body: dict | bytes

    """
    body = SavedQueryRestApiPut.from_dict(body)
    return web.Response(status=200)


async def saved_query_post(request: web.Request, body) -> web.Response:
    """saved_query_post

    Create a saved query

    :param body: Model schema
    :type body: dict | bytes

    """
    body = SavedQueryRestApiPost.from_dict(body)
    return web.Response(status=200)


async def saved_query_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """saved_query_related_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
