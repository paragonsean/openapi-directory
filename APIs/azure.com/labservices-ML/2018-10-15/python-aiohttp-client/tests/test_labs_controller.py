# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_users_payload import AddUsersPayload
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.lab import Lab
from openapi_server.models.lab_fragment import LabFragment
from openapi_server.models.response_with_continuation_lab import ResponseWithContinuationLab


pytestmark = pytest.mark.asyncio

async def test_labs_add_users(client):
    """Test case for labs_add_users

    
    """
    add_users_payload = {"emailAddresses":["emailAddresses","emailAddresses"]}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/addUsers'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        json=add_users_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_create_or_update(client):
    """Test case for labs_create_or_update

    
    """
    lab = {"properties":{"userAccessMode":"Restricted","createdDate":"2000-01-23T04:56:07.000+00:00","userQuota":6,"createdByObjectId":"createdByObjectId","createdByUserPrincipalName":"createdByUserPrincipalName","maxUsersInLab":0,"provisioningState":"provisioningState","latestOperationResult":{"operationUrl":"operationUrl","errorMessage":"errorMessage","errorCode":"errorCode","requestUri":"requestUri","httpMethod":"httpMethod","status":"status"},"invitationCode":"invitationCode","uniqueIdentifier":"uniqueIdentifier","usageQuota":"usageQuota"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        json=lab,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_delete(client):
    """Test case for labs_delete

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_get(client):
    """Test case for labs_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_list(client):
    """Test case for labs_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_register(client):
    """Test case for labs_register

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/register'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_labs_update(client):
    """Test case for labs_update

    
    """
    lab = {"properties":{"userAccessMode":"Restricted","maxUsersInLab":0,"provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier","usageQuota":"usageQuota"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        json=lab,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

