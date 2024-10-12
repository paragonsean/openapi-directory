from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_create import DocumentCreate
from openapi_server.models.document_update import DocumentUpdate
from openapi_server.models.documents import Documents
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server import util


async def delete_documents_templates_id(request: web.Request, template_id, zap_trace_span=None) -> web.Response:
    """Delete a template

    

    :param template_id: The template ID.
    :type template_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_documents_templates_id_labels_id(request: web.Request, template_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a template

    

    :param template_id: The template ID.
    :type template_id: str
    :param label_id: The label ID.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_documents_templates(request: web.Request, zap_trace_span=None, org=None, org_id=None) -> web.Response:
    """List all templates

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org: Specifies the name of the organization of the template.
    :type org: str
    :param org_id: Specifies the organization ID of the template.
    :type org_id: str

    """
    return web.Response(status=200)


async def get_documents_templates_id(request: web.Request, template_id, zap_trace_span=None) -> web.Response:
    """Retrieve a template

    

    :param template_id: The template ID.
    :type template_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_documents_templates_id_labels(request: web.Request, template_id, zap_trace_span=None) -> web.Response:
    """List all labels for a template

    

    :param template_id: The template ID.
    :type template_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_documents_templates(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a template

    

    :param body: Template that will be created
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = DocumentCreate.from_dict(body)
    return web.Response(status=200)


async def post_documents_templates_id_labels(request: web.Request, template_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a template

    

    :param template_id: The template ID.
    :type template_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def put_documents_templates_id(request: web.Request, template_id, body, zap_trace_span=None) -> web.Response:
    """Update a template

    

    :param template_id: The template ID.
    :type template_id: str
    :param body: Template that will be updated
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = DocumentUpdate.from_dict(body)
    return web.Response(status=200)
