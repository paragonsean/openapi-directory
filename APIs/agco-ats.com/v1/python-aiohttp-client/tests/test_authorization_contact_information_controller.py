# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apii_paged_response_authorization_codes_shared_models_authorization_contact_information import APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.authorization_codes_shared_models_authorization_contact_information import AuthorizationCodesSharedModelsAuthorizationContactInformation


pytestmark = pytest.mark.asyncio

async def test_authorization_contact_information_get(client):
    """Test case for authorization_contact_information_get

    Get contact information for authorization codes.
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('authorizationCode', 'authorization_code_example'),
                    ('afterDate', '2013-10-20T19:20:30+01:00'),
                    ('beforeDate', '2013-10-20T19:20:30+01:00'),
                    ('dealerCode', 'dealer_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/AuthorizationContactInformation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authorization_contact_information_post(client):
    """Test case for authorization_contact_information_post

    Add contact information for authorization code.
    """
    body = openapi_server.AuthorizationCodesSharedModelsAuthorizationContactInformation()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/AuthorizationContactInformation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

