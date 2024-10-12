# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_role import ApplicationRole


pytestmark = pytest.mark.asyncio

async def test_get_all_application_roles(client):
    """Test case for get_all_application_roles

    Get all application roles
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/applicationrole',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_role(client):
    """Test case for get_application_role

    Get application role
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/applicationrole/{key}'.format(key='jira-software'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

