# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.votes import Votes


pytestmark = pytest.mark.asyncio

async def test_add_vote(client):
    """Test case for add_vote

    Add vote
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/votes'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_votes(client):
    """Test case for get_votes

    Get votes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/votes'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_vote(client):
    """Test case for remove_vote

    Delete vote
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/votes'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

