# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_collection import AlertCollection
from openapi_server.models.configure_alert_request import ConfigureAlertRequest


pytestmark = pytest.mark.asyncio

async def test_replication_alert_settings_create(client):
    """Test case for replication_alert_settings_create

    Configures email notifications for this vault.
    """
    request = {"properties":{"sendToOwners":"sendToOwners","customEmailAddresses":["customEmailAddresses","customEmailAddresses"],"locale":"locale"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationAlertSettings/{alert_setting_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', alert_setting_name='alert_setting_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_alert_settings_get(client):
    """Test case for replication_alert_settings_get

    Gets an email notification(alert) configuration.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationAlertSettings/{alert_setting_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', alert_setting_name='alert_setting_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_alert_settings_list(client):
    """Test case for replication_alert_settings_list

    Gets the list of configured email notification(alert) configurations.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationAlertSettings'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

