# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_searchdocuments(client):
    """Test case for searchdocuments

    Search documents
    """
    params = [('_fields', 'email,firstName,document'),
                    ('_where', 'firstName is not null'),
                    ('_schema', '{{schema}}'),
                    ('_keyword', 'String to search'),
                    ('_sort', 'firstName ASC')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/vnd.vtex.ds.v10+json',
        'rest_range': 'resources=0-10',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{acronym}/search'.format(acronym='{{acronym}}'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

