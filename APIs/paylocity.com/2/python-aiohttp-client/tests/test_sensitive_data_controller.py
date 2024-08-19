# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.sensitive_data import SensitiveData


pytestmark = pytest.mark.asyncio

async def test_add_or_update_sensitive_data(client):
    """Test case for add_or_update_sensitive_data

    Add/update sensitive data
    """
    body = openapi_server.SensitiveData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/sensitivedata'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sensitive_data(client):
    """Test case for get_sensitive_data

    Get sensitive data
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/sensitivedata'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

