from typing import List, Dict
from aiohttp import web

from openapi_server.models.funding_account_response_v2 import FundingAccountResponseV2
from openapi_server.models.funding_request_v2 import FundingRequestV2
from openapi_server.models.funding_request_v3 import FundingRequestV3
from openapi_server.models.funding_response import FundingResponse
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.list_funding_accounts_response_v2 import ListFundingAccountsResponseV2
from openapi_server.models.page_resource_funding_payor_status_audit_response_funding_payor_status_audit_response import PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse
from openapi_server import util


async def create_funding_request_v2(request: web.Request, source_account_id, body) -> web.Response:
    """Create Funding Request

    Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo  (202 - accepted, 400 - invalid request body, 404 - source account not found).

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str
    :param body: Body to included amount to be funded
    :type body: dict | bytes

    """
    body = FundingRequestV2.from_dict(body)
    return web.Response(status=200)


async def create_funding_request_v3(request: web.Request, source_account_id, body) -> web.Response:
    """Create Funding Request

    &lt;p&gt;Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo&lt;/p&gt; 

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str
    :param body: Body to included amount to be funded
    :type body: dict | bytes

    """
    body = FundingRequestV3.from_dict(body)
    return web.Response(status=200)


async def get_funding_account_v2(request: web.Request, funding_account_id, sensitive=None) -> web.Response:
    """Get Funding Account

    Get Funding Account by ID

    :param funding_account_id: 
    :type funding_account_id: str
    :type funding_account_id: str
    :param sensitive: 
    :type sensitive: bool

    """
    return web.Response(status=200)


async def get_funding_accounts_v2(request: web.Request, payor_id=None, name=None, country=None, currency=None, type=None, page=None, page_size=None, sort=None, sensitive=None) -> web.Response:
    """Get Funding Accounts

    Get the funding accounts.

    :param payor_id: 
    :type payor_id: str
    :type payor_id: str
    :param name: The descriptive funding account name
    :type name: str
    :param country: The 2 letter ISO 3166-1 country code (upper case)
    :type country: str
    :param currency: The ISO 4217 currency code
    :type currency: str
    :param type: The type of funding account.
    :type type: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name.
    :type sort: str
    :param sensitive: 
    :type sensitive: bool

    """
    return web.Response(status=200)


async def get_funding_by_id_v1(request: web.Request, funding_id) -> web.Response:
    """Get Funding

    Get Funding by Id

    :param funding_id: 
    :type funding_id: str
    :type funding_id: str

    """
    return web.Response(status=200)


async def list_funding_audit_deltas(request: web.Request, payor_id, updated_since, page=None, page_size=None) -> web.Response:
    """Get Funding Audit Delta

    Get funding audit deltas for a payor

    :param payor_id: 
    :type payor_id: str
    :type payor_id: str
    :param updated_since: 
    :type updated_since: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int

    """
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)
