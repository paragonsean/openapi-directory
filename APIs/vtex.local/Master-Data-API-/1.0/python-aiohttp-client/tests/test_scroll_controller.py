# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_scrolldocuments(client):
    """Test case for scrolldocuments

    Scroll documents
    """
    params = [('_token', '{tokenValueExample}'),
                    ('_fields', 'email,firstName,document'),
                    ('_where', 'firstName is not null.'),
                    ('_schema', 'schema'),
                    ('_keyword', 'String to search'),
                    ('_sort', 'firstName ASC')]
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'rest_range': 'resources=0-10',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{data_entity_name}/scroll'.format(data_entity_name='Client'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

