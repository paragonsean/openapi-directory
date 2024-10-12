from typing import List, Dict
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.articles_creator import ArticlesCreator
from openapi_server.models.author import Author
from openapi_server.models.authors_creator import AuthorsCreator
from openapi_server.models.categories_creator import CategoriesCreator
from openapi_server.models.category import Category
from openapi_server.models.collection import Collection
from openapi_server.models.collection_complete import CollectionComplete
from openapi_server.models.collection_complete_private import CollectionCompletePrivate
from openapi_server.models.collection_create import CollectionCreate
from openapi_server.models.collection_doi import CollectionDOI
from openapi_server.models.collection_handle import CollectionHandle
from openapi_server.models.collection_private_link_creator import CollectionPrivateLinkCreator
from openapi_server.models.collection_search import CollectionSearch
from openapi_server.models.collection_update import CollectionUpdate
from openapi_server.models.collection_versions import CollectionVersions
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.location import Location
from openapi_server.models.location_warnings import LocationWarnings
from openapi_server.models.location_warnings_update import LocationWarningsUpdate
from openapi_server.models.private_collection_search import PrivateCollectionSearch
from openapi_server.models.private_link import PrivateLink
from openapi_server.models.private_link_response import PrivateLinkResponse
from openapi_server.models.resource import Resource
from openapi_server import util


async def collection_articles(request: web.Request, collection_id, page=None, page_size=None, limit=None, offset=None) -> web.Response:
    """Public Collection Articles

    Returns a list of public collection articles

    :param collection_id: Collection Unique identifier
    :type collection_id: int
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def collection_details(request: web.Request, collection_id) -> web.Response:
    """Collection details

    View a collection

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def collection_version_details(request: web.Request, collection_id, version_id) -> web.Response:
    """Collection Version details

    View details for a certain version of a collection

    :param collection_id: Collection Unique identifier
    :type collection_id: int
    :param version_id: Version Number
    :type version_id: int

    """
    return web.Response(status=200)


async def collection_versions(request: web.Request, collection_id) -> web.Response:
    """Collection Versions list

    Returns a list of public collection Versions

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def collections_list(request: web.Request, x_cursor=None, page=None, page_size=None, limit=None, offset=None, order=None, order_direction=None, institution=None, published_since=None, modified_since=None, group=None, resource_doi=None, doi=None, handle=None) -> web.Response:
    """Public Collections

    Returns a list of public collections

    :param x_cursor: Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    :type x_cursor: str
    :type x_cursor: str
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int
    :param order: The field by which to order. Default varies by endpoint/resource.
    :type order: str
    :param order_direction: 
    :type order_direction: str
    :param institution: only return collections from this institution
    :type institution: int
    :param published_since: Filter by collection publishing date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD
    :type published_since: str
    :param modified_since: Filter by collection modified date. Will only return collections published after the date. date(ISO 8601) YYYY-MM-DD
    :type modified_since: str
    :param group: only return collections from this group
    :type group: int
    :param resource_doi: only return collections with this resource_doi
    :type resource_doi: str
    :param doi: only return collections with this doi
    :type doi: str
    :param handle: only return collections with this handle
    :type handle: str

    """
    return web.Response(status=200)


async def collections_search(request: web.Request, x_cursor=None, body=None) -> web.Response:
    """Public Collections Search

    Returns a list of public collections

    :param x_cursor: Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    :type x_cursor: str
    :type x_cursor: str
    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = CollectionSearch.from_dict(body)
    return web.Response(status=200)


async def private_collection_article_delete(request: web.Request, collection_id, article_id) -> web.Response:
    """Delete collection article

    De-associate article from collection

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param article_id: Collection article unique identifier
    :type article_id: int

    """
    return web.Response(status=200)


async def private_collection_articles_add(request: web.Request, collection_id, body) -> web.Response:
    """Add collection articles

    Associate new articles with the collection. This will add new articles to the list of already associated articles

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: Articles list
    :type body: dict | bytes

    """
    body = ArticlesCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_articles_list(request: web.Request, collection_id, page=None, page_size=None, limit=None, offset=None) -> web.Response:
    """List collection articles

    List collection articles

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int

    """
    return web.Response(status=200)


async def private_collection_articles_replace(request: web.Request, collection_id, body) -> web.Response:
    """Replace collection articles

    Associate new articles with the collection. This will remove all already associated articles and add these new ones

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: Articles List
    :type body: dict | bytes

    """
    body = ArticlesCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_author_delete(request: web.Request, collection_id, author_id) -> web.Response:
    """Delete collection author

    Delete collection author

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param author_id: Collection Author unique identifier
    :type author_id: int

    """
    return web.Response(status=200)


async def private_collection_authors_add(request: web.Request, collection_id, body) -> web.Response:
    """Add collection authors

    Associate new authors with the collection. This will add new authors to the list of already associated authors

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: List of authors
    :type body: dict | bytes

    """
    body = AuthorsCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_authors_list(request: web.Request, collection_id) -> web.Response:
    """List collection authors

    List collection authors

    :param collection_id: Collection unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_authors_replace(request: web.Request, collection_id, body) -> web.Response:
    """Replace collection authors

    Associate new authors with the collection. This will remove all already associated authors and add these new ones

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: List of authors
    :type body: dict | bytes

    """
    body = AuthorsCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_categories_add(request: web.Request, collection_id, body) -> web.Response:
    """Add collection categories

    Associate new categories with the collection. This will add new categories to the list of already associated categories

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: Categories list
    :type body: dict | bytes

    """
    body = CategoriesCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_categories_list(request: web.Request, collection_id) -> web.Response:
    """List collection categories

    List collection categories

    :param collection_id: Collection unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_categories_replace(request: web.Request, collection_id, body) -> web.Response:
    """Replace collection categories

    Associate new categories with the collection. This will remove all already associated categories and add these new ones

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: Categories list
    :type body: dict | bytes

    """
    body = CategoriesCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_category_delete(request: web.Request, collection_id, category_id) -> web.Response:
    """Delete collection category

    De-associate category from collection

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param category_id: Collection category unique identifier
    :type category_id: int

    """
    return web.Response(status=200)


async def private_collection_create(request: web.Request, body) -> web.Response:
    """Create collection

    Create a new Collection by sending collection information

    :param body: Collection description
    :type body: dict | bytes

    """
    body = CollectionCreate.from_dict(body)
    return web.Response(status=200)


async def private_collection_delete(request: web.Request, collection_id) -> web.Response:
    """Delete collection

    Delete n collection

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_details(request: web.Request, collection_id) -> web.Response:
    """Collection details

    View a collection

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_private_link_create(request: web.Request, collection_id, body=None) -> web.Response:
    """Create collection private link

    Create new private link

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CollectionPrivateLinkCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_private_link_delete(request: web.Request, collection_id, link_id) -> web.Response:
    """Disable private link

    Disable/delete private link for this collection

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param link_id: Private link token
    :type link_id: str

    """
    return web.Response(status=200)


async def private_collection_private_link_update(request: web.Request, collection_id, link_id, body=None) -> web.Response:
    """Update collection private link

    Update existing private link for this collection

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param link_id: Private link token
    :type link_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CollectionPrivateLinkCreator.from_dict(body)
    return web.Response(status=200)


async def private_collection_private_links_list(request: web.Request, collection_id) -> web.Response:
    """List collection private links

    List article private links

    :param collection_id: Collection unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_publish(request: web.Request, collection_id) -> web.Response:
    """Private Collection Publish

    When a collection is published, a new public version will be generated. Any further updates to the collection will affect the private collection data. In order to make these changes publicly visible, an explicit publish operation is needed.

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_reserve_doi(request: web.Request, collection_id) -> web.Response:
    """Private Collection Reserve DOI

    Reserve DOI for collection

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_reserve_handle(request: web.Request, collection_id) -> web.Response:
    """Private Collection Reserve Handle

    Reserve Handle for collection

    :param collection_id: Collection Unique identifier
    :type collection_id: int

    """
    return web.Response(status=200)


async def private_collection_resource(request: web.Request, collection_id, body) -> web.Response:
    """Private Collection Resource

    Edit collection resource data.

    :param collection_id: Collection unique identifier
    :type collection_id: int
    :param body: Resource data
    :type body: dict | bytes

    """
    body = Resource.from_dict(body)
    return web.Response(status=200)


async def private_collection_update(request: web.Request, collection_id, body) -> web.Response:
    """Update collection

    Update collection details; request can also be made with the PATCH method.

    :param collection_id: Collection Unique identifier
    :type collection_id: int
    :param body: Collection description
    :type body: dict | bytes

    """
    body = CollectionUpdate.from_dict(body)
    return web.Response(status=200)


async def private_collections_list(request: web.Request, page=None, page_size=None, limit=None, offset=None, order=None, order_direction=None) -> web.Response:
    """Private Collections List

    List private collections

    :param page: Page number. Used for pagination with page_size
    :type page: int
    :param page_size: The number of results included on a page. Used for pagination with page
    :type page_size: int
    :param limit: Number of results included on a page. Used for pagination with query
    :type limit: int
    :param offset: Where to start the listing(the offset of the first result). Used for pagination with limit
    :type offset: int
    :param order: The field by which to order. Default varies by endpoint/resource.
    :type order: str
    :param order_direction: 
    :type order_direction: str

    """
    return web.Response(status=200)


async def private_collections_search(request: web.Request, body) -> web.Response:
    """Private Collections Search

    Returns a list of private Collections

    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = PrivateCollectionSearch.from_dict(body)
    return web.Response(status=200)
