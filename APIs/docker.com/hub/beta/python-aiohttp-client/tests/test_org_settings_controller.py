# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.org_settings import OrgSettings
from openapi_server.models.v2_orgs_name_settings_put_request import V2OrgsNameSettingsPutRequest


pytestmark = pytest.mark.asyncio

async def test_v2_orgs_name_settings_get(client):
    """Test case for v2_orgs_name_settings_get

    Get organization settings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/orgs/{name}/settings'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v2_orgs_name_settings_put(client):
    """Test case for v2_orgs_name_settings_put

    Update organization settings
    """
    body = openapi_server.V2OrgsNameSettingsPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/orgs/{name}/settings'.format(name='name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

