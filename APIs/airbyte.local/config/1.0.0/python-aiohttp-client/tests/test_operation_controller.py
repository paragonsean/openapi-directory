# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_operation_read import CheckOperationRead
from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.operation_create import OperationCreate
from openapi_server.models.operation_id_request_body import OperationIdRequestBody
from openapi_server.models.operation_read import OperationRead
from openapi_server.models.operation_read_list import OperationReadList
from openapi_server.models.operation_update import OperationUpdate
from openapi_server.models.operator_configuration import OperatorConfiguration


pytestmark = pytest.mark.asyncio

async def test_check_operation(client):
    """Test case for check_operation

    Check if an operation to be created is valid
    """
    body = {"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/operations/check',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_operation(client):
    """Test case for create_operation

    Create an operation to be applied as part of a connection pipeline
    """
    body = {"name":"name","operatorConfiguration":{"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"},"workspaceId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/operations/create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_operation(client):
    """Test case for delete_operation

    Delete an operation
    """
    body = {"operationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/operations/delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_operation(client):
    """Test case for get_operation

    Returns an operation
    """
    body = {"operationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/operations/get',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_operations_for_connection(client):
    """Test case for list_operations_for_connection

    Returns all operations for a connection.
    """
    body = {"connectionId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/operations/list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_operation(client):
    """Test case for update_operation

    Update an operation
    """
    body = {"name":"name","operationId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","operatorConfiguration":{"webhook":{"webhookConfigId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","dbtCloud":{"accountId":0,"jobId":6},"executionUrl":"executionUrl","executionBody":"executionBody","webhookType":"dbtCloud"},"normalization":{"option":"basic"},"dbt":{"gitRepoBranch":"gitRepoBranch","dockerImage":"dockerImage","dbtArguments":"dbtArguments","gitRepoUrl":"gitRepoUrl"},"operatorType":"normalization"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/operations/update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

