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
from openapi_server.models.visibility_settings import VisibilitySettings


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_domain_comment_reply_v2(client):
    """Test case for add_domain_comment_reply_v2

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
        path='/domains/{owner}/{domain}/{version}/comments/{comment}/replies'.format(owner='owner_example', domain='domain_example', version='version_example', comment='comment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_add_domain_comment_v2(client):
    """Test case for add_domain_comment_v2

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
        path='/domains/{owner}/{domain}/{version}/comments'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_clone_domain(client):
    """Test case for clone_domain

    Create a new domain version
    """
    new_version = openapi_server.NewVersion()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/domains/{owner}/{domain}/{version}/clone'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        json=new_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain(client):
    """Test case for delete_domain

    Delete a domain
    """
    params = [('force', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/domains/{owner}/{domain}'.format(owner='owner_example', domain='domain_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain_comment_reply_v2(client):
    """Test case for delete_domain_comment_reply_v2

    Delete a comment reply
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/domains/{owner}/{domain}/{version}/comments/{comment}/replies/{reply}'.format(owner='owner_example', domain='domain_example', version='version_example', comment='comment_example', reply='reply_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain_comment_v2(client):
    """Test case for delete_domain_comment_v2

    Delete a comment
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/domains/{owner}/{domain}/{version}/comments/{comment}'.format(owner='owner_example', domain='domain_example', version='version_example', comment='comment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_domain_version(client):
    """Test case for delete_domain_version

    Delete a domain version
    """
    params = [('force', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/domains/{owner}/{domain}/{version}'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_fork_domain(client):
    """Test case for fork_domain

    Fork a domain
    """
    fork_version = openapi_server.ForkVersion()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/domains/{owner}/{domain}/{version}/fork'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        json=fork_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_comments_v2(client):
    """Test case for get_domain_comments_v2

    Get comments for the specified domain version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/{version}/comments'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_default_version(client):
    """Test case for get_domain_default_version

    Get the default version of a domain
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/settings/default'.format(owner='owner_example', domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_definition(client):
    """Test case for get_domain_definition

    Get the OpenAPI definition of the specified domain version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/{version}'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_json_definition(client):
    """Test case for get_domain_json_definition

    Get the OpenAPI definition for the specified domain version in JSON format
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/{version}/domain.json'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_lifecycle_settings(client):
    """Test case for get_domain_lifecycle_settings

    Get the published status for the specified domain and version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/{version}/settings/lifecycle'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_private_settings(client):
    """Test case for get_domain_private_settings

    Get the visibility (public or private) of a domain version
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/{version}/settings/private'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_versions(client):
    """Test case for get_domain_versions

    Get a list of domain versions
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}'.format(owner='owner_example', domain='domain_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_domain_yaml_definition(client):
    """Test case for get_domain_yaml_definition

    Get the OpenAPI definition for the specified domain version in YAML format
    """
    headers = { 
        'Accept': 'application/yaml',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/domains/{owner}/{domain}/{version}/domain.yaml'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_owner_domains(client):
    """Test case for get_owner_domains

    Get a list of domains of the specified owner
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
        path='/domains/{owner}'.format(owner='owner_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_domain(client):
    """Test case for rename_domain

    Rename a domain
    """
    params = [('newName', 'new_name_example'),
                    ('force', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/domains/{owner}/{domain}/rename'.format(owner='owner_example', domain='domain_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_save_domain_definition(client):
    """Test case for save_domain_definition

    Create or update a domain
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
        path='/domains/{owner}/{domain}'.format(owner='owner_example', domain='domain_example'),
        headers=headers,
        json=definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_apis_and_domains_0(client):
    """Test case for search_apis_and_domains_0

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

async def test_search_domains(client):
    """Test case for search_domains

    Search domains
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
        path='/domains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_domain_comment_status_v2(client):
    """Test case for set_domain_comment_status_v2

    Resolve or reopen a comment
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/domains/{owner}/{domain}/{version}/comments/{comment}/status/{status}'.format(owner='owner_example', domain='domain_example', version='version_example', comment='comment_example', status='status_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_domain_default_version(client):
    """Test case for set_domain_default_version

    Set the default version for a domain
    """
    default_version = {"version":"1.0.0"}
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/domains/{owner}/{domain}/settings/default'.format(owner='owner_example', domain='domain_example'),
        headers=headers,
        json=default_version,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_domain_lifecycle_settings(client):
    """Test case for set_domain_lifecycle_settings

    Publish or unpublish a domain version
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
        path='/domains/{owner}/{domain}/{version}/settings/lifecycle'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        json=settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_domain_private_settings(client):
    """Test case for set_domain_private_settings

    Set the visibility (public or private) of a domain version
    """
    settings = {"private":True}
    params = [('force', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/domains/{owner}/{domain}/{version}/settings/private'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        json=settings,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_domain_comment_reply_v2(client):
    """Test case for update_domain_comment_reply_v2

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
        path='/domains/{owner}/{domain}/{version}/comments/{comment}/replies/{reply}'.format(owner='owner_example', domain='domain_example', version='version_example', comment='comment_example', reply='reply_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_domain_comment_v2(client):
    """Test case for update_domain_comment_v2

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
        path='/domains/{owner}/{domain}/{version}/comments/{comment}'.format(owner='owner_example', domain='domain_example', version='version_example', comment='comment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_domain_comments_v2(client):
    """Test case for update_domain_comments_v2

    Bulk update comments
    """
    body = openapi_server.CommentsBatch()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/domains/{owner}/{domain}/{version}/comments/batch'.format(owner='owner_example', domain='domain_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

