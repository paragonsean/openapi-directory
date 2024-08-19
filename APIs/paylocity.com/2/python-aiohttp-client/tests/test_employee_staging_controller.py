# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.staged_employee import StagedEmployee
from openapi_server.models.tracking_number_response import TrackingNumberResponse


pytestmark = pytest.mark.asyncio

async def test_add_new_employee_to_web_link(client):
    """Test case for add_new_employee_to_web_link

    Add new employee to Web Link
    """
    body = openapi_server.StagedEmployee()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/weblinkstaging/companies/{company_id}/employees/newemployees'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

