from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_product_id_specification_post200_response import ApiCatalogPvtProductProductIdSpecificationPost200Response
from openapi_server.models.api_catalog_pvt_product_product_id_specification_post_request import ApiCatalogPvtProductProductIdSpecificationPostRequest
from openapi_server.models.api_catalog_pvt_product_product_id_specificationvalue_put200_response_inner import ApiCatalogPvtProductProductIdSpecificationvaluePut200ResponseInner
from openapi_server.models.api_catalog_pvt_product_product_id_specificationvalue_put_request import ApiCatalogPvtProductProductIdSpecificationvaluePutRequest
from openapi_server.models.get_product_specificationby_product_id200_response_inner import GetProductSpecificationbyProductID200ResponseInner
from openapi_server.models.getor_update_product_specification import GetorUpdateProductSpecification
from openapi_server import util


async def api_catalog_pvt_product_product_id_specification_post(request: web.Request, content_type, accept, product_id, body=None) -> web.Response:
    """Associate Product Specification

    Associates a previously defined Specification to a Product.    ### Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;    ### Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 41,      \&quot;FieldId\&quot;: 19,      \&quot;FieldValueId\&quot;: 1,      \&quot;Text\&quot;: \&quot;test\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtProductProductIdSpecificationPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_product_product_id_specificationvalue_put(request: web.Request, content_type, accept, product_id, body=None) -> web.Response:
    """Associate product specification using specification name and group name

    Associates a specification to a product using specification name and group name. Automatically creates the informed group, specification and values if they had not been created before.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldName\&quot;: \&quot;Material\&quot;,      \&quot;GroupName\&quot;: \&quot;Additional Information\&quot;,      \&quot;RootLevelSpecification\&quot;: false,      \&quot;FieldValues\&quot;: [          \&quot;Cotton\&quot;,         \&quot;Polyester\&quot;          ]  }  &#x60;&#x60;&#x60;        ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 53,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 60,          \&quot;Text\&quot;: \&quot;Cotton\&quot;      },      {          \&quot;Id\&quot;: 54,          \&quot;ProductId\&quot;: 3,          \&quot;FieldId\&quot;: 21,          \&quot;FieldValueId\&quot;: 61,          \&quot;Text\&quot;: \&quot;Polyester\&quot;      }  ]  &#x60;&#x60;&#x60;  

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtProductProductIdSpecificationvaluePutRequest.from_dict(body)
    return web.Response(status=200)


async def delete_all_product_specifications(request: web.Request, content_type, accept, product_id) -> web.Response:
    """Delete all Product Specifications by Product ID

    Deletes all Product Specifications given a specific Product ID.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int

    """
    return web.Response(status=200)


async def deletea_product_specification(request: web.Request, content_type, accept, product_id, specification_id) -> web.Response:
    """Delete a specific Product Specification

    Deletes a specific Product Specification given a Product ID and a Specification ID.

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param specification_id: Product Specification’s unique numerical identifier.
    :type specification_id: int

    """
    return web.Response(status=200)


async def get_product_specification(request: web.Request, content_type, accept, product_id) -> web.Response:
    """Get Product Specification by Product ID

    Retrieves all specifications of a product by the product&#39;s ID.  &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.    ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int

    """
    return web.Response(status=200)


async def get_product_specificationby_product_id(request: web.Request, content_type, accept, product_id) -> web.Response:
    """Get Product Specification and its information by Product ID

    Retrieves information of all specifications of a product by the product&#39;s ID.     ### Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 227,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 33,          \&quot;FieldValueId\&quot;: 135,          \&quot;Text\&quot;: \&quot;ValueA\&quot;      },      {          \&quot;Id\&quot;: 228,          \&quot;ProductId\&quot;: 1,          \&quot;FieldId\&quot;: 34,          \&quot;FieldValueId\&quot;: 1,          \&quot;Text\&quot;: \&quot;Giant\&quot;      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int

    """
    return web.Response(status=200)


async def update_product_specification(request: web.Request, content_type, accept, product_id, body) -> web.Response:
    """Update Product Specification by Product ID

    Updates the value of a product specification by the product&#39;s ID. The ID or name can be used to identify what product specification will be updated. Specification fields must be previously created in your Catalog.    ### Request body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Value\&quot;: [              \&quot;Iron\&quot;,              \&quot;Plastic\&quot;          ],          \&quot;Id\&quot;: 30,          \&quot;Name\&quot;: \&quot;Material\&quot;      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Describes the type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique identifier.
    :type product_id: int
    :param body: 
    :type body: list | bytes

    """
    body = [GetorUpdateProductSpecification.from_dict(d) for d in body]
    return web.Response(status=200)
