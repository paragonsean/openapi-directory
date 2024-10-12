# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.non_primary_state_tax import NonPrimaryStateTax


pytestmark = pytest.mark.asyncio

async def test_add_or_update_non_primary_state_tax(client):
    """Test case for add_or_update_non_primary_state_tax

    Add/update non-primary state tax
    """
    body = openapi_server.NonPrimaryStateTax()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/nonprimaryStateTax'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

