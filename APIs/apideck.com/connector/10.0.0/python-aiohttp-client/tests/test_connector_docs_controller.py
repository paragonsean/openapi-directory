# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse


pytestmark = pytest.mark.asyncio

async def test_connector_docs_one(client):
    """Test case for connector_docs_one

    Get Connector Doc content
    """
    headers = { 
        'Accept': 'application/json',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/connector/connectors/{id}/docs/{doc_id}'.format(id='id_example', doc_id='application_owner+oauth_credentials'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

