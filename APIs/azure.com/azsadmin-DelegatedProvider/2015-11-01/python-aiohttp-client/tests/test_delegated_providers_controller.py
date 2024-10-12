# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delegated_providers_list200_response import DelegatedProvidersList200Response
from openapi_server.models.delegated_providers_list200_response_value_inner import DelegatedProvidersList200ResponseValueInner


pytestmark = pytest.mark.asyncio

async def test_delegated_providers_get(client):
    """Test case for delegated_providers_get

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegated_provider}'.format(subscription_id='subscription_id_example', delegated_provider='delegated_provider_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delegated_providers_list(client):
    """Test case for delegated_providers_list

    
    """
    params = [('api-version', '2015-11-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Subscriptions.Admin/delegatedProviders'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

