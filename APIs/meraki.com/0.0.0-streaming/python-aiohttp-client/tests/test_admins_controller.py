# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_admin_request import CreateOrganizationAdminRequest
from openapi_server.models.update_organization_admin_request import UpdateOrganizationAdminRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_admin(client):
    """Test case for create_organization_admin

    Create a new dashboard administrator
    """
    body = openapi_server.CreateOrganizationAdminRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/organizations/{organization_id}/admins'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_admin(client):
    """Test case for delete_organization_admin

    Revoke all access for a dashboard administrator within this organization
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/organizations/{organization_id}/admins/{admin_id}'.format(organization_id='organization_id_example', admin_id='admin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_admins(client):
    """Test case for get_organization_admins

    List the dashboard administrators in this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/admins'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_admin(client):
    """Test case for update_organization_admin

    Update an administrator
    """
    body = openapi_server.UpdateOrganizationAdminRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/organizations/{organization_id}/admins/{admin_id}'.format(organization_id='organization_id_example', admin_id='admin_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

