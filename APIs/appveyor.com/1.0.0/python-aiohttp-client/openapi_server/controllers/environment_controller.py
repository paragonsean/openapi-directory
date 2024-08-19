from typing import List, Dict
from aiohttp import web

from openapi_server.models.deployment_environment_addition import DeploymentEnvironmentAddition
from openapi_server.models.deployment_environment_deployments_results import DeploymentEnvironmentDeploymentsResults
from openapi_server.models.deployment_environment_lookup_model import DeploymentEnvironmentLookupModel
from openapi_server.models.deployment_environment_settings_results import DeploymentEnvironmentSettingsResults
from openapi_server.models.deployment_environment_with_settings import DeploymentEnvironmentWithSettings
from openapi_server.models.error import Error
from openapi_server import util


async def add_environment(request: web.Request, body) -> web.Response:
    """Add environment

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeploymentEnvironmentAddition.from_dict(body)
    return web.Response(status=200)


async def delete_environment(request: web.Request, deployment_environment_id) -> web.Response:
    """Delete environment

    

    :param deployment_environment_id: Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;) 
    :type deployment_environment_id: int

    """
    return web.Response(status=200)


async def get_environment_deployments(request: web.Request, deployment_environment_id) -> web.Response:
    """Get environment deployments

    

    :param deployment_environment_id: Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;) 
    :type deployment_environment_id: int

    """
    return web.Response(status=200)


async def get_environment_settings(request: web.Request, deployment_environment_id) -> web.Response:
    """Get environment settings

    

    :param deployment_environment_id: Deployment Environment ID (&#x60;deploymentEnvironmentId&#x60; property of &#x60;DeploymentEnvironment&#x60;) 
    :type deployment_environment_id: int

    """
    return web.Response(status=200)


async def get_environments(request: web.Request, ) -> web.Response:
    """Get environments

    


    """
    return web.Response(status=200)


async def update_environment(request: web.Request, body) -> web.Response:
    """Update environment

    

    :param body: 
    :type body: dict | bytes

    """
    body = DeploymentEnvironmentWithSettings.from_dict(body)
    return web.Response(status=200)
