from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_list import CollectionList
from openapi_server.models.database_create_collection_request import DatabaseCreateCollectionRequest
from openapi_server.models.database_create_document_request import DatabaseCreateDocumentRequest
from openapi_server.models.database_update_collection_request import DatabaseUpdateCollectionRequest
from openapi_server.models.database_update_document_request import DatabaseUpdateDocumentRequest
from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList
from openapi_server import util


async def database_create_collection(request: web.Request, body=None) -> web.Response:
    """Create Collection

    Create a new Collection.

    :param body: 
    :type body: dict | bytes

    """
    body = DatabaseCreateCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def database_create_document(request: web.Request, collection_id, body=None) -> web.Response:
    """Create Document

    Create a new Document. Before using this route, you should create a new collection resource using either a [server integration](/docs/server/database#databaseCreateCollection) API or directly from your database console.

    :param collection_id: Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    :type collection_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DatabaseCreateDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def database_delete_collection(request: web.Request, collection_id) -> web.Response:
    """Delete Collection

    Delete a collection by its unique ID. Only users with write permissions have access to delete this resource.

    :param collection_id: Collection unique ID.
    :type collection_id: str

    """
    return web.Response(status=200)


async def database_delete_document(request: web.Request, collection_id, document_id) -> web.Response:
    """Delete Document

    Delete a document by its unique ID. This endpoint deletes only the parent documents, its attributes and relations to other documents. Child documents **will not** be deleted.

    :param collection_id: Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    :type collection_id: str
    :param document_id: Document unique ID.
    :type document_id: str

    """
    return web.Response(status=200)


async def database_get_collection(request: web.Request, collection_id) -> web.Response:
    """Get Collection

    Get a collection by its unique ID. This endpoint response returns a JSON object with the collection metadata.

    :param collection_id: Collection unique ID.
    :type collection_id: str

    """
    return web.Response(status=200)


async def database_get_document(request: web.Request, collection_id, document_id) -> web.Response:
    """Get Document

    Get a document by its unique ID. This endpoint response returns a JSON object with the document data.

    :param collection_id: Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    :type collection_id: str
    :param document_id: Document unique ID.
    :type document_id: str

    """
    return web.Response(status=200)


async def database_list_collections(request: web.Request, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Collections

    Get a list of all the user collections. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s collections. [Learn more about different API modes](/docs/admin).

    :param search: Search term to filter your list results. Max length: 256 chars.
    :type search: str
    :param limit: Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Results offset. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_type: Order result by ASC or DESC order.
    :type order_type: str

    """
    return web.Response(status=200)


async def database_list_documents(request: web.Request, collection_id, filters=None, limit=None, offset=None, order_field=None, order_type=None, order_cast=None, search=None) -> web.Response:
    """List Documents

    Get a list of all the user documents. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s documents. [Learn more about different API modes](/docs/admin).

    :param collection_id: Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    :type collection_id: str
    :param filters: Array of filter strings. Each filter is constructed from a key name, comparison operator (&#x3D;, !&#x3D;, &gt;, &lt;, &lt;&#x3D;, &gt;&#x3D;) and a value. You can also use a dot (.) separator in attribute names to filter by child document attributes. Examples: &#39;name&#x3D;John Doe&#39; or &#39;category.$id&gt;&#x3D;5bed2d152c362&#39;.
    :type filters: List[str]
    :param limit: Maximum number of documents to return in response.  Use this value to manage pagination. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Offset value. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_field: Document field that results will be sorted by.
    :type order_field: str
    :param order_type: Order direction. Possible values are DESC for descending order, or ASC for ascending order.
    :type order_type: str
    :param order_cast: Order field type casting. Possible values are int, string, date, time or datetime. The database will attempt to cast the order field to the value you pass here. The default value is a string.
    :type order_cast: str
    :param search: Search query. Enter any free text search. The database will try to find a match against all document attributes and children. Max length: 256 chars.
    :type search: str

    """
    return web.Response(status=200)


async def database_update_collection(request: web.Request, collection_id, body=None) -> web.Response:
    """Update Collection

    Update a collection by its unique ID.

    :param collection_id: Collection unique ID.
    :type collection_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DatabaseUpdateCollectionRequest.from_dict(body)
    return web.Response(status=200)


async def database_update_document(request: web.Request, collection_id, document_id, body=None) -> web.Response:
    """Update Document

    Update a document by its unique ID. Using the patch method you can pass only specific fields that will get updated.

    :param collection_id: Collection unique ID. You can create a new collection with validation rules using the Database service [server integration](/docs/server/database#createCollection).
    :type collection_id: str
    :param document_id: Document unique ID.
    :type document_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = DatabaseUpdateDocumentRequest.from_dict(body)
    return web.Response(status=200)
