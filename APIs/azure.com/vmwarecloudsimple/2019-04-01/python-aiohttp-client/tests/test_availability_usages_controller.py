# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.sku_availability_list_response import SkuAvailabilityListResponse
from openapi_server.models.usage_list_response import UsageListResponse


pytestmark = pytest.mark.asyncio

async def test_skus_availability_list(client):
    """Test case for skus_availability_list

    Implements SkuAvailability List method
    """
    params = [('skuId', 'sku_id_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/availabilities'.format(subscription_id='subscription_id_example', region_id='region_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_usages_list(client):
    """Test case for usages_list

    Implements Usages List method
    """
    params = [('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/locations/{region_id}/usages'.format(subscription_id='subscription_id_example', region_id='region_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

