from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_response import RestResponse
from openapi_server import util


async def add_collection2_using_post(request: web.Request, access_key, secret_key, collection_name, preload=None, evictable=None, purposes=None) -> web.Response:
    """Create new empty collection with given name

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param collection_name: The name of the collection that will be created
    :type collection_name: str
    :param preload: Defined whether to preload collection
    :type preload: bool
    :param evictable: Defined whether the collection can be evicted
    :type evictable: bool
    :param purposes: The newly declared purposes of the collection
    :type purposes: List[str]

    """
    return web.Response(status=200)


async def add_collection_using_post(request: web.Request, access_key, secret_key, name, preload=None, evictable=None, purposes=None) -> web.Response:
    """Create new empty collection with given name

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param name: The name of the collection that will be created
    :type name: str
    :param preload: Defined whether to preload collection
    :type preload: bool
    :param evictable: Defined whether the collection can be evicted
    :type evictable: bool
    :param purposes: The newly declared purposes of the collection
    :type purposes: List[str]

    """
    return web.Response(status=200)


async def delete_collection2_using_delete(request: web.Request, access_key, secret_key, collection_id) -> web.Response:
    """Delete existing collection with associated profiles and faces.

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: The id of the collection that will be removed
    :type collection_id: str

    """
    return web.Response(status=200)


async def delete_collection_using_delete(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Delete existing collection with associated profiles and faces.

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the collection that will be removed
    :type id: str

    """
    return web.Response(status=200)


async def export_csv_using_get(request: web.Request, access_key, secret_key, collection_id) -> web.Response:
    """Retrieve collection content for data analysis.

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: The id of the collection for which the data will be retrieved
    :type collection_id: str

    """
    return web.Response(status=200)


async def get_all_collection_profiles_using_get(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Gets all the profiles associated to a collection

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param id: The collection that contains the profile
    :type id: str

    """
    return web.Response(status=200)


async def get_all_collections2_using_get(request: web.Request, access_key, secret_key) -> web.Response:
    """Retrieve all collections

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str

    """
    return web.Response(status=200)


async def get_all_collections_using_get(request: web.Request, access_key, secret_key) -> web.Response:
    """Retrieve all collections

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str

    """
    return web.Response(status=200)


async def get_collection2_using_get(request: web.Request, access_key, secret_key, collection_id) -> web.Response:
    """Retrieve existing collection content

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: The id of the collection for which the data will be retrieved
    :type collection_id: str

    """
    return web.Response(status=200)


async def get_collection_using_get(request: web.Request, access_key, secret_key, id) -> web.Response:
    """Retrieve existing collection content

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey or readOnlyKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the collection for which the data will be retrieved
    :type id: str

    """
    return web.Response(status=200)


async def repurpose_collection_using_put(request: web.Request, access_key, secret_key, collection_id, purposes) -> web.Response:
    """Change purpose of existing collection

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param collection_id: The id of the collection for which the data will be retrieved
    :type collection_id: str
    :param purposes: The newly declared purposes of the collection
    :type purposes: List[str]

    """
    return web.Response(status=200)


async def update_collection2_using_post(request: web.Request, access_key, secret_key, id, name=None, purposes=None) -> web.Response:
    """Update an existing collection with a given id

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the collection that will be updated
    :type id: str
    :param name: The name of the collection that will be updated
    :type name: str
    :param purposes: The newly declared purposes of the collection
    :type purposes: List[str]

    """
    return web.Response(status=200)


async def update_collection_using_patch(request: web.Request, access_key, secret_key, id, name=None, purposes=None) -> web.Response:
    """Update an existing collection with a given id

    

    :param access_key: The accessKey provided by VisageCloud
    :type access_key: str
    :param secret_key: The secretKey provided by VisageCloud
    :type secret_key: str
    :param id: The id of the collection that will be updated
    :type id: str
    :param name: The name of the collection that will be updated
    :type name: str
    :param purposes: The newly declared purposes of the collection
    :type purposes: List[str]

    """
    return web.Response(status=200)
