# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.article_project_create import ArticleProjectCreate
from openapi_server.models.create_project_response import CreateProjectResponse
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.location import Location
from openapi_server.models.location_warnings import LocationWarnings
from openapi_server.models.private_file import PrivateFile
from openapi_server.models.project import Project
from openapi_server.models.project_article import ProjectArticle
from openapi_server.models.project_collaborator import ProjectCollaborator
from openapi_server.models.project_collaborator_invite import ProjectCollaboratorInvite
from openapi_server.models.project_complete import ProjectComplete
from openapi_server.models.project_complete_private import ProjectCompletePrivate
from openapi_server.models.project_create import ProjectCreate
from openapi_server.models.project_note import ProjectNote
from openapi_server.models.project_note_create import ProjectNoteCreate
from openapi_server.models.project_note_private import ProjectNotePrivate
from openapi_server.models.project_private import ProjectPrivate
from openapi_server.models.project_update import ProjectUpdate
from openapi_server.models.projects_search import ProjectsSearch
from openapi_server.models.response_message import ResponseMessage


pytestmark = pytest.mark.asyncio

async def test_private_project_article_delete(client):
    """Test case for private_project_article_delete

    Delete project article
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/projects/{project_id}/articles/{article_id}'.format(project_id=56, article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_article_details(client):
    """Test case for private_project_article_details

    Project article details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/articles/{article_id}'.format(project_id=56, article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_article_file(client):
    """Test case for private_project_article_file

    Project article file details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/articles/{article_id}/files/{file_id}'.format(project_id=56, article_id=56, file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_article_files(client):
    """Test case for private_project_article_files

    Project article list files
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/articles/{article_id}/files'.format(project_id=56, article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_articles_create(client):
    """Test case for private_project_articles_create

    Create project article
    """
    body = {"categories_by_source_id":["300204","400207"],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","keywords":["tag1","tag2"],"references":["http://figshare.com","http://api.figshare.com"],"custom_fields":{"defined_key":"value for it"},"description":"Test description of article","handle":"","title":"Test article title","tags":["tag1","tag2"],"defined_type":"media","funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"license":1,"resource_doi":"","resource_title":"","timeline":{"firstOnline":"2015-12-31","publisherAcceptance":"2015-12-31","publisherPublication":"2015-12-31"},"categories":[1,10,11],"authors":[{"name":"John Doe"},{"id":1000008}],"doi":""}
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects/{project_id}/articles'.format(project_id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_articles_list(client):
    """Test case for private_project_articles_list

    List project articles
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/articles'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_collaborator_delete(client):
    """Test case for private_project_collaborator_delete

    Remove project collaborator
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/projects/{project_id}/collaborators/{user_id}'.format(project_id=56, user_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_collaborators_invite(client):
    """Test case for private_project_collaborators_invite

    Invite project collaborators
    """
    body = {"role_name":"viewer","user_id":100008,"comment":"hey","email":"user@domain.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects/{project_id}/collaborators'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_collaborators_list(client):
    """Test case for private_project_collaborators_list

    List project collaborators
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/collaborators'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_create(client):
    """Test case for private_project_create

    Create project
    """
    body = {"funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","group_id":0,"custom_fields":{"defined_key":"value for it"},"description":"project description","title":"project title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_delete(client):
    """Test case for private_project_delete

    Delete project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_details(client):
    """Test case for private_project_details

    View project details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_leave(client):
    """Test case for private_project_leave

    Private Project Leave
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects/{project_id}/leave'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_note(client):
    """Test case for private_project_note

    Project note details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/notes/{note_id}'.format(project_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_note_delete(client):
    """Test case for private_project_note_delete

    Delete project note
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/projects/{project_id}/notes/{note_id}'.format(project_id=56, note_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_note_update(client):
    """Test case for private_project_note_update

    Update project note
    """
    body = {"text":"note to remember"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/projects/{project_id}/notes/{note_id}'.format(project_id=56, note_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_notes_create(client):
    """Test case for private_project_notes_create

    Create project note
    """
    body = {"text":"note to remember"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects/{project_id}/notes'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_notes_list(client):
    """Test case for private_project_notes_list

    List project notes
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects/{project_id}/notes'.format(project_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_publish(client):
    """Test case for private_project_publish

    Private Project Publish
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects/{project_id}/publish'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_project_update(client):
    """Test case for private_project_update

    Update project
    """
    body = {"funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","custom_fields":{"defined_key":"value for it"},"description":"project description","title":"project title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/projects/{project_id}'.format(project_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_projects_list(client):
    """Test case for private_projects_list

    Private Projects
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56),
                    ('order', published_date),
                    ('order_direction', desc),
                    ('storage', 'storage_example'),
                    ('roles', 'roles_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_projects_search(client):
    """Test case for private_projects_search

    Private Projects search
    """
    body = {"order":"published_date"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/projects/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_articles(client):
    """Test case for project_articles

    Public Project Articles
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/projects/{project_id}/articles'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_details(client):
    """Test case for project_details

    Public Project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/projects/{project_id}'.format(project_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_list(client):
    """Test case for projects_list

    Public Projects
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56),
                    ('order', published_date),
                    ('order_direction', desc),
                    ('institution', 56),
                    ('published_since', 'published_since_example'),
                    ('group', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_cursor': 'x_cursor_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_projects_search(client):
    """Test case for projects_search

    Public Projects Search
    """
    body = {"order":"published_date"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_cursor': 'x_cursor_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/projects/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

