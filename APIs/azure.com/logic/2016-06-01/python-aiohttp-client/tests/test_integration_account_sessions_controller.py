# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.integration_account_session import IntegrationAccountSession
from openapi_server.models.integration_account_session_list_result import IntegrationAccountSessionListResult


pytestmark = pytest.mark.asyncio

async def test_sessions_create_or_update(client):
    """Test case for sessions_create_or_update

    
    """
    session = {"properties":{"createdTime":"2000-01-23T04:56:07.000+00:00","changedTime":"2000-01-23T04:56:07.000+00:00","content":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/sessions/{session_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', session_name='session_name_example'),
        headers=headers,
        json=session,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sessions_delete(client):
    """Test case for sessions_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/sessions/{session_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', session_name='session_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sessions_get(client):
    """Test case for sessions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/sessions/{session_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example', session_name='session_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sessions_list_by_integration_accounts(client):
    """Test case for sessions_list_by_integration_accounts

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Logic/integrationAccounts/{integration_account_name}/sessions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', integration_account_name='integration_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

