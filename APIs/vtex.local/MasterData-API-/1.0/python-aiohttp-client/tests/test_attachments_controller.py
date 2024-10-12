# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData



pytestmark = pytest.mark.asyncio

async def test_retrieveattachment(client):
    """Test case for retrieveattachment

    Retrieve attachment
    """
    headers = { 
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/dataentities/{acronym}/documents/{id}/{_field}/attachments/{file_name}'.format(acronym='{{acronym}}', id='{{id}}', _field='{{field}}', file_name='{{file-name}}'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_saveattachment(client):
    """Test case for saveattachment

    Save attachment
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    data = FormData()
    data.add_field('file', ['/path/to/file'])
    response = await client.request(
        method='POST',
        path='/api/dataentities/{acronym}/documents/{id}/{_field}/attachments'.format(acronym='{{acronym}}', id='{{id}}', _field='{{field}}'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

