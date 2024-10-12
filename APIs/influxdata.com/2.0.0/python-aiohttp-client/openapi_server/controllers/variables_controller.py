from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.variable import Variable
from openapi_server.models.variables import Variables
from openapi_server import util


async def delete_variables_id(request: web.Request, variable_id, zap_trace_span=None) -> web.Response:
    """Delete a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_variables_id_labels_id(request: web.Request, variable_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param label_id: The label ID to delete.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_variables(request: web.Request, zap_trace_span=None, org=None, org_id=None) -> web.Response:
    """List all variables

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org: The name of the organization.
    :type org: str
    :param org_id: The organization ID.
    :type org_id: str

    """
    return web.Response(status=200)


async def get_variables_id(request: web.Request, variable_id, zap_trace_span=None) -> web.Response:
    """Retrieve a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_variables_id_labels(request: web.Request, variable_id, zap_trace_span=None) -> web.Response:
    """List all labels for a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_variables_id(request: web.Request, variable_id, body, zap_trace_span=None) -> web.Response:
    """Update a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param body: Variable update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = Variable.from_dict(body)
    return web.Response(status=200)


async def post_variables(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a variable

    

    :param body: Variable to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = Variable.from_dict(body)
    return web.Response(status=200)


async def post_variables_id_labels(request: web.Request, variable_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def put_variables_id(request: web.Request, variable_id, body, zap_trace_span=None) -> web.Response:
    """Replace a variable

    

    :param variable_id: The variable ID.
    :type variable_id: str
    :param body: Variable to replace
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = Variable.from_dict(body)
    return web.Response(status=200)
