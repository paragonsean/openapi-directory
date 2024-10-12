from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body3 import RequestBody3
from openapi_server.models.request_body4 import RequestBody4
from openapi_server.models.sku_service import SKUService
from openapi_server import util


async def api_catalog_pvt_skuservice_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Associate SKU Service

    Associates an SKU Service to an SKU.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody3.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_skuservice_sku_service_id_delete(request: web.Request, content_type, accept, sku_service_id) -> web.Response:
    """Dissociate SKU Service

    Dissociates an SKU Service from an SKU.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_id: SKU Service unique identifier.
    :type sku_service_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservice_sku_service_id_get(request: web.Request, content_type, accept, sku_service_id) -> web.Response:
    """Get SKU Service

    Retrieves an SKU Service.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1,      \&quot;SkuServiceValueId\&quot;: 1,      \&quot;SkuId\&quot;: 1,      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_id: SKU Service unique identifier.
    :type sku_service_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservice_sku_service_id_put(request: web.Request, content_type, accept, sku_service_id, body=None) -> web.Response:
    """Update SKU Service

    Updates an SKU Service.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1,      \&quot;SkuServiceValueId\&quot;: 1,      \&quot;SkuId\&quot;: 1,      \&quot;Name\&quot;: \&quot;name\&quot;,      \&quot;Text\&quot;: \&quot;text\&quot;,      \&quot;IsActive\&quot;: false  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_id: SKU Service unique identifier.
    :type sku_service_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody4.from_dict(body)
    return web.Response(status=200)
