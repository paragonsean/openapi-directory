from typing import List, Dict
from aiohttp import web

from openapi_server.models.googlerpc_status import GooglerpcStatus
from openapi_server.models.serving_batch_query_request import ServingBatchQueryRequest
from openapi_server.models.serving_batch_query_response import ServingBatchQueryResponse
from openapi_server.models.stream_result_of_serving_response_set import StreamResultOfServingResponseSet
from openapi_server import util


async def query(request: web.Request, customer_id, body) -> web.Response:
    """query

    Query

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServingBatchQueryRequest.from_dict(body)
    return web.Response(status=200)


async def stream_query(request: web.Request, customer_id, body) -> web.Response:
    """stream_query

    Stream Query

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ServingBatchQueryRequest.from_dict(body)
    return web.Response(status=200)
