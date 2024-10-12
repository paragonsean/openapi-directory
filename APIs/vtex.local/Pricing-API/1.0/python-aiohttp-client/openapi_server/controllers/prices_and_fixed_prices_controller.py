from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update_price_or_fixed_price_request import CreateUpdatePriceOrFixedPriceRequest
from openapi_server.models.createorupdatefixedpricesonpricetableortradepolicy_request_inner import CreateorupdatefixedpricesonpricetableortradepolicyRequestInner
from openapi_server.models.fixed_price import FixedPrice
from openapi_server.models.getcomputedprice import Getcomputedprice
from openapi_server.models.getprice import Getprice
from openapi_server import util


async def create_update_price_or_fixed_price(request: web.Request, accept, content_type, item_id, body=None) -> web.Response:
    """Create or Update Base Price or Fixed Prices

    Creates or updates an SKU Base Price or Fixed Prices. The **base price** is the basic selling price of a product, it comprises the cost price and the markup wanted in the sale of the product. The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated.     &lt;p&gt; You may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula &lt;code&gt;costPrice * (1 + markup) &#x3D; basePrice&lt;/code&gt;.&lt;/p&gt; &lt;h2&gt;Request body example&lt;/h2&gt;    &#x60;&#x60;&#x60;json  {      \&quot;markup\&quot;: 30,      \&quot;basePrice\&quot;: 100,      \&quot;listPrice\&quot;: 35,      \&quot;fixedPrices\&quot;: [          {              \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,              \&quot;value\&quot;: 31,              \&quot;listPrice\&quot;: 32,              \&quot;minQuantity\&quot;: 1,              \&quot;dateRange\&quot;: {                  \&quot;from\&quot;: \&quot;2022-05-21T22:00:00Z\&quot;,                  \&quot;to\&quot;: \&quot;2023-05-28T22:00:00Z\&quot;              }          },          {              \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,              \&quot;value\&quot;: 31.5,              \&quot;listPrice\&quot;: 33,              \&quot;minQuantity\&quot;: 2          }      ]  }  &#x60;&#x60;&#x60;

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param item_id: SKU unique identifier number.
    :type item_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUpdatePriceOrFixedPriceRequest.from_dict(body)
    return web.Response(status=200)


async def createorupdatefixedpricesonpricetableortradepolicy(request: web.Request, content_type, accept, item_id, price_table_id, body=None) -> web.Response:
    """Create or Update Fixed Prices on a price table or trade policy

    Creates or updates the fixed prices of an SKU for a specific price table or trade policy. You can add one or multiple fixed prices per SKU.     ## Request body example    &#x60;&#x60;&#x60;json  [    {      \&quot;value\&quot;: 50.5,      \&quot;listPrice\&quot;: 50.5,      \&quot;minQuantity\&quot;: 2,      \&quot;dateRange\&quot;: {        \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,        \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-04:00\&quot;      }    }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param item_id: SKU ID.
    :type item_id: int
    :param price_table_id: SKU **price table** name or **trade policy** ID.
    :type price_table_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [CreateorupdatefixedpricesonpricetableortradepolicyRequestInner.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_price(request: web.Request, content_type, accept, item_id) -> web.Response:
    """Delete Price

    Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param item_id: SKU ID.
    :type item_id: int

    """
    return web.Response(status=200)


async def deletefixedpricesonapricetableortradepolicy(request: web.Request, content_type, accept, item_id, price_table_id) -> web.Response:
    """Delete Fixed Prices on a price table or trade policy

    Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param item_id: SKU ID.
    :type item_id: int
    :param price_table_id: Price Table or Trade Policy Name.
    :type price_table_id: str

    """
    return web.Response(status=200)


async def get_computed_pricebypricetable(request: web.Request, category_ids, brand_id, quantity, content_type, accept, item_id, price_table_id) -> web.Response:
    """Get Computed Price by price table or trade policy

    Gets the Computed Price, which is the price after all the steps in the Pricing pipeline, for an SKU in a specific price table or trade policy.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,      \&quot;listPrice\&quot;: 30,      \&quot;costPrice\&quot;: 76.92,      \&quot;sellingPrice\&quot;: 18.9,      \&quot;priceValidUntil\&quot;: \&quot;2018-12-20T18:12:14Z\&quot;  }  &#x60;&#x60;&#x60;

    :param category_ids: Category ID.
    :type category_ids: int
    :param brand_id: Brand ID.
    :type brand_id: int
    :param quantity: SKU quantity.
    :type quantity: int
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param item_id: SKU ID.
    :type item_id: int
    :param price_table_id: SKU Price Table Name.
    :type price_table_id: str

    """
    return web.Response(status=200)


async def get_fixed_prices(request: web.Request, accept, content_type, item_id) -> web.Response:
    """Get Fixed Prices

    The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated. This method retrieves an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities.     The default value for a Minimum Quantity is &#x60;1&#x60;. This means a Fixed Price will be valid for a SKU in a Trade Policy for orders containing the specified number of Minimum Quantity or above, unless a higher Minimum Quantity is specified.     Fixed prices may, optionally, be scheduled. If so, these objects will contain the &#x60;dateRange&#x60; object with &#x60;from&#x60; and &#x60;to&#x60; properties, indicating the start and end time of the scheduled fixed price in the RFC3339 timestamp format (&#x60;YYYY-MM-DDT23:59:60Z&#x60;).     Note that the &#39;Z&#39;, at the end, represents the UTC time (GMT+00:00). If it was in GMT-03:00, for example, it would be (&#x60;YYYY-MM-DDT23:59:60-03:00&#x60;).     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;6\&quot;,          \&quot;value\&quot;: 20.9,          \&quot;listPrice\&quot;: 22.9,          \&quot;minQuantity\&quot;: 1,          \&quot;dateRange\&quot;: {              \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,              \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;          }      },      {          \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,          \&quot;value\&quot;: 18.9,          \&quot;listPrice\&quot;: null,          \&quot;minQuantity\&quot;: 1,          \&quot;dateRange\&quot;: {              \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,              \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;          }      }  ]  &#x60;&#x60;&#x60;

    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param item_id: SKU ID.
    :type item_id: int

    """
    return web.Response(status=200)


async def get_fixed_pricesonapricetable(request: web.Request, content_type, accept, item_id, price_table_id) -> web.Response:
    """Get Fixed Prices on a price table or trade policy

    Retrieves all Fixed Prices on a price table or trade policy.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;6\&quot;,          \&quot;value\&quot;: 20.9,          \&quot;listPrice\&quot;: 22.9,          \&quot;minQuantity\&quot;: 1,          \&quot;dateRange\&quot;: {              \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,              \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-04:00\&quot;          }      },      {          \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,          \&quot;value\&quot;: 18.9,          \&quot;listPrice\&quot;: null,          \&quot;minQuantity\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: 
    :type accept: str
    :param item_id: SKU ID.
    :type item_id: int
    :param price_table_id: Price Table Name
    :type price_table_id: str

    """
    return web.Response(status=200)


async def get_price(request: web.Request, content_type, accept, item_id) -> web.Response:
    """Get Price

    Retrieves price data given a specific SKU ID. Within the &#x60;fixedPrices&#x60; object, there might be a list of prices for specific Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;itemId\&quot;: \&quot;1\&quot;,      \&quot;listPrice\&quot;: 50,      \&quot;costPrice\&quot;: 90,      \&quot;markup\&quot;: 30,      \&quot;basePrice\&quot;: 117,      \&quot;fixedPrices\&quot;: [          {              \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,              \&quot;value\&quot;: 50.5,              \&quot;listPrice\&quot;: 50.5,              \&quot;minQuantity\&quot;: 2,              \&quot;dateRange\&quot;: {                  \&quot;from\&quot;: \&quot;2021-12-31T01:00:00Z\&quot;,                  \&quot;to\&quot;: \&quot;2022-12-31T01:00:00Z\&quot;              }          },          {              \&quot;tradePolicyId\&quot;: \&quot;2\&quot;,              \&quot;value\&quot;: 30,              \&quot;listPrice\&quot;: 50,              \&quot;minQuantity\&quot;: 2          }      ]  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param item_id: SKU ID.
    :type item_id: int

    """
    return web.Response(status=200)
