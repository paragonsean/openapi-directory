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
from openapi_server.models.scraper_target_request import ScraperTargetRequest
from openapi_server.models.scraper_target_response import ScraperTargetResponse
from openapi_server.models.scraper_target_responses import ScraperTargetResponses
from openapi_server import util


async def delete_scrapers_id(request: web.Request, scraper_target_id, zap_trace_span=None) -> web.Response:
    """Delete a scraper target

    

    :param scraper_target_id: The identifier of the scraper target.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_scrapers_id_labels_id(request: web.Request, scraper_target_id, label_id, zap_trace_span=None) -> web.Response:
    """Delete a label from a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param label_id: The label ID.
    :type label_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_scrapers_id_members_id(request: web.Request, user_id, scraper_target_id, zap_trace_span=None) -> web.Response:
    """Remove a member from a scraper target

    

    :param user_id: The ID of member to remove.
    :type user_id: str
    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_scrapers_id_owners_id(request: web.Request, user_id, scraper_target_id, zap_trace_span=None) -> web.Response:
    """Remove an owner from a scraper target

    

    :param user_id: The ID of owner to remove.
    :type user_id: str
    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_scrapers(request: web.Request, zap_trace_span=None, name=None, id=None, org_id=None, org=None) -> web.Response:
    """List all scraper targets

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param name: Specifies the name of the scraper target.
    :type name: str
    :param id: List of scraper target IDs to return. If both &#x60;id&#x60; and &#x60;owner&#x60; are specified, only &#x60;id&#x60; is used.
    :type id: List[str]
    :param org_id: Specifies the organization ID of the scraper target.
    :type org_id: str
    :param org: Specifies the organization name of the scraper target.
    :type org: str

    """
    return web.Response(status=200)


async def get_scrapers_id(request: web.Request, scraper_target_id, zap_trace_span=None) -> web.Response:
    """Retrieve a scraper target

    

    :param scraper_target_id: The identifier of the scraper target.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_scrapers_id_labels(request: web.Request, scraper_target_id, zap_trace_span=None) -> web.Response:
    """List all labels for a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_scrapers_id_members(request: web.Request, scraper_target_id, zap_trace_span=None) -> web.Response:
    """List all users with member privileges for a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_scrapers_id_owners(request: web.Request, scraper_target_id, zap_trace_span=None) -> web.Response:
    """List all owners of a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_scrapers_id(request: web.Request, scraper_target_id, body, zap_trace_span=None) -> web.Response:
    """Update a scraper target

    

    :param scraper_target_id: The identifier of the scraper target.
    :type scraper_target_id: str
    :param body: Scraper target update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = ScraperTargetRequest.from_dict(body)
    return web.Response(status=200)


async def post_scrapers(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create a scraper target

    

    :param body: Scraper target to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = ScraperTargetRequest.from_dict(body)
    return web.Response(status=200)


async def post_scrapers_id_labels(request: web.Request, scraper_target_id, body, zap_trace_span=None) -> web.Response:
    """Add a label to a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param body: Label to add
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = LabelMapping.from_dict(body)
    return web.Response(status=200)


async def post_scrapers_id_members(request: web.Request, scraper_target_id, body, zap_trace_span=None) -> web.Response:
    """Add a member to a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param body: User to add as member
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_scrapers_id_owners(request: web.Request, scraper_target_id, body, zap_trace_span=None) -> web.Response:
    """Add an owner to a scraper target

    

    :param scraper_target_id: The scraper target ID.
    :type scraper_target_id: str
    :param body: User to add as owner
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)
