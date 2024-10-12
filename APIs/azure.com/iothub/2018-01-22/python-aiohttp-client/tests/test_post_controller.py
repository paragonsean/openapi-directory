# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.export_devices_request import ExportDevicesRequest
from openapi_server.models.import_devices_request import ImportDevicesRequest
from openapi_server.models.iot_hub_name_availability_info import IotHubNameAvailabilityInfo
from openapi_server.models.job_response import JobResponse
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server.models.shared_access_signature_authorization_rule import SharedAccessSignatureAuthorizationRule
from openapi_server.models.shared_access_signature_authorization_rule_list_result import SharedAccessSignatureAuthorizationRuleListResult


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_check_name_availability(client):
    """Test case for iot_hub_resource_check_name_availability

    Check if an IoT hub name is available.
    """
    operation_inputs = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Devices/checkNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=operation_inputs,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_export_devices(client):
    """Test case for iot_hub_resource_export_devices

    Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.
    """
    export_devices_parameters = {"excludeKeys":True,"exportBlobContainerUri":"exportBlobContainerUri"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/exportDevices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=export_devices_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_get_keys_for_key_name(client):
    """Test case for iot_hub_resource_get_keys_for_key_name

    Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/IotHubKeys/{key_name}/listkeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', key_name='key_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_import_devices(client):
    """Test case for iot_hub_resource_import_devices

    Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities.
    """
    import_devices_parameters = {"outputBlobContainerUri":"outputBlobContainerUri","inputBlobContainerUri":"inputBlobContainerUri"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/importDevices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=import_devices_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_list_keys(client):
    """Test case for iot_hub_resource_list_keys

    Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/listkeys'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

