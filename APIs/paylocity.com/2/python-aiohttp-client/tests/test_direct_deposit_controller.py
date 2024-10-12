# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.direct_deposit import DirectDeposit
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_all_direct_deposit(client):
    """Test case for get_all_direct_deposit

    Get All Direct Deposit
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/directDeposit'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

