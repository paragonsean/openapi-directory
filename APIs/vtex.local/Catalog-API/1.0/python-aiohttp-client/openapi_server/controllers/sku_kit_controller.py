from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body9 import RequestBody9
from openapi_server.models.sku_kit import SkuKit
from openapi_server import util


async def api_catalog_pvt_stockkeepingunitkit_delete(request: web.Request, content_type, accept, sku_id=None, parent_sku_id=None) -> web.Response:
    """Delete SKU Kit by SKU ID or Parent SKU ID

    Deletes all Kit’s components based on the Parent SKU ID or deletes a specific Kit’s component based on the SKU ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param parent_sku_id: Parent SKU’s unique numerical identifier.
    :type parent_sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunitkit_get(request: web.Request, content_type, accept, sku_id=None, parent_sku_id=None) -> web.Response:
    """Get SKU Kit by SKU ID or Parent SKU ID

    Retrieves general information about the components of an SKU Kit by SKU ID or Parent SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 7,      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param parent_sku_id: Parent SKU’s unique numerical identifier.
    :type parent_sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunitkit_kit_id_delete(request: web.Request, content_type, accept, kit_id) -> web.Response:
    """Delete SKU Kit by KitId

    Deletes a specific Kit’s component based on its Kit ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param kit_id: Kit’s unique numerical identifier.
    :type kit_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunitkit_kit_id_get(request: web.Request, content_type, accept, kit_id) -> web.Response:
    """Get SKU Kit

    Retrieves general information about a component of a Kit.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param kit_id: Kit’s unique numerical identifier
    :type kit_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunitkit_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create SKU Kit

    Adds a component to a specific Kit.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 7,      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody9.from_dict(body)
    return web.Response(status=200)
