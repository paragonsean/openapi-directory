# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.vote import Vote
from openapi_server.models.votes_post_request import VotesPostRequest


pytestmark = pytest.mark.asyncio

async def test_votes_get(client):
    """Test case for votes_get

    
    """
    params = [('user_id', 56),
                    ('feature_id', 56),
                    ('positive', True),
                    ('negative', True),
                    ('offset', 3.4),
                    ('limit', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/votes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_votes_post(client):
    """Test case for votes_post

    update specified votes for a User
    """
    data = openapi_server.VotesPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/votes',
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

