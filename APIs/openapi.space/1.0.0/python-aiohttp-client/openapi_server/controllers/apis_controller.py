from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_meta import APIMeta
from openapi_server import util


async def delete_api(request: web.Request, owner, api) -> web.Response:
    """Deletes the specified API

    

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str

    """
    return web.Response(status=200)


async def delete_api_version(request: web.Request, owner, api, version) -> web.Response:
    """Deletes a particular version of the specified API

    

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str
    :param version: version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_api_versions(request: web.Request, owner, api) -> web.Response:
    """Retrieves an API meta listing for all API versions for this owner and API

    

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str

    """
    return web.Response(status=200)


async def get_json_definition(request: web.Request, owner, api, version) -> web.Response:
    """Retrieves the Swagger definition for the specified API and version in JSON format

    

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str
    :param version: version identifier
    :type version: str

    """
    return web.Response(status=200)


async def get_owner_apis(request: web.Request, owner, sort=None, order=None) -> web.Response:
    """Retrieves an API meta listing of all APIs defined for this owner

    

    :param owner: API owner identifier
    :type owner: str
    :param sort: sort criteria or result set * NAME - * UPATED * CREATED * OWNER 
    :type sort: str
    :param order: sort order
    :type order: str

    """
    return web.Response(status=200)


async def get_yaml_definition(request: web.Request, owner, api, version) -> web.Response:
    """Retrieves the Swagger definition for the specified API and version in YAML format

    

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str
    :param version: version identifier
    :type version: str

    """
    return web.Response(status=200)


async def publish_api_version(request: web.Request, owner, api, version) -> web.Response:
    """Publish a particular version of the specified API

    

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str
    :param version: version identifier
    :type version: str

    """
    return web.Response(status=200)


async def save_definition(request: web.Request, owner, api, definition, private=None, force=None) -> web.Response:
    """Saves the provided Swagger definition

    Saves the provided Swagger definition; the owner must match the token owner. The version will be extracted from the Swagger definitions itself.

    :param owner: API owner identifier
    :type owner: str
    :param api: API identifier
    :type api: str
    :param definition: the Swagger definition of this API
    :type definition: 
    :param private: Defines whether the API has to be private
    :type private: bool
    :param force: force update
    :type force: bool

    """
    return web.Response(status=200)


async def search_apis(request: web.Request, query=None, limit=None, offset=None, sort=None, order=None) -> web.Response:
    """Retrieves a list of currently defined APIs in API meta list format.

    

    :param query: free text query to match
    :type query: str
    :param limit: the maximum number of APIs to return
    :type limit: int
    :param offset: the offset where to start from when fetching a limited number of APIs
    :type offset: int
    :param sort: sort criteria or result set * NAME - * UPATED * CREATED * OWNER 
    :type sort: str
    :param order: sort order
    :type order: str

    """
    return web.Response(status=200)
