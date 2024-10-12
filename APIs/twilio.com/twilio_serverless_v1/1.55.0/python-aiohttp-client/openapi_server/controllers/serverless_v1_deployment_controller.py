from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_deployment_response import ListDeploymentResponse
from openapi_server.models.serverless_v1_service_environment_deployment import ServerlessV1ServiceEnvironmentDeployment
from openapi_server import util


async def create_deployment(request: web.Request, service_sid, environment_sid, build_sid=None) -> web.Response:
    """create_deployment

    Create a new Deployment.

    :param service_sid: The SID of the Service to create the Deployment resource under.
    :type service_sid: str
    :param environment_sid: The SID of the Environment for the Deployment.
    :type environment_sid: str
    :param build_sid: The SID of the Build for the Deployment.
    :type build_sid: str

    """
    return web.Response(status=200)


async def fetch_deployment(request: web.Request, service_sid, environment_sid, sid) -> web.Response:
    """fetch_deployment

    Retrieve a specific Deployment.

    :param service_sid: The SID of the Service to fetch the Deployment resource from.
    :type service_sid: str
    :param environment_sid: The SID of the Environment used by the Deployment to fetch.
    :type environment_sid: str
    :param sid: The SID that identifies the Deployment resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_deployment(request: web.Request, service_sid, environment_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_deployment

    Retrieve a list of all Deployments.

    :param service_sid: The SID of the Service to read the Deployment resources from.
    :type service_sid: str
    :param environment_sid: The SID of the Environment used by the Deployment resources to read.
    :type environment_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
