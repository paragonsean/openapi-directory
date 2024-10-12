# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.role import Role


pytestmark = pytest.mark.asyncio

async def test_roles_list(client):
    """Test case for roles_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('name', 'name_example'),
                    ('contact', 'contact_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/roles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_roles_read(client):
    """Test case for roles_read

    
    """
    params = [('id2', ['id1,id2,id3']),
                    ('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/roles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

