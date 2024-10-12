# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment import Environment
from openapi_server.models.environment_fragment import EnvironmentFragment
from openapi_server.models.reset_password_payload import ResetPasswordPayload
from openapi_server.models.response_with_continuation_environment import ResponseWithContinuationEnvironment


pytestmark = pytest.mark.asyncio

async def test_environments_claim(client):
    """Test case for environments_claim

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}/claim'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_create_or_update(client):
    """Test case for environments_create_or_update

    
    """
    environment = {"properties":{"claimedByUserName":"claimedByUserName","claimedByUserPrincipalId":"claimedByUserPrincipalId","lastKnownPowerState":"lastKnownPowerState","networkInterface":{"rdpAuthority":"rdpAuthority","privateIpAddress":"privateIpAddress","sshAuthority":"sshAuthority","username":"username"},"claimedByUserObjectId":"claimedByUserObjectId","resourceSets":{"resourceSettingId":"resourceSettingId","vmResourceId":"vmResourceId"},"totalUsage":"totalUsage","provisioningState":"provisioningState","isClaimed":True,"latestOperationResult":{"operationUrl":"operationUrl","errorMessage":"errorMessage","errorCode":"errorCode","requestUri":"requestUri","httpMethod":"httpMethod","status":"status"},"passwordLastReset":"2000-01-23T04:56:07.000+00:00","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        json=environment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_delete(client):
    """Test case for environments_delete

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_get(client):
    """Test case for environments_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_list(client):
    """Test case for environments_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_reset_password(client):
    """Test case for environments_reset_password

    
    """
    reset_password_payload = {"password":"password","environmentId":"environmentId","username":"username"}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}/resetPassword'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        json=reset_password_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_start(client):
    """Test case for environments_start

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_stop(client):
    """Test case for environments_stop

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environments_update(client):
    """Test case for environments_update

    
    """
    environment = {"properties":{"resourceSets":{"resourceSettingId":"resourceSettingId","vmResourceId":"vmResourceId"},"provisioningState":"provisioningState","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/environments/{environment_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example', environment_name='environment_name_example'),
        headers=headers,
        json=environment,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

