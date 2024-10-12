from typing import List, Dict
from aiohttp import web

from openapi_server.models.sku_service_type_request import SKUServiceTypeRequest
from openapi_server.models.sku_service_type_response import SKUServiceTypeResponse
from openapi_server import util


async def api_catalog_pvt_skuservicetype_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create SKU Service Type

    Creates a new SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Test API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Teste API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = SKUServiceTypeRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_skuservicetype_sku_service_type_id_delete(request: web.Request, content_type, accept, sku_service_type_id) -> web.Response:
    """Delete SKU Service Type

    Deletes an existing SKU Service Type.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_type_id: SKU Service Type unique identifier.
    :type sku_service_type_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservicetype_sku_service_type_id_get(request: web.Request, content_type, accept, sku_service_type_id) -> web.Response:
    """Get SKU Service Type

    Retrieves information about an existing SKU Service Type.   ## Response body example:    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Test API SKU Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_type_id: SKU Service Type unique identifier.
    :type sku_service_type_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservicetype_sku_service_type_id_put(request: web.Request, content_type, accept, sku_service_type_id, body=None) -> web.Response:
    """Update SKU Service Type

    Updates an existing SKU Service Type.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Test API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 2,      \&quot;Name\&quot;: \&quot;Teste API Sku Services\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ShowOnProductFront\&quot;: true,      \&quot;ShowOnCartFront\&quot;: true,      \&quot;ShowOnAttachmentFront\&quot;: true,      \&quot;ShowOnFileUpload\&quot;: true,      \&quot;IsGiftCard\&quot;: true,      \&quot;IsRequired\&quot;: true  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_type_id: SKU Service Type unique identifier.
    :type sku_service_type_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SKUServiceTypeRequest.from_dict(body)
    return web.Response(status=200)
