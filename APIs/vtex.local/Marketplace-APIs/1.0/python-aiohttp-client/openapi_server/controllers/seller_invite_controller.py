from typing import List, Dict
from aiohttp import web

from openapi_server.models.accept_seller_lead_request import AcceptSellerLeadRequest
from openapi_server.models.create_seller_lead_request import CreateSellerLeadRequest
from openapi_server.models.resend_seller_lead_request_request import ResendSellerLeadRequestRequest
from openapi_server import util


async def accept_seller_lead(request: web.Request, account_name, environment, seller_lead_id, accept, content_type, body) -> web.Response:
    """Accept Seller Lead

    This endpoint is triggered by the seller onboarding wizard, once the seller confirms their invitation. It can be used by marketplace operators to manually accept seller leads, and carry on with their onboarding process.   Note that there&#39;s no specific API call that allows status changes. The operations only allow the seller lead to move forward:    From &#x60;invite&#x60; &gt; to &#x60;Accept&#x60; &gt; closing on &#x60;Create Seller&#x60;.    If you want to change the status, you can start the process again, by deleting that lead through the *Delete Seller Lead* endpoint, and resending the invite through the *Resend Seller Lead&#39;s Invite* endpoint.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_lead_id: ID of the Seller Lead invited to the marketplace.
    :type seller_lead_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = AcceptSellerLeadRequest.from_dict(body)
    return web.Response(status=200)


async def create_seller_from_seller_lead(request: web.Request, account_name, environment, is_active, seller_lead_id, accept, content_type) -> web.Response:
    """Create Seller From Lead

    This endpoint is used by marketplace operators to create seller accounts. The request will only accept Seller Leads whose status is &#x60;accepted&#x60;. If they are already &#x60;connected&#x60; or &#x60;invited&#x60;, the call will not be fulfilled.   The creation of the account at VTEX is done by an internal Billing service. There is no seller account and marketplace affiliation if you do not go through this step.   Note that there&#39;s no specific API call that allows status changes. The operations only allow the seller lead to move forward:    From &#x60;invite&#x60; &gt; to &#x60;Accept&#x60; &gt; closing on &#x60;Create Seller&#x60;.    If you want to change the status, you can start the process again, by deleting that lead through the *Delete Seller Lead* endpoint, and resending the invite through the *Resend Seller Lead&#39;s Invite* endpoint.

    :param account_name: Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param is_active: Whether the Seller Lead is &#x60;active&#x60; or not in Seller Portal. This request only supports the value &#x60;false&#x60; in this field. If that´s not the case, the request will respond with an internal error.
    :type is_active: bool
    :param seller_lead_id: ID of the Seller Lead invited to the marketplace.
    :type seller_lead_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def create_seller_lead(request: web.Request, account_name, environment, accept, content_type, body) -> web.Response:
    """Invite Seller Lead

    This API is used by marketplace operators to invite sellers to join their marketplace. The request sends an email to the seller, inviting sellers to activate their store. The invitation&#39;s link in the email is unique per user, and available for only seven days for the seller to click and begin activating their store.   The email template is completely customizable. All email templates that VTEX sends to seller leads can be found and edited in the marketplace&#39;s VTEX Admin, on the Message Center section.

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSellerLeadRequest.from_dict(body)
    return web.Response(status=200)


async def list_seller_leads(request: web.Request, account_name, environment, offset, limit, is_connected, search, status, order_by, accept, content_type) -> web.Response:
    """List Seller Leads

    This call&#39;s response includes a list of all sellers invited by the marketplace operator to join them. Retrieved results can be filtered by adding optional query fields to the request. Each seller listed includes the following information:   - &#x60;id&#x60;   - &#x60;createdAt&#x60;   - &#x60;status&#x60;   - &#x60;isConnected&#x60;   - &#x60;sellerEmail&#x60;   - &#x60;sellerName&#x60;   - &#x60;salesChannel&#x60;   - &#x60;email&#x60;

    :param account_name: Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param offset: This field determines the limit used to retrieve the list of sellers. The response includes objects starting &#x60;from&#x60; the value inputted here.
    :type offset: int
    :param limit: This field determines the limit used to retrieve the list of sellers. The response includes objects until the value inputted here.            
    :type limit: int
    :param is_connected: Query param that enables results to be filter by whether the seller lead is already connected to the marketplace or not.
    :type is_connected: str
    :param search: Custom search field, that filters sellers invited by specific marketplace operator&#39;s  email.
    :type search: str
    :param status: Seller Lead&#39;s status. Includes &#x60;accepted&#x60;, &#x60;connected&#x60; or &#x60;invited&#x60;.
    :type status: str
    :param order_by: Query param determining how data will be ordered in the response, ordering by name or ID in descending our ascending order. Includes the following values:   &#x60;namesort&#x60; &#x3D; desc/asc   &#x60;idsort&#x60; &#x3D; desc/asc
    :type order_by: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def remove_seller_lead(request: web.Request, account_name, environment, seller_lead_id, accept, content_type) -> web.Response:
    """Delete Seller Lead

    This endpoint permanently deletes a seller previously invited to the marketplace, if the seller has not already accepted the invitation.

    :param account_name: Name of the VTEX account that belongs to the marketplace.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_lead_id: ID of the Seller Lead invited to the marketplace.
    :type seller_lead_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def resend_seller_lead_request(request: web.Request, account_name, environment, seller_lead_id, accept, content_type, body) -> web.Response:
    """Resend Seller Lead Invite

    This endpoint allows marketplace operators to resend an invitation to a seller lead, previously invited to join their marketplace. The request will only accept Seller Leads whose status is &#x60;invited&#x60;. If they are already &#x60;connected&#x60; or &#x60;accepted&#x60;, the call will not be fulfilled.

    :param account_name: Name of the VTEX account that belongs to the marketplace.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_lead_id: ID of the Seller Lead invited to the marketplace.
    :type seller_lead_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResendSellerLeadRequestRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_seller_lead(request: web.Request, account_name, environment, seller_lead_id, accept, content_type) -> web.Response:
    """Get Seller Lead&#39;s Data by Id

    Marketplace operators may call this endpoint to retrieve information about a specific seller invited to the Seller Portal, by searching through their &#x60;Seller Lead Id&#x60;. To know the chosen seller&#39;s &#x60;sellerLeadId&#x60;, marketplace operators can count on the *List Sellers* endpoint&#39;s response as well. Each seller listed includes the following information:   - &#x60;id&#x60;   - &#x60;createdAt&#x60;   - &#x60;status&#x60;   - &#x60;isConnected&#x60;   - &#x60;sellerEmail&#x60;   - &#x60;sellerName&#x60;   - &#x60;salesChannel&#x60;   - &#x60;email&#x60;

    :param account_name: Name of the VTEX account that belongs to the marketplace.
    :type account_name: str
    :param environment: Environment to use. Used as part of the URL.
    :type environment: str
    :param seller_lead_id: ID of the Seller Lead invited to the marketplace.
    :type seller_lead_id: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)
