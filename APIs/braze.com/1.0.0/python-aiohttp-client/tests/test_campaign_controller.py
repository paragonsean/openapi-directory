# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_campaign_analytics_0(client):
    """Test case for campaign_analytics_0

    Campaign Analytics
    """
    params = [('campaign_id', '{{campaign_identifier}}'),
                    ('length', '7'),
                    ('ending_at', '2020-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/campaigns/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaign_details_0(client):
    """Test case for campaign_details_0

    Campaign Details
    """
    params = [('campaign_id', '{{campaign_identifier}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/campaigns/details',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaign_list_0(client):
    """Test case for campaign_list_0

    Campaign List
    """
    params = [('page', '0'),
                    ('include_archived', 'false'),
                    ('sort_direction', 'desc'),
                    ('last_edit.time[gt]', '2020-06-28T23:59:59-5:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/campaigns/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_analytics_0(client):
    """Test case for send_analytics_0

    Send Analytics
    """
    params = [('campaign_id', '{{campaign_identifier}}'),
                    ('send_id', '{{send_identifier}}'),
                    ('length', '30'),
                    ('ending_at', '2014-12-10T23:59:59-05:00')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/sends/data_series',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

