from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.domain_detail import DomainDetail
from openapi_server.models.edit_domain_will_renew_request import EditDomainWillRenewRequest
from openapi_server.models.edit_name_servers import EditNameServers
from openapi_server.models.register_domain import RegisterDomain
from openapi_server.models.transfer_domain import TransferDomain
from openapi_server import util


async def configure_domain(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Edit domain name renew state

    Allowed if can_toggle_renew is true on the domain detail:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;If there are no unpaid invoices for the domain name anymore.&lt;/li&gt;&lt;li&gt;If the renewal won&#39;t start within 1 month.&lt;/li&gt;&lt;/ul&gt;  Allowed if the requesting user has the finance role.

    :param domain_name: The domain name
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: Contains the domain renew information
    :type body: dict | bytes

    """
    body = EditDomainWillRenewRequest.from_dict(body)
    return web.Response(status=200)


async def edit_name_servers(request: web.Request, domain_name, domain_name2, body=None) -> web.Response:
    """Edit domain name servers

    

    :param domain_name: The domain name
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str
    :param body: 
    :type body: dict | bytes

    """
    body = EditNameServers.from_dict(body)
    return web.Response(status=200)


async def get_domain(request: web.Request, domain_name, domain_name2) -> web.Response:
    """Details of a domain

    

    :param domain_name: The domain name
    :type domain_name: str
    :param domain_name2: Automatically added
    :type domain_name2: str

    """
    return web.Response(status=200)


async def get_domains(request: web.Request, skip=None, take=None) -> web.Response:
    """Overviews of domains

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)


async def register(request: web.Request, body=None) -> web.Response:
    """Register a domain

    Registers an available domain.&lt;br /&gt;Domain names with extension &#39;.ca&#39; are only available for registrants with country code &#39;CA&#39;.

    :param body: 
    :type body: dict | bytes

    """
    body = RegisterDomain.from_dict(body)
    return web.Response(status=200)


async def transfer(request: web.Request, body=None) -> web.Response:
    """Transfer a domain

    Transfers a domain with a transfer authorization code.&lt;br /&gt;Domain names with extension &#39;.ca&#39; are only available for registrants with country code &#39;CA&#39;.

    :param body: 
    :type body: dict | bytes

    """
    body = TransferDomain.from_dict(body)
    return web.Response(status=200)
