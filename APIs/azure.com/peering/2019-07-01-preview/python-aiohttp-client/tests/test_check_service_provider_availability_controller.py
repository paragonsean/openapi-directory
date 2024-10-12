# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_service_provider_availability_input import CheckServiceProviderAvailabilityInput
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_check_service_provider_availability(client):
    """Test case for check_service_provider_availability

    
    """
    check_service_provider_availability_input = {"peeringServiceLocation":"peeringServiceLocation","peeringServiceProvider":"peeringServiceProvider"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Peering/CheckServiceProviderAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=check_service_provider_availability_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

