from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_build_response import ListBuildResponse
from openapi_server.models.serverless_v1_service_build import ServerlessV1ServiceBuild
from openapi_server import util


async def create_build(request: web.Request, service_sid, asset_versions=None, dependencies=None, function_versions=None, runtime=None) -> web.Response:
    """create_build

    Create a new Build resource. At least one function version or asset version is required.

    :param service_sid: The SID of the Service to create the Build resource under.
    :type service_sid: str
    :param asset_versions: The list of Asset Version resource SIDs to include in the Build.
    :type asset_versions: List[str]
    :param dependencies: A list of objects that describe the Dependencies included in the Build. Each object contains the &#x60;name&#x60; and &#x60;version&#x60; of the dependency.
    :type dependencies: str
    :param function_versions: The list of the Function Version resource SIDs to include in the Build.
    :type function_versions: List[str]
    :param runtime: The Runtime version that will be used to run the Build resource when it is deployed.
    :type runtime: str

    """
    return web.Response(status=200)


async def delete_build(request: web.Request, service_sid, sid) -> web.Response:
    """delete_build

    Delete a Build resource.

    :param service_sid: The SID of the Service to delete the Build resource from.
    :type service_sid: str
    :param sid: The SID of the Build resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_build(request: web.Request, service_sid, sid) -> web.Response:
    """fetch_build

    Retrieve a specific Build resource.

    :param service_sid: The SID of the Service to fetch the Build resource from.
    :type service_sid: str
    :param sid: The SID of the Build resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_build(request: web.Request, service_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_build

    Retrieve a list of all Builds.

    :param service_sid: The SID of the Service to read the Build resources from.
    :type service_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
