# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_lab_properties import CreateLabProperties
from openapi_server.models.get_regional_availability_response import GetRegionalAvailabilityResponse
from openapi_server.models.lab_account import LabAccount
from openapi_server.models.lab_account_fragment import LabAccountFragment
from openapi_server.models.response_with_continuation_lab_account import ResponseWithContinuationLabAccount


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_create_lab(client):
    """Test case for lab_accounts_create_lab

    
    """
    create_lab_properties = {"name":"name","location":"location","environmentSettingCreationParameters":{"resourceSettingCreationParameters":{"galleryImageResourceId":"galleryImageResourceId","size":"Basic","name":"name","location":"location","referenceVmCreationParameters":{"password":"password","userName":"userName"}}},"labCreationParameters":{"maxUsersInLab":0},"tags":{"key":"tags"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/createLab'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        json=create_lab_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_create_or_update(client):
    """Test case for lab_accounts_create_or_update

    
    """
    lab_account = {"properties":{"sizeConfiguration":{"environmentSizes":[{"minMemory":6.027456183070403,"minNumberOfCores":1,"name":"Basic","vmSizes":[{"memory":5.962133916683182,"price":2.3021358869347655,"computeSize":"computeSize","numberOfCores":5},{"memory":5.962133916683182,"price":2.3021358869347655,"computeSize":"computeSize","numberOfCores":5}],"maxPrice":0.8008281904610115},{"minMemory":6.027456183070403,"minNumberOfCores":1,"name":"Basic","vmSizes":[{"memory":5.962133916683182,"price":2.3021358869347655,"computeSize":"computeSize","numberOfCores":5},{"memory":5.962133916683182,"price":2.3021358869347655,"computeSize":"computeSize","numberOfCores":5}],"maxPrice":0.8008281904610115}]},"enabledRegionSelection":True,"provisioningState":"provisioningState","latestOperationResult":{"operationUrl":"operationUrl","errorMessage":"errorMessage","errorCode":"errorCode","requestUri":"requestUri","httpMethod":"httpMethod","status":"status"},"uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        json=lab_account,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_delete(client):
    """Test case for lab_accounts_delete

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_get(client):
    """Test case for lab_accounts_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_get_regional_availability(client):
    """Test case for lab_accounts_get_regional_availability

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/getRegionalAvailability'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_list_by_resource_group(client):
    """Test case for lab_accounts_list_by_resource_group

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_list_by_subscription(client):
    """Test case for lab_accounts_list_by_subscription

    
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
        path='/subscriptions/{subscription_id}/providers/Microsoft.LabServices/labaccounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_accounts_update(client):
    """Test case for lab_accounts_update

    
    """
    lab_account = {"properties":{"enabledRegionSelection":True,"provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example'),
        headers=headers,
        json=lab_account,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

