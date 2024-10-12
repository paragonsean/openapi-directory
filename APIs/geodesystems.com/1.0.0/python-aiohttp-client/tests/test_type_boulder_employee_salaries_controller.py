# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_boulder_employee_salaries(client):
    """Test case for search_boulder_employee_salaries

    Search API for 'Boulder Employee Salaries' entry type
    """
    params = [('text', 'text_example'),
                    ('name', 'name_example'),
                    ('description', 'description_example'),
                    ('fromdate', '2013-10-20T19:20:30+01:00'),
                    ('todate', '2013-10-20T19:20:30+01:00'),
                    ('createdate.from', '2013-10-20T19:20:30+01:00'),
                    ('createdate.to', '2013-10-20T19:20:30+01:00'),
                    ('changedate.from', '2013-10-20T19:20:30+01:00'),
                    ('changedate.to', '2013-10-20T19:20:30+01:00'),
                    ('group', 'group_example'),
                    ('filesuffix', 'filesuffix_example'),
                    ('maxlatitude', 3.4),
                    ('minlongitude', 3.4),
                    ('minlatitude', 3.4),
                    ('maxlongitude', 3.4),
                    ('max', 56),
                    ('skip', 56),
                    ('search.db_boulder_employee_salaries.position_description', 'search_db_boulder_employee_salaries_position_description_example'),
                    ('search.db_boulder_employee_salaries.department', 'search_db_boulder_employee_salaries_department_example'),
                    ('search.db_boulder_employee_salaries.employee_flsa_exempt_y_n', 'search_db_boulder_employee_salaries_employee_flsa_exempt_y_n_example'),
                    ('search.db_boulder_employee_salaries.pay_range_min', 3.4),
                    ('search.db_boulder_employee_salaries.pay_range_max', 3.4),
                    ('search.db_boulder_employee_salaries.employee_hourly_pay_rate', 3.4),
                    ('search.db_boulder_employee_salaries.employee_fte_in_this_position', 3.4),
                    ('search.db_boulder_employee_salaries.employee_annual_base_salary', 3.4)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/repository/search/type/boulder_employee_salaries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

