# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compose_deployment_status_info import ComposeDeploymentStatusInfo
from openapi_server.models.compose_deployment_upgrade_description import ComposeDeploymentUpgradeDescription
from openapi_server.models.compose_deployment_upgrade_progress_info import ComposeDeploymentUpgradeProgressInfo
from openapi_server.models.create_compose_deployment_description import CreateComposeDeploymentDescription
from openapi_server.models.fabric_error import FabricError
from openapi_server.models.paged_compose_deployment_status_info_list import PagedComposeDeploymentStatusInfoList


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_create_compose_deployment(client):
    """Test case for create_compose_deployment

    Creates a Service Fabric compose deployment.
    """
    create_compose_deployment_description = openapi_server.CreateComposeDeploymentDescription()
    params = [('api-version', 6.0-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/ComposeDeployments/$/Create',
        headers=headers,
        json=create_compose_deployment_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compose_deployment_status(client):
    """Test case for get_compose_deployment_status

    Gets information about a Service Fabric compose deployment.
    """
    params = [('api-version', 6.0-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ComposeDeployments/{deployment_name}'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compose_deployment_status_list(client):
    """Test case for get_compose_deployment_status_list

    Gets the list of compose deployments created in the Service Fabric cluster.
    """
    params = [('api-version', 6.0-preview),
                    ('ContinuationToken', 'continuation_token_example'),
                    ('MaxResults', 0),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ComposeDeployments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_compose_deployment_upgrade_progress(client):
    """Test case for get_compose_deployment_upgrade_progress

    Gets details for the latest upgrade performed on this Service Fabric compose deployment.
    """
    params = [('api-version', 6.0-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ComposeDeployments/{deployment_name}/$/GetUpgradeProgress'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_compose_deployment(client):
    """Test case for remove_compose_deployment

    Deletes an existing Service Fabric compose deployment from cluster.
    """
    params = [('api-version', 6.0-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ComposeDeployments/{deployment_name}/$/Delete'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_start_compose_deployment_upgrade(client):
    """Test case for start_compose_deployment_upgrade

    Starts upgrading a compose deployment in the Service Fabric cluster.
    """
    compose_deployment_upgrade_description = openapi_server.ComposeDeploymentUpgradeDescription()
    params = [('api-version', 6.0-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ComposeDeployments/{deployment_name}/$/Upgrade'.format(deployment_name='deployment_name_example'),
        headers=headers,
        json=compose_deployment_upgrade_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_rollback_compose_deployment_upgrade(client):
    """Test case for start_rollback_compose_deployment_upgrade

    Starts rolling back a compose deployment upgrade in the Service Fabric cluster.
    """
    params = [('api-version', 6.4-preview),
                    ('timeout', 60)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/ComposeDeployments/{deployment_name}/$/RollbackUpgrade'.format(deployment_name='deployment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

