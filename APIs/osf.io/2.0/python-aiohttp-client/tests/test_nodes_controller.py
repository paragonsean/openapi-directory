# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon import Addon
from openapi_server.models.citation_detail import CitationDetail
from openapi_server.models.comment import Comment
from openapi_server.models.contributor import Contributor
from openapi_server.models.draft_registration import DraftRegistration
from openapi_server.models.file import File
from openapi_server.models.identifier import Identifier
from openapi_server.models.institution import Institution
from openapi_server.models.log import Log
from openapi_server.models.node import Node
from openapi_server.models.node_addon import NodeAddon
from openapi_server.models.preprint import Preprint
from openapi_server.models.registration import Registration
from openapi_server.models.styled_citation import StyledCitation
from openapi_server.models.view_only_links import ViewOnlyLinks
from openapi_server.models.wiki import Wiki


pytestmark = pytest.mark.asyncio

async def test_nodes_addon_read(client):
    """Test case for nodes_addon_read

    Retrieve an addon
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/addons/{provider}'.format(node_id='node_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_addons_folders_list(client):
    """Test case for nodes_addons_folders_list

    List all addon folders
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/addons/{provider}/folders'.format(node_id='node_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_addons_list(client):
    """Test case for nodes_addons_list

    List all addons
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/addons'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_children_create(client):
    """Test case for nodes_children_create

    Create a child node
    """
    body = {"data":{"attributes":{"category":"software","title":"An Excellent Project Title"},"type":"nodes"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/nodes/{node_id}/children'.format(node_id='node_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_children_list(client):
    """Test case for nodes_children_list

    List all child nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/children'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_citation_list(client):
    """Test case for nodes_citation_list

    Retrieve citation details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/citation'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_citation_read(client):
    """Test case for nodes_citation_read

    Retrieve a styled citation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/citation/{style_id}'.format(style_id='style_id_example', node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_comment_create(client):
    """Test case for nodes_comment_create

    Create a comment
    """
    body = {"data":{"attributes":{"content":"comment content"},"relationships":{"target":{"data":{"id":"{target_id}","type":"{target_type}"}}},"type":"comments"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/nodes/{node_id}/comments'.format(node_id='node_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_comments_list(client):
    """Test case for nodes_comments_list

    List all comments
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/comments'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_contributors_create(client):
    """Test case for nodes_contributors_create

    Create a contributor
    """
    body = {"data":{"attributes":{},"relationships":{"user":{"data":{"id":"guid0","type":"users"}}},"type":"contributors"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/nodes/{node_id}/contributors'.format(node_id='node_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_contributors_delete(client):
    """Test case for nodes_contributors_delete

    Delete a contributor
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/nodes/{node_id}/contributors/{user_id}'.format(node_id='node_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_contributors_list(client):
    """Test case for nodes_contributors_list

    List all contributors
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/contributors'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_contributors_partial_update(client):
    """Test case for nodes_contributors_partial_update

    Update a contributor
    """
    body = {"data":{"attributes":{},"relationships":{"user":{"data":{"id":"guid0","type":"users"}}},"type":"contributors"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/nodes/{node_id}/contributors/{user_id}'.format(node_id='node_id_example', user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_contributors_read(client):
    """Test case for nodes_contributors_read

    Retrieve a contributor
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/contributors/{user_id}'.format(node_id='node_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_create(client):
    """Test case for nodes_create

    Create a node
    """
    body = {"data":{"attributes":{"category":"software","title":"An Excellent Project Title"},"type":"nodes"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/nodes/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_delete(client):
    """Test case for nodes_delete

    Delete a node
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/nodes/{node_id}'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_draft_registrations_create(client):
    """Test case for nodes_draft_registrations_create

    Create a draft registration based on your current project Node.
    """
    body = openapi_server.DraftRegistration()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/nodes/{node_id}/draft_registrations'.format(node_id='node_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_draft_registrations_delete(client):
    """Test case for nodes_draft_registrations_delete

    Delete a draft registration
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/nodes/{node_id}/draft_registrations/{draft_id}'.format(node_id='node_id_example', draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_draft_registrations_list(client):
    """Test case for nodes_draft_registrations_list

    List all draft registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/draft_registrations'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_draft_registrations_partial_update(client):
    """Test case for nodes_draft_registrations_partial_update

    Update a draft registration
    """
    body = openapi_server.DraftRegistration()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/nodes/{node_id}/draft_registrations/{draft_id}'.format(node_id='node_id_example', draft_id='draft_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_files_list(client):
    """Test case for nodes_files_list

    List all node files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/files/{provider}'.format(node_id='node_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_files_read(client):
    """Test case for nodes_files_read

    Retrieve a file
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/files/{provider}/{path}'.format(node_id='node_id_example', provider='provider_example', path='path_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_forks_create(client):
    """Test case for nodes_forks_create

    Create a fork of this node
    """
    body = {"data":{"attributes":{"category":"software","title":"An Excellent Project Title"},"type":"nodes"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/nodes/{node_id}/forks'.format(node_id='node_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_forks_list(client):
    """Test case for nodes_forks_list

    List all forks of this node
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/forks'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_identifiers_list(client):
    """Test case for nodes_identifiers_list

    List all identifiers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/identifiers'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_institutions_list(client):
    """Test case for nodes_institutions_list

    List all institutions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/institutions'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_linked_nodes_list(client):
    """Test case for nodes_linked_nodes_list

    List all linked nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/linked_nodes'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_list(client):
    """Test case for nodes_list

    List all nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_logs_list(client):
    """Test case for nodes_logs_list

    List all logs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/logs'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_node_addon_update(client):
    """Test case for nodes_node_addon_update

    Update an addon
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/nodes/{node_id}/addons/{provider}'.format(node_id='node_id_example', provider='provider_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_partial_update(client):
    """Test case for nodes_partial_update

    Update a node
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/nodes/{node_id}'.format(node_id='node_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_preprints_list(client):
    """Test case for nodes_preprints_list

    List all preprints
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/preprints'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_providers_list(client):
    """Test case for nodes_providers_list

    List all storage providers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/files'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_providers_read(client):
    """Test case for nodes_providers_read

    Retrieve a storage provider
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/files/providers/{provider}'.format(node_id='node_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_read(client):
    """Test case for nodes_read

    Retrieve a node
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_registrations_list(client):
    """Test case for nodes_registrations_list

    List all registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/registrations'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_view_only_links_list(client):
    """Test case for nodes_view_only_links_list

    List all view only links
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/view_only_links'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_view_only_links_read(client):
    """Test case for nodes_view_only_links_read

    Retrieve a view only link
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/view_only_links/{link_id}'.format(node_id='node_id_example', link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_wikis_list(client):
    """Test case for nodes_wikis_list

    List all wikis
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/wikis'.format(node_id='node_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

