# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apis_filter import ApisFilter
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_api_response import GetApiResponse
from openapi_server.models.get_apis_response import GetApisResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse


pytestmark = pytest.mark.asyncio

async def test_apis_all(client):
    """Test case for apis_all

    List APIs
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.ApisFilter())]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/apis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apis_one(client):
    """Test case for apis_one

    Get API
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/apis/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

