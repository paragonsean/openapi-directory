# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.advisor import Advisor
from openapi_server.models.advisor_list_result import AdvisorListResult


pytestmark = pytest.mark.asyncio

async def test_database_advisors_create_or_update(client):
    """Test case for database_advisors_create_or_update

    
    """
    parameters = {"kind":"kind","location":"location","properties":{"autoExecuteValue":"Enabled","lastChecked":"2000-01-23T04:56:07.000+00:00","advisorStatus":"GA","recommendationsStatus":"recommendationsStatus"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/advisors/{advisor_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', advisor_name='advisor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_advisors_get(client):
    """Test case for database_advisors_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/advisors/{advisor_name}'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', advisor_name='advisor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_advisors_list_by_database(client):
    """Test case for database_advisors_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/advisors'.format(resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

