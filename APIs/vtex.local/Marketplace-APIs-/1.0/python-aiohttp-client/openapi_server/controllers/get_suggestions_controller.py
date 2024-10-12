from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_suggestion(request: web.Request, account_name, accept, content_type, seller_id, seller_sku_id) -> web.Response:
    """Get SKU Suggestion by ID

    This endpoint retrieves the data of a specific SKU sent by the seller, to the marketplace. Marketplaces or external matchers can call this endpoint when they want to check the information about a single SKU.   Note that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint&#39;s response is given by the Matcher.   Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param seller_sku_id: A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    :type seller_sku_id: str

    """
    return web.Response(status=200)


async def getsuggestions(request: web.Request, account_name, accept, content_type, q=None, type=None, seller=None, status=None, hasmapping=None, matcherid=None, _from=None, to=None) -> web.Response:
    """Get all SKU suggestions

    This endpoint retrieves a list of all SKUs sent by the seller for the Marketplace&#39;s approval. Marketplace operators should use this endpoint whenever they want to check the full list of received SKUs and their  information.   Note that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint&#39;s response is given by the Matcher.   Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param q: This field allows you to customize your search. You can fill in this query param if you want to narrow down your search using the available filters on Received SKU modules.
    :type q: str
    :param type: This field allows users to filter SKU suggestions, by searching only the new suggestions that were just sent, and suggestions that have already been sent, but were updated. Possible values for this field include &#x60;new&#x60; and &#x60;update&#x60;.
    :type type: str
    :param seller: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller so it can call this endpoint.
    :type seller: str
    :param status: Narrow down you search, filtering by status. Values allowed on this field include: &#x60;accepted&#x60;, &#x60;pending&#x60; and &#x60;denied.&#x60;
    :type status: str
    :param hasmapping: This field allows you to filter SKUs that have mapping or not. Insert &#x60;true&#x60; to filter SKUs that have mapping, or &#x60;false&#x60; to retrieve SKUs that aren&#39;t mapped.
    :type hasmapping: str
    :param matcherid: Identifies the matching entity. It can be either VTEX&#39;s matcher, or an external matcher developed by partners, for example. The &#x60;matcherId&#x60;&#39;s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint.
    :type matcherid: str
    :param _from: Define your pagination range, by adding the pagination starting value. Values should be bigger than 0, with a maximum of 50 records per page.
    :type _from: int
    :param to: Define your pagination range, by adding the pagination ending value. Values should be bigger than 0, with a maximum of 50 records per page.
    :type to: int

    """
    return web.Response(status=200)
