from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.export_template_request import ExportTemplateRequest
from openapi_server.models.list_stacks200_response import ListStacks200Response
from openapi_server.models.patch_stack_request import PatchStackRequest
from openapi_server.models.post_stack_request import PostStackRequest
from openapi_server.models.stack import Stack
from openapi_server.models.template_apply import TemplateApply
from openapi_server.models.template_inner import TemplateInner
from openapi_server.models.template_summary import TemplateSummary
from openapi_server import util


async def apply_template(request: web.Request, body) -> web.Response:
    """Apply or dry-run an InfluxDB Template

    

    :param body: 
    :type body: dict | bytes

    """
    body = TemplateApply.from_dict(body)
    return web.Response(status=200)


async def create_stack(request: web.Request, body) -> web.Response:
    """Create a new stack

    

    :param body: Stack to create.
    :type body: dict | bytes

    """
    body = PostStackRequest.from_dict(body)
    return web.Response(status=200)


async def delete_stack(request: web.Request, stack_id, org_id) -> web.Response:
    """Delete a stack and associated resources

    

    :param stack_id: Theidentifier of the stack.
    :type stack_id: str
    :param org_id: The identifier of the organization.
    :type org_id: str

    """
    return web.Response(status=200)


async def export_template(request: web.Request, body=None) -> web.Response:
    """Export a new Influx Template

    

    :param body: Export resources as an InfluxDB template.
    :type body: dict | bytes

    """
    body = ExportTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def list_stacks(request: web.Request, org_id, name=None, stack_id=None) -> web.Response:
    """List all installed InfluxDB templates

    

    :param org_id: The organization id of the stacks
    :type org_id: str
    :param name: A collection of names to filter the list by.
    :type name: str
    :param stack_id: A collection of stackIDs to filter the list by.
    :type stack_id: str

    """
    return web.Response(status=200)


async def read_stack(request: web.Request, stack_id) -> web.Response:
    """Retrieve a stack

    

    :param stack_id: Theidentifier of the stack.
    :type stack_id: str

    """
    return web.Response(status=200)


async def uninstall_stack(request: web.Request, stack_id) -> web.Response:
    """Uninstall an InfluxDB Stack

    

    :param stack_id: The stack id
    :type stack_id: str

    """
    return web.Response(status=200)


async def update_stack(request: web.Request, stack_id, body) -> web.Response:
    """Update an InfluxDB Stack

    

    :param stack_id: Theidentifier of the stack.
    :type stack_id: str
    :param body: Influx stack to update.
    :type body: dict | bytes

    """
    body = PatchStackRequest.from_dict(body)
    return web.Response(status=200)
