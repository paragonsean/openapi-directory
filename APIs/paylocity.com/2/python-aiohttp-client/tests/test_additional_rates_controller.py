# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.additional_rate import AdditionalRate
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_add_or_update_additional_rates(client):
    """Test case for add_or_update_additional_rates

    Add/update additional rates
    """
    body = openapi_server.AdditionalRate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/additionalRates'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

