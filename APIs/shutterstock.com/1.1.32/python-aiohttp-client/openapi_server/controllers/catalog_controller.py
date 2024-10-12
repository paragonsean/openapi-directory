from typing import List, Dict
from aiohttp import web

from openapi_server.models.catalog_collection import CatalogCollection
from openapi_server.models.catalog_collection_data_list import CatalogCollectionDataList
from openapi_server.models.catalog_collection_item_data_list import CatalogCollectionItemDataList
from openapi_server.models.create_catalog_collection import CreateCatalogCollection
from openapi_server.models.create_catalog_collection_items import CreateCatalogCollectionItems
from openapi_server.models.remove_catalog_collection_items import RemoveCatalogCollectionItems
from openapi_server.models.update_catalog_collection import UpdateCatalogCollection
from openapi_server import util


async def add_to_collection(request: web.Request, collection_id, body) -> web.Response:
    """Add items to catalog collections

    This endpoint adds assets to a catalog collection. It also automatically adds the assets to the user&#39;s account&#39;s catalog.

    :param collection_id: The ID of the collection to add assets to
    :type collection_id: str
    :param body: Collection item attributes to add to collection
    :type body: dict | bytes

    """
    body = CreateCatalogCollectionItems.from_dict(body)
    return web.Response(status=200)


async def create_collection(request: web.Request, body) -> web.Response:
    """Create catalog collections

    This endpoint creates a catalog collection and optionally adds assets. To add assets to the collection later, use &#x60;PATCH /v2/catalog/collections/{collection_id}/items&#x60;.

    :param body: Create a catalog collection and, optionally, add items.
    :type body: dict | bytes

    """
    body = CreateCatalogCollection.from_dict(body)
    return web.Response(status=200)


async def delete_collection(request: web.Request, collection_id) -> web.Response:
    """Delete catalog collections

    This endpoint deletes a catalog collection. It does not remove the assets from the user&#39;s account&#39;s catalog.

    :param collection_id: The ID of the collection to delete
    :type collection_id: str

    """
    return web.Response(status=200)


async def delete_from_collection(request: web.Request, collection_id, body) -> web.Response:
    """Remove items from catalog collection

    This endpoint removes assets from a catalog collection. It does not remove the assets from the user&#39;s account&#39;s catalog.

    :param collection_id: The ID of the collection to remove assets from
    :type collection_id: str
    :param body: Items to remove from the collection
    :type body: dict | bytes

    """
    body = RemoveCatalogCollectionItems.from_dict(body)
    return web.Response(status=200)


async def get_collections(request: web.Request, page=None, per_page=None, sort=None, shared=None) -> web.Response:
    """List catalog collections

    This endpoint returns a list of catalog collections.

    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param sort: Sort by
    :type sort: str
    :param shared: Set to true to omit collections that you own and return only collections  that are shared with you
    :type shared: bool

    """
    return web.Response(status=200)


async def search_catalog(request: web.Request, sort=None, page=None, per_page=None, query=None, collection_id=None, asset_type=None) -> web.Response:
    """Search catalogs for assets

    This endpoint searches for assets in the account&#39;s catalog. If you specify more than one search parameter, the API uses an AND condition. Array parameters can be specified multiple times; in this case, the API uses an AND or an OR condition with those values, depending on the parameter. You can also filter search terms out in the &#x60;query&#x60; parameter by prefixing the term with NOT.

    :param sort: Sort by
    :type sort: str
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param query: One or more search terms separated by spaces
    :type query: str
    :param collection_id: Filter by collection id
    :type collection_id: List[str]
    :param asset_type: Filter by asset type
    :type asset_type: List[str]

    """
    return web.Response(status=200)


async def update_collection(request: web.Request, collection_id, body) -> web.Response:
    """Update collection metadata

    This endpoint updates the metadata of a catalog collection.

    :param collection_id: ID of collection that needs to be modified
    :type collection_id: str
    :param body: Collections Metadata to update
    :type body: dict | bytes

    """
    body = UpdateCatalogCollection.from_dict(body)
    return web.Response(status=200)
