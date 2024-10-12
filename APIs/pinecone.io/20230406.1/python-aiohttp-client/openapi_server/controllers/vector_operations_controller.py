from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_request import DeleteRequest
from openapi_server.models.describe_index_stats_request import DescribeIndexStatsRequest
from openapi_server.models.describe_index_stats_response import DescribeIndexStatsResponse
from openapi_server.models.fetch_request import FetchRequest
from openapi_server.models.fetch_response import FetchResponse
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_response import QueryResponse
from openapi_server.models.update_request import UpdateRequest
from openapi_server.models.upsert_request import UpsertRequest
from openapi_server.models.upsert_response import UpsertResponse
from openapi_server import util


async def delete(request: web.Request, body) -> web.Response:
    """Delete

    The &#x60;Delete&#x60; operation deletes vectors, by id, from a single namespace. You can delete items by their id, from a single namespace.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteRequest.from_dict(body)
    return web.Response(status=200)


async def describe_index_stats(request: web.Request, body) -> web.Response:
    """Describe Index Stats

    The &#x60;DescribeIndexStats&#x60; operation returns statistics about the index&#39;s contents, including the vector count per namespace and the number of dimensions.

    :param body: 
    :type body: dict | bytes

    """
    body = DescribeIndexStatsRequest.from_dict(body)
    return web.Response(status=200)


async def fetch(request: web.Request, body) -> web.Response:
    """Fetch

    The &#x60;Fetch&#x60; operation looks up and returns vectors, by ID, from a single namespace. The returned vectors include the vector data and/or metadata.

    :param body: 
    :type body: dict | bytes

    """
    body = FetchRequest.from_dict(body)
    return web.Response(status=200)


async def query(request: web.Request, body) -> web.Response:
    """Query

    The &#x60;Query&#x60; operation searches a namespace, using a query vector. It retrieves the ids of the most similar items in a namespace, along with their similarity scores.

    :param body: 
    :type body: dict | bytes

    """
    body = QueryRequest.from_dict(body)
    return web.Response(status=200)


async def update(request: web.Request, body) -> web.Response:
    """Fetch

    The &#x60;Update&#x60; operation updates vector in a namespace. If a value is included, it will overwrite the previous value. If a set_metadata is included, the values of the fields specified in it will be added or overwrite the previous value.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateRequest.from_dict(body)
    return web.Response(status=200)


async def upsert(request: web.Request, body) -> web.Response:
    """Upsert

    The Upsert operation writes vectors into a namespace. If a new value is upserted for an existing vector id, it will overwrite the previous value.

    :param body: 
    :type body: dict | bytes

    """
    body = UpsertRequest.from_dict(body)
    return web.Response(status=200)
