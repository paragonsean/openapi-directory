# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_credentials_parameters import GenerateCredentialsParameters
from openapi_server.models.generate_credentials_result import GenerateCredentialsResult


pytestmark = pytest.mark.asyncio

async def test_registries_generate_credentials(client):
    """Test case for registries_generate_credentials

    
    """
    generate_credentials_parameters = {"tokenId":"tokenId","name":"password1","expiry":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerRegistry/registries/{registry_name}/generateCredentials'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', registry_name='registry_name_example'),
        headers=headers,
        json=generate_credentials_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

