# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pay_statement_details import PayStatementDetails
from openapi_server.models.pay_statement_summary import PayStatementSummary


pytestmark = pytest.mark.asyncio

async def test_gets_employee_pay_statement_detail_data_based_on_the_specified_year(client):
    """Test case for gets_employee_pay_statement_detail_data_based_on_the_specified_year

    Get employee pay statement details data for the specified year.
    """
    params = [('pagesize', 56),
                    ('pagenumber', 56),
                    ('includetotalcount', True),
                    ('codegroup', 'codegroup_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/paystatement/details/{year}'.format(company_id='company_id_example', employee_id='employee_id_example', year='year_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gets_employee_pay_statement_detail_data_based_on_the_specified_year_and_check_date(client):
    """Test case for gets_employee_pay_statement_detail_data_based_on_the_specified_year_and_check_date

    Get employee pay statement details data for the specified year and check date.
    """
    params = [('pagesize', 56),
                    ('pagenumber', 56),
                    ('includetotalcount', True),
                    ('codegroup', 'codegroup_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/paystatement/details/{year}/{check_date}'.format(company_id='company_id_example', employee_id='employee_id_example', year='year_example', check_date='check_date_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gets_employee_pay_statement_summary_data_based_on_the_specified_year(client):
    """Test case for gets_employee_pay_statement_summary_data_based_on_the_specified_year

    Get employee pay statement summary data for the specified year.
    """
    params = [('pagesize', 56),
                    ('pagenumber', 56),
                    ('includetotalcount', True),
                    ('codegroup', 'codegroup_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/paystatement/summary/{year}'.format(company_id='company_id_example', employee_id='employee_id_example', year='year_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gets_employee_pay_statement_summary_data_based_on_the_specified_year_and_check_date(client):
    """Test case for gets_employee_pay_statement_summary_data_based_on_the_specified_year_and_check_date

    Get employee pay statement summary data for the specified year and check date.
    """
    params = [('pagesize', 56),
                    ('pagenumber', 56),
                    ('includetotalcount', True),
                    ('codegroup', 'codegroup_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/companies/{company_id}/employees/{employee_id}/paystatement/summary/{year}/{check_date}'.format(company_id='company_id_example', employee_id='employee_id_example', year='year_example', check_date='check_date_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

