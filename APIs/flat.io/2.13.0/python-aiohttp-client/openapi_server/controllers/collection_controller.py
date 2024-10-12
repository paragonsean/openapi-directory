from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_creation import CollectionCreation
from openapi_server.models.collection_modification import CollectionModification
from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.score_details import ScoreDetails
from openapi_server import util


async def add_score_to_collection(request: web.Request, collection, score, sharing_key=None) -> web.Response:
    """Add a score to the collection

    This operation will add a score to a collection. The default behavior will make the score available across multiple collections. You must have the capability &#x60;canAddScores&#x60; on the provided &#x60;collection&#x60; to perform the action. 

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str
    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def create_collection(request: web.Request, body) -> web.Response:
    """Create a new collection

    This method will create a new collection and add it to your &#x60;root&#x60; collection. 

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionCreation.from_dict(body)
    return web.Response(status=200)


async def delete_collection(request: web.Request, collection) -> web.Response:
    """Delete the collection

    This method will schedule the deletion of the collection. Until deleted, the collection will be available in the &#x60;trash&#x60;. 

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str

    """
    return web.Response(status=200)


async def delete_score_from_collection(request: web.Request, collection, score, sharing_key=None) -> web.Response:
    """Delete a score from the collection

    This method will delete a score from the collection. Unlike [&#x60;DELETE /scores/{score}&#x60;](#operation/deleteScore), this score will not remove the score from your account, but only from the collection. This can be used to *move* a score from one collection to another, or simply remove a score from one collection when this one is contained in multiple collections. 

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str
    :param score: Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;). 
    :type score: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def edit_collection(request: web.Request, collection, body=None) -> web.Response:
    """Update a collection&#39;s metadata

    

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str
    :param body: 
    :type body: dict | bytes

    """
    body = CollectionModification.from_dict(body)
    return web.Response(status=200)


async def get_collection(request: web.Request, collection, sharing_key=None) -> web.Response:
    """Get collection details

    

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str

    """
    return web.Response(status=200)


async def list_collection_scores(request: web.Request, collection, sharing_key=None, sort=None, direction=None, limit=None, next=None, previous=None) -> web.Response:
    """List the scores contained in a collection

    Use this method to list the scores contained in a collection. If no sort option is provided, the scores are sorted by &#x60;modificationDate&#x60; &#x60;desc&#x60;. 

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str
    :param sharing_key: This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document. 
    :type sharing_key: str
    :param sort: Sort
    :type sort: str
    :param direction: Sort direction
    :type direction: str
    :param limit: This is the maximum number of objects that may be returned
    :type limit: int
    :param next: An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type next: str
    :param previous: An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type previous: str

    """
    return web.Response(status=200)


async def list_collections(request: web.Request, parent=None, sort=None, direction=None, limit=None, next=None, previous=None) -> web.Response:
    """List the collections

    Use this method to list the user&#39;s collections contained in &#x60;parent&#x60; (by default in the &#x60;root&#x60; collection). If no sort option is provided, the collections are sorted by &#x60;creationDate&#x60; &#x60;desc&#x60;.  Note that this method will not include the &#x60;parent&#x60; collection in the listing. For example, if you need the details of the &#x60;root&#x60; collection, you can use &#x60;GET /v2/collections/root&#x60;. 

    :param parent: List the collection contained in this &#x60;parent&#x60; collection.  This option doesn&#39;t provide a complete multi-level collection support. When sharing a collection with someone, this one will have as &#x60;parent&#x60; &#x60;sharedWithMe&#x60;. 
    :type parent: str
    :param sort: Sort
    :type sort: str
    :param direction: Sort direction
    :type direction: str
    :param limit: This is the maximum number of objects that may be returned
    :type limit: int
    :param next: An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type next: str
    :param previous: An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type previous: str

    """
    return web.Response(status=200)


async def untrash_collection(request: web.Request, collection) -> web.Response:
    """Untrash a collection

    This method will restore the collection by removing it from the &#x60;trash&#x60; and add it back to the &#x60;root&#x60; collection. 

    :param collection: Unique identifier of the collection. The following aliases are supported: - &#x60;root&#x60;: The root collection of the account - &#x60;sharedWithMe&#x60;: Automatically contains new resources that have been shared individually - &#x60;trash&#x60;: Automatically contains resources that have been deleted 
    :type collection: str

    """
    return web.Response(status=200)
