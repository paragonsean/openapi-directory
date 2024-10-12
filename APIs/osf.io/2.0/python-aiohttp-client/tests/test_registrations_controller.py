# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.citation_detail import CitationDetail
from openapi_server.models.citation_style import CitationStyle
from openapi_server.models.comment import Comment
from openapi_server.models.contributor import Contributor
from openapi_server.models.file import File
from openapi_server.models.identifier import Identifier
from openapi_server.models.institution import Institution
from openapi_server.models.log import Log
from openapi_server.models.node import Node
from openapi_server.models.registration import Registration
from openapi_server.models.view_only_links import ViewOnlyLinks
from openapi_server.models.wiki import Wiki


pytestmark = pytest.mark.asyncio

async def test_registrations_children_list(client):
    """Test case for registrations_children_list

    List all child registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/children'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_citation_read(client):
    """Test case for registrations_citation_read

    Retrieve a citation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/citations/{citation_id}'.format(registration_id='registration_id_example', citation_id='citation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_citations_list(client):
    """Test case for registrations_citations_list

    List all citation styles
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/citations'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_comments_list(client):
    """Test case for registrations_comments_list

    List all comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/comments'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_contributors_list(client):
    """Test case for registrations_contributors_list

    List all contributors
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/contributors'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_contributors_read(client):
    """Test case for registrations_contributors_read

    Retrieve a contributor
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/contributors/{user_id}'.format(registration_id='registration_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_files_list(client):
    """Test case for registrations_files_list

    List all files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/files/{provider}'.format(registration_id='registration_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_files_read(client):
    """Test case for registrations_files_read

    Retrieve a file
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/files/{provider}/{path}'.format(registration_id='registration_id_example', provider='provider_example', path='path_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_forks_create(client):
    """Test case for registrations_forks_create

    Create a fork
    """
    body = {"data":{"attributes":{"draft_registration":"{draft_registration_id}","lift_embargo":"2017-05-10T20:44:03.185000","registration_choice":"embargo"},"type":"registrations"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/registrations/{registration_id}/forks'.format(registration_id='registration_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_forks_list(client):
    """Test case for registrations_forks_list

    List all forks
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/forks'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_identifiers_list(client):
    """Test case for registrations_identifiers_list

    List all identifiers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/identifiers'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_institutions_list(client):
    """Test case for registrations_institutions_list

    List all institutions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/institutions'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_linked_nodes_list(client):
    """Test case for registrations_linked_nodes_list

    List all linked nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/linked_nodes'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_list(client):
    """Test case for registrations_list

    List all registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_logs_list(client):
    """Test case for registrations_logs_list

    List all logs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/logs'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_partial_update(client):
    """Test case for registrations_partial_update

    Update a registration
    """
    body = {"data":{"attributes":{"draft_registration":"{draft_registration_id}","lift_embargo":"2017-05-10T20:44:03.185000","registration_choice":"embargo"},"type":"registrations"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/registrations/{registration_id}'.format(registration_id='registration_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_providers_list(client):
    """Test case for registrations_providers_list

    List all storage providers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/files'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_read(client):
    """Test case for registrations_read

    Retrieve a registration
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_view_only_links_list(client):
    """Test case for registrations_view_only_links_list

    List all view only links
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/view_only_links'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_view_only_links_read(client):
    """Test case for registrations_view_only_links_read

    Retrieve a view only link
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/view_only_links/{link_id}'.format(registration_id='registration_id_example', link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registrations_wikis_list(client):
    """Test case for registrations_wikis_list

    List all wikis
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/registrations/{registration_id}/wikis'.format(registration_id='registration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

