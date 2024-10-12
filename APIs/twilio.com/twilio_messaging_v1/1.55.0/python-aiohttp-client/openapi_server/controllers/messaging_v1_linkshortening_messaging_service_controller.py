from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_linkshortening_messaging_service import MessagingV1LinkshorteningMessagingService
from openapi_server import util


async def create_linkshortening_messaging_service(request: web.Request, domain_sid, messaging_service_sid) -> web.Response:
    """create_linkshortening_messaging_service

    

    :param domain_sid: The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
    :type domain_sid: str
    :param messaging_service_sid: A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
    :type messaging_service_sid: str

    """
    return web.Response(status=200)


async def delete_linkshortening_messaging_service(request: web.Request, domain_sid, messaging_service_sid) -> web.Response:
    """delete_linkshortening_messaging_service

    

    :param domain_sid: The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
    :type domain_sid: str
    :param messaging_service_sid: A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
    :type messaging_service_sid: str

    """
    return web.Response(status=200)
