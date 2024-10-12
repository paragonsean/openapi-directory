# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_drive_group_response import CreateDriveGroupResponse
from openapi_server.models.delete_drive_group_response import DeleteDriveGroupResponse
from openapi_server.models.drive_group import DriveGroup
from openapi_server.models.drive_groups_filter import DriveGroupsFilter
from openapi_server.models.get_drive_group_response import GetDriveGroupResponse
from openapi_server.models.get_drive_groups_response import GetDriveGroupsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_drive_group_response import UpdateDriveGroupResponse


pytestmark = pytest.mark.asyncio

async def test_drive_groups_add(client):
    """Test case for drive_groups_add

    Create DriveGroup
    """
    body = {"updated_at":"2020-09-30T07:43:32Z","name":"accounting","updated_by":"12345","created_at":"2020-09-30T07:43:32Z","description":"A description","id":"12345","display_name":"accounting","created_by":"12345","custom_mappings":"{}"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/file-storage/drive-groups',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_groups_all(client):
    """Test case for drive_groups_all

    List DriveGroups
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.DriveGroupsFilter()),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/file-storage/drive-groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_groups_delete(client):
    """Test case for drive_groups_delete

    Delete DriveGroup
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/file-storage/drive-groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_groups_one(client):
    """Test case for drive_groups_one

    Get DriveGroup
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/file-storage/drive-groups/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_drive_groups_update(client):
    """Test case for drive_groups_update

    Update DriveGroup
    """
    body = {"updated_at":"2020-09-30T07:43:32Z","name":"accounting","updated_by":"12345","created_at":"2020-09-30T07:43:32Z","description":"A description","id":"12345","display_name":"accounting","created_by":"12345","custom_mappings":"{}"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/file-storage/drive-groups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

