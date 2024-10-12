from typing import List, Dict
from aiohttp import web

from openapi_server.models.bindtoanothersku_request import BindtoanotherskuRequest
from openapi_server.models.get_sk_useller200_response import GetSKUseller200Response
from openapi_server.models.getallby_seller_id200_response_inner import GetallbySellerId200ResponseInner
from openapi_server.models.getby_sku_id200_response_inner import GetbySkuId200ResponseInner
from openapi_server.models.getpagedadmin200_response import Getpagedadmin200Response
from openapi_server.models.insert_sku_binding_request import InsertSKUBindingRequest
from openapi_server import util


async def activate_sku_binding(request: web.Request, content_type, accept, seller_id, sku_seller_id) -> web.Response:
    """Activate SKU Binding

    Changes the status of an SKU Binding to active, setting &#x60;isActive&#x60; to &#x60;true&#x60;.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/activate/{sellerId}/{skuSellerId}&#x60;.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param sku_seller_id: SKU ID in the seller&#39;s store.
    :type sku_seller_id: str

    """
    return web.Response(status=200)


async def bindtoanothersku(request: web.Request, content_type, accept, seller_id, seller_sku_id, body=None) -> web.Response:
    """Bind a seller&#39;s SKU to another SKU

    Associates a seller&#39;s SKU to another marketplace SKU.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId}&#x60;.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;StockKeepingUnitId\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param seller_sku_id: SKU ID in the seller&#39;s store.
    :type seller_sku_id: str
    :param body: Request body
    :type body: dict | bytes

    """
    body = BindtoanotherskuRequest.from_dict(body)
    return web.Response(status=200)


async def change_notification(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Change Notification with SKU ID

    The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  The body of the request should be empty.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/changenotification/{skuId}&#x60;.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use to look for the SKU whose change the seller wants to inform. If the marketplace finds this ID, it responds with status code &#x60;200&#x60;. Otherwise, it responds with status code &#x60;404&#x60;.
    :type sku_id: str

    """
    return web.Response(status=200)


async def deactivate_sku_binding(request: web.Request, content_type, accept, seller_id, sku_seller_id) -> web.Response:
    """Deactivate SKU Binding

    Changes the status of an SKU Binding to inactive, setting &#x60;isActive&#x60; to &#x60;false&#x60;.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/inactivate/{sellerId}/{skuSellerId}&#x60;.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param sku_seller_id: SKU ID in the seller&#39;s store.
    :type sku_seller_id: str

    """
    return web.Response(status=200)


async def delete_sk_usellerassociation(request: web.Request, content_type, accept, seller_id, seller_sku_id) -> web.Response:
    """Remove a seller&#39;s SKU Binding

    Remove a seller&#39;s SKU binding, given the Seller ID and the SKU ID in the seller&#39;s store.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/remove/{sellerId}/{sellerSkuId}&#x60;.

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

    Retrieves the details of a seller&#39;s SKU given a seller ID and the SKU ID in the seller&#39;s store.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId}&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;IsPersisted\&quot;: true,      \&quot;IsRemoved\&quot;: false,      \&quot;SkuSellerId\&quot;: 102,      \&quot;UpdateDate\&quot;: \&quot;2021-04-12T20:06:59.413Z\&quot;,      \&quot;RequestedUpdateDate\&quot;: null,      \&quot;SellerStockKeepingUnitId\&quot;: \&quot;71\&quot;,      \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

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


async def getallby_seller_id(request: web.Request, content_type, accept, seller_id) -> web.Response:
    """Get all SKU Bindings by Seller ID

    Retrieves a list of SKU Bindings given a specific Seller ID.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/list/bysellerId/{sellerId}&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;24\&quot;,          \&quot;FreightCommissionPercentage\&quot;: null,          \&quot;ProductCommissionPercentage\&quot;: null,          \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,          \&quot;StockKeepingUnitId\&quot;: 121,          \&quot;IsActive\&quot;: true      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str

    """
    return web.Response(status=200)


async def getby_sku_id(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Get SKU Bindings by SKU ID

    Retrieves SKU Bindings details by SKU ID.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 48,          \&quot;SellerId\&quot;: \&quot;cosmetics1\&quot;,          \&quot;StockKeepingUnitId\&quot;: 1,          \&quot;SellerSkuId\&quot;: \&quot;42\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;LastUpdateDate\&quot;: \&quot;2020-10-21T19:13:00.657\&quot;,          \&quot;SalesPolicy\&quot;: 0      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU&#39;s unique identifier in the marketplace.
    :type sku_id: str

    """
    return web.Response(status=200)


async def getpagedadmin(request: web.Request, content_type, accept, seller_id=None, sku_id=None, seller_sku_id=None, is_active=None, size=None) -> web.Response:
    """Get SKU Bindings information

    Retrieves SKU Bindings administrative information using optional query params &#x60;sellerId&#x60;, &#x60;skuId&#x60;, &#x60;sellerSkuId&#x60; and &#x60;IsActive&#x60; to filter results and &#x60;size&#x60; to restrict the amount of results.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/admin&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;IsPersisted\&quot;: true,          \&quot;IsRemoved\&quot;: false,          \&quot;SkuSellerId\&quot;: 1,          \&quot;UpdateDate\&quot;: \&quot;2019-12-04T01:56:00.673Z\&quot;,          \&quot;RequestedUpdateDate\&quot;: null,          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;12\&quot;,          \&quot;SellerId\&quot;: \&quot;cosmetics1\&quot;,          \&quot;StockKeepingUnitId\&quot;: 25,          \&quot;IsActive\&quot;: true      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str
    :param sku_id: SKU&#39;s unique identifier in the marketplace.
    :type sku_id: str
    :param seller_sku_id: SKU ID in the seller&#39;s store.
    :type seller_sku_id: str
    :param is_active: Defines if the SKU binding is active.
    :type is_active: bool
    :param size: Amount of results.
    :type size: str

    """
    return web.Response(status=200)


async def getpagedby_seller_id(request: web.Request, page, size, content_type, accept, seller_id) -> web.Response:
    """Get paged SKU Bindings by Seller ID

    Retrieves a paged list of SKU Bindings given a specific Seller ID.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/paged/sellerid/{sellerId}&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,          \&quot;StockKeepingUnitId\&quot;: 121,          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;24\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;FreightCommissionPercentage\&quot;: null,          \&quot;ProductCommissionPercentage\&quot;: null      },      {          \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,          \&quot;StockKeepingUnitId\&quot;: 14,          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;60\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;FreightCommissionPercentage\&quot;: null,          \&quot;ProductCommissionPercentage\&quot;: null      }  ]  &#x60;&#x60;&#x60;

    :param page: Page number.
    :type page: str
    :param size: Amount of results per page.
    :type size: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param seller_id: ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    :type seller_id: str

    """
    return web.Response(status=200)


async def insert_sku_binding(request: web.Request, content_type, accept, body) -> web.Response:
    """Insert SKU Binding

    Creates an SKU Binding, associating a seller&#39;s SKU with a marketplace&#39;s SKU.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/insertion&#x60;.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: Request body
    :type body: dict | bytes

    """
    body = InsertSKUBindingRequest.from_dict(body)
    return web.Response(status=200)


async def sku_binding_pvt_skuseller_changenotification_seller_id_seller_sku_id_post(request: web.Request, content_type, accept, seller_id, seller_sku_id) -> web.Response:
    """Change Notification with Seller ID and Seller SKU ID

    The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  There are two information expected by the marketplace in this request: the &#x60;sellerId&#x60;, which identifies the seller, and the &#x60;sellerSkuId&#x60;, which identifies the binding of the seller with the SKU.  Both information are passed through the request URL. The body of the request should be empty.   &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId}&#x60;.    ## Example    Let&#39;s say your seller has the ID &#x60;123&#x60; in the marketplace and you want to inform the marketplace that has been a change in the SKU with ID &#x60;700&#x60;.    In this case, you would have to replace the &#x60;sellerId&#x60; parameter with the value &#x60;123&#x60; and the &#x60;skuId&#x60; parameter with the value &#x60;700&#x60;. The URL of the request would be the following.    &#x60;&#x60;&#x60;  https://{{accountName}}.vtexcommercestable.com.br/api/sku-binding/pvt/skuseller/changenotification/123/700  &#x60;&#x60;&#x60;    ## Response codes    The following response codes are possible for this request.  * 200: the SKU whose ID was informed in the URL already exists in the marketplace and was found. The marketplace can now proceed with a fulfillment simulation in order to get updated information about this SKU&#39;s inventory and price.  * 403: Failure in the authentication.  * 404: the SKU was not found in the marketplace. The body of the response, in this case, should follow this format: \&quot;Seller StockKeepingUnit &#x60;{{skuId}}&#x60; not found for this seller id &#x60;{{sellerId}}&#x60;. This means that the seller can now proceed with sending an offer to the marketplace in order to suggest that this SKU is sold there.  * 429: Failure due to too many requests.

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
