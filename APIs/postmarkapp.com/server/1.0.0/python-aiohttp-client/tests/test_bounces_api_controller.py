# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bounce_activation_response import BounceActivationResponse
from openapi_server.models.bounce_dump_response import BounceDumpResponse
from openapi_server.models.bounce_info_response import BounceInfoResponse
from openapi_server.models.bounce_search_response import BounceSearchResponse
from openapi_server.models.delivery_stats_response import DeliveryStatsResponse
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse


pytestmark = pytest.mark.asyncio

async def test_activate_bounce(client):
    """Test case for activate_bounce

    Activate a bounce
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='PUT',
        path='/bounces/{bounceid}/activate'.format(bounceid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bounces_bounceid_dump_get(client):
    """Test case for bounces_bounceid_dump_get

    Get bounce dump
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/bounces/{bounceid}/dump'.format(bounceid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bounces(client):
    """Test case for get_bounces

    Get bounces
    """
    params = [('count', 56),
                    ('offset', 56),
                    ('type', 'type_example'),
                    ('inactive', True),
                    ('emailFilter', 'email_filter_example'),
                    ('messageID', 'message_id_example'),
                    ('tag', 'tag_example'),
                    ('todate', '2013-10-20'),
                    ('fromdate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/bounces',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_delivery_stats(client):
    """Test case for get_delivery_stats

    Get delivery stats
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/deliverystats',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_bounce(client):
    """Test case for get_single_bounce

    Get a single bounce
    """
    headers = { 
        'Accept': 'application/json',
        'x_postmark_server_token': 'x_postmark_server_token_example',
    }
    response = await client.request(
        method='GET',
        path='/bounces/{bounceid}'.format(bounceid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

