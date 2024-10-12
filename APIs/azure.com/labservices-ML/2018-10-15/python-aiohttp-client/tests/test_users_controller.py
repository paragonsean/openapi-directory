# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_user import ResponseWithContinuationUser
from openapi_server.models.user import User
from openapi_server.models.user_fragment import UserFragment


pytestmark = pytest.mark.asyncio

async def test_users_create_or_update(client):
    """Test case for users_create_or_update

    
    """
    user = {"properties":{"familyName":"familyName","givenName":"givenName","tenantId":"tenantId","totalUsage":"totalUsage","provisioningState":"provisioningState","latestOperationResult":{"operationUrl":"operationUrl","errorMessage":"errorMessage","errorCode":"errorCode","requestUri":"requestUri","httpMethod":"httpMethod","status":"status"},"email":"email","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/users/{user_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        json=user,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete(client):
    """Test case for users_delete

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/users/{user_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_get(client):
    """Test case for users_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/users/{user_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    
    """
    params = [('$expand', 'expand_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$orderby', 'orderby_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/users'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update(client):
    """Test case for users_update

    
    """
    user = {"properties":{"provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/users/{user_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', user_name='user_name_example'),
        headers=headers,
        json=user,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

