# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.store_tracking_status import StoreTrackingStatus
from openapi_server.models.tracked_clicks import TrackedClicks
from openapi_server.models.tracked_external_orders import TrackedExternalOrders
from openapi_server.models.tracked_orders import TrackedOrders
from openapi_server.models.tracking_status import TrackingStatus


pytestmark = pytest.mark.asyncio

async def test_get_store_tracked_clicks(client):
    """Test case for get_store_tracked_clicks

    Get the latest tracked clicks
    """
    params = [('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/tracking/clicks'.format(store_id='store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_tracked_external_orders(client):
    """Test case for get_store_tracked_external_orders

    Get the latest tracked external orders
    """
    params = [('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/tracking/externalorders'.format(store_id='store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_tracked_orders(client):
    """Test case for get_store_tracked_orders

    Get the latest tracked orders
    """
    params = [('count', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/tracking/orders'.format(store_id='store_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_store_tracking_status(client):
    """Test case for get_store_tracking_status

    Get the synchronization status of clicks and orders of a store
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/{store_id}/tracking/status'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tracking_status(client):
    """Test case for get_tracking_status

    Get the global synchronization status of clicks and orders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/analytics/tracking/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

