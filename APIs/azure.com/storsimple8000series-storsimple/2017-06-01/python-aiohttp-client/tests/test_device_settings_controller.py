# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.alert_settings import AlertSettings
from openapi_server.models.network_settings import NetworkSettings
from openapi_server.models.network_settings_patch import NetworkSettingsPatch
from openapi_server.models.security_settings import SecuritySettings
from openapi_server.models.security_settings_patch import SecuritySettingsPatch
from openapi_server.models.time_settings import TimeSettings


pytestmark = pytest.mark.asyncio

async def test_device_settings_create_or_update_alert_settings(client):
    """Test case for device_settings_create_or_update_alert_settings

    
    """
    parameters = {"properties":{"emailNotification":"Enabled","alertNotificationCulture":"alertNotificationCulture","notificationToServiceOwners":"Enabled","additionalRecipientEmailList":["additionalRecipientEmailList","additionalRecipientEmailList"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/alertSettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_create_or_update_time_settings(client):
    """Test case for device_settings_create_or_update_time_settings

    
    """
    parameters = {"properties":{"primaryTimeServer":"primaryTimeServer","secondaryTimeServer":["secondaryTimeServer","secondaryTimeServer"],"timeZone":"timeZone"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/timeSettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_get_alert_settings(client):
    """Test case for device_settings_get_alert_settings

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/alertSettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_get_network_settings(client):
    """Test case for device_settings_get_network_settings

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/networkSettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_get_security_settings(client):
    """Test case for device_settings_get_security_settings

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/securitySettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_get_time_settings(client):
    """Test case for device_settings_get_time_settings

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/timeSettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_sync_remotemanagement_certificate(client):
    """Test case for device_settings_sync_remotemanagement_certificate

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/securitySettings/default/syncRemoteManagementCertificate'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_update_network_settings(client):
    """Test case for device_settings_update_network_settings

    
    """
    parameters = {"properties":{"dnsSettings":{"primaryDnsServer":"primaryDnsServer","secondaryDnsServers":["secondaryDnsServers","secondaryDnsServers"],"primaryIpv6DnsServer":"primaryIpv6DnsServer","secondaryIpv6DnsServers":["secondaryIpv6DnsServers","secondaryIpv6DnsServers"]},"networkAdapters":{"value":[{"mode":"Invalid","isDefault":True,"nicIpv6Settings":{"ipv6Gateway":"ipv6Gateway","ipv6Address":"ipv6Address","controller0Ipv6Address":"controller0Ipv6Address","controller1Ipv6Address":"controller1Ipv6Address","ipv6Prefix":"ipv6Prefix"},"netInterfaceStatus":"Enabled","interfaceId":"Invalid","speed":0,"iscsiAndCloudStatus":"Disabled","nicIpv4Settings":{"controller1Ipv4Address":"controller1Ipv4Address","controller0Ipv4Address":"controller0Ipv4Address","ipv4Gateway":"ipv4Gateway","ipv4Address":"ipv4Address","ipv4Netmask":"ipv4Netmask"}},{"mode":"Invalid","isDefault":True,"nicIpv6Settings":{"ipv6Gateway":"ipv6Gateway","ipv6Address":"ipv6Address","controller0Ipv6Address":"controller0Ipv6Address","controller1Ipv6Address":"controller1Ipv6Address","ipv6Prefix":"ipv6Prefix"},"netInterfaceStatus":"Enabled","interfaceId":"Invalid","speed":0,"iscsiAndCloudStatus":"Disabled","nicIpv4Settings":{"controller1Ipv4Address":"controller1Ipv4Address","controller0Ipv4Address":"controller0Ipv4Address","ipv4Gateway":"ipv4Gateway","ipv4Address":"ipv4Address","ipv4Netmask":"ipv4Netmask"}}]}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/networkSettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_device_settings_update_security_settings(client):
    """Test case for device_settings_update_security_settings

    
    """
    parameters = {"properties":{"remoteManagementSettings":{"remoteManagementMode":"Unknown"},"snapshotPassword":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"},"cloudApplianceSettings":{"serviceDataEncryptionKey":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"},"channelIntegrityKey":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"}},"chapSettings":{"initiatorSecret":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"},"initiatorUser":"initiatorUser","targetSecret":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"},"targetUser":"targetUser"},"deviceAdminPassword":{"encryptionAlgorithm":"None","encryptionCertThumbprint":"encryptionCertThumbprint","value":"value"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.StorSimple/managers/{manager_name}/devices/{device_name}/securitySettings/default'.format(device_name='device_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', manager_name='manager_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

