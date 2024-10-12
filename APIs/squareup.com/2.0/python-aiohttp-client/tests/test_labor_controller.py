# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_break_type_request import CreateBreakTypeRequest
from openapi_server.models.create_break_type_response import CreateBreakTypeResponse
from openapi_server.models.create_shift_request import CreateShiftRequest
from openapi_server.models.create_shift_response import CreateShiftResponse
from openapi_server.models.delete_break_type_response import DeleteBreakTypeResponse
from openapi_server.models.delete_shift_response import DeleteShiftResponse
from openapi_server.models.get_break_type_response import GetBreakTypeResponse
from openapi_server.models.get_employee_wage_response import GetEmployeeWageResponse
from openapi_server.models.get_shift_response import GetShiftResponse
from openapi_server.models.get_team_member_wage_response import GetTeamMemberWageResponse
from openapi_server.models.list_break_types_response import ListBreakTypesResponse
from openapi_server.models.list_employee_wages_response import ListEmployeeWagesResponse
from openapi_server.models.list_team_member_wages_response import ListTeamMemberWagesResponse
from openapi_server.models.list_workweek_configs_response import ListWorkweekConfigsResponse
from openapi_server.models.search_shifts_request import SearchShiftsRequest
from openapi_server.models.search_shifts_response import SearchShiftsResponse
from openapi_server.models.update_break_type_request import UpdateBreakTypeRequest
from openapi_server.models.update_break_type_response import UpdateBreakTypeResponse
from openapi_server.models.update_shift_request import UpdateShiftRequest
from openapi_server.models.update_shift_response import UpdateShiftResponse
from openapi_server.models.update_workweek_config_request import UpdateWorkweekConfigRequest
from openapi_server.models.update_workweek_config_response import UpdateWorkweekConfigResponse


pytestmark = pytest.mark.asyncio

async def test_create_break_type(client):
    """Test case for create_break_type

    CreateBreakType
    """
    body = {"request_body":{"break_type":{"break_name":"Lunch Break","expected_duration":"PT30M","is_paid":True,"location_id":"CGJN03P1D08GF"},"idempotency_key":"PAD3NG5KSN2GL"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/labor/break-types',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_shift(client):
    """Test case for create_shift

    CreateShift
    """
    body = {"request_body":{"idempotency_key":"HIDSNG5KS478L","shift":{"breaks":[{"break_type_id":"REGS1EQR1TPZ5","end_at":"2019-01-25T06:16:00-05:00","expected_duration":"PT5M","is_paid":True,"name":"Tea Break","start_at":"2019-01-25T06:11:00-05:00"}],"end_at":"2019-01-25T13:11:00-05:00","location_id":"PAA1RJZZKXBFG","start_at":"2019-01-25T03:11:00-05:00","team_member_id":"ormj0jJJZ5OZIzxrZYJI","wage":{"hourly_rate":{"amount":1100,"currency":"USD"},"title":"Barista"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/labor/shifts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_break_type(client):
    """Test case for delete_break_type

    DeleteBreakType
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/labor/break-types/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_shift(client):
    """Test case for delete_shift

    DeleteShift
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/labor/shifts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_break_type(client):
    """Test case for get_break_type

    GetBreakType
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/break-types/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_wage(client):
    """Test case for get_employee_wage

    GetEmployeeWage
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/employee-wages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shift(client):
    """Test case for get_shift

    GetShift
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/shifts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_team_member_wage(client):
    """Test case for get_team_member_wage

    GetTeamMemberWage
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/team-member-wages/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_break_types(client):
    """Test case for list_break_types

    ListBreakTypes
    """
    params = [('location_id', 'location_id_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/break-types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_employee_wages(client):
    """Test case for list_employee_wages

    ListEmployeeWages
    """
    params = [('employee_id', 'employee_id_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/employee-wages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_team_member_wages(client):
    """Test case for list_team_member_wages

    ListTeamMemberWages
    """
    params = [('team_member_id', 'team_member_id_example'),
                    ('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/team-member-wages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_workweek_configs(client):
    """Test case for list_workweek_configs

    ListWorkweekConfigs
    """
    params = [('limit', 56),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/labor/workweek-configs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_shifts(client):
    """Test case for search_shifts

    SearchShifts
    """
    body = {"request_body":{"limit":100,"query":{"filter":{"workday":{"date_range":{"end_date":"2019-02-03","start_date":"2019-01-20"},"default_timezone":"America/Los_Angeles","match_shifts_by":"START_AT"}}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/labor/shifts/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_break_type(client):
    """Test case for update_break_type

    UpdateBreakType
    """
    body = {"request_body":{"break_type":{"break_name":"Lunch","expected_duration":"PT50M","is_paid":True,"location_id":"26M7H24AZ9N6R","version":1}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/labor/break-types/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_shift(client):
    """Test case for update_shift

    UpdateShift
    """
    body = {"request_body":{"shift":{"breaks":[{"break_type_id":"REGS1EQR1TPZ5","end_at":"2019-01-25T06:16:00-05:00","expected_duration":"PT5M","id":"X7GAQYVVRRG6P","is_paid":True,"name":"Tea Break","start_at":"2019-01-25T06:11:00-05:00"}],"end_at":"2019-01-25T13:11:00-05:00","location_id":"PAA1RJZZKXBFG","start_at":"2019-01-25T03:11:00-05:00","team_member_id":"ormj0jJJZ5OZIzxrZYJI","version":1,"wage":{"hourly_rate":{"amount":1500,"currency":"USD"},"title":"Bartender"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/labor/shifts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_workweek_config(client):
    """Test case for update_workweek_config

    UpdateWorkweekConfig
    """
    body = {"request_body":{"workweek_config":{"start_of_day_local_time":600,"start_of_week":"MON","version":10}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/labor/workweek-configs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

