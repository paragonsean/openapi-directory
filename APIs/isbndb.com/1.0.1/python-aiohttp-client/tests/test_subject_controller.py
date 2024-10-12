# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.subject import Subject


pytestmark = pytest.mark.asyncio

async def test_subject_name_get(client):
    """Test case for subject_name_get

    Gets subject details
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subject/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subjects_query_get(client):
    """Test case for subjects_query_get

    Search subjects
    """
    params = [('pageSize', 'page_size_example'),
                    ('page', 'page_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/subjects/{query}'.format(query='query_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

