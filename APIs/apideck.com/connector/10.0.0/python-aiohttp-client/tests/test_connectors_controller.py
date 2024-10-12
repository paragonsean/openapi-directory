# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.connectors_filter import ConnectorsFilter
from openapi_server.models.get_connector_response import GetConnectorResponse
from openapi_server.models.get_connectors_response import GetConnectorsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse


pytestmark = pytest.mark.asyncio

async def test_connectors_all(client):
    """Test case for connectors_all

    List Connectors
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.ConnectorsFilter())]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/connectors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connectors_one(client):
    """Test case for connectors_one

    Get Connector
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/connectors/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

