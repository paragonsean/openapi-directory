from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_product_id_salespolicy_get200_response_inner import ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner
from openapi_server import util


async def api_catalog_pvt_product_product_id_salespolicy_get(request: web.Request, content_type, accept, product_id) -> web.Response:
    """Get Trade Policies by Product ID

    Retrieves a list of Trade Policies associated to a Product based on the Product&#39;s ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 2      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 3      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 4      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_product_product_id_salespolicy_tradepolicy_id_delete(request: web.Request, content_type, accept, product_id, tradepolicy_id) -> web.Response:
    """Remove Product from Trade Policy

    Disassociates a Trade Policy of a Product.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param tradepolicy_id: Trade Policy’s unique numerical identifier.
    :type tradepolicy_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_product_product_id_salespolicy_tradepolicy_id_post(request: web.Request, content_type, accept, product_id, tradepolicy_id) -> web.Response:
    """Associate Product with Trade Policy

    Associates an existing Trade Policy with a Product.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param tradepolicy_id: Trade Policy’s unique numerical identifier.
    :type tradepolicy_id: int

    """
    return web.Response(status=200)


async def api_catalog_system_pvt_sku_stockkeepingunitidsbysaleschannel_get(request: web.Request, content_type, accept, sc, page=None, page_size=None, only_assigned=None) -> web.Response:
    """List all SKUs of a Trade Policy

    Retrieves a list of SKU IDs of a Trade Policy.   ## Response body example    &#x60;&#x60;&#x60;json  [      405380,      405381,      405382,      405383,      405384,      405385,      405386,      405387,      405388,      405389,      405390,      405391,      405392,      405393,      405394,      405395,      405396,      405397,      405398,      405399,      405400,      405556  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sc: Trade Policy’s unique numerical identifier.
    :type sc: int
    :param page: Page number.
    :type page: int
    :param page_size: Number of items in the page.
    :type page_size: int
    :param only_assigned: If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned.
    :type only_assigned: bool

    """
    return web.Response(status=200)
