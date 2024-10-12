from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_deployment import CreateDeployment
from openapi_server.models.create_deployment_result import CreateDeploymentResult
from openapi_server.models.deployment import Deployment
from openapi_server import util


async def deployments_create(request: web.Request, body=None) -> web.Response:
    """Create a new deployment.

    Required permission: &#x60;deployments_write&#x60;

    :param body: The deployment object to create.
    :type body: dict | bytes

    """
    body = CreateDeployment.from_dict(body)
    return web.Response(status=200)


async def deployments_delete(request: web.Request, id) -> web.Response:
    """Delete a deployment by its ID.

    This endpoint doesn&#39;t clear the version number of messages already annotated with this deployment version.&lt;br/&gt;&lt;br/&gt;Required permission: &#x60;deployments_delete&#x60;

    :param id: The ID of the deployment to delete.
    :type id: str

    """
    return web.Response(status=200)


async def deployments_get(request: web.Request, id) -> web.Response:
    """Fetch a deployment by its ID.

    Required permission: &#x60;deployments_read&#x60;

    :param id: The ID of the deployment to fetch.
    :type id: str

    """
    return web.Response(status=200)


async def deployments_get_all(request: web.Request, ) -> web.Response:
    """Fetch a list of deployments.

    Required permission: &#x60;deployments_read&#x60;


    """
    return web.Response(status=200)
