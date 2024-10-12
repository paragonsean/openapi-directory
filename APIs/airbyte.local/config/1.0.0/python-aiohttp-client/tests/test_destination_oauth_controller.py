# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.complete_destination_o_auth_request import CompleteDestinationOAuthRequest
from openapi_server.models.destination_oauth_consent_request import DestinationOauthConsentRequest
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.known_exception_info import KnownExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.o_auth_consent_read import OAuthConsentRead
from openapi_server.models.set_instancewide_destination_oauth_params_request_body import SetInstancewideDestinationOauthParamsRequestBody


pytestmark = pytest.mark.asyncio

async def test_complete_destination_o_auth(client):
    """Test case for complete_destination_o_auth

    Given a destination def ID generate an access/refresh token etc.
    """
    body = {"redirectUrl":"redirectUrl","queryParams":{"key":""},"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","oAuthInputConfiguration":"","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_oauths/complete_oauth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_destination_o_auth_consent(client):
    """Test case for get_destination_o_auth_consent

    Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.
    """
    body = {"redirectUrl":"redirectUrl","destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","oAuthInputConfiguration":"","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_oauths/get_consent_url',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_instancewide_destination_oauth_params(client):
    """Test case for set_instancewide_destination_oauth_params

    Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables. 
    """
    body = {"destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","params":{"key":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destination_oauths/oauth_params/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

