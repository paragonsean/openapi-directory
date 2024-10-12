# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.discovered_security_solution import DiscoveredSecuritySolution
from openapi_server.models.discovered_security_solution_list import DiscoveredSecuritySolutionList
from openapi_server.models.discovered_security_solutions_list_default_response import DiscoveredSecuritySolutionsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_discovered_security_solutions_get(client):
    """Test case for discovered_security_solutions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Security/locations/{asc_location}/discoveredSecuritySolutions/{discovered_security_solution_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', asc_location='asc_location_example', discovered_security_solution_name='discovered_security_solution_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discovered_security_solutions_list(client):
    """Test case for discovered_security_solutions_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/discoveredSecuritySolutions'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_discovered_security_solutions_list_by_home_region(client):
    """Test case for discovered_security_solutions_list_by_home_region

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/locations/{asc_location}/discoveredSecuritySolutions'.format(subscription_id='subscription_id_example', asc_location='asc_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

