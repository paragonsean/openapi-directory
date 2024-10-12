from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_specification_nonstructured_get200_response_inner import ApiCatalogPvtSpecificationNonstructuredGet200ResponseInner
from openapi_server import util


async def api_catalog_pvt_specification_nonstructured_delete(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Delete Non Structured Specification by SKU ID

    Deletes unmapped Specifications of a Seller&#39;S SKU in a Marketplace by SKU ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_specification_nonstructured_get(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Get Non Structured Specification by SKU ID

    Gets general information about unmapped Specifications of a Seller&#39;s SKU in a Marketplace by SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  [  {      \&quot;Id\&quot;: 1010,      \&quot;SkuId\&quot;: 310119072,      \&quot;SpecificationName\&quot;: \&quot;size\&quot;,      \&quot;SpecificationValue\&quot;: \&quot;Small\&quot;  }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_specification_nonstructured_id_delete(request: web.Request, content_type, accept, id) -> web.Response:
    """Delete Non Structured Specification

    Deletes unmapped Specifications of a Seller&#39;S SKU in a Marketplace by its unique ID.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: Non Structured Specification’s unique numerical identifier.
    :type id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_specification_nonstructured_id_get(request: web.Request, content_type, accept, id) -> web.Response:
    """Get Non Structured Specification by ID

    Retrieves general information about unmapped Specifications of a Seller&#39;s SKU in a Marketplace.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1010,      \&quot;SkuId\&quot;: 310119072,      \&quot;SpecificationName\&quot;: \&quot;size\&quot;,      \&quot;SpecificationValue\&quot;: \&quot;Small\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param id: Non Structured Specification’s unique numerical identifier.
    :type id: int

    """
    return web.Response(status=200)
