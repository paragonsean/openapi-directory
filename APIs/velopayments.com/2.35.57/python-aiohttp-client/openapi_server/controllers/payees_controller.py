from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.paged_payee_response_v3 import PagedPayeeResponseV3
from openapi_server.models.paged_payee_response_v4 import PagedPayeeResponseV4
from openapi_server.models.payee_delta_response_v3 import PayeeDeltaResponseV3
from openapi_server.models.payee_delta_response_v4 import PayeeDeltaResponseV4
from openapi_server.models.payee_detail_response_v3 import PayeeDetailResponseV3
from openapi_server.models.payee_detail_response_v4 import PayeeDetailResponseV4
from openapi_server.models.update_payee_details_request_v3 import UpdatePayeeDetailsRequestV3
from openapi_server.models.update_payee_details_request_v4 import UpdatePayeeDetailsRequestV4
from openapi_server.models.update_remote_id_request_v3 import UpdateRemoteIdRequestV3
from openapi_server.models.update_remote_id_request_v4 import UpdateRemoteIdRequestV4
from openapi_server import util


async def delete_payee_by_id_v3(request: web.Request, payee_id) -> web.Response:
    """Delete Payee by Id

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:&lt;/p&gt; &lt;p&gt;* Payee ID is not found&lt;/p&gt; &lt;p&gt;* If Payee has not been on-boarded&lt;/p&gt; &lt;p&gt;* If Payee is in grace period&lt;/p&gt; &lt;p&gt;* If Payee has existing payments&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str

    """
    return web.Response(status=200)


async def delete_payee_by_id_v4(request: web.Request, payee_id) -> web.Response:
    """Delete Payee by Id

    &lt;p&gt;This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:&lt;/p&gt; &lt;p&gt;* Payee ID is not found&lt;/p&gt; &lt;p&gt;* If Payee has not been on-boarded&lt;/p&gt; &lt;p&gt;* If Payee is in grace period&lt;/p&gt; &lt;p&gt;* If Payee has existing payments&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str

    """
    return web.Response(status=200)


async def get_payee_by_id_v3(request: web.Request, payee_id, sensitive=None) -> web.Response:
    """Get Payee by Id

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Get Payee by Id&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    return web.Response(status=200)


async def get_payee_by_id_v4(request: web.Request, payee_id, sensitive=None) -> web.Response:
    """Get Payee by Id

    Get Payee by Id

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
    :type sensitive: bool

    """
    return web.Response(status=200)


async def list_payee_changes_v3(request: web.Request, payor_id, updated_since, page=None, page_size=None) -> web.Response:
    """List Payee Changes

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Get a paginated response listing payee changes.&lt;/p&gt; 

    :param payor_id: The Payor ID to find associated Payees
    :type payor_id: str
    :type payor_id: str
    :param updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    :type updated_since: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: Page size. Default is 100. Max allowable is 1000.
    :type page_size: int

    """
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def list_payee_changes_v4(request: web.Request, payor_id, updated_since, page=None, page_size=None) -> web.Response:
    """List Payee Changes

    Get a paginated response listing payee changes (updated since a particular time) to a limited set of fields: - dbaName - displayName - email - onboardedStatus - payeeCountry - payeeId - remoteId 

    :param payor_id: The Payor ID to find associated Payees
    :type payor_id: str
    :type payor_id: str
    :param updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    :type updated_since: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: Page size. Default is 100. Max allowable is 1000.
    :type page_size: int

    """
    updated_since = util.deserialize_datetime(updated_since)
    return web.Response(status=200)


async def list_payees_v3(request: web.Request, payor_id, watchlist_status=None, disabled=None, onboarded_status=None, email=None, display_name=None, remote_id=None, payee_type=None, payee_country=None, page=None, page_size=None, sort=None) -> web.Response:
    """List Payees

    &lt;p&gt;Use v4 instead&lt;/p&gt; Get a paginated response listing the payees for a payor. 

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param watchlist_status: The watchlistStatus of the payees.
    :type watchlist_status: str
    :param disabled: Payee disabled
    :type disabled: bool
    :param onboarded_status: The onboarded status of the payees.
    :type onboarded_status: str
    :param email: Email address
    :type email: str
    :param display_name: The display name of the payees.
    :type display_name: str
    :param remote_id: The remote id of the payees.
    :type remote_id: str
    :param payee_type: The onboarded status of the payees.
    :type payee_type: str
    :param payee_country: The country of the payee - 2 letter ISO 3166-1 country code (upper case)
    :type payee_country: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: Page size. Default is 25. Max allowable is 100.
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus. 
    :type sort: str

    """
    return web.Response(status=200)


async def list_payees_v4(request: web.Request, payor_id, watchlist_status=None, disabled=None, onboarded_status=None, email=None, display_name=None, remote_id=None, payee_type=None, payee_country=None, ofac_status=None, page=None, page_size=None, sort=None) -> web.Response:
    """List Payees

    Get a paginated response listing the payees for a payor.

    :param payor_id: The account owner Payor ID
    :type payor_id: str
    :type payor_id: str
    :param watchlist_status: The watchlistStatus of the payees.
    :type watchlist_status: str
    :param disabled: Payee disabled
    :type disabled: bool
    :param onboarded_status: The onboarded status of the payees.
    :type onboarded_status: str
    :param email: Email address
    :type email: str
    :param display_name: The display name of the payees.
    :type display_name: str
    :param remote_id: The remote id of the payees.
    :type remote_id: str
    :param payee_type: The onboarded status of the payees.
    :type payee_type: str
    :param payee_country: The country of the payee - 2 letter ISO 3166-1 country code (upper case)
    :type payee_country: str
    :param ofac_status: The ofacStatus of the payees.
    :type ofac_status: str
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: Page size. Default is 25. Max allowable is 100.
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus. 
    :type sort: str

    """
    return web.Response(status=200)


async def payee_details_update_v3(request: web.Request, payee_id, body) -> web.Response:
    """Update Payee Details

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Update payee details for the given Payee Id.&lt;p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param body: Request to update payee details
    :type body: dict | bytes

    """
    body = UpdatePayeeDetailsRequestV3.from_dict(body)
    return web.Response(status=200)


async def payee_details_update_v4(request: web.Request, payee_id, body) -> web.Response:
    """Update Payee Details

    &lt;p&gt;Update payee details for the given Payee Id.&lt;/p&gt; &lt;p&gt;Payors may only update the payee details if the payee has not yet onboarded&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param body: Request to update payee details
    :type body: dict | bytes

    """
    body = UpdatePayeeDetailsRequestV4.from_dict(body)
    return web.Response(status=200)


async def v3_payees_payee_id_remote_id_update_post(request: web.Request, payee_id, body) -> web.Response:
    """Update Payee Remote Id

    &lt;p&gt;Use v4 instead&lt;/p&gt; &lt;p&gt;Update the remote Id for the given Payee Id.&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param body: Request to update payee remote id v3
    :type body: dict | bytes

    """
    body = UpdateRemoteIdRequestV3.from_dict(body)
    return web.Response(status=200)


async def v4_payees_payee_id_remote_id_update_post(request: web.Request, payee_id, body) -> web.Response:
    """Update Payee Remote Id

    &lt;p&gt;Update the remote Id for the given Payee Id.&lt;/p&gt; 

    :param payee_id: The UUID of the payee.
    :type payee_id: str
    :type payee_id: str
    :param body: Request to update payee remote id v4
    :type body: dict | bytes

    """
    body = UpdateRemoteIdRequestV4.from_dict(body)
    return web.Response(status=200)
