# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.billing_response_list_result import BillingResponseListResult
from openapi_server.models.capabilities_result import CapabilitiesResult
from openapi_server.models.locations_list_billing_specs_default_response import LocationsListBillingSpecsDefaultResponse
from openapi_server.models.usages_list_result import UsagesListResult


pytestmark = pytest.mark.asyncio

async def test_locations_get_capabilities(client):
    """Test case for locations_get_capabilities

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HDInsight/locations/{location}/capabilities'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_list_billing_specs(client):
    """Test case for locations_list_billing_specs

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HDInsight/locations/{location}/billingSpecs'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_list_usages(client):
    """Test case for locations_list_usages

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.HDInsight/locations/{location}/usages'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

