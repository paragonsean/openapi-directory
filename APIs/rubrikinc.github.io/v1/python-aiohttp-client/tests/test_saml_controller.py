# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rubrik_saml_metadata_info import RubrikSamlMetadataInfo
from openapi_server.models.rubrik_saml_metadata_summary import RubrikSamlMetadataSummary
from openapi_server.models.saml_sso_authn_request_detail import SamlSsoAuthnRequestDetail
from openapi_server.models.saml_sso_authn_request_info import SamlSsoAuthnRequestInfo
from openapi_server.models.saml_sso_status import SamlSsoStatus


pytestmark = pytest.mark.asyncio

async def test_config_rubrik_saml_metadata(client):
    """Test case for config_rubrik_saml_metadata

    Configure and generate Rubrik SAML metadata
    """
    body = {"hostAddress":"hostAddress"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/saml/rubrik_metadata',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_saml_sso_status(client):
    """Test case for get_saml_sso_status

    Check SAML SSO Status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/saml/sso_status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_make_saml_authn_request(client):
    """Test case for make_saml_authn_request

    Make SAML authentication request
    """
    body = {"isForIdpTest":False,"redirectPath":"redirectPath"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/saml/authn_request/{idp_name}'.format(idp_name='idp_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

