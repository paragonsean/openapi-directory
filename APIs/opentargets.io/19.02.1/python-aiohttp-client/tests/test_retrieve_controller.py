# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_association_by_id_0(client):
    """Test case for get_association_by_id_0

    Get association by id
    """
    params = [('id', 'id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/association',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_evidence_by_id_0(client):
    """Test case for get_evidence_by_id_0

    Get evidence by ID
    """
    params = [('id', 'id_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/v3/platform/public/evidence',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_evidence_by_id_0(client):
    """Test case for post_evidence_by_id_0

    Get evidence for a list of IDs
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v3/platform/public/evidence',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

