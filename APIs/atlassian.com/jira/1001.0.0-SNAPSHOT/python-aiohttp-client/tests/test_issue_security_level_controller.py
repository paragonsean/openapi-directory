# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_bean_issue_security_level_member import PageBeanIssueSecurityLevelMember
from openapi_server.models.security_level import SecurityLevel


pytestmark = pytest.mark.asyncio

async def test_get_issue_security_level(client):
    """Test case for get_issue_security_level

    Get issue security level
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/securitylevel/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_security_level_members(client):
    """Test case for get_issue_security_level_members

    Get issue security level members
    """
    params = [('startAt', 0),
                    ('maxResults', 50),
                    ('issueSecurityLevelId', [56]),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issuesecurityschemes/{issue_security_scheme_id}/members'.format(issue_security_scheme_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

