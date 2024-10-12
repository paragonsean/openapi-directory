# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.citation_detail import CitationDetail
from openapi_server.models.contributor1 import Contributor1
from openapi_server.models.preprint import Preprint
from openapi_server.models.styled_citation import StyledCitation


pytestmark = pytest.mark.asyncio

async def test_preprints_bibliographic_contributors_list(client):
    """Test case for preprints_bibliographic_contributors_list

    List all Bibliographic Contributors
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/{preprint_id}/bibliographic_contributors'.format(preprint_id='preprint_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_citation_list(client):
    """Test case for preprints_citation_list

    Retrieve citation details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/{preprint_id}/citation'.format(preprint_id='preprint_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_citation_read(client):
    """Test case for preprints_citation_read

    Retrieve a styled citation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/{preprint_id}/citation/{style_id}'.format(style_id='style_id_example', preprint_id='preprint_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_contributor_read(client):
    """Test case for preprints_contributor_read

    Retrieve a contributor
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/{preprint_id}/contributors/{user_id}'.format(preprint_id='preprint_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_contributors_create(client):
    """Test case for preprints_contributors_create

    Create a Contributor
    """
    body = openapi_server.Contributor1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/preprints/{preprint_id}/contributors'.format(preprint_id='preprint_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_contributors_list(client):
    """Test case for preprints_contributors_list

    List all Contributors for a Preprint
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/{preprint_id}/contributors'.format(preprint_id='preprint_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_create(client):
    """Test case for preprints_create

    Create a preprint
    """
    body = {"data":{"attributes":{},"relationships":{"node":{"data":{"id":"{node_id}","type":"nodes"}},"primary_file":{"data":{"id":"{primary_file_id}","type":"primary_files"}},"provider":{"data":{"id":"{preprint_provider_id}","type":"providers"}}}}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/preprints/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_list(client):
    """Test case for preprints_list

    List all preprints
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_partial_update(client):
    """Test case for preprints_partial_update

    Update a preprint
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/preprints/{preprint_id}'.format(preprint_id='preprint_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_preprints_read(client):
    """Test case for preprints_read

    Retrieve a preprint
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/preprints/{preprint_id}'.format(preprint_id='preprint_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

