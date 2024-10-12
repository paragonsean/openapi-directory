# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.popular_error_response import PopularErrorResponse
from openapi_server.models.popular_response import PopularResponse
from openapi_server.models.programmes_response import ProgrammesResponse
from openapi_server.models.radio_error_response import RadioErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_popular_episodes_clips(client):
    """Test case for get_popular_episodes_clips

    Popular Episodes & Clips
    """
    params = [('type', 'type_example'),
                    ('distinct', 'distinct_example'),
                    ('network', 'network_example'),
                    ('network_url_key', 'network_url_key_example'),
                    ('category', 'category_example'),
                    ('format', 'format_example'),
                    ('group', 'group_example'),
                    ('media_type', 'media_type_example'),
                    ('container', 'container_example'),
                    ('media_set', None),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/radio/popular',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_radio_programmes(client):
    """Test case for get_radio_programmes

    Radio programmes
    """
    params = [('kind', 'kind_example'),
                    ('network', 'network_example'),
                    ('network_url_key', 'network_url_key_example'),
                    ('category', 'category_example'),
                    ('sort', 'sort_example'),
                    ('container', 'container_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/radio/programmes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_radio_programmes_by_pid(client):
    """Test case for get_radio_programmes_by_pid

    Available radio programme by Pid
    """
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/radio/programmes/{pid}'.format(pid='pid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_recommendations(client):
    """Test case for get_recommendations

    Recommended Programmes
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('rights', 'rights_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/programmes/recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

