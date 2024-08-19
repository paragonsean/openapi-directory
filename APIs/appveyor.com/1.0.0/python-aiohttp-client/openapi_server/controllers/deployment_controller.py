from typing import List, Dict
from aiohttp import web

from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_cancellation import DeploymentCancellation
from openapi_server.models.deployment_start_request import DeploymentStartRequest
from openapi_server.models.error import Error
from openapi_server.models.project_deployment import ProjectDeployment
from openapi_server import util


async def cancel_deployment(request: web.Request, body) -> web.Response:
    """Cancel deployment

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeploymentCancellation.from_dict(body)
    return web.Response(status=200)


async def get_deployment(request: web.Request, deployment_id) -> web.Response:
    """Get deployment

    

    :param deployment_id: Deployment ID (&#x60;deploymentId&#x60; property of &#x60;Deployment&#x60;)
    :type deployment_id: int

    """
    return web.Response(status=200)


async def start_deployment(request: web.Request, body) -> web.Response:
    """Start deployment

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeploymentStartRequest.from_dict(body)
    return web.Response(status=200)
