# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.org import Org
from openapi_server.models.org_response import OrgResponse


pytestmark = pytest.mark.asyncio

async def test_add_organization(client):
    """Test case for add_organization

    
    """
    org_object = {"name":"name","type":"type","desc":"desc"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/orgs',
        headers=headers,
        json=org_object,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_my_organization(client):
    """Test case for get_my_organization

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/orgs/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

