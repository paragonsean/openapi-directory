from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_sk_useller200_response import GetSKUseller200Response
from openapi_server import util


async def api_catalog_system_pvt_skuseller_changenotification_seller_id_seller_sku_id_post(request: web.Request, content_type, accept, seller_id, seller_sku_id) -> web.Response:
    """Change Notification with Seller ID and Seller SKU ID

     &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  There are two information expected by the marketplace in this request: the &#x60;sellerId&#x60;, which identifies the seller, and the &#x60;sellerSkuId&#x60;, which identifies the binding of the seller with the SKU.  Both information are passed through the request URL. The body of the request should be empty.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param seller_sku_id: ID of the binding of the seller with the SKU.
    :type seller_sku_id: str

    """
    return web.Response(status=200)


async def change_notification(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Change Notification with SKU ID

     &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  The body of the request should be empty.  ## Example    Let&#39;s say your seller has the ID &#x60;123&#x60; in the marketplace and you want to inform the marketplace that has been a change in the SKU with ID &#x60;700&#x60;.    In this case, you would have to replace the &#x60;sellerId&#x60; parameter with the value &#x60;123&#x60; and the &#x60;skuId&#x60; parameter with the value &#x60;700&#x60;. The URL of the request would be the following.    &#x60;&#x60;&#x60;  https://{{accountName}}.vtexcommercestable.com.br/api/catalog_system/pvt/skuseller/changenotification/123/700  &#x60;&#x60;&#x60;    ## Response codes    The following response codes are possible for this request.    * 404: the SKU was not found in the marketplace. The body of the response, in this case, should follow this format: \&quot;Seller StockKeepingUnit &#x60;{{skuId}}&#x60; not found for this seller id &#x60;{{sellerId}}&#x60;\&quot;. This means that the seller can now proceed with sending an offer to the marketplace in order to suggest that this SKU is sold there.  * 200: the SKU whose ID was informed in the URL already exists in the marketplace and was found. The marketplace can now proceed with a fulfillment simulation in order to get updated information about this SKU&#39;s inventory and price.  * 429 - Failure due to too many requests.  * 403 - Failure in the authentication.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use to look for the SKU whose change the seller wants to inform. If the marketplace finds this ID, it responds with status code 200. Otherwise, it responds with status code 404.
    :type sku_id: str

    """
    return web.Response(status=200)


async def delete_sk_usellerassociation(request: web.Request, content_type, accept, seller_id, seller_sku_id) -> web.Response:
    """Remove a seller&#39;s SKU binding

     &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  Remove a seller&#39;s SKU binding, given the seller ID and the SKU ID in the seller&#39;s store.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param seller_sku_id: SKU ID in the seller&#39;s store.
    :type seller_sku_id: str

    """
    return web.Response(status=200)


async def get_sk_useller(request: web.Request, content_type, accept, seller_id, seller_sku_id) -> web.Response:
    """Get details of a seller&#39;s SKU

     &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  Retrieves the details of a seller&#39;s SKU given a seller ID and the SKU ID in the seller&#39;s store.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;IsPersisted\&quot;: true,      \&quot;IsRemoved\&quot;: false,      \&quot;SkuSellerId\&quot;: 799,      \&quot;SellerId\&quot;: \&quot;myseller\&quot;,      \&quot;StockKeepingUnitId\&quot;: 50,      \&quot;SellerStockKeepingUnitId\&quot;: \&quot;502\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;UpdateDate\&quot;: \&quot;2018-10-11T04:52:42.1\&quot;,      \&quot;RequestedUpdateDate\&quot;: null  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param seller_sku_id: SKU ID in the seller&#39;s store.
    :type seller_sku_id: str

    """
    return web.Response(status=200)
