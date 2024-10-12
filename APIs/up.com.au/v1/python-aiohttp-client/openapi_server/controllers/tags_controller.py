from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_tags_response import ListTagsResponse
from openapi_server.models.update_transaction_tags_request import UpdateTransactionTagsRequest
from openapi_server import util


async def tags_get(request: web.Request, page_size=None) -> web.Response:
    """List tags

    Retrieve a list of all tags currently in use. The returned list is [paginated](#pagination) and can be scrolled by following the &#x60;next&#x60; and &#x60;prev&#x60; links where present. Results are ordered lexicographically. The &#x60;transactions&#x60; relationship for each tag exposes a link to get the transactions with the given tag. 

    :param page_size: The number of records to return in each page. 
    :type page_size: int

    """
    return web.Response(status=200)


async def transactions_transaction_id_relationships_tags_delete(request: web.Request, transaction_id, body=None) -> web.Response:
    """Remove tags from transaction

    Disassociates one or more tags from a specific transaction. Tags that are not associated are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

    :param transaction_id: The unique identifier for the transaction. 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTransactionTagsRequest.from_dict(body)
    return web.Response(status=200)


async def transactions_transaction_id_relationships_tags_post(request: web.Request, transaction_id, body=None) -> web.Response:
    """Add tags to transaction

    Associates one or more tags with a specific transaction. No more than 6 tags may be present on any single transaction. Duplicate tags are silently ignored. An HTTP &#x60;204&#x60; is returned on success. The associated tags, along with this request URL, are also exposed via the &#x60;tags&#x60; relationship on the transaction resource returned from &#x60;/transactions/{id}&#x60;. 

    :param transaction_id: The unique identifier for the transaction. 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTransactionTagsRequest.from_dict(body)
    return web.Response(status=200)
