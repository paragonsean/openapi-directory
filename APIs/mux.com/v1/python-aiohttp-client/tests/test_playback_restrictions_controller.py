# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_playback_restriction_request import CreatePlaybackRestrictionRequest
from openapi_server.models.list_playback_restrictions_response import ListPlaybackRestrictionsResponse
from openapi_server.models.playback_restriction_response import PlaybackRestrictionResponse
from openapi_server.models.update_referrer_domain_restriction_request import UpdateReferrerDomainRestrictionRequest


pytestmark = pytest.mark.asyncio

async def test_create_playback_restriction(client):
    """Test case for create_playback_restriction

    Create a Playback Restriction
    """
    body = {"referrer":{"allow_no_referrer":False,"allowed_domains":["allowed_domains","allowed_domains"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/video/v1/playback-restrictions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_playback_restriction(client):
    """Test case for delete_playback_restriction

    Delete a Playback Restriction
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/video/v1/playback-restrictions/{playback_restriction_id}'.format(playback_restriction_id='playback_restriction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playback_restriction(client):
    """Test case for get_playback_restriction

    Retrieve a Playback Restriction
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/playback-restrictions/{playback_restriction_id}'.format(playback_restriction_id='playback_restriction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_playback_restrictions(client):
    """Test case for list_playback_restrictions

    List Playback Restrictions
    """
    params = [('page', 1),
                    ('limit', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/video/v1/playback-restrictions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_referrer_domain_restriction(client):
    """Test case for update_referrer_domain_restriction

    Update the Referrer Playback Restriction
    """
    body = {"allow_no_referrer":False,"allowed_domains":["allowed_domains","allowed_domains"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/video/v1/playback-restrictions/{playback_restriction_id}/referrer'.format(playback_restriction_id='playback_restriction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

