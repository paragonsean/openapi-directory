# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.connection_state import ConnectionState
from openapi_server.models.connection_state_create_or_update import ConnectionStateCreateOrUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo


pytestmark = pytest.mark.asyncio

async def test_create_or_update_state(client):
    """Test case for create_or_update_state

    Create or update the state for a connection.
    """
    body = {"connectionState":{"globalState":{"shared_state":"{}","streamStates":[{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"},{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"}]},"stateType":"global","connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","streamState":[{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"},{"streamDescriptor":{"name":"name","namespace":"namespace"},"streamState":"{}"}],"state":"{}"},"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/state/create_or_update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_state(client):
    """Test case for get_state

    Fetch the current state for a connection.
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/state/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

