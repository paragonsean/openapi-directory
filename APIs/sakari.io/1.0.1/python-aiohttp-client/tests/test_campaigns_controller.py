# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.campaign_request import CampaignRequest
from openapi_server.models.campaign_response import CampaignResponse
from openapi_server.models.campaigns_remove200_response import CampaignsRemove200Response
from openapi_server.models.campaigns_response import CampaignsResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_campaigns_create(client):
    """Test case for campaigns_create

    Create campaign
    """
    body = {"template":"template","filters":{"attributes":["attributes","attributes"],"contacts":["contacts","contacts"],"tags":["tags","tags"]},"trigger":{"code":"M"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/accounts/{account_id}/campaigns'.format(account_id='account_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaigns_fetch(client):
    """Test case for campaigns_fetch

    Fetch campaign by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/campaigns/{campaign_id}'.format(account_id='account_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaigns_fetch_all(client):
    """Test case for campaigns_fetch_all

    Fetch campaigns
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/accounts/{account_id}/campaigns'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaigns_remove(client):
    """Test case for campaigns_remove

    Deletes a campaign
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/accounts/{account_id}/campaigns/{campaign_id}'.format(account_id='account_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_campaigns_update(client):
    """Test case for campaigns_update

    Updates a campaign
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/accounts/{account_id}/campaigns/{campaign_id}'.format(account_id='account_id_example', campaign_id='campaign_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

