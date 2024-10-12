# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_organization_saml_idp_request import CreateOrganizationSamlIdpRequest
from openapi_server.models.get_organization_saml_idps200_response_inner import GetOrganizationSamlIdps200ResponseInner
from openapi_server.models.update_organization_saml_idp_request import UpdateOrganizationSamlIdpRequest


pytestmark = pytest.mark.asyncio

async def test_create_organization_saml_idp_2(client):
    """Test case for create_organization_saml_idp_2

    Create a SAML IdP for your organization.
    """
    body = openapi_server.CreateOrganizationSamlIdpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/organizations/{organization_id}/saml/idps'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_organization_saml_idp_2(client):
    """Test case for delete_organization_saml_idp_2

    Remove a SAML IdP in your organization.
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/organizations/{organization_id}/saml/idps/{idp_id}'.format(organization_id='organization_id_example', idp_id='idp_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_idp_2(client):
    """Test case for get_organization_saml_idp_2

    Get a SAML IdP from your organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/saml/idps/{idp_id}'.format(organization_id='organization_id_example', idp_id='idp_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_saml_idps_2(client):
    """Test case for get_organization_saml_idps_2

    List the SAML IdPs in your organization.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/saml/idps'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_saml_idp_2(client):
    """Test case for update_organization_saml_idp_2

    Update a SAML IdP in your organization
    """
    body = openapi_server.UpdateOrganizationSamlIdpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/saml/idps/{idp_id}'.format(organization_id='organization_id_example', idp_id='idp_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

