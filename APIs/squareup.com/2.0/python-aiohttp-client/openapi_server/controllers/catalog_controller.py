from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_delete_catalog_objects_request import BatchDeleteCatalogObjectsRequest
from openapi_server.models.batch_delete_catalog_objects_response import BatchDeleteCatalogObjectsResponse
from openapi_server.models.batch_retrieve_catalog_objects_request import BatchRetrieveCatalogObjectsRequest
from openapi_server.models.batch_retrieve_catalog_objects_response import BatchRetrieveCatalogObjectsResponse
from openapi_server.models.batch_upsert_catalog_objects_request import BatchUpsertCatalogObjectsRequest
from openapi_server.models.batch_upsert_catalog_objects_response import BatchUpsertCatalogObjectsResponse
from openapi_server.models.catalog_info_response import CatalogInfoResponse
from openapi_server.models.delete_catalog_object_response import DeleteCatalogObjectResponse
from openapi_server.models.list_catalog_response import ListCatalogResponse
from openapi_server.models.retrieve_catalog_object_response import RetrieveCatalogObjectResponse
from openapi_server.models.search_catalog_items_request import SearchCatalogItemsRequest
from openapi_server.models.search_catalog_items_response import SearchCatalogItemsResponse
from openapi_server.models.search_catalog_objects_request import SearchCatalogObjectsRequest
from openapi_server.models.search_catalog_objects_response import SearchCatalogObjectsResponse
from openapi_server.models.update_item_modifier_lists_request import UpdateItemModifierListsRequest
from openapi_server.models.update_item_modifier_lists_response import UpdateItemModifierListsResponse
from openapi_server.models.update_item_taxes_request import UpdateItemTaxesRequest
from openapi_server.models.update_item_taxes_response import UpdateItemTaxesResponse
from openapi_server.models.upsert_catalog_object_request import UpsertCatalogObjectRequest
from openapi_server.models.upsert_catalog_object_response import UpsertCatalogObjectResponse
from openapi_server import util


async def batch_delete_catalog_objects(request: web.Request, body) -> web.Response:
    """BatchDeleteCatalogObjects

    Deletes a set of [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem)s based on the provided list of target IDs and returns a set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted object are also deleted. For example, deleting a CatalogItem will also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.  &#x60;BatchDeleteCatalogObjects&#x60; succeeds even if only a portion of the targeted IDs can be deleted. The response will only include IDs that were actually deleted.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchDeleteCatalogObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_retrieve_catalog_objects(request: web.Request, body) -> web.Response:
    """BatchRetrieveCatalogObjects

    Returns a set of objects based on the provided ID. Each [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) returned in the set includes all of its child information including: all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) objects, references to its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchRetrieveCatalogObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_upsert_catalog_objects(request: web.Request, body) -> web.Response:
    """BatchUpsertCatalogObjects

    Creates or updates up to 10,000 target objects based on the provided list of objects. The target objects are grouped into batches and each batch is inserted/updated in an all-or-nothing manner. If an object within a batch is malformed in some way, or violates a database constraint, the entire batch containing that item will be disregarded. However, other batches in the same request may still succeed. Each batch may contain up to 1,000 objects, and batches will be processed in order as long as the total object count for the request (items, variations, modifier lists, discounts, and taxes) is no more than 10,000.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchUpsertCatalogObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_info(request: web.Request, ) -> web.Response:
    """CatalogInfo

    Retrieves information about the Square Catalog API, such as batch size limits that can be used by the &#x60;BatchUpsertCatalogObjects&#x60; endpoint.


    """
    return web.Response(status=200)


async def delete_catalog_object(request: web.Request, object_id) -> web.Response:
    """DeleteCatalogObject

    Deletes a single [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID and returns the set of successfully deleted IDs in the response. Deletion is a cascading event such that all children of the targeted object are also deleted. For example, deleting a [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) will also delete all of its [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children.

    :param object_id: The ID of the catalog object to be deleted. When an object is deleted, other objects in the graph that depend on that object will be deleted as well (for example, deleting a catalog item will delete its catalog item variations).
    :type object_id: str

    """
    return web.Response(status=200)


async def list_catalog(request: web.Request, cursor=None, types=None, catalog_version=None) -> web.Response:
    """ListCatalog

    Returns a list of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s that includes all objects of a set of desired types (for example, all [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) and [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects) in the catalog. The &#x60;types&#x60; parameter is specified as a comma-separated list of valid [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) types: &#x60;ITEM&#x60;, &#x60;ITEM_VARIATION&#x60;, &#x60;MODIFIER&#x60;, &#x60;MODIFIER_LIST&#x60;, &#x60;CATEGORY&#x60;, &#x60;DISCOUNT&#x60;, &#x60;TAX&#x60;, &#x60;IMAGE&#x60;.  __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects) and set the &#x60;include_deleted_objects&#x60; attribute value to &#x60;true&#x60;.

    :param cursor: The pagination cursor returned in the previous response. Leave unset for an initial request. The page size is currently set to be 100. See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
    :type cursor: str
    :param types: An optional case-insensitive, comma-separated list of object types to retrieve.  The valid values are defined in the [CatalogObjectType](https://developer.squareup.com/reference/square_2021-08-18/enums/CatalogObjectType) enum, including &#x60;ITEM&#x60;, &#x60;ITEM_VARIATION&#x60;, &#x60;CATEGORY&#x60;, &#x60;DISCOUNT&#x60;, &#x60;TAX&#x60;, &#x60;MODIFIER&#x60;, &#x60;MODIFIER_LIST&#x60;, or &#x60;IMAGE&#x60;.  If this is unspecified, the operation returns objects of all the types at the version of the Square API used to make the request.
    :type types: str
    :param catalog_version: The specific version of the catalog objects to be included in the response.  This allows you to retrieve historical versions of objects. The specified version value is matched against the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s&#39; &#x60;version&#x60; attribute.
    :type catalog_version: int

    """
    return web.Response(status=200)


async def retrieve_catalog_object(request: web.Request, object_id, include_related_objects=None, catalog_version=None) -> web.Response:
    """RetrieveCatalogObject

    Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) as a [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) based on the provided ID. The returned object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItemVariation) children, references to its [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects, and the ids of any [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to it.

    :param object_id: The object ID of any type of catalog objects to be retrieved.
    :type object_id: str
    :param include_related_objects: If &#x60;true&#x60;, the response will include additional objects that are related to the requested object, as follows:  If the &#x60;object&#x60; field of the response contains a &#x60;CatalogItem&#x60;, its associated &#x60;CatalogCategory&#x60;, &#x60;CatalogTax&#x60;, &#x60;CatalogImage&#x60; and &#x60;CatalogModifierList&#x60; objects will be returned in the &#x60;related_objects&#x60; field of the response. If the &#x60;object&#x60; field of the response contains a &#x60;CatalogItemVariation&#x60;, its parent &#x60;CatalogItem&#x60; will be returned in the &#x60;related_objects&#x60; field of the response.  Default value: &#x60;false&#x60;
    :type include_related_objects: bool
    :param catalog_version: Requests objects as of a specific version of the catalog. This allows you to retrieve historical versions of objects. The value to retrieve a specific version of an object can be found in the version field of [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s.
    :type catalog_version: int

    """
    return web.Response(status=200)


async def search_catalog_items(request: web.Request, body) -> web.Response:
    """SearchCatalogItems

    Searches for catalog items or item variations by matching supported search attribute values, including custom attribute values, against one or more of the specified query expressions.  This (&#x60;SearchCatalogItems&#x60;) endpoint differs from the [SearchCatalogObjects](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-objects) endpoint in the following aspects:  - &#x60;SearchCatalogItems&#x60; can only search for items or item variations, whereas &#x60;SearchCatalogObjects&#x60; can search for any type of catalog objects. - &#x60;SearchCatalogItems&#x60; supports the custom attribute query filters to return items or item variations that contain custom attribute values, where &#x60;SearchCatalogObjects&#x60; does not. - &#x60;SearchCatalogItems&#x60; does not support the &#x60;include_deleted_objects&#x60; filter to search for deleted items or item variations, whereas &#x60;SearchCatalogObjects&#x60; does. - The both endpoints use different call conventions, including the query filter formats.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchCatalogItemsRequest.from_dict(body)
    return web.Response(status=200)


async def search_catalog_objects(request: web.Request, body) -> web.Response:
    """SearchCatalogObjects

    Searches for [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) of any type by matching supported search attribute values, excluding custom attribute values on items or item variations, against one or more of the specified query expressions.  This (&#x60;SearchCatalogObjects&#x60;) endpoint differs from the [SearchCatalogItems](https://developer.squareup.com/reference/square_2021-08-18/catalog-api/search-catalog-items) endpoint in the following aspects:  - &#x60;SearchCatalogItems&#x60; can only search for items or item variations, whereas &#x60;SearchCatalogObjects&#x60; can search for any type of catalog objects. - &#x60;SearchCatalogItems&#x60; supports the custom attribute query filters to return items or item variations that contain custom attribute values, where &#x60;SearchCatalogObjects&#x60; does not. - &#x60;SearchCatalogItems&#x60; does not support the &#x60;include_deleted_objects&#x60; filter to search for deleted items or item variations, whereas &#x60;SearchCatalogObjects&#x60; does. - The both endpoints have different call conventions, including the query filter formats.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchCatalogObjectsRequest.from_dict(body)
    return web.Response(status=200)


async def update_item_modifier_lists(request: web.Request, body) -> web.Response:
    """UpdateItemModifierLists

    Updates the [CatalogModifierList](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogModifierList) objects that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an upsert on the entire item.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateItemModifierListsRequest.from_dict(body)
    return web.Response(status=200)


async def update_item_taxes(request: web.Request, body) -> web.Response:
    """UpdateItemTaxes

    Updates the [CatalogTax](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogTax) objects that apply to the targeted [CatalogItem](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogItem) without having to perform an upsert on the entire item.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateItemTaxesRequest.from_dict(body)
    return web.Response(status=200)


async def upsert_catalog_object(request: web.Request, body) -> web.Response:
    """UpsertCatalogObject

    Creates or updates the target [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpsertCatalogObjectRequest.from_dict(body)
    return web.Response(status=200)
