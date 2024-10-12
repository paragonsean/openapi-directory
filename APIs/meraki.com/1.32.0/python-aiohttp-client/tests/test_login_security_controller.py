# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_login_security200_response import GetOrganizationLoginSecurity200Response
from openapi_server.models.update_organization_login_security_request import UpdateOrganizationLoginSecurityRequest


pytestmark = pytest.mark.asyncio

async def test_get_organization_login_security_1(client):
    """Test case for get_organization_login_security_1

    Returns the login security settings for an organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/loginSecurity'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_login_security_1(client):
    """Test case for update_organization_login_security_1

    Update the login security settings for an organization
    """
    body = openapi_server.UpdateOrganizationLoginSecurityRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/loginSecurity'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

