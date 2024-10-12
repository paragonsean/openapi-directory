# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.secret import Secret
from openapi_server.models.secret_fragment import SecretFragment
from openapi_server.models.secret_list import SecretList


pytestmark = pytest.mark.asyncio

async def test_secrets_create_or_update(client):
    """Test case for secrets_create_or_update

    
    """
    secret = {"properties":{"provisioningState":"provisioningState","value":"value","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/secrets/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=secret,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_delete(client):
    """Test case for secrets_delete

    
    """
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/secrets/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_get(client):
    """Test case for secrets_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/secrets/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_list(client):
    """Test case for secrets_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/secrets'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_secrets_update(client):
    """Test case for secrets_update

    
    """
    secret = {"properties":{"value":"value"}}
    params = [('api-version', '2018-09-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/users/{user_name}/secrets/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', user_name='user_name_example', name='name_example'),
        headers=headers,
        json=secret,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

