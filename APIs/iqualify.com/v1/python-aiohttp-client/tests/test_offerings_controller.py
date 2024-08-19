# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offering import Offering
from openapi_server.models.offering_metadata_response import OfferingMetadataResponse
from openapi_server.models.offering_required import OfferingRequired
from openapi_server.models.portfolio_activations import PortfolioActivations


pytestmark = pytest.mark.asyncio

async def test_offerings_current_get(client):
    """Test case for offerings_current_get

    Find active offerings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/current',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_future_get(client):
    """Test case for offerings_future_get

    Find scheduled offerings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/future',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_get(client):
    """Test case for offerings_get

    Find current, past and future offerings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_info_text_pattern_get(client):
    """Test case for offerings_info_text_pattern_get

    Find offerings where info field matches the specified textPattern
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/info/{text_pattern}'.format(text_pattern='text_pattern_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_get(client):
    """Test case for offerings_offering_id_get

    Find offering by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}'.format(offering_id='offering_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_patch(client):
    """Test case for offerings_offering_id_patch

    Update offering
    """
    body = {"identifier":"identifier","overview":"overview","isReadonly":True,"metadata":{"level":"level","topic":"topic","category":"category","tags":["tags","tags"]},"contentId":"contentId","start":"2000-01-23T04:56:07.000+00:00","description":"description","useRelativeDates":True,"rootContentId":"rootContentId","hasEarlyCloseOff":True,"badge":{"badgeExpiry":{"expires":True,"timeframeAmount":0.8008281904610115,"expiryType":"date","timeframeUnit":"days","expirationDate":"2000-01-23T04:56:07.000+00:00"},"requiresApproval":True,"description":"description","title":"title"},"earlyCloseOffDate":"2000-01-23T04:56:07.000+00:00","name":"name","end":"2000-01-23T04:56:07.000+00:00","trailerVideoUrl":"trailerVideoUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/offerings/{offering_id}'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_past_get(client):
    """Test case for offerings_past_get

    Find past offerings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/past',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_post(client):
    """Test case for offerings_post

    Create offering
    """
    body = {"identifier":"identifier","isReadonly":True,"metadata":{"level":"level","topic":"topic","category":"category","tags":["tags","tags"]},"contentId":"contentId","start":"2000-01-23T04:56:07.000+00:00","description":"description","useRelativeDates":False,"rootContentId":"rootContentId","hasEarlyCloseOff":True,"badge":{"badgeExpiry":{"expires":True,"timeframeAmount":0.8008281904610115,"expiryType":"date","timeframeUnit":"days","expirationDate":"2000-01-23T04:56:07.000+00:00"},"requiresApproval":True,"description":"description","title":"title"},"earlyCloseOffDate":"2000-01-23T04:56:07.000+00:00","name":"name","createDefaultChannels":False,"end":"2000-01-23T04:56:07.000+00:00","trailerVideoUrl":"trailerVideoUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_summary_get(client):
    """Test case for offerings_summary_get

    Offerings summary
    """
    params = [('$top', '50'),
                    ('$orderby', 'orderby_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

