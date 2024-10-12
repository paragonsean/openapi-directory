from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.dashboard_get200_response import DashboardGet200Response
from openapi_server.models.dashboard_id_or_slug_charts_get200_response import DashboardIdOrSlugChartsGet200Response
from openapi_server.models.dashboard_id_or_slug_datasets_get200_response import DashboardIdOrSlugDatasetsGet200Response
from openapi_server.models.dashboard_id_or_slug_get200_response import DashboardIdOrSlugGet200Response
from openapi_server.models.dashboard_pk_put200_response import DashboardPkPut200Response
from openapi_server.models.dashboard_post201_response import DashboardPost201Response
from openapi_server.models.dashboard_rest_api_post import DashboardRestApiPost
from openapi_server.models.dashboard_rest_api_put import DashboardRestApiPut
from openapi_server.models.get_fav_star_ids_schema import GetFavStarIdsSchema
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server.models.thumbnail_query_schema import ThumbnailQuerySchema
from openapi_server import util


async def dashboard_delete(request: web.Request, q=None) -> web.Response:
    """dashboard_delete

    Deletes multiple Dashboards in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def dashboard_export_get(request: web.Request, q=None) -> web.Response:
    """dashboard_export_get

    Exports multiple Dashboards and downloads them as YAML files.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def dashboard_favorite_status_get(request: web.Request, q=None) -> web.Response:
    """dashboard_favorite_status_get

    Check favorited dashboards for current user

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def dashboard_get(request: web.Request, q=None) -> web.Response:
    """dashboard_get

    Get a list of dashboards, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dashboard_id_or_slug_charts_get(request: web.Request, id_or_slug) -> web.Response:
    """dashboard_id_or_slug_charts_get

    Get the chart definitions for a given dashboard

    :param id_or_slug: 
    :type id_or_slug: str

    """
    return web.Response(status=200)


async def dashboard_id_or_slug_datasets_get(request: web.Request, id_or_slug) -> web.Response:
    """dashboard_id_or_slug_datasets_get

    Returns a list of a dashboard&#39;s datasets. Each dataset includes only the information necessary to render the dashboard&#39;s charts.

    :param id_or_slug: Either the id of the dashboard, or its slug
    :type id_or_slug: str

    """
    return web.Response(status=200)


async def dashboard_id_or_slug_get(request: web.Request, id_or_slug) -> web.Response:
    """dashboard_id_or_slug_get

    Get a dashboard detail information.

    :param id_or_slug: Either the id of the dashboard, or its slug
    :type id_or_slug: str

    """
    return web.Response(status=200)


async def dashboard_import_post(request: web.Request, form_data=None, overwrite=None, passwords=None) -> web.Response:
    """dashboard_import_post

    

    :param form_data: upload file (ZIP or JSON)
    :type form_data: str
    :param overwrite: overwrite existing databases?
    :type overwrite: bool
    :param passwords: JSON map of passwords for each file
    :type passwords: str

    """
    return web.Response(status=200)


async def dashboard_info_get(request: web.Request, q=None) -> web.Response:
    """dashboard_info_get

    Several metadata information about dashboard API endpoints.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dashboard_pk_delete(request: web.Request, pk) -> web.Response:
    """dashboard_pk_delete

    Deletes a Dashboard.

    :param pk: 
    :type pk: int

    """
    return web.Response(status=200)


async def dashboard_pk_put(request: web.Request, pk, body) -> web.Response:
    """dashboard_pk_put

    Changes a Dashboard.

    :param pk: 
    :type pk: int
    :param body: Dashboard schema
    :type body: dict | bytes

    """
    body = DashboardRestApiPut.from_dict(body)
    return web.Response(status=200)


async def dashboard_pk_thumbnail_digest_get(request: web.Request, pk, digest, q=None) -> web.Response:
    """dashboard_pk_thumbnail_digest_get

    Compute async or get already computed dashboard thumbnail from cache.

    :param pk: 
    :type pk: int
    :param digest: A hex digest that makes this dashboard unique
    :type digest: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def dashboard_post(request: web.Request, body) -> web.Response:
    """dashboard_post

    Create a new Dashboard.

    :param body: Dashboard schema
    :type body: dict | bytes

    """
    body = DashboardRestApiPost.from_dict(body)
    return web.Response(status=200)


async def dashboard_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """dashboard_related_column_name_get

    Get a list of all possible owners for a dashboard.

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
