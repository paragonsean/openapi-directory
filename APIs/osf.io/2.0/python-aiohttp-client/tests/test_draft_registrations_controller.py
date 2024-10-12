# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contributor import Contributor
from openapi_server.models.draft_registration import DraftRegistration
from openapi_server.models.institution import Institution
from openapi_server.models.subject import Subject


pytestmark = pytest.mark.asyncio

async def test_draft_registration_contributors_create(client):
    """Test case for draft_registration_contributors_create

    Add a contributor to a Draft Registration
    """
    body = {"data":{"attributes":{},"relationships":{"user":{"data":{"id":"guid0","type":"users"}}},"type":"contributors"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/draft_registrations/{draft_id}/contributors'.format(draft_id='draft_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registration_contributors_list(client):
    """Test case for draft_registration_contributors_list

    Retreive a list Contributors from a Draft Registration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/draft_registrations/{draft_id}/contributors'.format(draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_create(client):
    """Test case for draft_registrations_create

    Create a Draft Registration
    """
    body = openapi_server.DraftRegistration()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/draft_registrations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_draft_id_contributors_user_id_get(client):
    """Test case for draft_registrations_draft_id_contributors_user_id_get

    Retreive a Contributor from a Draft Registration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/draft_registrations/{draft_id}/contributors/{user_id}'.format(draft_id='draft_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_draft_id_delete(client):
    """Test case for draft_registrations_draft_id_delete

    Delete a draft registration
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/v2/draft_registrations/{draft_id}'.format(draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_draft_id_get(client):
    """Test case for draft_registrations_draft_id_get

    Retrieve a Draft Registration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/draft_registrations/{draft_id}'.format(draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_draft_id_institutions_get(client):
    """Test case for draft_registrations_draft_id_institutions_get

    Retrieve Institutions afilliated with a Draft Registration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/draft_registrations/{draft_id}/institutions'.format(draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_draft_id_patch(client):
    """Test case for draft_registrations_draft_id_patch

    Update a Draft Registration
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/draft_registrations/{draft_id}'.format(draft_id='draft_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_draft_registrations_read(client):
    """Test case for draft_registrations_read

    Retrieve a list of Draft Registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/draft_registrations/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_draft_registrations_read(client):
    """Test case for nodes_draft_registrations_read

    Retrieve a Draft Registration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/nodes/{node_id}/draft_registrations/{draft_id}'.format(node_id='node_id_example', draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_nodes_draft_registrations_subjects(client):
    """Test case for nodes_draft_registrations_subjects

    Retrieve Subjects associated with a Draft Registration
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/draft_registrations/{draft_id}/subjects'.format(draft_id='draft_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

