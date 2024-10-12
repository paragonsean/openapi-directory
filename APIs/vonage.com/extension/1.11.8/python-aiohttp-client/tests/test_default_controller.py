# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.end_user_route_hal_response import EndUserRouteHalResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.validation_errors_response import ValidationErrorsResponse


pytestmark = pytest.mark.asyncio

async def test_extension_ctrl_get_account_extension_by_id(client):
    """Test case for extension_ctrl_get_account_extension_by_id

    Get extension data by account ID and extension number
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}/extensions/{extension_number}'.format(account_id='account_id_example', extension_number=789),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extension_ctrl_get_account_extensions(client):
    """Test case for extension_ctrl_get_account_extensions

    Get account extensions data by account ID
    """
    params = [('page_size', 10),
                    ('page', 10),
                    ('location_id', 145214),
                    ('phone_number', '14155550100'),
                    ('login_name', 'jsmith'),
                    ('email', 'john.smith@example.com')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}/extensions'.format(account_id='account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

