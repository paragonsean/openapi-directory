# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaign_wrapped import CampaignWrapped
from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.syndicate_marshaller_wrapped import SyndicateMarshallerWrapped


pytestmark = pytest.mark.asyncio

async def test_resources_campaigns_id_json_get(client):
    """Test case for resources_campaigns_id_json_get

    Get Campaign by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/campaigns/{id_jso}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_campaigns_id_media_json_get(client):
    """Test case for resources_campaigns_id_media_json_get

    Get MediaItems by Campaign ID
    """
    params = [('sort', 'sort_example'),
                    ('max', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/campaigns/{id}/media.json'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_campaigns_id_syndicate_format_get(client):
    """Test case for resources_campaigns_id_syndicate_format_get

    Get MediaItems for Campaign
    """
    params = [('displayMethod', 'display_method_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/campaigns/{id}/syndicate.{format}'.format(id=56, format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resources_campaigns_json_get(client):
    """Test case for resources_campaigns_json_get

    Get Campaigns
    """
    params = [('max', 56),
                    ('offset', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/resources/campaigns.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

