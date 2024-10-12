# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.member_reports import MemberReports


pytestmark = pytest.mark.asyncio

async def test_find_member_reports(client):
    """Test case for find_member_reports

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/member_reports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

