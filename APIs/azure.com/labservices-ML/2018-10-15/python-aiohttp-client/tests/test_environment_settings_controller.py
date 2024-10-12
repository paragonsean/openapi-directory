# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.environment_setting import EnvironmentSetting
from openapi_server.models.environment_setting_fragment import EnvironmentSettingFragment
from openapi_server.models.publish_payload import PublishPayload
from openapi_server.models.response_with_continuation_environment_setting import ResponseWithContinuationEnvironmentSetting


pytestmark = pytest.mark.asyncio

async def test_environment_settings_claim_any(client):
    """Test case for environment_settings_claim_any

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/claimAny'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_create_or_update(client):
    """Test case for environment_settings_create_or_update

    
    """
    environment_setting = {"properties":{"resourceSettings":{"cores":0,"imageName":"imageName","galleryImageResourceId":"galleryImageResourceId","size":"Basic","referenceVm":{"password":"password","vmStateDetails":{"powerState":"powerState","lastKnownPowerState":"lastKnownPowerState","rdpAuthority":"rdpAuthority","sshAuthority":"sshAuthority"},"userName":"userName","vmResourceId":"vmResourceId"},"id":"id"},"lastChanged":"2000-01-23T04:56:07.000+00:00","description":"description","lastPublished":"2000-01-23T04:56:07.000+00:00","provisioningState":"provisioningState","latestOperationResult":{"operationUrl":"operationUrl","errorMessage":"errorMessage","errorCode":"errorCode","requestUri":"requestUri","httpMethod":"httpMethod","status":"status"},"title":"title","configurationState":"NotApplicable","publishingState":"Draft","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        json=environment_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_delete(client):
    """Test case for environment_settings_delete

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_get(client):
    """Test case for environment_settings_get

    
    """
    params = [('$expand', 'expand_example'),
                    ('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_list(client):
    """Test case for environment_settings_list

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_publish(client):
    """Test case for environment_settings_publish

    
    """
    publish_payload = {"useExistingImage":True}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/publish'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        json=publish_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_start(client):
    """Test case for environment_settings_start

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/start'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_stop(client):
    """Test case for environment_settings_stop

    
    """
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}/stop'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_environment_settings_update(client):
    """Test case for environment_settings_update

    
    """
    environment_setting = {"properties":{"resourceSettings":{"galleryImageResourceId":"galleryImageResourceId","size":"Basic","referenceVm":{"password":"password","userName":"userName"}},"description":"description","provisioningState":"provisioningState","title":"title","configurationState":"NotApplicable","uniqueIdentifier":"uniqueIdentifier"}}
    params = [('api-version', '2018-10-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.LabServices/labaccounts/{lab_account_name}/labs/{lab_name}/environmentsettings/{environment_setting_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_account_name='lab_account_name_example', lab_name='lab_name_example', environment_setting_name='environment_setting_name_example'),
        headers=headers,
        json=environment_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

