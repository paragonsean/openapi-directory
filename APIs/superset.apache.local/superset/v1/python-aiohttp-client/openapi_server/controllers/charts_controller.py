from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.chart_cache_screenshot_response_schema import ChartCacheScreenshotResponseSchema
from openapi_server.models.chart_data_async_response_schema import ChartDataAsyncResponseSchema
from openapi_server.models.chart_data_query_context_schema import ChartDataQueryContextSchema
from openapi_server.models.chart_data_response_schema import ChartDataResponseSchema
from openapi_server.models.chart_get200_response import ChartGet200Response
from openapi_server.models.chart_pk_get200_response import ChartPkGet200Response
from openapi_server.models.chart_pk_put200_response import ChartPkPut200Response
from openapi_server.models.chart_post201_response import ChartPost201Response
from openapi_server.models.chart_rest_api_post import ChartRestApiPost
from openapi_server.models.chart_rest_api_put import ChartRestApiPut
from openapi_server.models.get_fav_star_ids_schema import GetFavStarIdsSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server.models.screenshot_query_schema import ScreenshotQuerySchema
from openapi_server import util


async def chart_data_cache_key_get(request: web.Request, cache_key) -> web.Response:
    """chart_data_cache_key_get

    Takes a query context cache key and returns payload data response for the given query.

    :param cache_key: 
    :type cache_key: str

    """
    return web.Response(status=200)


async def chart_data_post(request: web.Request, body) -> web.Response:
    """chart_data_post

    Takes a query context constructed in the client and returns payload data response for the given query.

    :param body: A query context consists of a datasource from which to fetch data and one or many query objects.
    :type body: dict | bytes

    """
    body = ChartDataQueryContextSchema.from_dict(body)
    return web.Response(status=200)


async def chart_delete(request: web.Request, q=None) -> web.Response:
    """chart_delete

    Deletes multiple Charts in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def chart_export_get(request: web.Request, q=None) -> web.Response:
    """chart_export_get

    Exports multiple charts and downloads them as YAML files

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def chart_favorite_status_get(request: web.Request, q=None) -> web.Response:
    """chart_favorite_status_get

    Check favorited dashboards for current user

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def chart_get(request: web.Request, q=None) -> web.Response:
    """chart_get

    Get a list of charts, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def chart_import_post(request: web.Request, form_data=None, overwrite=None, passwords=None) -> web.Response:
    """chart_import_post

    

    :param form_data: upload file (ZIP)
    :type form_data: str
    :param overwrite: overwrite existing databases?
    :type overwrite: bool
    :param passwords: JSON map of passwords for each file
    :type passwords: str

    """
    return web.Response(status=200)


async def chart_info_get(request: web.Request, q=None) -> web.Response:
    """chart_info_get

    Several metadata information about chart API endpoints.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def chart_pk_cache_screenshot_get(request: web.Request, pk, q=None) -> web.Response:
    """chart_pk_cache_screenshot_get

    Compute and cache a screenshot.

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def chart_pk_data_get(request: web.Request, pk, format=None, type=None) -> web.Response:
    """chart_pk_data_get

    Takes a chart ID and uses the query context stored when the chart was saved to return payload data response.

    :param pk: The chart ID
    :type pk: int
    :param format: The format in which the data should be returned
    :type format: str
    :param type: The type in which the data should be returned
    :type type: str

    """
    return web.Response(status=200)


async def chart_pk_delete(request: web.Request, pk) -> web.Response:
    """chart_pk_delete

    Deletes a Chart.

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def chart_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """chart_pk_get

    Get a chart detail information.

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def chart_pk_put(request: web.Request, pk, body) -> web.Response:
    """chart_pk_put

    Changes a Chart.

    :param pk: 
    :type pk: int
    :param body: Chart schema
    :type body: dict | bytes

    """
    body = ChartRestApiPut.from_dict(body)
    return web.Response(status=200)


async def chart_pk_screenshot_digest_get(request: web.Request, pk, digest) -> web.Response:
    """chart_pk_screenshot_digest_get

    Get a computed screenshot from cache.

    :param pk: 
    :type pk: int
    :param digest: 
    :type digest: str

    """
    return web.Response(status=200)


async def chart_pk_thumbnail_digest_get(request: web.Request, pk, digest) -> web.Response:
    """chart_pk_thumbnail_digest_get

    Compute or get already computed chart thumbnail from cache.

    :param pk: 
    :type pk: int
    :param digest: 
    :type digest: str

    """
    return web.Response(status=200)


async def chart_post(request: web.Request, body) -> web.Response:
    """chart_post

    Create a new Chart.

    :param body: Chart schema
    :type body: dict | bytes

    """
    body = ChartRestApiPost.from_dict(body)
    return web.Response(status=200)


async def chart_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """chart_related_column_name_get

    Get a list of all possible owners for a chart. Use &#x60;owners&#x60; has the &#x60;column_name&#x60; parameter

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
