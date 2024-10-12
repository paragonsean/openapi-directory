from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_specification_post_request import ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put200_response_inner import ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePut200ResponseInner
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put_request import ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest
from openapi_server.models.request_body import RequestBody
from openapi_server.models.sku_specification_response import SKUSpecificationResponse
from openapi_server import util


async def api_catalog_pvt_stockkeepingunit_sku_id_specification_delete(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Delete all SKU Specifications

    Deletes all SKU Specifications.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_specification_get(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Get SKU Specifications

    Retrieves information about an SKU&#39;s Specifications.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 427,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 32,          \&quot;FieldValueId\&quot;: 131,          \&quot;Text\&quot;: \&quot;500g\&quot;      },      {          \&quot;Id\&quot;: 428,          \&quot;SkuId\&quot;: 7,          \&quot;FieldId\&quot;: 40,          \&quot;FieldValueId\&quot;: 133,          \&quot;Text\&quot;: \&quot;A\&quot;      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_specification_post(request: web.Request, content_type, accept, sku_id, body=None) -> web.Response:
    """Associate SKU Specification

    Associates a previously created Specification to an SKU.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 730,      \&quot;SkuId\&quot;: 31,      \&quot;FieldId\&quot;: 65,      \&quot;FieldValueId\&quot;: 138,      \&quot;Text\&quot;: \&quot;Size\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtStockkeepingunitSkuIdSpecificationPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_specification_put(request: web.Request, content_type, accept, sku_id, body=None) -> web.Response:
    """Update SKU Specification

    Updates an existing Specification on an existing SKU. This endpoint only updates the &#x60;FieldValueId&#x60;.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 65,    \&quot;SkuId\&quot;: 21,    \&quot;FieldId\&quot;: 32,    \&quot;FieldValueId\&quot;: 131,    \&quot;Text\&quot;: \&quot;Red\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_specification_specification_id_delete(request: web.Request, content_type, accept, sku_id, specification_id) -> web.Response:
    """Delete SKU Specification

    Deletes a specific SKU Specification.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param specification_id: Specification’s unique numerical identifier.
    :type specification_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_specificationvalue_put(request: web.Request, content_type, accept, sku_id, body=None) -> web.Response:
    """Associate SKU specification using specification name and group name

    Associates a specification to an SKU using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Size\&quot;,      \&quot;GroupName\&quot;: \&quot;Sizes\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;M\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 419,          \&quot;SkuId\&quot;: 5,          \&quot;FieldId\&quot;: 22,          \&quot;FieldValueId\&quot;: 62,          \&quot;Text\&quot;: \&quot;M\&quot;      }  ]  &#x60;&#x60;&#x60;  

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtStockkeepingunitSkuIdSpecificationvaluePutRequest.from_dict(body)
    return web.Response(status=200)
