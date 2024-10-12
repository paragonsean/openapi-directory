from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.notification_endpoint import NotificationEndpoint
from openapi_server.models.notification_endpoint_update import NotificationEndpointUpdate
from openapi_server.models.notification_endpoints import NotificationEndpoints
from openapi_server.models.post_notification_endpoint import PostNotificationEndpoint
from openapi_server import util


async def create_notification_endpoint(request: web.Request, body) -> web.Response:
    """Add a notification endpoint

    

    :param body: Notification endpoint to create
    :type body: dict | bytes

    """
    body = PostNotificationEndpoint.from_dict(body)
    return web.Response(status=200)


async def delete_notification_endpoints_id(request: web.Request, endpoint_id, zap_trace_span=None) -> web.Response:
    """Delete a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_notification_endpoints_id_labels_id(request: web.Request, endpoint_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param label_id: The ID of the label to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_notification_endpoints(request: web.Request, org_id, zap_trace_span=None, offset=None, limit=None) -> web.Response:
    """List all notification endpoints

    

    :param org_id: Only show notification endpoints that belong to specific organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_notification_endpoints_id(request: web.Request, endpoint_id, zap_trace_span=None) -> web.Response:
    """Retrieve a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_notification_endpoints_id_labels(request: web.Request, endpoint_id, zap_trace_span=None) -> web.Response:
    """List all labels for a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_notification_endpoints_id(request: web.Request, endpoint_id, body, zap_trace_span=None) -> web.Response:
    """Update a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param body: Check update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = NotificationEndpointUpdate.from_dict(body)
    return web.Response(status=200)


async def post_notification_endpoint_id_labels(request: web.Request, endpoint_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def put_notification_endpoints_id(request: web.Request, endpoint_id, body, zap_trace_span=None) -> web.Response:
    """Update a notification endpoint

    

    :param endpoint_id: The notification endpoint ID.
    :type endpoint_id: str
    :param body: A new notification endpoint to replace the existing endpoint with
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = NotificationEndpoint.from_dict(body)
    return web.Response(status=200)
