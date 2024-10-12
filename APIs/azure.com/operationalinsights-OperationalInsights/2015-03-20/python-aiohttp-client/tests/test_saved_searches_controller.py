# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.saved_search import SavedSearch
from openapi_server.models.saved_searches_list_result import SavedSearchesListResult


pytestmark = pytest.mark.asyncio

async def test_saved_searches_create_or_update(client):
    """Test case for saved_searches_create_or_update

    
    """
    parameters = {"name":"name","eTag":"eTag","id":"id","type":"type","properties":{"displayName":"displayName","query":"query","category":"category","version":1,"tags":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/savedSearches/{saved_search_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', saved_search_id='saved_search_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saved_searches_delete(client):
    """Test case for saved_searches_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/savedSearches/{saved_search_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', saved_search_id='saved_search_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saved_searches_get(client):
    """Test case for saved_searches_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/savedSearches/{saved_search_id}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', saved_search_id='saved_search_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_saved_searches_list_by_workspace(client):
    """Test case for saved_searches_list_by_workspace

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.OperationalInsights/workspaces/{workspace_name}/savedSearches'.format(resource_group_name='resource_group_name_example', workspace_name='workspace_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

