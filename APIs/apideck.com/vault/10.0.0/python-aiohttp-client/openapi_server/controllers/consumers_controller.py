from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.consumer import Consumer
from openapi_server.models.consumer_request_counts_in_date_range_response import ConsumerRequestCountsInDateRangeResponse
from openapi_server.models.create_consumer_response import CreateConsumerResponse
from openapi_server.models.delete_consumer_response import DeleteConsumerResponse
from openapi_server.models.get_consumer_response import GetConsumerResponse
from openapi_server.models.get_consumers_response import GetConsumersResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_consumer_request import UpdateConsumerRequest
from openapi_server.models.update_consumer_response import UpdateConsumerResponse
from openapi_server import util


async def consumer_request_counts_all(request: web.Request, x_apideck_app_id, consumer_id, start_datetime, end_datetime) -> web.Response:
    """Consumer request counts

    Get consumer request counts within a given datetime range. 

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param consumer_id: ID of the consumer to return
    :type consumer_id: str
    :param start_datetime: Scopes results to requests that happened after datetime
    :type start_datetime: str
    :param end_datetime: Scopes results to requests that happened before datetime
    :type end_datetime: str

    """
    return web.Response(status=200)


async def consumers_add(request: web.Request, x_apideck_app_id, body) -> web.Response:
    """Create consumer

    Create a consumer

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Consumer.from_dict(body)
    return web.Response(status=200)


async def consumers_all(request: web.Request, x_apideck_app_id, cursor=None, limit=None) -> web.Response:
    """Get all consumers

    This endpoint includes all application consumers, along with an aggregated count of requests made. 

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int

    """
    return web.Response(status=200)


async def consumers_delete(request: web.Request, x_apideck_app_id, consumer_id) -> web.Response:
    """Delete consumer

    Delete consumer and all their connections, including credentials.

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param consumer_id: ID of the consumer to return
    :type consumer_id: str

    """
    return web.Response(status=200)


async def consumers_one(request: web.Request, x_apideck_app_id, consumer_id) -> web.Response:
    """Get consumer

    Consumer detail including their aggregated counts with the connections they have authorized. 

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param consumer_id: ID of the consumer to return
    :type consumer_id: str

    """
    return web.Response(status=200)


async def consumers_update(request: web.Request, x_apideck_app_id, consumer_id, body) -> web.Response:
    """Update consumer

    Update consumer metadata such as name and email.

    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param consumer_id: ID of the consumer to return
    :type consumer_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateConsumerRequest.from_dict(body)
    return web.Response(status=200)
