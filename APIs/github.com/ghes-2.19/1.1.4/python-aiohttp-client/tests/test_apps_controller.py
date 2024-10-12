# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.apps_create_content_attachment_request import AppsCreateContentAttachmentRequest
from openapi_server.models.apps_create_from_manifest201_response import AppsCreateFromManifest201Response
from openapi_server.models.apps_create_installation_access_token_request import AppsCreateInstallationAccessTokenRequest
from openapi_server.models.apps_get_installation415_response import AppsGetInstallation415Response
from openapi_server.models.apps_list_installation_repos_for_authenticated_user200_response import AppsListInstallationReposForAuthenticatedUser200Response
from openapi_server.models.apps_list_repos_accessible_to_installation200_response import AppsListReposAccessibleToInstallation200Response
from openapi_server.models.basic_error import BasicError
from openapi_server.models.content_reference_attachment import ContentReferenceAttachment
from openapi_server.models.installation_ghes2 import InstallationGhes2
from openapi_server.models.installation_token import InstallationToken
from openapi_server.models.integration import Integration
from openapi_server.models.orgs_list_app_installations200_response import OrgsListAppInstallations200Response
from openapi_server.models.validation_error import ValidationError
from openapi_server.models.validation_error_simple import ValidationErrorSimple


pytestmark = pytest.mark.asyncio

async def test_apps_add_repo_to_installation(client):
    """Test case for apps_add_repo_to_installation

    Add a repository to an app installation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/user/installations/{installation_id}/repositories/{repository_id}'.format(installation_id=56, repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_create_content_attachment(client):
    """Test case for apps_create_content_attachment

    Create a content attachment
    """
    body = openapi_server.AppsCreateContentAttachmentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/content_references/{content_reference_id}/attachments'.format(owner='owner_example', repo='repo_example', content_reference_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_create_from_manifest(client):
    """Test case for apps_create_from_manifest

    Create a GitHub App from a manifest
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/app-manifests/{code}/conversions'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_create_installation_access_token(client):
    """Test case for apps_create_installation_access_token

    Create an installation access token for an app
    """
    body = openapi_server.AppsCreateInstallationAccessTokenRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/app/installations/{installation_id}/access_tokens'.format(installation_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_delete_installation(client):
    """Test case for apps_delete_installation

    Delete an installation for the authenticated app
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.gambit-preview+json,application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/app/installations/{installation_id}'.format(installation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_authenticated(client):
    """Test case for apps_get_authenticated

    Get the authenticated app
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/app',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_by_slug(client):
    """Test case for apps_get_by_slug

    Get an app
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/apps/{app_slug}'.format(app_slug='app_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_installation(client):
    """Test case for apps_get_installation

    Get an installation for the authenticated app
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/app/installations/{installation_id}'.format(installation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_org_installation(client):
    """Test case for apps_get_org_installation

    Get an organization installation for the authenticated app
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/installation'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_repo_installation(client):
    """Test case for apps_get_repo_installation

    Get a repository installation for the authenticated app
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/installation'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_get_user_installation(client):
    """Test case for apps_get_user_installation

    Get a user installation for the authenticated app
    """
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/installation'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_installation_repos_for_authenticated_user(client):
    """Test case for apps_list_installation_repos_for_authenticated_user

    List repositories accessible to the user access token
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/installations/{installation_id}/repositories'.format(installation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_installations(client):
    """Test case for apps_list_installations

    List installations for the authenticated app
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/app/installations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_installations_for_authenticated_user(client):
    """Test case for apps_list_installations_for_authenticated_user

    List app installations accessible to the user access token
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/installations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_list_repos_accessible_to_installation(client):
    """Test case for apps_list_repos_accessible_to_installation

    List repositories accessible to the app installation
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/vnd.github.machine-man-preview+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/installation/repositories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_apps_remove_repo_from_installation(client):
    """Test case for apps_remove_repo_from_installation

    Remove a repository from an app installation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/installations/{installation_id}/repositories/{repository_id}'.format(installation_id=56, repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

