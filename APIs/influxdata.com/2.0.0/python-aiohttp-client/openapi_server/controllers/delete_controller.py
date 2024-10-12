from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_predicate_request import DeletePredicateRequest
from openapi_server.models.error import Error
from openapi_server import util


async def post_delete(request: web.Request, body, zap_trace_span=None, org=None, bucket=None, org_id=None, bucket_id=None) -> web.Response:
    """Delete time series data from InfluxDB

    

    :param body: Predicate delete request
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org: Specifies the organization to delete data from.
    :type org: str
    :param bucket: Specifies the bucket to delete data from.
    :type bucket: str
    :param org_id: Specifies the organization ID of the resource.
    :type org_id: str
    :param bucket_id: Specifies the bucket ID to delete data from.
    :type bucket_id: str

    """
    body = DeletePredicateRequest.from_dict(body)
    return web.Response(status=200)
