# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_operation_result import AsyncOperationResult
from openapi_server.models.certificate_list_description import CertificateListDescription
from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.iot_dps_sku_definition_list_result import IotDpsSkuDefinitionListResult
from openapi_server.models.provisioning_service_description import ProvisioningServiceDescription
from openapi_server.models.provisioning_service_description_list_result import ProvisioningServiceDescriptionListResult


pytestmark = pytest.mark.asyncio

async def test_dps_certificate_get(client):
    """Test case for dps_certificate_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/certificates/{certificate_name}'.format(certificate_name='certificate_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dps_certificates_list(client):
    """Test case for dps_certificates_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/certificates'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_get(client):
    """Test case for iot_dps_resource_get

    Get the non-security related metadata of the provisioning service.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}'.format(provisioning_service_name='provisioning_service_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_get_operation_result(client):
    """Test case for iot_dps_resource_get_operation_result

    
    """
    params = [('asyncinfo', 'true'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/operationresults/{operation_id}'.format(operation_id='operation_id_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_list_by_resource_group(client):
    """Test case for iot_dps_resource_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_list_by_subscription(client):
    """Test case for iot_dps_resource_list_by_subscription

    Get all the provisioning services in a subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Devices/provisioningServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_list_valid_skus(client):
    """Test case for iot_dps_resource_list_valid_skus

    Get the list of valid SKUs for a provisioning service.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/skus'.format(provisioning_service_name='provisioning_service_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

