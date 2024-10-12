# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subscription_cycle_response import SubscriptionCycleResponse


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_cycles_cycle_id_get(client):
    """Test case for api_rns_pub_cycles_cycle_id_get

    Get cycle details
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pub/cycles/{cycle_id}'.format(cycle_id='cycle_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_cycles_cycle_id_retry_post(client):
    """Test case for api_rns_pub_cycles_cycle_id_retry_post

    Retry cycle
    """
    headers = { 
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rns/pub/cycles/{cycle_id}/retry'.format(cycle_id='cycle_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_rns_pub_cycles_get(client):
    """Test case for api_rns_pub_cycles_get

    List cycles
    """
    params = [('beginDate', 'begin_date_example'),
                    ('endDate', 'end_date_example'),
                    ('subscriptionId', 'subscription_id_example'),
                    ('customerEmail', 'customer_email_example'),
                    ('status', 'status_example'),
                    ('page', 1),
                    ('size', 15)]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/rns/pub/cycles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

