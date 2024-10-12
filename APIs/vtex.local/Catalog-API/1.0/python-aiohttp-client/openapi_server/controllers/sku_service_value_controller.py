from typing import List, Dict
from aiohttp import web

from openapi_server.models.sku_service_value_request import SKUServiceValueRequest
from openapi_server.models.sku_service_value_response import SKUServiceValueResponse
from openapi_server import util


async def api_catalog_pvt_skuservicevalue_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create SKU Service Value

    Creates an SKU Service Value for an existing SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SKUServiceValueRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_skuservicevalue_sku_service_value_id_delete(request: web.Request, content_type, accept, sku_service_value_id) -> web.Response:
    """Delete SKU Service Value

    Deletes an existing SKU Service Value.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_value_id: SKU Service Value unique identifier.
    :type sku_service_value_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservicevalue_sku_service_value_id_get(request: web.Request, content_type, accept, sku_service_value_id) -> web.Response:
    """Get SKU Service Value

    Retrieves an existing SKU Service Value.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_value_id: SKU Service Value unique identifier.
    :type sku_service_value_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservicevalue_sku_service_value_id_put(request: web.Request, content_type, accept, sku_service_value_id, body=None) -> web.Response:
    """Update SKU Service Value

    Updates an existing SKU Service Value.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;SkuServiceTypeId\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test ServiceValue API\&quot;,      \&quot;Value\&quot;: 10.5,      \&quot;Cost\&quot;: 10.5  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_value_id: SKU Service Value unique identifier.
    :type sku_service_value_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SKUServiceValueRequest.from_dict(body)
    return web.Response(status=200)
