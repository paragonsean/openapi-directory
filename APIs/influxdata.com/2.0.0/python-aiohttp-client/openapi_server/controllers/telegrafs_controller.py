from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.error import Error
from openapi_server.models.label_mapping import LabelMapping
from openapi_server.models.label_response import LabelResponse
from openapi_server.models.labels_response import LabelsResponse
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.telegraf import Telegraf
from openapi_server.models.telegraf_request import TelegrafRequest
from openapi_server.models.telegrafs import Telegrafs
from openapi_server import util


async def delete_telegrafs_id(request: web.Request, telegraf_id, zap_trace_span=None) -> web.Response:
    """Delete a Telegraf configuration

    

    :param telegraf_id: The Telegraf configuration ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_telegrafs_id_labels_id(request: web.Request, telegraf_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a Telegraf config

    

    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param label_id: The label ID.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_telegrafs_id_members_id(request: web.Request, user_id, telegraf_id, zap_trace_span=None) -> web.Response:
    """Remove a member from a Telegraf config

    

    :param user_id: The ID of the member to remove.
    :type user_id: str
    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_telegrafs_id_owners_id(request: web.Request, user_id, telegraf_id, zap_trace_span=None) -> web.Response:
    """Remove an owner from a Telegraf config

    

    :param user_id: The ID of the owner to remove.
    :type user_id: str
    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_telegrafs(request: web.Request, zap_trace_span=None, org_id=None) -> web.Response:
    """List all Telegraf configurations

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param org_id: The organization ID the Telegraf config belongs to.
    :type org_id: str

    """
    return web.Response(status=200)


async def get_telegrafs_id(request: web.Request, telegraf_id, zap_trace_span=None, accept=None) -> web.Response:
    """Retrieve a Telegraf configuration

    

    :param telegraf_id: The Telegraf configuration ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param accept: 
    :type accept: str

    """
    return web.Response(status=200)


async def get_telegrafs_id_labels(request: web.Request, telegraf_id, zap_trace_span=None) -> web.Response:
    """List all labels for a Telegraf config

    

    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_telegrafs_id_members(request: web.Request, telegraf_id, zap_trace_span=None) -> web.Response:
    """List all users with member privileges for a Telegraf config

    

    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_telegrafs_id_owners(request: web.Request, telegraf_id, zap_trace_span=None) -> web.Response:
    """List all owners of a Telegraf configuration

    

    :param telegraf_id: The Telegraf configuration ID.
    :type telegraf_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_telegrafs(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a Telegraf configuration

    

    :param body: Telegraf configuration to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = TelegrafRequest.from_dict(body)
    return web.Response(status=200)


async def post_telegrafs_id_labels(request: web.Request, telegraf_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a Telegraf config

    

    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def post_telegrafs_id_members(request: web.Request, telegraf_id, body, zap_trace_span=None) -> web.Response:
    """Add a member to a Telegraf config

    

    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param body: User to add as member
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_telegrafs_id_owners(request: web.Request, telegraf_id, body, zap_trace_span=None) -> web.Response:
    """Add an owner to a Telegraf configuration

    

    :param telegraf_id: The Telegraf configuration ID.
    :type telegraf_id: str
    :param body: User to add as owner
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def put_telegrafs_id(request: web.Request, telegraf_id, body, zap_trace_span=None) -> web.Response:
    """Update a Telegraf configuration

    

    :param telegraf_id: The Telegraf config ID.
    :type telegraf_id: str
    :param body: Telegraf configuration update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = TelegrafRequest.from_dict(body)
    return web.Response(status=200)
