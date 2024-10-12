# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api401_response import API401Response
from openapi_server.models.api404_response import API404Response
from openapi_server.models.get_feed_versions_response import GetFeedVersionsResponse
from openapi_server.models.get_feeds_response import GetFeedsResponse
from openapi_server.models.get_latest_feed_version_response import GetLatestFeedVersionResponse
from openapi_server.models.get_locations_response import GetLocationsResponse


pytestmark = pytest.mark.asyncio

async def test_get_feed_versions(client):
    """Test case for get_feed_versions

    Retrieve a list of versions of specified (or all) feeds.
    """
    params = [('key', 'YOUR_API_KEY'),
                    ('feed', 'feed_example'),
                    ('page', 1),
                    ('limit', 10),
                    ('err', 1),
                    ('warn', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/getFeedVersions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feeds(client):
    """Test case for get_feeds

    Retrieve a list of feeds.
    """
    params = [('key', 'YOUR_API_KEY'),
                    ('location', 56),
                    ('descendants', 1),
                    ('page', 1),
                    ('limit', 10),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/getFeeds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_feed_version(client):
    """Test case for get_latest_feed_version

    Retrieve the download URL for the latest version of a feed.
    """
    params = [('key', 'YOUR_API_KEY'),
                    ('feed', 'feed_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/getLatestFeedVersion',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_locations(client):
    """Test case for get_locations

    Retrieve a list of locations.
    """
    params = [('key', 'YOUR_API_KEY')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/getLocations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

