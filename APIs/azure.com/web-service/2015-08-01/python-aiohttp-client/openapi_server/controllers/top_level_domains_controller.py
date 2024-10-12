from typing import List, Dict
from aiohttp import web

from openapi_server.models.tld_legal_agreement_collection import TldLegalAgreementCollection
from openapi_server.models.top_level_domain import TopLevelDomain
from openapi_server.models.top_level_domain_agreement_option import TopLevelDomainAgreementOption
from openapi_server.models.top_level_domain_collection import TopLevelDomainCollection
from openapi_server import util


async def top_level_domains_get_get_top_level_domains(request: web.Request, subscription_id, api_version) -> web.Response:
    """Lists all top level domains supported for registration

    

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def top_level_domains_get_top_level_domain(request: web.Request, name, subscription_id, api_version) -> web.Response:
    """Gets details of a top level domain

    

    :param name: Name of the top level domain
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def top_level_domains_list_top_level_domain_agreements(request: web.Request, name, subscription_id, api_version, agreement_option) -> web.Response:
    """Lists legal agreements that user needs to accept before purchasing domain

    

    :param name: Name of the top level domain
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param agreement_option: Domain agreement options
    :type agreement_option: dict | bytes

    """
    agreement_option = TopLevelDomainAgreementOption.from_dict(agreement_option)
    return web.Response(status=200)
