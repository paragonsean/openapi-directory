# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_campaign_event_result200_response import GetCampaignEventResult200Response
from openapi_server.models.get_campaign_event_result_for_node200_response import GetCampaignEventResultForNode200Response
from openapi_server.models.get_campaign_history200_response import GetCampaignHistory200Response


pytestmark = pytest.mark.asyncio

async def test_get_campaign_event_result(client):
    """Test case for get_campaign_event_result

    Get a campaign event result
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/systemUpdate/events/{id}/result'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_event_result_for_node(client):
    """Test case for get_campaign_event_result_for_node

    Get detailed campaign event result for a Node
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/systemUpdate/events/{id}/result/{node_id}'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde', node_id='9a1773c9-0889-40b6-be89-f6504443ac1b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_history(client):
    """Test case for get_campaign_history

    Get a campaign result history
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('before', '2013-10-20'),
                    ('after', '2013-10-20'),
                    ('order', 'order_example'),
                    ('asc', 'asc_example')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/systemUpdate/campaigns/{id}/history'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

