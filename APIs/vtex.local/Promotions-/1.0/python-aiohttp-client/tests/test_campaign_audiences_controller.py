# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.getcampaignaudiences200_response_inner import Getcampaignaudiences200ResponseInner
from openapi_server.models.getcampaignconfiguration200_response import Getcampaignconfiguration200Response
from openapi_server.models.setcampaignconfiguration200_response import Setcampaignconfiguration200Response
from openapi_server.models.setcampaignconfiguration_request import SetcampaignconfigurationRequest


pytestmark = pytest.mark.asyncio

async def test_getcampaignaudiences(client):
    """Test case for getcampaignaudiences

    Get all campaign audiences
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
        path='/api/rnb/pvt/campaignConfiguration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_getcampaignconfiguration(client):
    """Test case for getcampaignconfiguration

    Get campaign audience configuration
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
        path='/api/rnb/pvt/campaignConfiguration/{campaign_id}'.format(campaign_id='dd270d06-1ed1-47fc-b04e-a2431121b5a4'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setcampaignconfiguration(client):
    """Test case for setcampaignconfiguration

    Create campaign audience
    """
    body = openapi_server.SetcampaignconfigurationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/rnb/pvt/campaignConfiguration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

