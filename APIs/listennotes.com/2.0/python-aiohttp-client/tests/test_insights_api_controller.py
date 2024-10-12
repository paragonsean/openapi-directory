# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.podcast_audience_response import PodcastAudienceResponse
from openapi_server.models.podcast_domain_response import PodcastDomainResponse


pytestmark = pytest.mark.asyncio

async def test_get_podcast_audience(client):
    """Test case for get_podcast_audience

    Fetch audience demographics for a podcast
    """
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/{id}/audience'.format(id='25212ac3c53240a880dd5032e547047b'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_podcasts_by_domain_name(client):
    """Test case for get_podcasts_by_domain_name

    Fetch podcasts by a publisher's domain name
    """
    params = [('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/podcasts/domains/{domain_name}'.format(domain_name='nytimes.com'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

