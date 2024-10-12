from typing import List, Dict
from aiohttp import web

from openapi_server.models.save_suggestion_request import SaveSuggestionRequest
from openapi_server import util


async def delete_suggestion(request: web.Request, account_name, accept, content_type, seller_id, seller_sku_id) -> web.Response:
    """Delete SKU Suggestion

    This endpoint deletes a chosen SKU suggestion. Only one SKU should be deleted per request. This request cannot be undone. A workaround to revert its action, is to send the suggestion again, through the Send Suggestion API.

    :param account_name: Name of the VTEX account. Used as part of the URL.
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


async def save_suggestion(request: web.Request, account_name, accept, content_type, seller_id, seller_sku_id, body) -> web.Response:
    """Send SKU Suggestion

    This request is used by the seller when it wants to suggest that one of their SKUs is sold in the marketplace.  Before using this request, the seller should always use the [Change Notification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-seller-sku-notification) request in order to check if the SKU already exists in the marketplace. If it doesn&#39;t, then this is the next call in the SKU integration flow.  In the Send Suggestion request, the seller must send information about the SKU, such as the product and SKU name, the seller ID, and the image URL. All parameters are explained below. 

    :param account_name: Name of the VTEX account to which the seller wants to suggest a new SKU. It is used as part of the request URL.
    :type account_name: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param seller_id: A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
    :type seller_id: str
    :param seller_sku_id: A string that identifies the SKU in the seller. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
    :type seller_sku_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveSuggestionRequest.from_dict(body)
    return web.Response(status=200)
