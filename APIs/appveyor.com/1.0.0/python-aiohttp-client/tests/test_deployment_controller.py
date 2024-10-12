# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_cancellation import DeploymentCancellation
from openapi_server.models.deployment_start_request import DeploymentStartRequest
from openapi_server.models.error import Error
from openapi_server.models.project_deployment import ProjectDeployment


pytestmark = pytest.mark.asyncio

async def test_cancel_deployment(client):
    """Test case for cancel_deployment

    Cancel deployment
    """
    body = {"deploymentId":123}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/deployments/stop',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deployment(client):
    """Test case for get_deployment

    Get deployment
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/deployments/{deployment_id}'.format(deployment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_deployment(client):
    """Test case for start_deployment

    Start deployment
    """
    body = {"accountName":"your-account-name","buildJobId":"sfke9239ydzf","buildVersion":"1.2.0","environmentName":"environment-to-deploy","environmentVariables":{"another_var":"another value","server":"myserver.com"},"projectSlug":"project-slug-from-url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/deployments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

