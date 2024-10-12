# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.global_user_group import GlobalUserGroup
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_globalusergroups_get(client):
    """Test case for globalusergroups_get

    List Global User Groups.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/globalusergroups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_globalusergroups_groupid_members_get(client):
    """Test case for globalusergroups_groupid_members_get

    List of all users in group.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/globalusergroups/{groupid}/members'.format(groupid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

