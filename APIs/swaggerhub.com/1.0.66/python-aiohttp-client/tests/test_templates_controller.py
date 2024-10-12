# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apis_json import ApisJson
from openapi_server.models.closable_comment import ClosableComment
from openapi_server.models.comments_batch import CommentsBatch
from openapi_server.models.fork_version import ForkVersion
from openapi_server.models.lifecycle_settings import LifecycleSettings
from openapi_server.models.template_wrapper import TemplateWrapper
from openapi_server.models.visibility_settings import VisibilitySettings


pytestmark = pytest.mark.asyncio

async def test_delete_template(client):
    """Test case for delete_template

    Delete a template
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/templates/{owner}/{template_id}'.format(owner='owner_example', template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_template_version(client):
    """Test case for delete_template_version

    Delete a particular version of a template
    """
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/templates/{owner}/{template_id}/{version}'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_fork_template(client):
    """Test case for fork_template

    Create a fork for a template
    """
    body = openapi_server.ForkVersion()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/templates/{owner}/{template_id}/{version}/fork'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_comments(client):
    """Test case for get_template_comments

    Return the list of comments for a template
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/templates/{owner}/{template_id}/{version}/comments'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_definition(client):
    """Test case for get_template_definition

    Retrieve a template definition
    """
    params = [('flatten', False)]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/templates/{owner}/{template_id}/{version}'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_lifecycle_settings(client):
    """Test case for get_template_lifecycle_settings

    Retrieve lifecycle settings for a template
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/templates/{owner}/{template_id}/{version}/settings/lifecycle'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_private_settings(client):
    """Test case for get_template_private_settings

    Retrieve visibility settings for a template
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/templates/{owner}/{template_id}/{version}/settings/private'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_versions(client):
    """Test case for get_template_versions

    Retrieve an APIs.json listing for all template versions for an owner and template
    """
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/templates/{owner}/{template_id}'.format(owner='owner_example', template_id='template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_templates(client):
    """Test case for get_templates

    Retrieve a list of templates for an owner
    """
    params = [('owner', 'owner_example')]
    headers = { 
        'Accept': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_template(client):
    """Test case for rename_template

    Rename a template
    """
    params = [('newName', 'new_name_example')]
    headers = { 
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/templates/{owner}/{template_id}/rename'.format(owner='owner_example', template_id='template_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_save_template_definition(client):
    """Test case for save_template_definition

    Create or update a template
    """
    body = 'body_example'
    params = [('isPrivate', False),
                    ('version', 'version_example'),
                    ('force', True),
                    ('projectName', 'project_name_example')]
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/templates/{owner}/{template_id}'.format(owner='owner_example', template_id='template_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_apis_and_domains_1(client):
    """Test case for search_apis_and_domains_1

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

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_template_lifecycle_settings(client):
    """Test case for set_template_lifecycle_settings

    Update lifecycle settings for a template
    """
    body = openapi_server.LifecycleSettings()
    params = [('force', True)]
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/templates/{owner}/{template_id}/{version}/settings/lifecycle'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_template_private_settings(client):
    """Test case for set_template_private_settings

    Update visibility settings for a template
    """
    body = openapi_server.VisibilitySettings()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/templates/{owner}/{template_id}/{version}/settings/private'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_template_comments(client):
    """Test case for update_template_comments

    Update the list of comments for a template
    """
    body = openapi_server.CommentsBatch()
    headers = { 
        'Content-Type': 'application/json',
        'TokenSecured': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/templates/{owner}/{template_id}/{version}/comments/batch'.format(owner='owner_example', template_id='template_id_example', version='version_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

