# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_api_definition import ManagedApiDefinition
from openapi_server.models.managed_api_definition_collection import ManagedApiDefinitionCollection


pytestmark = pytest.mark.asyncio

async def test_managed_apis_get(client):
    """Test case for managed_apis_get

    Gets managed API
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/managedApis/{api_name}'.format(subscription_id='subscription_id_example', location='location_example', api_name='api_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_apis_list(client):
    """Test case for managed_apis_list

    Lists managed APIs
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/managedApis'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

