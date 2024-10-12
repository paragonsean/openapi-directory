# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_technique200_response import CreateTechnique200Response
from openapi_server.models.delete_technique200_response import DeleteTechnique200Response
from openapi_server.models.editor_technique import EditorTechnique
from openapi_server.models.get_technique_all_version200_response import GetTechniqueAllVersion200Response
from openapi_server.models.get_techniques_resources200_response import GetTechniquesResources200Response
from openapi_server.models.list_technique_version_directives200_response import ListTechniqueVersionDirectives200Response
from openapi_server.models.list_techniques200_response import ListTechniques200Response
from openapi_server.models.list_techniques_directives200_response import ListTechniquesDirectives200Response
from openapi_server.models.list_techniques_versions200_response import ListTechniquesVersions200Response
from openapi_server.models.methods200_response import Methods200Response
from openapi_server.models.technique_categories200_response import TechniqueCategories200Response
from openapi_server.models.technique_revisions200_response import TechniqueRevisions200Response


pytestmark = pytest.mark.asyncio

async def test_create_technique(client):
    """Test case for create_technique

    Create technique
    """
    body = [openapi_server.EditorTechnique()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/techniques',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_technique(client):
    """Test case for delete_technique

    Delete technique
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/techniques/{technique_id}/{technique_version}'.format(technique_id='userManagement', technique_version='6.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_technique_all_version(client):
    """Test case for get_technique_all_version

    Technique metadata by ID
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/{technique_id}'.format(technique_id='userManagement'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_technique_all_version_id(client):
    """Test case for get_technique_all_version_id

    Technique metadata by version and ID
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/{technique_id}/{technique_version}'.format(technique_id='userManagement', technique_version='6.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_techniques_resources(client):
    """Test case for get_techniques_resources

    Technique's resources
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/{technique_id}/{technique_version}/resources'.format(technique_id='userManagement', technique_version='6.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_technique_version_directives(client):
    """Test case for list_technique_version_directives

    List all directives based on a version of a technique
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/{technique_id}/{technique_version}/directives'.format(technique_id='userManagement', technique_version='6.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_techniques(client):
    """Test case for list_techniques

    List all techniques
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_techniques_directives(client):
    """Test case for list_techniques_directives

    List all directives based on a technique
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/{technique_id}/directives'.format(technique_id='userManagement'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_techniques_versions(client):
    """Test case for list_techniques_versions

    List versions
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/versions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_methods(client):
    """Test case for methods

    List methods
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/methods',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reload_methods(client):
    """Test case for reload_methods

    Reload methods
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/methods/reload',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_technique_categories(client):
    """Test case for technique_categories

    List categories
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_technique_revisions(client):
    """Test case for technique_revisions

    Technique's revisions
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/techniques/{technique_id}/{technique_version}/revisions'.format(technique_id='userManagement', technique_version='6.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_techniques(client):
    """Test case for techniques

    Reload techniques
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/techniques/reload',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_technique(client):
    """Test case for update_technique

    Update technique
    """
    body = [openapi_server.EditorTechnique()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/techniques/{technique_id}/{technique_version}'.format(technique_id='userManagement', technique_version='6.0'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

