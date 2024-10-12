from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_alternate_contact_request import DeleteAlternateContactRequest
from openapi_server.models.disable_region_request import DisableRegionRequest
from openapi_server.models.enable_region_request import EnableRegionRequest
from openapi_server.models.get_alternate_contact_request import GetAlternateContactRequest
from openapi_server.models.get_alternate_contact_response import GetAlternateContactResponse
from openapi_server.models.get_contact_information_request import GetContactInformationRequest
from openapi_server.models.get_contact_information_response import GetContactInformationResponse
from openapi_server.models.get_region_opt_status_request import GetRegionOptStatusRequest
from openapi_server.models.get_region_opt_status_response import GetRegionOptStatusResponse
from openapi_server.models.list_regions_request import ListRegionsRequest
from openapi_server.models.list_regions_response import ListRegionsResponse
from openapi_server.models.put_alternate_contact_request import PutAlternateContactRequest
from openapi_server.models.put_contact_information_request import PutContactInformationRequest
from openapi_server import util


async def delete_alternate_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_alternate_contact

    &lt;p&gt;Deletes the specified alternate contact from an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the alternate contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Access or updating the alternate contacts&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html\&quot;&gt;Enabling trusted access for Amazon Web Services Account Management&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DeleteAlternateContactRequest.from_dict(body)
    return web.Response(status=200)


async def disable_region(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disable_region

    Disables (opts-out) a particular Region for an account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = DisableRegionRequest.from_dict(body)
    return web.Response(status=200)


async def enable_region(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """enable_region

    Enables (opts-in) a particular Region for an account.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = EnableRegionRequest.from_dict(body)
    return web.Response(status=200)


async def get_alternate_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_alternate_contact

    &lt;p&gt;Retrieves the specified alternate contact attached to an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the alternate contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Access or updating the alternate contacts&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html\&quot;&gt;Enabling trusted access for Amazon Web Services Account Management&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetAlternateContactRequest.from_dict(body)
    return web.Response(status=200)


async def get_contact_information(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_contact_information

    &lt;p&gt;Retrieves the primary contact information of an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the primary contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Update the primary and alternate contact information&lt;/a&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetContactInformationRequest.from_dict(body)
    return web.Response(status=200)


async def get_region_opt_status(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_region_opt_status

    Retrieves the opt-in status of a particular Region.

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = GetRegionOptStatusRequest.from_dict(body)
    return web.Response(status=200)


async def list_regions(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """list_regions

    Lists all the Regions for a given account and their respective opt-in statuses. Optionally, this list can be filtered by the &lt;code&gt;region-opt-status-contains&lt;/code&gt; parameter. 

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str

    """
    body = ListRegionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_alternate_contact(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_alternate_contact

    &lt;p&gt;Modifies the specified alternate contact attached to an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the alternate contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Access or updating the alternate contacts&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html\&quot;&gt;Enabling trusted access for Amazon Web Services Account Management&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutAlternateContactRequest.from_dict(body)
    return web.Response(status=200)


async def put_contact_information(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_contact_information

    &lt;p&gt;Updates the primary contact information of an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the primary contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Update the primary and alternate contact information&lt;/a&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutContactInformationRequest.from_dict(body)
    return web.Response(status=200)
