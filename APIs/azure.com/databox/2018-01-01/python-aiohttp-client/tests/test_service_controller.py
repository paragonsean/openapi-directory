# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.address_validation_output import AddressValidationOutput
from openapi_server.models.available_sku_request import AvailableSkuRequest
from openapi_server.models.available_skus_result import AvailableSkusResult
from openapi_server.models.validate_address import ValidateAddress


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

async def test_service_validate_address(client):
    """Test case for service_validate_address

    
    """
    validate_address = {"deviceType":"DataBox","shippingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","zipExtendedCode":"zipExtendedCode","addressType":"None","companyName":"companyName","postalCode":"postalCode","streetAddress1":"streetAddress1","streetAddress2":"streetAddress2","streetAddress3":"streetAddress3"}}
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

