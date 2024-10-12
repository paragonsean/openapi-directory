# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_tier_advisor import ServiceTierAdvisor
from openapi_server.models.service_tier_advisor_list_result import ServiceTierAdvisorListResult


pytestmark = pytest.mark.asyncio

async def test_service_tier_advisors_get(client):
    """Test case for service_tier_advisors_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/serviceTierAdvisors/{service_tier_advisor_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', service_tier_advisor_name='service_tier_advisor_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_tier_advisors_list_by_database(client):
    """Test case for service_tier_advisors_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/serviceTierAdvisors'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

