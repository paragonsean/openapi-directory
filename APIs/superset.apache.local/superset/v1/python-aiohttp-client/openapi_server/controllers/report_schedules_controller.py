from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.annotation_layer_info_get200_response import AnnotationLayerInfoGet200Response
from openapi_server.models.get_info_schema import GetInfoSchema
from openapi_server.models.get_item_schema import GetItemSchema
from openapi_server.models.get_list_schema import GetListSchema
from openapi_server.models.get_related_schema import GetRelatedSchema
from openapi_server.models.related_response_schema import RelatedResponseSchema
from openapi_server.models.report_get200_response import ReportGet200Response
from openapi_server.models.report_pk_get200_response import ReportPkGet200Response
from openapi_server.models.report_pk_log_get200_response import ReportPkLogGet200Response
from openapi_server.models.report_pk_log_log_id_get200_response import ReportPkLogLogIdGet200Response
from openapi_server.models.report_pk_put200_response import ReportPkPut200Response
from openapi_server.models.report_post201_response import ReportPost201Response
from openapi_server.models.report_schedule_rest_api_post import ReportScheduleRestApiPost
from openapi_server.models.report_schedule_rest_api_put import ReportScheduleRestApiPut
from openapi_server import util


async def report_delete(request: web.Request, q=None) -> web.Response:
    """report_delete

    Deletes multiple report schedules in a bulk operation.

    :param q: 
    :type q: List[int]

    """
    return web.Response(status=200)


async def report_get(request: web.Request, q=None) -> web.Response:
    """report_get

    Get a list of report schedules, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def report_info_get(request: web.Request, q=None) -> web.Response:
    """report_info_get

    Get metadata information about this API resource

    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def report_pk_delete(request: web.Request, pk) -> web.Response:
    """report_pk_delete

    Delete a report schedule

    :param pk: The report schedule pk
    :type pk: int

    """
    return web.Response(status=200)


async def report_pk_get(request: web.Request, pk, q=None) -> web.Response:
    """report_pk_get

    Get a report schedule

    :param pk: 
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def report_pk_log_get(request: web.Request, pk, q=None) -> web.Response:
    """report_pk_log_get

    Get a list of report schedule logs, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

    :param pk: The report schedule id for these logs
    :type pk: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def report_pk_log_log_id_get(request: web.Request, pk, log_id, q=None) -> web.Response:
    """report_pk_log_log_id_get

    Get a report schedule log

    :param pk: The report schedule pk for log
    :type pk: int
    :param log_id: The log pk
    :type log_id: int
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)


async def report_pk_put(request: web.Request, pk, body) -> web.Response:
    """report_pk_put

    Update a report schedule

    :param pk: The Report Schedule pk
    :type pk: int
    :param body: Report Schedule schema
    :type body: dict | bytes

    """
    body = ReportScheduleRestApiPut.from_dict(body)
    return web.Response(status=200)


async def report_post(request: web.Request, body) -> web.Response:
    """report_post

    Create a report schedule

    :param body: Report Schedule schema
    :type body: dict | bytes

    """
    body = ReportScheduleRestApiPost.from_dict(body)
    return web.Response(status=200)


async def report_related_column_name_get(request: web.Request, column_name, q=None) -> web.Response:
    """report_related_column_name_get

    

    :param column_name: 
    :type column_name: str
    :param q: 
    :type q: dict | bytes

    """
    q = .from_dict(q)
    return web.Response(status=200)
