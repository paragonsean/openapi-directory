from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_sk_ucomplementsbytype200_response import GetSKUcomplementsbytype200Response
from openapi_server.models.request_body2 import RequestBody2
from openapi_server.models.sku_complement_inner import SkuComplementInner
from openapi_server import util


async def create_sku_complement(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create SKU Complement

    Creates a new SKU Complement on a Parent SKU.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody2.from_dict(body)
    return web.Response(status=200)


async def delete_sku_complementby_sku_complement_id(request: web.Request, content_type, accept, sku_complement_id) -> web.Response:
    """Delete SKU Complement by SKU Complement ID

    Deletes a previously existing SKU Complement by SKU Complement ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_complement_id: SKU Complement’s unique numerical identifier.
    :type sku_complement_id: int

    """
    return web.Response(status=200)


async def get_sk_ucomplementsbytype(request: web.Request, content_type, accept, parent_sku_id, type) -> web.Response:
    """Get SKU complements by type

    Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementSkuIds\&quot;: [          7      ],      \&quot;Type\&quot;: \&quot;1\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param parent_sku_id: ID of the Parent SKU, where the Complement is inserted.
    :type parent_sku_id: int
    :param type: Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together.
    :type type: int

    """
    return web.Response(status=200)


async def get_sku_complementby_sku_complement_id(request: web.Request, content_type, accept, sku_complement_id) -> web.Response:
    """Get SKU Complement by SKU Complement ID

    Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_complement_id: SKU Complement’s unique numerical identifier.
    :type sku_complement_id: int

    """
    return web.Response(status=200)


async def get_sku_complementby_skuid(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Get SKU Complement by SKU ID

    Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def get_sku_complementsby_complement_type_id(request: web.Request, content_type, accept, sku_id, complement_type_id) -> web.Response:
    """Get SKU Complements by Complement Type ID

    Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: ID of the SKU which will be inserted as a Complement in the Parent SKU.
    :type sku_id: int
    :param complement_type_id: Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together.
    :type complement_type_id: int

    """
    return web.Response(status=200)
