from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_domain_config import MessagingV1DomainConfig
from openapi_server import util


async def fetch_domain_config(request: web.Request, domain_sid) -> web.Response:
    """fetch_domain_config

    

    :param domain_sid: Unique string used to identify the domain that this config should be associated with.
    :type domain_sid: str

    """
    return web.Response(status=200)


async def update_domain_config(request: web.Request, domain_sid, callback_url=None, continue_on_failure=None, disable_https=None, fallback_url=None) -> web.Response:
    """update_domain_config

    

    :param domain_sid: Unique string used to identify the domain that this config should be associated with.
    :type domain_sid: str
    :param callback_url: URL to receive click events to your webhook whenever the recipients click on the shortened links
    :type callback_url: str
    :param continue_on_failure: Boolean field to set customer delivery preference when there is a failure in linkShortening service
    :type continue_on_failure: bool
    :param disable_https: Customer&#39;s choice to send links with/without \\\&quot;https://\\\&quot; attached to shortened url. If true, messages will not be sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of the url. False is the default behavior if it is not specified.
    :type disable_https: bool
    :param fallback_url: Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.
    :type fallback_url: str

    """
    return web.Response(status=200)
