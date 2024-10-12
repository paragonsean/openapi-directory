from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_skuattachment_post200_response import ApiCatalogPvtSkuattachmentPost200Response
from openapi_server.models.associateattachmentsto_sku_request import AssociateattachmentstoSKURequest
from openapi_server.models.request_body1 import RequestBody1
from openapi_server import util


async def api_catalog_pvt_skuattachment_delete(request: web.Request, content_type, accept, sku_id=None, attachment_id=None) -> web.Response:
    """Dissociate attachments and SKUs

    Dissociates attachments and SKUs based on an SKU ID or an attachment ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU ID. By using this query param, you can dissociate all the attachments from an SKU based on its SKU ID.
    :type sku_id: int
    :param attachment_id: Attachment ID. By using this query param, you can dissociate the given attachment from all previously associated SKUs.
    :type attachment_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_skuattachment_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Associate SKU Attachment

    Associates an existing SKU to an existing Attachment.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuId\&quot;: 7  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 31,      \&quot;AttachmentId\&quot;: 1,      \&quot;SkuId\&quot;: 7  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody1.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_skuattachment_sku_attachment_association_id_delete(request: web.Request, content_type, accept, sku_attachment_association_id) -> web.Response:
    """Delete SKU Attachment by Attachment Association ID

    Deletes the association of an SKU to an Attachment.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_attachment_association_id: ID of the association between the attachment and the SKU, which corresponds to the &#x60;Id&#x60; in the response body of the [Associate SKU Attachment](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-post-sku-attachment) and the [Get SKU Attachment by SKU ID](https://developers.vtex.com/vtex-rest-api/reference/get_api-catalog-pvt-stockkeepingunit-skuid-attachment) endpoints.
    :type sku_attachment_association_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_attachment_get(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Get SKU Attachments by SKU ID

    Retrieves existing SKU Attachments by SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 97,          \&quot;AttachmentId\&quot;: 1,          \&quot;SkuId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU unique identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def associateattachmentsto_sku(request: web.Request, content_type, accept, body) -> web.Response:
    """Associate attachments to an SKU

    Associates attachments to an SKU based on a given SKU ID and attachment names.  This request removes existing SKU attachment associations and recreates the associations with the attachments being sent.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1,      \&quot;AttachmentNames\&quot;: [          \&quot;T-Shirt Customization\&quot;      ]  }  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = AssociateattachmentstoSKURequest.from_dict(body)
    return web.Response(status=200)
