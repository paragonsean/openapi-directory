from typing import List, Dict
from aiohttp import web

from openapi_server.models.check import Check
from openapi_server.models.check_patch import CheckPatch
from openapi_server.models.checks import Checks
from openapi_server.models.error import Error
from openapi_server.models.flux_response import FluxResponse
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.post_check import PostCheck
from openapi_server import util


async def create_check(request: web.Request, body) -> web.Response:
    """Add new check

    

    :param body: Check to create
    :type body: dict | bytes

    """
    body = PostCheck.from_dict(body)
    return web.Response(status=200)


async def delete_checks_id(request: web.Request, check_id, zap_trace_span=None) -> web.Response:
    """Delete a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_checks_id_labels_id(request: web.Request, check_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete label from a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param label_id: The ID of the label to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_checks(request: web.Request, org_id, zap_trace_span=None, offset=None, limit=None) -> web.Response:
    """List all checks

    

    :param org_id: Only show checks that belong to a specific organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def get_checks_id(request: web.Request, check_id, zap_trace_span=None) -> web.Response:
    """Retrieve a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_checks_id_labels(request: web.Request, check_id, zap_trace_span=None) -> web.Response:
    """List all labels for a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_checks_id_query(request: web.Request, check_id, zap_trace_span=None) -> web.Response:
    """Retrieve a check query

    

    :param check_id: The check ID.
    :type check_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_checks_id(request: web.Request, check_id, body, zap_trace_span=None) -> web.Response:
    """Update a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param body: Check update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = CheckPatch.from_dict(body)
    return web.Response(status=200)


async def post_checks_id_labels(request: web.Request, check_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def put_checks_id(request: web.Request, check_id, body, zap_trace_span=None) -> web.Response:
    """Update a check

    

    :param check_id: The check ID.
    :type check_id: str
    :param body: Check update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = Check.from_dict(body)
    return web.Response(status=200)
