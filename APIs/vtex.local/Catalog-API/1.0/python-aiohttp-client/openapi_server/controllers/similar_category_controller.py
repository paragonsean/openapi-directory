from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_product_product_id_similarcategory_category_id_post200_response import ApiCatalogPvtProductProductIdSimilarcategoryCategoryIdPost200Response
from openapi_server.models.api_catalog_pvt_product_product_id_similarcategory_get200_response_inner import ApiCatalogPvtProductProductIdSimilarcategoryGet200ResponseInner
from openapi_server import util


async def api_catalog_pvt_product_product_id_similarcategory_category_id_delete(request: web.Request, content_type, accept, product_id, category_id) -> web.Response:
    """Delete Similar Category

    Deletes a Similar Category from a Product.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param category_id: Similar Category’s unique numerical identifier.
    :type category_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_product_product_id_similarcategory_category_id_post(request: web.Request, content_type, accept, product_id, category_id) -> web.Response:
    """Add Similar Category

    Adds a Similar Category to a Product.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ProductId\&quot;: 1,      \&quot;StoreId\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int
    :param category_id: Similar Category’s unique numerical identifier.
    :type category_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_product_product_id_similarcategory_get(request: web.Request, content_type, accept, product_id) -> web.Response:
    """Get Similar Categories

    Retrieves Similar Categories from a Product.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;CategoryId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;CategoryId\&quot;: 20      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param product_id: Product’s unique numerical identifier.
    :type product_id: int

    """
    return web.Response(status=200)
