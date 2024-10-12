# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artifact import Artifact
from openapi_server.models.build import Build
from openapi_server.models.build_detail import BuildDetail
from openapi_server.models.build_summary import BuildSummary
from openapi_server.models.envvar import Envvar
from openapi_server.models.key import Key
from openapi_server.models.project import Project
from openapi_server.models.project_username_project_build_cache_delete200_response import ProjectUsernameProjectBuildCacheDelete200Response
from openapi_server.models.project_username_project_checkout_key_fingerprint_delete200_response import ProjectUsernameProjectCheckoutKeyFingerprintDelete200Response
from openapi_server.models.project_username_project_post_request import ProjectUsernameProjectPostRequest
from openapi_server.models.project_username_project_ssh_key_post_default_response import ProjectUsernameProjectSshKeyPostDefaultResponse
from openapi_server.models.project_username_project_ssh_key_post_request import ProjectUsernameProjectSshKeyPostRequest
from openapi_server.models.project_username_project_tree_branch_post_request import ProjectUsernameProjectTreeBranchPostRequest
from openapi_server.models.tests import Tests
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_me_get(client):
    """Test case for me_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_build_cache_delete(client):
    """Test case for project_username_project_build_cache_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/project/{username}/{project}/build-cache'.format(username='username_example', project='project_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_build_num_artifacts_get(client):
    """Test case for project_username_project_build_num_artifacts_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/{build_num}/artifacts'.format(username='username_example', project='project_example', build_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_build_num_cancel_post(client):
    """Test case for project_username_project_build_num_cancel_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}/{build_num}/cancel'.format(username='username_example', project='project_example', build_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_build_num_get(client):
    """Test case for project_username_project_build_num_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/{build_num}'.format(username='username_example', project='project_example', build_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_build_num_retry_post(client):
    """Test case for project_username_project_build_num_retry_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}/{build_num}/retry'.format(username='username_example', project='project_example', build_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_build_num_tests_get(client):
    """Test case for project_username_project_build_num_tests_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/{build_num}/tests'.format(username='username_example', project='project_example', build_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_checkout_key_fingerprint_delete(client):
    """Test case for project_username_project_checkout_key_fingerprint_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/project/{username}/{project}/checkout-key/{fingerprint}'.format(username='username_example', project='project_example', fingerprint='fingerprint_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_checkout_key_fingerprint_get(client):
    """Test case for project_username_project_checkout_key_fingerprint_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/checkout-key/{fingerprint}'.format(username='username_example', project='project_example', fingerprint='fingerprint_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_checkout_key_get(client):
    """Test case for project_username_project_checkout_key_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/checkout-key'.format(username='username_example', project='project_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_checkout_key_post(client):
    """Test case for project_username_project_checkout_key_post

    
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}/checkout-key'.format(username='username_example', project='project_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_envvar_get(client):
    """Test case for project_username_project_envvar_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/envvar'.format(username='username_example', project='project_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_envvar_name_delete(client):
    """Test case for project_username_project_envvar_name_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/project/{username}/{project}/envvar/{name}'.format(username='username_example', project='project_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_envvar_name_get(client):
    """Test case for project_username_project_envvar_name_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}/envvar/{name}'.format(username='username_example', project='project_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_envvar_post(client):
    """Test case for project_username_project_envvar_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}/envvar'.format(username='username_example', project='project_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_get(client):
    """Test case for project_username_project_get

    
    """
    params = [('limit', 30),
                    ('offset', 0),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/project/{username}/{project}'.format(username='username_example', project='project_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_post(client):
    """Test case for project_username_project_post

    
    """
    body = openapi_server.ProjectUsernameProjectPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}'.format(username='username_example', project='project_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_ssh_key_post(client):
    """Test case for project_username_project_ssh_key_post

    
    """
    body = openapi_server.ProjectUsernameProjectSshKeyPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'content_type_example',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}/ssh-key'.format(username='username_example', project='project_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_username_project_tree_branch_post(client):
    """Test case for project_username_project_tree_branch_post

    
    """
    body = openapi_server.ProjectUsernameProjectTreeBranchPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/project/{username}/{project}/tree/{branch}'.format(username='username_example', project='project_example', branch='branch_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_get(client):
    """Test case for projects_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recent_builds_get(client):
    """Test case for recent_builds_get

    
    """
    params = [('limit', 30),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/recent-builds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_heroku_key_post(client):
    """Test case for user_heroku_key_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/user/heroku-key',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

