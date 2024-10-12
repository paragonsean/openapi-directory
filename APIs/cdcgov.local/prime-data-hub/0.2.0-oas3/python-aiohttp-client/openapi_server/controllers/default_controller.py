from typing import List, Dict
from aiohttp import web

from openapi_server.models.organization import Organization
from openapi_server.models.receiver import Receiver
from openapi_server.models.report import Report
from openapi_server.models.sender import Sender
from openapi_server import util


async def reports_post(request: web.Request, client, body, option=None, default=None, route_to=None) -> web.Response:
    """Post a report to the data hub

    

    :param client: The client&#39;s name that matches the client name in metadata
    :type client: str
    :param body: The public health information being routed
    :type body: str
    :param option: Optional ways to process the request
    :type option: str
    :param default: Dynamic default values for an element. &#39;:&#39; or %3A is used to seperate element name and value
    :type default: List[str]
    :param route_to: A comma speparated list of receiver names. Limit the list of possible receivers to these receivers.
    :type route_to: List[str]

    """
    return web.Response(status=200)


async def settings_organizations_get(request: web.Request, ) -> web.Response:
    """settings_organizations_get

    The settings for all organizations of the system. Must have admin access.


    """
    return web.Response(status=200)


async def settings_organizations_head(request: web.Request, ) -> web.Response:
    """settings_organizations_head

    Retrived the last modified for all settings of the system. Must have admin access.


    """
    return web.Response(status=200)


async def settings_organizations_organization_name_delete(request: web.Request, organization_name) -> web.Response:
    """settings_organizations_organization_name_delete

    Delete an organization (and the associated receivers and senders)

    :param organization_name: The name of the organization
    :type organization_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_get(request: web.Request, organization_name) -> web.Response:
    """settings_organizations_organization_name_get

    A single organization settings

    :param organization_name: The name of the organization
    :type organization_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_put(request: web.Request, organization_name, body=None) -> web.Response:
    """settings_organizations_organization_name_put

    Create or update the direct settings associated with an organization

    :param organization_name: The name of the organization
    :type organization_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = Organization.from_dict(body)
    return web.Response(status=200)


async def settings_organizations_organization_name_receivers_get(request: web.Request, organization_name) -> web.Response:
    """settings_organizations_organization_name_receivers_get

    A list of receivers and their current settings

    :param organization_name: Fetch receivers with this organization name
    :type organization_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_receivers_receiver_name_delete(request: web.Request, organization_name, receiver_name) -> web.Response:
    """settings_organizations_organization_name_receivers_receiver_name_delete

    Delete a receiver

    :param organization_name: the organization name
    :type organization_name: str
    :param receiver_name: The name of the receiver
    :type receiver_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_receivers_receiver_name_get(request: web.Request, organization_name, receiver_name) -> web.Response:
    """settings_organizations_organization_name_receivers_receiver_name_get

    The settings of a single of receiver

    :param organization_name: Create receivers under this organization name
    :type organization_name: str
    :param receiver_name: The name of the receiver
    :type receiver_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_receivers_receiver_name_put(request: web.Request, organization_name, receiver_name, body=None) -> web.Response:
    """settings_organizations_organization_name_receivers_receiver_name_put

    Update a single reciever

    :param organization_name: Create receivers under this organization name
    :type organization_name: str
    :param receiver_name: The name of the receiver
    :type receiver_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = Receiver.from_dict(body)
    return web.Response(status=200)


async def settings_organizations_organization_name_senders_get(request: web.Request, organization_name) -> web.Response:
    """settings_organizations_organization_name_senders_get

    A list of senders

    :param organization_name: Fetch senders with this organization name
    :type organization_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_senders_sender_name_delete(request: web.Request, organization_name, sender_name) -> web.Response:
    """settings_organizations_organization_name_senders_sender_name_delete

    Delete a sender

    :param organization_name: the organization name
    :type organization_name: str
    :param sender_name: The name of a sender to the data hub
    :type sender_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_senders_sender_name_get(request: web.Request, organization_name, sender_name) -> web.Response:
    """settings_organizations_organization_name_senders_sender_name_get

    The settings of a single of sender

    :param organization_name: Fetch senders with this organization name
    :type organization_name: str
    :param sender_name: The name of a sender to the data hub
    :type sender_name: str

    """
    return web.Response(status=200)


async def settings_organizations_organization_name_senders_sender_name_put(request: web.Request, organization_name, sender_name, body=None) -> web.Response:
    """settings_organizations_organization_name_senders_sender_name_put

    Update a single sender

    :param organization_name: Fetch senders with this organization name
    :type organization_name: str
    :param sender_name: The name of a sender to the data hub
    :type sender_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = Sender.from_dict(body)
    return web.Response(status=200)
