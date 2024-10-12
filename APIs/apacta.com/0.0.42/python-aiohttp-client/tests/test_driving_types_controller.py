# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.driving_type import DrivingType
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_driving_types200_response import GetDrivingTypes200Response
from openapi_server.models.post_driving_types_request import PostDrivingTypesRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_driving_types(client):
    """Test case for bulk_delete_driving_types

    Bulk delete driving types
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/driving_types/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_driving_types_driving_type_id(client):
    """Test case for delete_driving_types_driving_type_id

    Delete driving type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/driving_types/{driving_type_id}'.format(driving_type_id='driving_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_driving_types(client):
    """Test case for get_driving_types

    List the driving types of the company
    """
    params = [('q', 'q_example'),
                    ('sort', 'sort_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/driving_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_driving_types_driving_type_id(client):
    """Test case for get_driving_types_driving_type_id

    View driving type
    """
    params = [('driving_type_id2', 'driving_type_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/driving_types/{driving_type_id}'.format(driving_type_id='driving_type_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_driving_types(client):
    """Test case for post_driving_types

    Create driving type
    """
    body = openapi_server.PostDrivingTypesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/driving_types',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_driving_types_driving_type_id(client):
    """Test case for put_driving_types_driving_type_id

    Edit driving type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/driving_types/{driving_type_id}'.format(driving_type_id='driving_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

