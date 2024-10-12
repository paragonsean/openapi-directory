# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apis_json import ApisJson
from openapi_server.models.closable_comment import ClosableComment
from openapi_server.models.closable_comment_patch import ClosableCommentPatch
from openapi_server.models.comment import Comment
from openapi_server.models.comment_patch import CommentPatch
from openapi_server.models.comments_batch import CommentsBatch
from openapi_server.models.default_version import DefaultVersion
from openapi_server.models.fork_version import ForkVersion
from openapi_server.models.lifecycle_settings import LifecycleSettings
from openapi_server.models.new_comment import NewComment
from openapi_server.models.new_reply import NewReply
from openapi_server.models.new_version import NewVersion
from openapi_server.models.standardization_result import StandardizationResult
from openapi_server.models.validation_result import ValidationResult
from openapi_server.models.visibility_settings import VisibilitySettings


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_api_comment_reply_v2(client):
    """Test case for add_api_comment_reply_v2

    Reply to a comment
    """
    body = openapi_server.NewReply()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/comments/{comment}/replies'.format(owner='owner_example', api='api_example', version='version_example', comment='comment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_api_comment_v2(client):
    """Test case for add_api_comment_v2

    Add a new comment
    """
    body = openapi_server.NewComment()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/comments'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_clone_api(client):
    """Test case for clone_api

    Create a new API version
    """
    new_version = openapi_server.NewVersion()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/clone'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=new_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api(client):
    """Test case for delete_api

    Delete an API
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/{owner}/{api}'.format(owner='owner_example', api='api_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_comment_reply_v2(client):
    """Test case for delete_api_comment_reply_v2

    Delete a comment reply
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/{owner}/{api}/{version}/comments/{comment}/replies/{reply}'.format(owner='owner_example', api='api_example', version='version_example', comment='comment_example', reply='reply_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_comment_v2(client):
    """Test case for delete_api_comment_v2

    Delete a comment
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/{owner}/{api}/{version}/comments/{comment}'.format(owner='owner_example', api='api_example', version='version_example', comment='comment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_version(client):
    """Test case for delete_api_version

    Delete an API version
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/{owner}/{api}/{version}'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_fork_api(client):
    """Test case for fork_api

    Fork an API
    """
    fork_version = openapi_server.ForkVersion()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/fork'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=fork_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_comments_v2(client):
    """Test case for get_api_comments_v2

    Get comments for the specified API version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/comments'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_default_version(client):
    """Test case for get_api_default_version

    Get the default version of an API
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/settings/default'.format(owner='owner_example', api='api_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_versions(client):
    """Test case for get_api_versions

    Get a list of API versions
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}'.format(owner='owner_example', api='api_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_definition(client):
    """Test case for get_definition

    Get the OpenAPI definition of the specified API version
    """
    params = [('resolved', False),
                    ('flatten', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_json_definition(client):
    """Test case for get_json_definition

    Get the OpenAPI definition for the specified API version in JSON format
    """
    params = [('resolved', False),
                    ('flatten', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/swagger.json'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lifecycle_settings(client):
    """Test case for get_lifecycle_settings

    Get the published status for the specified API and version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/settings/lifecycle'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_owner_apis(client):
    """Test case for get_owner_apis

    Get a list of APIs of the specified owner
    """
    params = [('page', 0),
                    ('limit', 10),
                    ('sort', NAME),
                    ('order', ASC)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}'.format(owner='owner_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_private_settings(client):
    """Test case for get_private_settings

    Get the visibility (public or private) of API version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/settings/private'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_standardization_errors(client):
    """Test case for get_standardization_errors

    Retrieve the standardization errors for a given API definition
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/standardization'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_validation(client):
    """Test case for get_validation

    Deprecated Get API Standardization errors and warnings
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/validation'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_yaml_definition(client):
    """Test case for get_yaml_definition

    Get the OpenAPI definition for the specified API version in YAML format
    """
    params = [('resolved', False),
                    ('flatten', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/{owner}/{api}/{version}/swagger.yaml'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_api(client):
    """Test case for rename_api

    Rename an API
    """
    params = [('newName', 'new_name_example')]
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/rename'.format(owner='owner_example', api='api_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_save_definition(client):
    """Test case for save_definition

    Create or update an API
    """
    definition = 'definition_example'
    params = [('isPrivate', False),
                    ('version', 'version_example'),
                    ('force', True)]
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}'.format(owner='owner_example', api='api_example'),
        headers=headers,
        json=definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_apis(client):
    """Test case for search_apis

    Search APIs
    """
    params = [('query', 'query_example'),
                    ('state', ALL),
                    ('page', 0),
                    ('limit', 10),
                    ('sort', NAME),
                    ('order', ASC)]
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_apis_and_domains(client):
    """Test case for search_apis_and_domains

    Retrieve a list of currently defined APIs, domains, and templates in APIs.json format
    """
    params = [('specType', ANY),
                    ('visibility', ANY),
                    ('state', ALL),
                    ('owner', 'owner_example'),
                    ('query', 'query_example'),
                    ('page', 0),
                    ('limit', 10),
                    ('sort', NAME),
                    ('order', ASC)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/specs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_api_comment_status_v2(client):
    """Test case for set_api_comment_status_v2

    Resolve or reopen a comment
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apis/{owner}/{api}/{version}/comments/{comment}/status/{status}'.format(owner='owner_example', api='api_example', version='version_example', comment='comment_example', status='status_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_api_default_version(client):
    """Test case for set_api_default_version

    Set the default API version
    """
    default_version = {"version":"1.0.0"}
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apis/{owner}/{api}/settings/default'.format(owner='owner_example', api='api_example'),
        headers=headers,
        json=default_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_lifecycle_settings(client):
    """Test case for set_lifecycle_settings

    Publish or unpublish an API version
    """
    settings = {"published":True}
    params = [('force', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apis/{owner}/{api}/{version}/settings/lifecycle'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_private_settings(client):
    """Test case for set_private_settings

    Set the visibility (public or private) of an API version
    """
    settings = {"private":True}
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apis/{owner}/{api}/{version}/settings/private'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=settings,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_api_comment_reply_v2(client):
    """Test case for update_api_comment_reply_v2

    Update a comment reply
    """
    body = openapi_server.CommentPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apis/{owner}/{api}/{version}/comments/{comment}/replies/{reply}'.format(owner='owner_example', api='api_example', version='version_example', comment='comment_example', reply='reply_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_api_comment_v2(client):
    """Test case for update_api_comment_v2

    Update a comment
    """
    body = openapi_server.ClosableCommentPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/apis/{owner}/{api}/{version}/comments/{comment}'.format(owner='owner_example', api='api_example', version='version_example', comment='comment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_api_comments_v2(client):
    """Test case for update_api_comments_v2

    Bulk update comments
    """
    body = openapi_server.CommentsBatch()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/{owner}/{api}/{version}/comments/batch'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

