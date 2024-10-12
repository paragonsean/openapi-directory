# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_reg_types_reg_type import CredasApiModelsRegTypesRegType


pytestmark = pytest.mark.asyncio

async def test_get_all(client):
    """Test case for get_all

    Gets all available RegTypes.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/reg-types',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

