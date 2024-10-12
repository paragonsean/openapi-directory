# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_web_verifications_get_web_verifications_by_reference_id_request import CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest
from openapi_server.models.credas_api_models_web_verifications_get_web_verifications_by_registration_id_request import CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest
from openapi_server.models.credas_api_models_web_verifications_get_web_verifications_response import CredasApiModelsWebVerificationsGetWebVerificationsResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_web_verifications_by_reference_id(client):
    """Test case for get_web_verifications_by_reference_id

    Retrieves secure links to web verification pages searching by the Reference Id.
    """
    body = openapi_server.CredasApiModelsWebVerificationsGetWebVerificationsByReferenceIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/web-verifications/by-referenceid',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_get_web_verifications_by_registration_id(client):
    """Test case for get_web_verifications_by_registration_id

    Retrieves secure link to web verification page searching by the Registration Id.
    """
    body = openapi_server.CredasApiModelsWebVerificationsGetWebVerificationsByRegistrationIdRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/web-verifications/by-registrationid',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

