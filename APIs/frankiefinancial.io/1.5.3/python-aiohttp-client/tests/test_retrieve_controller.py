# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_object import ErrorObject
from openapi_server.models.retrieved_response_object import RetrievedResponseObject


pytestmark = pytest.mark.asyncio

async def test_retrieve_result(client):
    """Test case for retrieve_result

    (Re)retrieve Response Result.
    """
    params = [('payload', 'payload_example')]
    headers = { 
        'Accept': 'application/json',
        'x_frankie_customer_id': 'x_frankie_customer_id_example',
        'x_frankie_customer_child_id': 'x_frankie_customer_child_id_example',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/compliance/v1.2/retrieve/response/{request_id}'.format(request_id='request_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

