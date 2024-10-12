from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_headers_in import EndpointHeadersIn
from openapi_server.models.endpoint_headers_out import EndpointHeadersOut
from openapi_server.models.endpoint_headers_patch_in import EndpointHeadersPatchIn
from openapi_server.models.endpoint_in import EndpointIn
from openapi_server.models.endpoint_out import EndpointOut
from openapi_server.models.endpoint_secret_out import EndpointSecretOut
from openapi_server.models.endpoint_secret_rotate_in import EndpointSecretRotateIn
from openapi_server.models.endpoint_stats import EndpointStats
from openapi_server.models.endpoint_transformation_in import EndpointTransformationIn
from openapi_server.models.endpoint_transformation_out import EndpointTransformationOut
from openapi_server.models.endpoint_update import EndpointUpdate
from openapi_server.models.event_example_in import EventExampleIn
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_endpoint_out import ListResponseEndpointOut
from openapi_server.models.message_out import MessageOut
from openapi_server.models.ordering import Ordering
from openapi_server.models.recover_in import RecoverIn
from openapi_server.models.recover_out import RecoverOut
from openapi_server.models.replay_in import ReplayIn
from openapi_server.models.replay_out import ReplayOut
from openapi_server import util


async def create_endpoint_api_v1_app_app_id_endpoint_post(request: web.Request, app_id, body, idempotency_key=None) -> web.Response:
    """Create Endpoint

    Create a new endpoint for the application.  When &#x60;secret&#x60; is &#x60;null&#x60; the secret is automatically generated (recommended)

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EndpointIn.from_dict(body)
    return web.Response(status=200)


async def delete_endpoint_api_v1_app_app_id_endpoint_endpoint_id_delete(request: web.Request, endpoint_id, app_id, idempotency_key=None) -> web.Response:
    """Delete Endpoint

    Delete an endpoint.

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_endpoint_api_v1_app_app_id_endpoint_endpoint_id_get(request: web.Request, endpoint_id, app_id, idempotency_key=None) -> web.Response:
    """Get Endpoint

    Get an application.

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_get(request: web.Request, endpoint_id, app_id, idempotency_key=None) -> web.Response:
    """Get Endpoint Headers

    Get the additional headers to be sent with the webhook

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_get(request: web.Request, endpoint_id, app_id, idempotency_key=None) -> web.Response:
    """Get Endpoint Secret

    Get the endpoint&#39;s signing secret.  This is used to verify the authenticity of the webhook. For more information please refer to [the consuming webhooks docs](https://docs.svix.com/consuming-webhooks/).

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_endpoint_stats_api_v1_app_app_id_endpoint_endpoint_id_stats_get(request: web.Request, endpoint_id, app_id, since=None, until=None, idempotency_key=None) -> web.Response:
    """Get Endpoint Stats

    Get basic statistics for the endpoint.

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param since: 
    :type since: str
    :param until: 
    :type until: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    since = util.deserialize_datetime(since)
    until = util.deserialize_datetime(until)
    return web.Response(status=200)


async def get_endpoint_transformation_api_v1_app_app_id_endpoint_endpoint_id_transformation_get(request: web.Request, endpoint_id, app_id, idempotency_key=None) -> web.Response:
    """Get Endpoint Transformation

    Get the transformation code associated with this endpoint

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_endpoints_api_v1_app_app_id_endpoint_get(request: web.Request, app_id, iterator=None, limit=None, order=None, idempotency_key=None) -> web.Response:
    """List Endpoints

    List the application&#39;s endpoints.

    :param app_id: 
    :type app_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param order: 
    :type order: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    order = .from_dict(order)
    return web.Response(status=200)


async def patch_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_patch(request: web.Request, app_id, endpoint_id, body, idempotency_key=None) -> web.Response:
    """Patch Endpoint Headers

    Partially set the additional headers to be sent with the webhook

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EndpointHeadersPatchIn.from_dict(body)
    return web.Response(status=200)


async def recover_failed_webhooks_api_v1_app_app_id_endpoint_endpoint_id_recover_post(request: web.Request, app_id, endpoint_id, body, idempotency_key=None) -> web.Response:
    """Recover Failed Webhooks

    Resend all failed messages since a given time.

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = RecoverIn.from_dict(body)
    return web.Response(status=200)


async def replay_missing_webhooks_api_v1_app_app_id_endpoint_endpoint_id_replay_missing_post(request: web.Request, app_id, endpoint_id, body, idempotency_key=None) -> web.Response:
    """Replay Missing Webhooks

    Replays messages to the endpoint. Only messages that were created after &#x60;since&#x60; will be sent. Messages that were previously sent to the endpoint are not resent.

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = ReplayIn.from_dict(body)
    return web.Response(status=200)


async def rotate_endpoint_secret_api_v1_app_app_id_endpoint_endpoint_id_secret_rotate_post(request: web.Request, endpoint_id, app_id, body, idempotency_key=None) -> web.Response:
    """Rotate Endpoint Secret

    Rotates the endpoint&#39;s signing secret.  The previous secret will be valid for the next 24 hours.

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EndpointSecretRotateIn.from_dict(body)
    return web.Response(status=200)


async def send_event_type_example_message_api_v1_app_app_id_endpoint_endpoint_id_send_example_post(request: web.Request, app_id, endpoint_id, body, idempotency_key=None) -> web.Response:
    """Send Event Type Example Message

    Send an example message for event

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EventExampleIn.from_dict(body)
    return web.Response(status=200)


async def set_endpoint_transformation_api_v1_app_app_id_endpoint_endpoint_id_transformation_patch(request: web.Request, app_id, endpoint_id, body, idempotency_key=None) -> web.Response:
    """Set Endpoint Transformation

    Set or unset the transformation code associated with this endpoint

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EndpointTransformationIn.from_dict(body)
    return web.Response(status=200)


async def update_endpoint_api_v1_app_app_id_endpoint_endpoint_id_put(request: web.Request, endpoint_id, app_id, body, idempotency_key=None) -> web.Response:
    """Update Endpoint

    Update an endpoint.

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EndpointUpdate.from_dict(body)
    return web.Response(status=200)


async def update_endpoint_headers_api_v1_app_app_id_endpoint_endpoint_id_headers_put(request: web.Request, app_id, endpoint_id, body, idempotency_key=None) -> web.Response:
    """Update Endpoint Headers

    Set the additional headers to be sent with the webhook

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EndpointHeadersIn.from_dict(body)
    return web.Response(status=200)
