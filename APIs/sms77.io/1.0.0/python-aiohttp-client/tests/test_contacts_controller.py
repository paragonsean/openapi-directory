# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_contacts_get(client):
    """Test case for contacts_get

    
    """
    params = [('action', 'action_example'),
                    ('json', 0)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_post(client):
    """Test case for contacts_post

    
    """
    params = [('action', 'action_example'),
                    ('json', 0),
                    ('id', 'id_example'),
                    ('nick', 'nick_example'),
                    ('empfaenger', 'empfaenger_example'),
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

