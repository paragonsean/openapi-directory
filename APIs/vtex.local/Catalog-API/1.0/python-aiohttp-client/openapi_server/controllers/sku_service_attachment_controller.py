from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_skuservicetypeattachment_post200_response import ApiCatalogPvtSkuservicetypeattachmentPost200Response
from openapi_server.models.request_body5 import RequestBody5
from openapi_server import util


async def api_catalog_pvt_skuservicetypeattachment_delete(request: web.Request, content_type, accept, attachment_id=None, sku_service_type_id=None) -> web.Response:
    """Dissociate Attachment by Attachment ID or SKU Service Type ID

    Dissociates an Attachment by its Attachment ID or SKU Service Type ID from an SKU Service Type.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param attachment_id: SKU Service Attachment unique identifier.
    :type attachment_id: int
    :param sku_service_type_id: SKU Service Type unique identifier.
    :type sku_service_type_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuservicetypeattachment_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Associate SKU Service Attachment

    Associates an Attachment for an existing SKU Service Type.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuServiceTypeId\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody5.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_skuservicetypeattachment_sku_service_type_attachment_id_delete(request: web.Request, content_type, accept, sku_service_type_attachment_id) -> web.Response:
    """Dissociate Attachment from SKU Service Type

    Dissociates an Attachment from an SKU Service Type

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_service_type_attachment_id: SKU Service Attachment unique identifier.
    :type sku_service_type_attachment_id: int

    """
    return web.Response(status=200)
