# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_stack_collection import ApplicationStackCollection
from openapi_server.models.provider_list_operations200_response import ProviderListOperations200Response


pytestmark = pytest.mark.asyncio

async def test_provider_get_available_stacks(client):
    """Test case for provider_get_available_stacks

    Get available application frameworks and their versions
    """
    params = [('osTypeSelected', 'os_type_selected_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/availableStacks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provider_get_available_stacks_on_prem(client):
    """Test case for provider_get_available_stacks_on_prem

    Get available application frameworks and their versions
    """
    params = [('osTypeSelected', 'os_type_selected_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/availableStacks'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_provider_list_operations(client):
    """Test case for provider_list_operations

    Gets all available operations for the Microsoft.Web resource provider. Also exposes resource metric definitions
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Web/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

