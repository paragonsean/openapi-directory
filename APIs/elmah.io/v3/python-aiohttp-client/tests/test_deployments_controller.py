# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_deployment import CreateDeployment
from openapi_server.models.create_deployment_result import CreateDeploymentResult
from openapi_server.models.deployment import Deployment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_deployments_create(client):
    """Test case for deployments_create

    Create a new deployment.
    """
    body = {"created":"2000-01-23T04:56:07.000+00:00","description":"description","logId":"logId","userEmail":"userEmail","userName":"userName","version":"version"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/deployments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_delete(client):
    """Test case for deployments_delete

    Delete a deployment by its ID.
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/deployments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get(client):
    """Test case for deployments_get

    Fetch a deployment by its ID.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/deployments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deployments_get_all(client):
    """Test case for deployments_get_all

    Fetch a list of deployments.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/deployments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

