# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_property_register_property_register_check_request import CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest
from openapi_server.models.credas_api_models_property_register_property_register_check_response import CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_property_register_check(client):
    """Test case for add_property_register_check

    Creates new property registry check against the registration.
    """
    body = openapi_server.CredasApiModelsPropertyRegisterPropertyRegisterCheckRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/property-register',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_property_register_check_result(client):
    """Test case for get_property_register_check_result

    Retrieves property registry check associated with the registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/property-register/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

