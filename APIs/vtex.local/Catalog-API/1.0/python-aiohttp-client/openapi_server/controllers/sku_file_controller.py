from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_stockkeepingunit_copy_sku_idfrom_sku_idto_file_put200_response_inner import ApiCatalogPvtStockkeepingunitCopySkuIdfromSkuIdtoFilePut200ResponseInner
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_file_get200_response_inner import ApiCatalogPvtStockkeepingunitSkuIdFileGet200ResponseInner
from openapi_server.models.api_catalog_pvt_stockkeepingunit_sku_id_file_post200_response import ApiCatalogPvtStockkeepingunitSkuIdFilePost200Response
from openapi_server.models.sku_file_url import SKUFileURL
from openapi_server import util


async def api_catalog_pvt_stockkeepingunit_copy_sku_idfrom_sku_idto_file_put(request: web.Request, content_type, accept, sku_idfrom, sku_idto) -> web.Response:
    """Copy Files from an SKU to another SKU

    Copy all existing files from an SKU to another SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1964,          \&quot;ArchiveId\&quot;: 155404,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;\&quot;      },      {          \&quot;Id\&quot;: 1965,          \&quot;ArchiveId\&quot;: 155429,          \&quot;SkuId\&quot;: 1,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_idfrom: __Origin__ SKU’s unique numerical identifier.
    :type sku_idfrom: int
    :param sku_idto: __Target__ SKU’s unique numerical identifier.
    :type sku_idto: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_disassociate_sku_id_file_sku_file_id_delete(request: web.Request, content_type, accept, sku_id, sku_file_id) -> web.Response:
    """Disassociate SKU File

    Disassociates an SKU File from an SKU.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param sku_file_id: ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field.
    :type sku_file_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_file_delete(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Delete All SKU Files

    Deletes all SKU Image Files.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_file_get(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """Get SKU Files

    Gets general information about all Files in the SKU.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 549,          \&quot;ArchiveId\&quot;: 155485,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;chimera-cat-quimera-5\&quot;,          \&quot;IsMain\&quot;: true,          \&quot;Label\&quot;: \&quot;miau\&quot;      },      {          \&quot;Id\&quot;: 550,          \&quot;ArchiveId\&quot;: 155486,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Gato-siames\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: \&quot;Gato siames\&quot;      },      {          \&quot;Id\&quot;: 555,          \&quot;ArchiveId\&quot;: 155491,          \&quot;SkuId\&quot;: 310118490,          \&quot;Name\&quot;: \&quot;Cat-Sleeping-Pics\&quot;,          \&quot;IsMain\&quot;: false,          \&quot;Label\&quot;: null      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_file_post(request: web.Request, content_type, accept, sku_id, body=None) -> web.Response:
    """Create SKU File

    Creates a new Image for an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;Text\&quot;: null,        \&quot;Url\&quot;: \&quot;https://1.bp.blogspot.com/_SLQk9aAv9-o/S7NNbJPv7NI/AAAAAAAAAN8/V1LcO0ViDc4/s1600/waterbottle.jpg\&quot;          }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {        \&quot;Id\&quot;: 503,        \&quot;ArchiveId\&quot;: 155491,        \&quot;SkuId\&quot;: 1,        \&quot;Name\&quot;: \&quot;Royal-Canin-Feline-Urinary-SO\&quot;,        \&quot;IsMain\&quot;: true,        \&quot;Label\&quot;: \&quot;\&quot;  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SKUFileURL.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_file_sku_file_id_delete(request: web.Request, content_type, accept, sku_id, sku_file_id) -> web.Response:
    """Delete SKU Image File

    Deletes a specific SKU Image File.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param sku_file_id: ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field.
    :type sku_file_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_stockkeepingunit_sku_id_file_sku_file_id_put(request: web.Request, content_type, accept, sku_id, sku_file_id, body=None) -> web.Response:
    """Update SKU File

    Updates a new Image on an SKU based on its URL or on a form-data request body.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null,      \&quot;Name\&quot;: \&quot;toilet-paper\&quot;,      \&quot;Text\&quot;: null,      \&quot;Url\&quot;: \&quot;https://images-na.ssl-images-amazon.com/images/I/81DLLXaGI7L._SL1500_.jpg\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 508,      \&quot;ArchiveId\&quot;: 155491,      \&quot;SkuId\&quot;: 7,      \&quot;IsMain\&quot;: true,      \&quot;Label\&quot;: null  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int
    :param sku_file_id: ID of the association of the SKU and the image, which can be obtained by placing a request to the [Get SKU File](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-sku-file) endpoint and copying the &#x60;Id&#x60; field.
    :type sku_file_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SKUFileURL.from_dict(body)
    return web.Response(status=200)
