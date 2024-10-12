# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_create_team_members_request import BulkCreateTeamMembersRequest
from openapi_server.models.bulk_create_team_members_response import BulkCreateTeamMembersResponse
from openapi_server.models.bulk_update_team_members_request import BulkUpdateTeamMembersRequest
from openapi_server.models.bulk_update_team_members_response import BulkUpdateTeamMembersResponse
from openapi_server.models.create_team_member_request import CreateTeamMemberRequest
from openapi_server.models.create_team_member_response import CreateTeamMemberResponse
from openapi_server.models.retrieve_team_member_response import RetrieveTeamMemberResponse
from openapi_server.models.retrieve_wage_setting_response import RetrieveWageSettingResponse
from openapi_server.models.search_team_members_request import SearchTeamMembersRequest
from openapi_server.models.search_team_members_response import SearchTeamMembersResponse
from openapi_server.models.update_team_member_request import UpdateTeamMemberRequest
from openapi_server.models.update_team_member_response import UpdateTeamMemberResponse
from openapi_server.models.update_wage_setting_request import UpdateWageSettingRequest
from openapi_server.models.update_wage_setting_response import UpdateWageSettingResponse


pytestmark = pytest.mark.asyncio

async def test_bulk_create_team_members(client):
    """Test case for bulk_create_team_members

    BulkCreateTeamMembers
    """
    body = {"request_body":{"team_members":{"idempotency-key-1":{"team_member":{"assigned_locations":{"assignment_type":"EXPLICIT_LOCATIONS","location_ids":["YSGH2WBKG94QZ","GA2Y9HSJ8KRYT"]},"email_address":"joe_doe@gmail.com","family_name":"Doe","given_name":"Joe","phone_number":"+14159283333","reference_id":"reference_id_1"}},"idempotency-key-2":{"team_member":{"assigned_locations":{"assignment_type":"ALL_CURRENT_AND_FUTURE_LOCATIONS"},"email_address":"jane_smith@gmail.com","family_name":"Smith","given_name":"Jane","phone_number":"+14159223334","reference_id":"reference_id_2"}}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/team-members/bulk-create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_team_members(client):
    """Test case for bulk_update_team_members

    BulkUpdateTeamMembers
    """
    body = {"request_body":{"team_members":{"AFMwA08kR-MIF-3Vs0OE":{"team_member":{"assigned_locations":{"assignment_type":"ALL_CURRENT_AND_FUTURE_LOCATIONS"},"email_address":"jane_smith@gmail.com","family_name":"Smith","given_name":"Jane","is_owner":False,"phone_number":"+14159223334","reference_id":"reference_id_2","status":"ACTIVE"}},"fpgteZNMaf0qOK-a4t6P":{"team_member":{"assigned_locations":{"assignment_type":"EXPLICIT_LOCATIONS","location_ids":["YSGH2WBKG94QZ","GA2Y9HSJ8KRYT"]},"email_address":"joe_doe@gmail.com","family_name":"Doe","given_name":"Joe","is_owner":False,"phone_number":"+14159283333","reference_id":"reference_id_1","status":"ACTIVE"}}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/team-members/bulk-update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_team_member(client):
    """Test case for create_team_member

    CreateTeamMember
    """
    body = {"request_body":{"idempotency_key":"idempotency-key-0","team_member":{"assigned_locations":{"assignment_type":"EXPLICIT_LOCATIONS","location_ids":["YSGH2WBKG94QZ","GA2Y9HSJ8KRYT"]},"email_address":"joe_doe@gmail.com","family_name":"Doe","given_name":"Joe","phone_number":"+14159283333","reference_id":"reference_id_1","status":"ACTIVE"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/team-members',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_team_member(client):
    """Test case for retrieve_team_member

    RetrieveTeamMember
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/team-members/{team_member_id}'.format(team_member_id='team_member_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_wage_setting(client):
    """Test case for retrieve_wage_setting

    RetrieveWageSetting
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/team-members/{team_member_id}/wage-setting'.format(team_member_id='team_member_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_team_members(client):
    """Test case for search_team_members

    SearchTeamMembers
    """
    body = {"request_body":{"limit":10,"query":{"filter":{"location_ids":["0G5P3VGACMMQZ"],"status":"ACTIVE"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/team-members/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_team_member(client):
    """Test case for update_team_member

    UpdateTeamMember
    """
    body = {"request_body":{"team_member":{"assigned_locations":{"assignment_type":"EXPLICIT_LOCATIONS","location_ids":["YSGH2WBKG94QZ","GA2Y9HSJ8KRYT"]},"email_address":"joe_doe@gmail.com","family_name":"Doe","given_name":"Joe","phone_number":"+14159283333","reference_id":"reference_id_1","status":"ACTIVE"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/team-members/{team_member_id}'.format(team_member_id='team_member_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_wage_setting(client):
    """Test case for update_wage_setting

    UpdateWageSetting
    """
    body = {"request_body":{"wage_setting":{"is_overtime_exempt":True,"job_assignments":[{"annual_rate":{"amount":3000000,"currency":"USD"},"job_title":"Manager","pay_type":"SALARY","weekly_hours":40},{"hourly_rate":{"amount":1200,"currency":"USD"},"job_title":"Cashier","pay_type":"HOURLY"}]}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/team-members/{team_member_id}/wage-setting'.format(team_member_id='team_member_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

