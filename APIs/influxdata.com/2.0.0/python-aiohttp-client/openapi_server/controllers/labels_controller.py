from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_create_request import LabelCreateRequest
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.label_update import LabelUpdate
from openapi_server.models.labels_response import LabelsResponse
from openapi_server import util


async def delete_labels_id(request: web.Request, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label

    

    :param label_id: The ID of the label to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_labels(request: web.Request, zap_trace_span=None, org_id=None) -> web.Response:
    """List all labels

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org_id: The organization ID.
    :type org_id: str

    """
    return web.Response(status=200)


async def get_labels_id(request: web.Request, label_id, zap_trace_span=None) -> web.Response:
    """Retrieve a label

    

    :param label_id: The ID of the label to update.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_labels_id(request: web.Request, label_id, body, zap_trace_span=None) -> web.Response:
    """Update a label

    

    :param label_id: The ID of the label to update.
    :type label_id: str
    :param body: Label update
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelUpdate.from_dict(body)
    return web.Response(status=200)


async def post_labels(request: web.Request, body) -> web.Response:
    """Create a label

    

    :param body: Label to create
    :type body: dict | bytes

    """
    body = LabelCreateRequest.from_dict(body)
    return web.Response(status=200)
