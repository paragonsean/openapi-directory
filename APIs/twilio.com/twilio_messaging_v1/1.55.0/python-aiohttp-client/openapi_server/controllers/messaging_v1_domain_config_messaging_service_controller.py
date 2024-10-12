from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_domain_config_messaging_service import MessagingV1DomainConfigMessagingService
from openapi_server import util


async def fetch_domain_config_messaging_service(request: web.Request, messaging_service_sid) -> web.Response:
    """fetch_domain_config_messaging_service

    

    :param messaging_service_sid: Unique string used to identify the Messaging service that this domain should be associated with.
    :type messaging_service_sid: str

    """
    return web.Response(status=200)
