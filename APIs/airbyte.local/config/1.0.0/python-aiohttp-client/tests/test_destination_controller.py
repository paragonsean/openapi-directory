# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_connection_read import CheckConnectionRead
from openapi_server.models.destination_clone_request_body import DestinationCloneRequestBody
from openapi_server.models.destination_create import DestinationCreate
from openapi_server.models.destination_id_request_body import DestinationIdRequestBody
from openapi_server.models.destination_read import DestinationRead
from openapi_server.models.destination_read_list import DestinationReadList
from openapi_server.models.destination_search import DestinationSearch
from openapi_server.models.destination_update import DestinationUpdate
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.workspace_id_request_body import WorkspaceIdRequestBody


pytestmark = pytest.mark.asyncio

async def test_check_connection_to_destination(client):
    """Test case for check_connection_to_destination

    Check connection to the destination
    """
    body = {"destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/check_connection',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_connection_to_destination_for_update(client):
    """Test case for check_connection_to_destination_for_update

    Check connection for a proposed update to a destination
    """
    body = {"connectionConfiguration":{"user":"charles"},"name":"name","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/check_connection_for_update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clone_destination(client):
    """Test case for clone_destination

    Clone destination
    """
    body = {"destinationConfiguration":{"connectionConfiguration":{"user":"charles"},"name":"name"},"destinationCloneId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/clone',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_destination(client):
    """Test case for create_destination

    Create a destination
    """
    body = {"connectionConfiguration":{"user":"charles"},"name":"name","destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_destination(client):
    """Test case for delete_destination

    Delete the destination
    """
    body = {"destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_destination(client):
    """Test case for get_destination

    Get configured destination
    """
    body = {"destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_destinations_for_workspace(client):
    """Test case for list_destinations_for_workspace

    List configured destinations for a workspace
    """
    body = {"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_destinations(client):
    """Test case for search_destinations

    Search destinations
    """
    body = {"connectionConfiguration":{"user":"charles"},"destinationName":"destinationName","name":"name","destinationDefinitionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_destination(client):
    """Test case for update_destination

    Update a destination
    """
    body = {"connectionConfiguration":{"user":"charles"},"name":"name","destinationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/destinations/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

