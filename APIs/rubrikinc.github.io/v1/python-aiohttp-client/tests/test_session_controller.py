# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.session_summary import SessionSummary


pytestmark = pytest.mark.asyncio

async def test_create_session(client):
    """Test case for create_session

    Create user session
    """
    params = [('organization_id', 'organization_id_example'),
                    ('realm', 'realm_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/session',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_session(client):
    """Test case for delete_session

    Delete user session
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/session/{id}'.format(id='me'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

