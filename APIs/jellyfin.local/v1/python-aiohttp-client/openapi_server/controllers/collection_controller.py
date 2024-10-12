from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_creation_result import CollectionCreationResult
from openapi_server import util


async def add_to_collection(request: web.Request, collection_id, ids) -> web.Response:
    """Adds items to a collection.

    

    :param collection_id: The collection id.
    :type collection_id: str
    :type collection_id: str
    :param ids: Item ids, comma delimited.
    :type ids: List[str]

    """
    return web.Response(status=200)


async def create_collection(request: web.Request, name=None, ids=None, parent_id=None, is_locked=None) -> web.Response:
    """Creates a new collection.

    

    :param name: The name of the collection.
    :type name: str
    :param ids: Item Ids to add to the collection.
    :type ids: List[str]
    :param parent_id: Optional. Create the collection within a specific folder.
    :type parent_id: str
    :type parent_id: str
    :param is_locked: Whether or not to lock the new collection.
    :type is_locked: bool

    """
    return web.Response(status=200)


async def remove_from_collection(request: web.Request, collection_id, ids) -> web.Response:
    """Removes items from a collection.

    

    :param collection_id: The collection id.
    :type collection_id: str
    :type collection_id: str
    :param ids: Item ids, comma delimited.
    :type ids: List[str]

    """
    return web.Response(status=200)
