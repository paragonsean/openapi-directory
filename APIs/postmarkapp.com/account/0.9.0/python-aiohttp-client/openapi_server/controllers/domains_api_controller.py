from typing import List, Dict
from aiohttp import web

from openapi_server.models.dkim_rotation_response import DKIMRotationResponse
from openapi_server.models.domain_creation_model import DomainCreationModel
from openapi_server.models.domain_editing_model import DomainEditingModel
from openapi_server.models.domain_extended_information import DomainExtendedInformation
from openapi_server.models.domain_listing_results import DomainListingResults
from openapi_server.models.domain_spf_result import DomainSPFResult
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def create_domain(request: web.Request, x_postmark_account_token, body=None) -> web.Response:
    """Create a Domain

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DomainCreationModel.from_dict(body)
    return web.Response(status=200)


async def delete_domain(request: web.Request, x_postmark_account_token, domainid) -> web.Response:
    """Delete a Domain

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Domain that should be deleted by the request.
    :type domainid: int

    """
    return web.Response(status=200)


async def edit_domain(request: web.Request, x_postmark_account_token, domainid, body=None) -> web.Response:
    """Update a Domain

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Domain that should be modified by the request.
    :type domainid: int
    :param body: 
    :type body: dict | bytes

    """
    body = DomainEditingModel.from_dict(body)
    return web.Response(status=200)


async def get_domain(request: web.Request, x_postmark_account_token, domainid) -> web.Response:
    """Get a Domain

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Domain that should be retrieved.
    :type domainid: int

    """
    return web.Response(status=200)


async def list_domains(request: web.Request, x_postmark_account_token, count, offset) -> web.Response:
    """List Domains

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param count: Number of records to return per request. Max 500.
    :type count: int
    :param offset: Number of records to skip
    :type offset: int

    """
    return web.Response(status=200)


async def request_dkim_verification_for_domain(request: web.Request, x_postmark_account_token, domainid) -> web.Response:
    """Request DNS Verification for DKIM

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Domain for which DKIM DNS records should be verified.
    :type domainid: int

    """
    return web.Response(status=200)


async def request_return_path_verification_for_domain(request: web.Request, x_postmark_account_token, domainid) -> web.Response:
    """Request DNS Verification for Return-Path

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Domain for which Return-Path DNS records should be verified.
    :type domainid: int

    """
    return web.Response(status=200)


async def request_spf_verification_for_domain(request: web.Request, x_postmark_account_token, domainid) -> web.Response:
    """Request DNS Verification for SPF

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Domain for which SPF DNS records should be verified.
    :type domainid: int

    """
    return web.Response(status=200)


async def rotate_dkim_key_for_domain(request: web.Request, x_postmark_account_token, domainid) -> web.Response:
    """Rotate DKIM Key

    Creates a new DKIM key to replace your current key. Until the DNS entries are confirmed, the new values will be in the &#x60;DKIMPendingHost&#x60; and &#x60;DKIMPendingTextValue&#x60; fields. After the new DKIM value is verified in DNS, the pending values will migrate to &#x60;DKIMTextValue&#x60; and &#x60;DKIMPendingTextValue&#x60; and Postmark will begin to sign emails with the new DKIM key. 

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param domainid: The ID for the Sender Signature for which a new DKIM Key should be generated.
    :type domainid: int

    """
    return web.Response(status=200)
