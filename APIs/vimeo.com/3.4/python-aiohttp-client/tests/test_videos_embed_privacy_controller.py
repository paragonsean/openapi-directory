# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_add_video_privacy_domain(client):
    """Test case for add_video_privacy_domain

    Permit a video to be embedded on a domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/videos/{video_id}/privacy/domains/{domain}'.format(domain='example.com', video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_privacy_domain(client):
    """Test case for delete_video_privacy_domain

    Restrict a video from being embedded on a domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/privacy/domains/{domain}'.format(domain='example.com', video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_privacy_domains(client):
    """Test case for get_video_privacy_domains

    Get all the domains on which a video can be embedded
    """
    params = [('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/vnd.vimeo.domain+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/privacy/domains'.format(video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

