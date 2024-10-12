# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.role_assignment_list_result import RoleAssignmentListResult
from openapi_server.models.role_assignment_resource_format import RoleAssignmentResourceFormat


pytestmark = pytest.mark.asyncio

async def test_role_assignments_create_or_update(client):
    """Test case for role_assignments_create_or_update

    
    """
    parameters = {"properties":{"connectors":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"role":"Admin","relationshipLinks":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"displayName":{"key":"displayName"},"profiles":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"description":{"key":"description"},"principals":[{"principalId":"principalId","principalType":"principalType","principalMetadata":{"key":"principalMetadata"}},{"principalId":"principalId","principalType":"principalType","principalMetadata":{"key":"principalMetadata"}}],"provisioningState":"Provisioning","interactions":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"segments":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"relationships":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"sasPolicies":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"widgetTypes":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"tenantId":"tenantId","links":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"roleAssignments":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"conflationPolicies":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"kpis":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]},"assignmentName":"assignmentName","views":{"elements":["elements","elements"],"exceptions":["exceptions","exceptions"]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/roleAssignments/{assignment_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', assignment_name='assignment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_assignments_delete(client):
    """Test case for role_assignments_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/roleAssignments/{assignment_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', assignment_name='assignment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_assignments_get(client):
    """Test case for role_assignments_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/roleAssignments/{assignment_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', assignment_name='assignment_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_role_assignments_list_by_hub(client):
    """Test case for role_assignments_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/roleAssignments'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

