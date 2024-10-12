from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_linkshortening_messaging_service_domain_association import MessagingV1LinkshorteningMessagingServiceDomainAssociation
from openapi_server import util


async def fetch_linkshortening_messaging_service_domain_association(request: web.Request, messaging_service_sid) -> web.Response:
    """fetch_linkshortening_messaging_service_domain_association

    

    :param messaging_service_sid: Unique string used to identify the Messaging service that this domain should be associated with.
    :type messaging_service_sid: str

    """
    return web.Response(status=200)
