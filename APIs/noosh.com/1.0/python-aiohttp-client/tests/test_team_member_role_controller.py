# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.role_list_vo import RoleListVO


pytestmark = pytest.mark.asyncio

async def test_get_member_roles(client):
    """Test case for get_member_roles

    List all the role options for the user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/memberroles/{user_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

