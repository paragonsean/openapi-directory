# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_saml_role_request import CreateOrganizationSamlRoleRequest
from openapi_server.models.update_organization_saml_role_request import UpdateOrganizationSamlRoleRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_saml_role(client):
    """Test case for create_organization_saml_role

    Create a SAML role
    """
    body = openapi_server.CreateOrganizationSamlRoleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/organizations/{organization_id}/samlRoles'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_role(client):
    """Test case for get_organization_saml_role

    Return a SAML role
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/samlRoles/{saml_role_id}'.format(organization_id='organization_id_example', saml_role_id='saml_role_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_roles(client):
    """Test case for get_organization_saml_roles

    List the SAML roles for this organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/organizations/{organization_id}/samlRoles'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_saml_role(client):
    """Test case for update_organization_saml_role

    Update a SAML role
    """
    body = openapi_server.UpdateOrganizationSamlRoleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/organizations/{organization_id}/samlRoles/{saml_role_id}'.format(organization_id='organization_id_example', saml_role_id='saml_role_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

