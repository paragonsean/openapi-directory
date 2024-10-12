from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_catalog_pvt_collection_collection_id_position_post_request import ApiCatalogPvtCollectionCollectionIdPositionPostRequest
from openapi_server.models.api_catalog_pvt_collection_collection_id_subcollection_get200_response_inner import ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner
from openapi_server.models.api_catalog_pvt_subcollection_post200_response import ApiCatalogPvtSubcollectionPost200Response
from openapi_server.models.api_catalog_pvt_subcollection_post_request import ApiCatalogPvtSubcollectionPostRequest
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_brand_post200_response import ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_category_post200_response import ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_put_request import ApiCatalogPvtSubcollectionSubCollectionIdPutRequest
from openapi_server.models.api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_post200_response import ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response
from openapi_server.models.request_body10 import RequestBody10
from openapi_server.models.request_body11 import RequestBody11
from openapi_server.models.request_body12 import RequestBody12
from openapi_server import util


async def api_catalog_pvt_collection_collection_id_position_post(request: web.Request, content_type, accept, collection_id, body=None) -> web.Response:
    """Reposition SKU on the Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection’s unique numerical identifier.
    :type collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtCollectionCollectionIdPositionPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_collection_collection_id_subcollection_get(request: web.Request, content_type, accept, collection_id) -> web.Response:
    """Get Subcollection by Collection ID

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection’s unique numerical identifier.
    :type collection_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtSubcollectionPostRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_brand_brand_id_delete(request: web.Request, content_type, accept, sub_collection_id, brand_id) -> web.Response:
    """Delete Brand from Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param brand_id: Brand’s unique numerical identifier.
    :type brand_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_brand_category_id_delete(request: web.Request, content_type, accept, sub_collection_id, category_id) -> web.Response:
    """Delete Category from Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param category_id: Category’s unique numerical identifier.
    :type category_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_brand_post(request: web.Request, content_type, accept, sub_collection_id, body=None) -> web.Response:
    """Associate Brand to Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody10.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_category_post(request: web.Request, content_type, accept, sub_collection_id, body=None) -> web.Response:
    """Associate Category to Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody11.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_delete(request: web.Request, content_type, accept, sub_collection_id) -> web.Response:
    """Delete Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_get(request: web.Request, content_type, accept, sub_collection_id) -> web.Response:
    """Get Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int

    """
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_put(request: web.Request, content_type, accept, sub_collection_id, body=None) -> web.Response:
    """Update Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ApiCatalogPvtSubcollectionSubCollectionIdPutRequest.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_post(request: web.Request, content_type, accept, sub_collection_id, body=None) -> web.Response:
    """Add SKU to Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody12.from_dict(body)
    return web.Response(status=200)


async def api_catalog_pvt_subcollection_sub_collection_id_stockkeepingunit_sku_id_delete(request: web.Request, content_type, accept, sub_collection_id, sku_id) -> web.Response:
    """Delete SKU from Subcollection

     &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param sub_collection_id: Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    :type sub_collection_id: int
    :param sku_id: SKU’s unique numerical identifier.
    :type sku_id: int

    """
    return web.Response(status=200)
