# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_podcast_response import DeletePodcastResponse
from openapi_server.models.submit_podcast_response import SubmitPodcastResponse


pytestmark = pytest.mark.asyncio

async def test_delete_podcast_by_id(client):
    """Test case for delete_podcast_by_id

    Request to delete a podcast
    """
    params = [('reason', 'the podcaster wants to delete it')]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/podcasts/{id}'.format(id='4d3fe717742d4963a85562e9f84d8c79'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_submit_podcast(client):
    """Test case for submit_podcast

    Submit a podcast to Listen Notes database
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    data = {
        'email': 'email_example',
        'rss': 'rss_example'
        }
    response = await client.request(
        method='POST',
        path='/api/v2/podcasts/submit',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

