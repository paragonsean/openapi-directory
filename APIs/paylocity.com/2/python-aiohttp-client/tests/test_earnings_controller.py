# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.earning import Earning
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_add_or_update_an_employee_earning(client):
    """Test case for add_or_update_an_employee_earning

    Add/Update Earning
    """
    body = openapi_server.Earning()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/earnings'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_earning_by_earning_code_and_start_date(client):
    """Test case for delete_earning_by_earning_code_and_start_date

    Delete Earning by Earning Code and Start Date
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/earnings/{earning_code}/{start_date}'.format(company_id='company_id_example', employee_id='employee_id_example', earning_code='earning_code_example', start_date='start_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_earnings(client):
    """Test case for get_all_earnings

    Get All Earnings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/earnings'.format(company_id='company_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_earning_by_earning_code_and_start_date(client):
    """Test case for get_earning_by_earning_code_and_start_date

    Get Earning by Earning Code and Start Date
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/earnings/{earning_code}/{start_date}'.format(company_id='company_id_example', employee_id='employee_id_example', earning_code='earning_code_example', start_date='start_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_earnings_by_earning_code(client):
    """Test case for get_earnings_by_earning_code

    Get Earnings by Earning Code
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/earnings/{earning_code}'.format(company_id='company_id_example', employee_id='employee_id_example', earning_code='earning_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

