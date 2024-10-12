# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.issue_link import IssueLink
from openapi_server.models.link_issue_request_json_bean import LinkIssueRequestJsonBean


pytestmark = pytest.mark.asyncio

async def test_delete_issue_link(client):
    """Test case for delete_issue_link

    Delete issue link
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issueLink/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_issue_link(client):
    """Test case for get_issue_link

    Get issue link
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issueLink/{link_id}'.format(link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_link_issues(client):
    """Test case for link_issues

    Create issue link
    """
    body = {"outwardIssue":{"self":"https://openapi-generator.tech","id":"id","fields":"","key":"key"},"comment":{"renderedBody":"renderedBody","visibility":"","author":"","created":"2000-01-23T04:56:07.000+00:00","updateAuthor":"","self":"self","jsdPublic":True,"id":"id","body":"","jsdAuthorCanSeeRequest":True,"updated":"2000-01-23T04:56:07.000+00:00","properties":[{"value":"","key":"key"},{"value":"","key":"key"}]},"inwardIssue":{"self":"https://openapi-generator.tech","id":"id","fields":"","key":"key"},"type":{"inward":"inward","name":"name","self":"https://openapi-generator.tech","id":"id","outward":"outward"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issueLink',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

