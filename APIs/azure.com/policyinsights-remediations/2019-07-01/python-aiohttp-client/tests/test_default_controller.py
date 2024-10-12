# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.remediation import Remediation
from openapi_server.models.remediation_deployments_list_result import RemediationDeploymentsListResult
from openapi_server.models.remediation_list_result import RemediationListResult


pytestmark = pytest.mark.asyncio

async def test_remediations_cancel_at_management_group(client):
    """Test case for remediations_cancel_at_management_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/cancel'.format(management_groups_namespace='management_groups_namespace_example', management_group_id='management_group_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_cancel_at_resource(client):
    """Test case for remediations_cancel_at_resource

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/cancel'.format(resource_id='resource_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_cancel_at_resource_group(client):
    """Test case for remediations_cancel_at_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/cancel'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_cancel_at_subscription(client):
    """Test case for remediations_cancel_at_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/cancel'.format(subscription_id='subscription_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_remediations_create_or_update_at_management_group(client):
    """Test case for remediations_create_or_update_at_management_group

    
    """
    parameters = openapi_server.Remediation()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(management_groups_namespace='management_groups_namespace_example', management_group_id='management_group_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_remediations_create_or_update_at_resource(client):
    """Test case for remediations_create_or_update_at_resource

    
    """
    parameters = openapi_server.Remediation()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(resource_id='resource_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_remediations_create_or_update_at_resource_group(client):
    """Test case for remediations_create_or_update_at_resource_group

    
    """
    parameters = openapi_server.Remediation()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', remediation_name='remediation_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_remediations_create_or_update_at_subscription(client):
    """Test case for remediations_create_or_update_at_subscription

    
    """
    parameters = openapi_server.Remediation()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(subscription_id='subscription_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_delete_at_management_group(client):
    """Test case for remediations_delete_at_management_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(management_groups_namespace='management_groups_namespace_example', management_group_id='management_group_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_delete_at_resource(client):
    """Test case for remediations_delete_at_resource

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(resource_id='resource_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_delete_at_resource_group(client):
    """Test case for remediations_delete_at_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_delete_at_subscription(client):
    """Test case for remediations_delete_at_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(subscription_id='subscription_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_get_at_management_group(client):
    """Test case for remediations_get_at_management_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(management_groups_namespace='management_groups_namespace_example', management_group_id='management_group_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_get_at_resource(client):
    """Test case for remediations_get_at_resource

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(resource_id='resource_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_get_at_resource_group(client):
    """Test case for remediations_get_at_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_get_at_subscription(client):
    """Test case for remediations_get_at_subscription

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}'.format(subscription_id='subscription_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_deployments_at_management_group(client):
    """Test case for remediations_list_deployments_at_management_group

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/listDeployments'.format(management_groups_namespace='management_groups_namespace_example', management_group_id='management_group_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_deployments_at_resource(client):
    """Test case for remediations_list_deployments_at_resource

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/listDeployments'.format(resource_id='resource_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_deployments_at_resource_group(client):
    """Test case for remediations_list_deployments_at_resource_group

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/listDeployments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_deployments_at_subscription(client):
    """Test case for remediations_list_deployments_at_subscription

    
    """
    params = [('$top', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/remediations/{remediation_name}/listDeployments'.format(subscription_id='subscription_id_example', remediation_name='remediation_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_for_management_group(client):
    """Test case for remediations_list_for_management_group

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/{management_groups_namespace}/managementGroups/{management_group_id}/providers/Microsoft.PolicyInsights/remediations'.format(management_groups_namespace='management_groups_namespace_example', management_group_id='management_group_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_for_resource(client):
    """Test case for remediations_list_for_resource

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{resource_id}/providers/Microsoft.PolicyInsights/remediations'.format(resource_id='resource_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_for_resource_group(client):
    """Test case for remediations_list_for_resource_group

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.PolicyInsights/remediations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remediations_list_for_subscription(client):
    """Test case for remediations_list_for_subscription

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.PolicyInsights/remediations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

