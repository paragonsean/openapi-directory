# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.comment import Comment
from openapi_server.models.issue_comment_list_request_bean import IssueCommentListRequestBean
from openapi_server.models.page_bean_comment import PageBeanComment
from openapi_server.models.page_of_comments import PageOfComments


pytestmark = pytest.mark.asyncio

async def test_add_comment(client):
    """Test case for add_comment

    Add comment
    """
    body = {"renderedBody":"renderedBody","visibility":"","author":"","created":"2000-01-23T04:56:07.000+00:00","updateAuthor":"","self":"self","jsdPublic":True,"id":"id","body":"","jsdAuthorCanSeeRequest":True,"updated":"2000-01-23T04:56:07.000+00:00","properties":[{"value":"","key":"key"},{"value":"","key":"key"}]}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/issue/{issue_id_or_key}/comment'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_comment(client):
    """Test case for delete_comment

    Delete comment
    """
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/api/3/issue/{issue_id_or_key}/comment/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comment(client):
    """Test case for get_comment

    Get comment
    """
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/comment/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments(client):
    """Test case for get_comments

    Get comments
    """
    params = [('startAt', 0),
                    ('maxResults', 5000),
                    ('orderBy', 'order_by_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/rest/api/3/issue/{issue_id_or_key}/comment'.format(issue_id_or_key='issue_id_or_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_comments_by_ids(client):
    """Test case for get_comments_by_ids

    Get comments by IDs
    """
    body = {"ids":[0,0]}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/comment/list',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_comment(client):
    """Test case for update_comment

    Update comment
    """
    body = {"renderedBody":"renderedBody","visibility":"","author":"","created":"2000-01-23T04:56:07.000+00:00","updateAuthor":"","self":"self","jsdPublic":True,"id":"id","body":"","jsdAuthorCanSeeRequest":True,"updated":"2000-01-23T04:56:07.000+00:00","properties":[{"value":"","key":"key"},{"value":"","key":"key"}]}
    params = [('notifyUsers', True),
                    ('overrideEditableFlag', False),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/rest/api/3/issue/{issue_id_or_key}/comment/{id}'.format(issue_id_or_key='issue_id_or_key_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

