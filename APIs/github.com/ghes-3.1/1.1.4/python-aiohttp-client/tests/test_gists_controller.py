# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_gist import BaseGist
from openapi_server.models.basic_error import BasicError
from openapi_server.models.gist_comment import GistComment
from openapi_server.models.gist_commit import GistCommit
from openapi_server.models.gist_simple import GistSimple
from openapi_server.models.gists_create_comment_request import GistsCreateCommentRequest
from openapi_server.models.gists_create_request import GistsCreateRequest
from openapi_server.models.gists_get403_response import GistsGet403Response
from openapi_server.models.gists_update_request import GistsUpdateRequest
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_gists_check_is_starred(client):
    """Test case for gists_check_is_starred

    Check if a gist is starred
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}/star'.format(gist_id='gist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_create(client):
    """Test case for gists_create

    Create a gist
    """
    body = {"description":"Example of a gist","files":{"README.md":{"content":"Hello World"}},"public":false}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/gists',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_create_comment(client):
    """Test case for gists_create_comment

    Create a gist comment
    """
    body = {"body":"This is a comment to a gist"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/gists/{gist_id}/comments'.format(gist_id='gist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_delete(client):
    """Test case for gists_delete

    Delete a gist
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/gists/{gist_id}'.format(gist_id='gist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_delete_comment(client):
    """Test case for gists_delete_comment

    Delete a gist comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/gists/{gist_id}/comments/{comment_id}'.format(gist_id='gist_id_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_fork(client):
    """Test case for gists_fork

    Fork a gist
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/gists/{gist_id}/forks'.format(gist_id='gist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_get(client):
    """Test case for gists_get

    Get a gist
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}'.format(gist_id='gist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_get_comment(client):
    """Test case for gists_get_comment

    Get a gist comment
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}/comments/{comment_id}'.format(gist_id='gist_id_example', comment_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_get_revision(client):
    """Test case for gists_get_revision

    Get a gist revision
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}/{sha}'.format(gist_id='gist_id_example', sha='sha_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list(client):
    """Test case for gists_list

    List gists for the authenticated user
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list_comments(client):
    """Test case for gists_list_comments

    List gist comments
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}/comments'.format(gist_id='gist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list_commits(client):
    """Test case for gists_list_commits

    List gist commits
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}/commits'.format(gist_id='gist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list_for_user(client):
    """Test case for gists_list_for_user

    List gists for a user
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/gists'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list_forks(client):
    """Test case for gists_list_forks

    List gist forks
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/{gist_id}/forks'.format(gist_id='gist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list_public(client):
    """Test case for gists_list_public

    List public gists
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/public',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_list_starred(client):
    """Test case for gists_list_starred

    List starred gists
    """
    params = [('since', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/gists/starred',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_star(client):
    """Test case for gists_star

    Star a gist
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/gists/{gist_id}/star'.format(gist_id='gist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_unstar(client):
    """Test case for gists_unstar

    Unstar a gist
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/gists/{gist_id}/star'.format(gist_id='gist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_update(client):
    """Test case for gists_update

    Update a gist
    """
    body = {"description":"An update to a gist","files":{"README.md":{"content":"Hello World from GitHub"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/gists/{gist_id}'.format(gist_id='gist_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gists_update_comment(client):
    """Test case for gists_update_comment

    Update a gist comment
    """
    body = {"body":"This is an update to a comment in a gist"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/gists/{gist_id}/comments/{comment_id}'.format(gist_id='gist_id_example', comment_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

