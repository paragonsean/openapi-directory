# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.user_details_expand_vo import UserDetailsExpandVO
from openapi_server.models.workgroup_members_list_vo import WorkgroupMembersListVO


pytestmark = pytest.mark.asyncio

async def test_get_workgroup_member_info(client):
    """Test case for get_workgroup_member_info

    Workgroup Member Info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/workgroupMembers/{user_id}'.format(workgroup_id='workgroup_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_workgroup_member_list(client):
    """Test case for get_workgroup_member_list

    List the workgroup members
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/workgroupMembers'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

