# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.benefit_setup import BenefitSetup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_update_or_add_employee_benefit_setup(client):
    """Test case for update_or_add_employee_benefit_setup

    Add/update employee's benefit setup
    """
    body = openapi_server.BenefitSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/benefitSetup'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

