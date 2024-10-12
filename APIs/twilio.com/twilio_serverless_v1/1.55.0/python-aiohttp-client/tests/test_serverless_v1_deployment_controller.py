# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_deployment_response import ListDeploymentResponse
from openapi_server.models.serverless_v1_service_environment_deployment import ServerlessV1ServiceEnvironmentDeployment


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_deployment(client):
    """Test case for create_deployment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'build_sid': 'build_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments'.format(service_sid='service_sid_example', environment_sid='environment_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_deployment(client):
    """Test case for fetch_deployment

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments/{sid}'.format(service_sid='service_sid_example', environment_sid='environment_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_deployment(client):
    """Test case for list_deployment

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Services/{service_sid}/Environments/{environment_sid}/Deployments'.format(service_sid='service_sid_example', environment_sid='environment_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

