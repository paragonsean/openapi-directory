# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_api_resource_coverage_response import GetApiResourceCoverageResponse
from openapi_server.models.get_api_resource_response import GetApiResourceResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse


pytestmark = pytest.mark.asyncio

async def test_api_resource_coverage_one(client):
    """Test case for api_resource_coverage_one

    Get API Resource Coverage
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/apis/{id}/resources/{resource_id}/coverage'.format(id='id_example', resource_id='resource_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_resources_one(client):
    """Test case for api_resources_one

    Get API Resource
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/apis/{id}/resources/{resource_id}'.format(id='id_example', resource_id='resource_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

