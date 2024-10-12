# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.absence_periods_response import AbsencePeriodsResponse
from openapi_server.models.attendance_periods_response import AttendancePeriodsResponse
from openapi_server.models.company_time_off_types_get200_response import CompanyTimeOffTypesGet200Response
from openapi_server.models.company_time_offs_post201_response import CompanyTimeOffsPost201Response
from openapi_server.models.create_time_off_period_request import CreateTimeOffPeriodRequest
from openapi_server.models.detailed_error_response import DetailedErrorResponse
from openapi_server.models.employee_response import EmployeeResponse
from openapi_server.models.employees_response import EmployeesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.new_attendance_period_request import NewAttendancePeriodRequest
from openapi_server.models.new_attendance_period_response import NewAttendancePeriodResponse
from openapi_server.models.response import Response
from openapi_server.models.update_attendance_period_request import UpdateAttendancePeriodRequest


pytestmark = pytest.mark.asyncio

async def test_company_attendances_get(client):
    """Test case for company_attendances_get

    
    """
    params = [('start_date', '2013-10-20'),
                    ('end_date', '2013-10-20'),
                    ('updated_from', 'updated_from_example'),
                    ('updated_to', 'updated_to_example'),
                    ('employees', [56]),
                    ('limit', 200),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/attendances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_attendances_id_delete(client):
    """Test case for company_attendances_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/company/attendances/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_attendances_id_patch(client):
    """Test case for company_attendances_id_patch

    
    """
    body = {"break":35,"comment":null,"date":"2019-03-17","end_time":720,"start_time":540}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/company/attendances/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_attendances_post(client):
    """Test case for company_attendances_post

    
    """
    body = {"attendances":[{"break":120,"comment":{"$ref":"#/components/schemas/UpdateAttendancePeriodRequest/example/comment"},"date":"2017-01-18","employee":1234,"end_time":1080,"start_time":"08:00"},{"break":35,"comment":"I was productive as hell","date":"2017-01-17","employee":1235,"end_time":720,"start_time":"09:00"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/company/attendances',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_employees_employee_id_get(client):
    """Test case for company_employees_employee_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/employees/{employee_id}'.format(employee_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_employees_employee_id_profile_picture_width_get(client):
    """Test case for company_employees_employee_id_profile_picture_width_get

    
    """
    headers = { 
        'Accept': 'image/png',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/employees/{employee_id}/profile-picture/{width}'.format(employee_id=56, width=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_employees_get(client):
    """Test case for company_employees_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/employees',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_company_employees_post(client):
    """Test case for company_employees_post

    Create an employee
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'employee_department': 'employee_department_example',
        'employee_email': 'employee_email_example',
        'employee_first_name': 'employee_first_name_example',
        'employee_gender': 'employee_gender_example',
        'employee_hire_date': '2013-10-20',
        'employee_last_name': 'employee_last_name_example',
        'employee_position': 'employee_position_example',
        'employee_weekly_hours': 3.4
        }
    response = await client.request(
        method='POST',
        path='/v1/company/employees',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_time_off_types_get(client):
    """Test case for company_time_off_types_get

    
    """
    params = [('limit', 200),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/time-off-types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_time_offs_get(client):
    """Test case for company_time_offs_get

    
    """
    params = [('start_date', '2013-10-20'),
                    ('end_date', '2013-10-20'),
                    ('updated_from', 'updated_from_example'),
                    ('updated_to', 'updated_to_example'),
                    ('employees', [56]),
                    ('limit', 200),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/time-offs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_time_offs_id_delete(client):
    """Test case for company_time_offs_id_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/company/time-offs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_time_offs_id_get(client):
    """Test case for company_time_offs_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/company/time-offs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_time_offs_post(client):
    """Test case for company_time_offs_post

    
    """
    body = {"end_date":"2000-01-23","half_day_end":True,"half_day_start":True,"time_off_type_id":6,"employee_id":0,"comment":"comment","start_date":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/company/time-offs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

