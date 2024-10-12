# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.transparent_data_encryption import TransparentDataEncryption
from openapi_server.models.transparent_data_encryption_activity_list_result import TransparentDataEncryptionActivityListResult


pytestmark = pytest.mark.asyncio

async def test_transparent_data_encryption_activities_list_by_configuration(client):
    """Test case for transparent_data_encryption_activities_list_by_configuration

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/transparentDataEncryption/{transparent_data_encryption_name}/operationResults'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', transparent_data_encryption_name='transparent_data_encryption_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transparent_data_encryptions_create_or_update(client):
    """Test case for transparent_data_encryptions_create_or_update

    
    """
    parameters = {"location":"location","properties":{"status":"Enabled"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/transparentDataEncryption/{transparent_data_encryption_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', transparent_data_encryption_name='transparent_data_encryption_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_transparent_data_encryptions_get(client):
    """Test case for transparent_data_encryptions_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/transparentDataEncryption/{transparent_data_encryption_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', transparent_data_encryption_name='transparent_data_encryption_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

