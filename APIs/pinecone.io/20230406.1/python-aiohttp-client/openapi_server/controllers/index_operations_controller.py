from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_definition import CollectionDefinition
from openapi_server.models.index import Index
from openapi_server.models.index_configuration import IndexConfiguration
from openapi_server.models.index_definition import IndexDefinition
from openapi_server import util


async def configure_index(request: web.Request, index_name, body) -> web.Response:
    """Configure index

    This operation specifies the pod type and number of replicas for an index.

    :param index_name: 
    :type index_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = IndexConfiguration.from_dict(body)
    return web.Response(status=200)


async def create_collection(request: web.Request, body) -> web.Response:
    """Create collection

    This operation creates a Pinecone collection.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionDefinition.from_dict(body)
    return web.Response(status=200)


async def create_index(request: web.Request, body) -> web.Response:
    """Create index

    This operation creates a Pinecone index. You can use it to specify the measure of similarity, the dimension of vectors to be stored in the index, the numbers of replicas to use, and more.

    :param body: 
    :type body: dict | bytes

    """
    body = IndexDefinition.from_dict(body)
    return web.Response(status=200)


async def delete_collection(request: web.Request, collection_name) -> web.Response:
    """Delete Collection

    This operation deletes an existing collection.

    :param collection_name: 
    :type collection_name: str

    """
    return web.Response(status=200)


async def delete_index(request: web.Request, index_name) -> web.Response:
    """Delete Index

    This operation deletes an existing index.

    :param index_name: 
    :type index_name: str

    """
    return web.Response(status=200)


async def describe_collection(request: web.Request, collection_name) -> web.Response:
    """Describe collection

    Get a description of a collection.

    :param collection_name: 
    :type collection_name: str

    """
    return web.Response(status=200)


async def describe_index(request: web.Request, index_name) -> web.Response:
    """Describe index

    Get a description of an index.

    :param index_name: 
    :type index_name: str

    """
    return web.Response(status=200)


async def list_collections(request: web.Request, ) -> web.Response:
    """List collections

    This operation returns a list of your Pinecone collections.


    """
    return web.Response(status=200)


async def list_indexes(request: web.Request, ) -> web.Response:
    """List indexes

    This operation returns a list of your Pinecone indexes.


    """
    return web.Response(status=200)
