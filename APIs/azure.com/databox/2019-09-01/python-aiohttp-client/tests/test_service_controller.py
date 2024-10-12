# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_validation_output import AddressValidationOutput
from openapi_server.models.available_sku_request import AvailableSkuRequest
from openapi_server.models.available_skus_result import AvailableSkusResult
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.region_configuration_request import RegionConfigurationRequest
from openapi_server.models.region_configuration_response import RegionConfigurationResponse
from openapi_server.models.validate_address import ValidateAddress
from openapi_server.models.validation_request import ValidationRequest
from openapi_server.models.validation_response import ValidationResponse


pytestmark = pytest.mark.asyncio

async def test_service_list_available_skus(client):
    """Test case for service_list_available_skus

    
    """
    available_sku_request = {"country":"country","transferType":"ImportToAzure","location":"location","skuNames":["DataBox","DataBox"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataBox/locations/{location}/availableSkus'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=available_sku_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_list_available_skus_by_resource_group(client):
    """Test case for service_list_available_skus_by_resource_group

    
    """
    available_sku_request = {"country":"country","transferType":"ImportToAzure","location":"location","skuNames":["DataBox","DataBox"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/locations/{location}/availableSkus'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        json=available_sku_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_region_configuration(client):
    """Test case for service_region_configuration

    
    """
    region_configuration_request = {"transportAvailabilityRequest":{"skuName":"DataBox"},"scheduleAvailabilityRequest":{"skuName":"DataBox","storageLocation":"storageLocation"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataBox/locations/{location}/regionConfiguration'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=region_configuration_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_validate_address(client):
    """Test case for service_validate_address

    
    """
    validate_address = {"deviceType":"DataBox","shippingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","zipExtendedCode":"zipExtendedCode","addressType":"None","companyName":"companyName","postalCode":"postalCode","streetAddress1":"streetAddress1","streetAddress2":"streetAddress2","streetAddress3":"streetAddress3"},"transportPreferences":{"preferredShipmentType":"CustomerManaged"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataBox/locations/{location}/validateAddress'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=validate_address,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_validate_inputs(client):
    """Test case for service_validate_inputs

    
    """
    validation_request = {"validationCategory":"JobCreationValidation","individualRequestDetails":[{"validationType":"ValidateAddress"},{"validationType":"ValidateAddress"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataBox/locations/{location}/validateInputs'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=validation_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_validate_inputs_by_resource_group(client):
    """Test case for service_validate_inputs_by_resource_group

    
    """
    validation_request = {"validationCategory":"JobCreationValidation","individualRequestDetails":[{"validationType":"ValidateAddress"},{"validationType":"ValidateAddress"}]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/locations/{location}/validateInputs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        json=validation_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

