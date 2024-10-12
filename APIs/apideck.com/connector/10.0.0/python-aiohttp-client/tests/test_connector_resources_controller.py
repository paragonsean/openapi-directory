# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_connector_resource_response import GetConnectorResourceResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unified_api_id import UnifiedApiId


pytestmark = pytest.mark.asyncio

async def test_connector_resources_one(client):
    """Test case for connector_resources_one

    Get Connector Resource
    """
    params = [('unified_api', openapi_server.UnifiedApiId())]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/connectors/{id}/resources/{resource_id}'.format(id='id_example', resource_id='resource_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

