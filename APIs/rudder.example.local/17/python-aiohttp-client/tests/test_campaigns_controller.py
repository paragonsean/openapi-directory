# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.all_campaigns200_response import AllCampaigns200Response
from openapi_server.models.campaign_details import CampaignDetails
from openapi_server.models.delete_campaign200_response import DeleteCampaign200Response
from openapi_server.models.delete_campaign_event200_response import DeleteCampaignEvent200Response
from openapi_server.models.get_all_campaign_events200_response import GetAllCampaignEvents200Response
from openapi_server.models.get_campaign200_response import GetCampaign200Response
from openapi_server.models.get_events_campaign200_response import GetEventsCampaign200Response
from openapi_server.models.save_campaign200_response import SaveCampaign200Response
from openapi_server.models.save_campaign_event200_response import SaveCampaignEvent200Response
from openapi_server.models.schedule_campaign200_response import ScheduleCampaign200Response


pytestmark = pytest.mark.asyncio

async def test_all_campaigns(client):
    """Test case for all_campaigns

    Get all campaigns details
    """
    params = [('campaignType', 'system-update'),
                    ('status', 'enabled')]
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/campaigns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_campaign(client):
    """Test case for delete_campaign

    Delete a campaign
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/campaigns/{id}'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_campaign_event(client):
    """Test case for delete_campaign_event

    Delete a campaign event details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/campaigns/events/{id}'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_campaign_events(client):
    """Test case for get_all_campaign_events

    Get all campaign events
    """
    params = [('campaignType', 'system-update'),
                    ('state', 'enabled'),
                    ('campaignId', 'system-update'),
                    ('limit', 56),
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
        path='/rudder/api/latest/campaigns/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign(client):
    """Test case for get_campaign

    Get a campaign details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/campaigns/{id}'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_campaign_event(client):
    """Test case for get_campaign_event

    Get a campaign event details
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/campaigns/events/{id}'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_campaign(client):
    """Test case for get_events_campaign

    Get campaign events for a campaign
    """
    params = [('campaignType', 'system-update'),
                    ('state', 'enabled'),
                    ('limit', 56),
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
        path='/rudder/api/latest/campaigns/{id}/events'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_campaign(client):
    """Test case for save_campaign

    Save a campaign
    """
    body = openapi_server.CampaignDetails()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/campaigns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_campaign_event(client):
    """Test case for save_campaign_event

    Update an existing event
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/campaigns/events/{id}'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_campaign(client):
    """Test case for schedule_campaign

    Schedule a campaign event for a campaign
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/campaigns/{id}/schedule'.format(id='0076a379-f32d-4732-9e91-33ab219d8fde'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

