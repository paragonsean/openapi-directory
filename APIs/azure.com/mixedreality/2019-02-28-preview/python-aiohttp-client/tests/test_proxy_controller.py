# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_name_availability_request import CheckNameAvailabilityRequest
from openapi_server.models.check_name_availability_response import CheckNameAvailabilityResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.operation_list import OperationList
from openapi_server.models.spatial_anchors_account_list import SpatialAnchorsAccountList


pytestmark = pytest.mark.asyncio

async def test_check_name_availability_local(client):
    """Test case for check_name_availability_local

    
    """
    check_name_availability = {"name":"name","type":"type"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MixedReality/locations/{location}/checkNameAvailability'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=check_name_availability,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.MixedReality/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_spatial_anchors_accounts_list_by_subscription_0(client):
    """Test case for spatial_anchors_accounts_list_by_subscription_0

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MixedReality/spatialAnchorsAccounts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

