from typing import List, Dict
from aiohttp import web

from openapi_server.models.match_request import MatchRequest
from openapi_server import util


async def match(request: web.Request, account_name, accept, content_type, seller_id, sellerskuid, version, matchid, body) -> web.Response:
    """Match Received SKUs individually

    All SKUs sent from a seller to a marketplace must be reviewed and matched. Actions in the matching process are added in the request body through the [matchType] object. Match type actions include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;itemMatch&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productMatch&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.   5. &#x60;pending&#x60;: the received SKU requires attention.   6. &#x60;incomplete&#x60;: the received SKU is lacking information to be matched.   7. &#x60;insufficientScore&#x60;: the score given by the Matcher to this received SKU doesn&#39;t qualify it to be matched.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param sellerskuid: A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    :type sellerskuid: str
    :param version: Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the versionId associated to the version you choose to search for. You can get this field&#39;s value through the[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the &#x60;latestVersionId&#x60; field.
    :type version: str
    :param matchid: Whenever an SKU suggestion is matched, it is associated to a unique ID. Fill in this field with the matchId you wish to filter by. The &#x60;matchId&#x60;&#39;s value can be obtained through the *[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint.
    :type matchid: str
    :param body: 
    :type body: dict | bytes

    """
    body = MatchRequest.from_dict(body)
    return web.Response(status=200)


async def match_multiple(request: web.Request, account_name, content_type, accept, action_name, body) -> web.Response:
    """Match Multiple Received SKUs

    This endpoint allows the user to bulk approve, deny, or associate received SKUs. In a single request, you can match up to 25 received SKUs from your sellers.  Through the &#x60;actionName&#x60; attribute you can select the operation you want to apply to the received SKU.   Actions include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;skuassociation&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productassociation&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param action_name: This field refers to the operation you choose to apply to received SKUs. Values include: newproduct, skuassociation, productassociation or deny.
    :type action_name: str
    :param body: 
    :type body: List[]

    """
    return web.Response(status=200)
