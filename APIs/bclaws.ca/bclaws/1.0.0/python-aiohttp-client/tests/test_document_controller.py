# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_document_id_aspect_id_civix_index_id_civix_document_id_get(client):
    """Test case for document_id_aspect_id_civix_index_id_civix_document_id_get

    Retrieves a specific document from the BCLaws legislative repository (HTML format)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/document/id/{aspect_id}/{civix_index_id}/{civix_document_id}'.format(aspect_id=complete, civix_index_id='statreg', civix_document_id='01009_01'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_id_aspect_id_civix_index_id_civix_document_id_search_search_string_get(client):
    """Test case for document_id_aspect_id_civix_index_id_civix_document_id_search_search_string_get

    Retrieves a specific document from the BCLaws legislative repository with search text highlighted (HTML format)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/document/id/{aspect_id}/{civix_index_id}/{civix_document_id}/search/{search_string}'.format(aspect_id=complete, civix_index_id='statreg', civix_document_id='01009_01', search_string='water'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_id_aspect_id_civix_index_id_civix_document_id_xml_get(client):
    """Test case for document_id_aspect_id_civix_index_id_civix_document_id_xml_get

    Retrieves a specific document from the BCLaws legislative repository (XML format)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/document/id/{aspect_id}/{civix_index_id}/{civix_document_id}/xml'.format(aspect_id=complete, civix_index_id='statreg', civix_document_id='01009_01'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_document_id_aspect_id_civix_index_id_civix_document_id_xml_search_search_string_get(client):
    """Test case for document_id_aspect_id_civix_index_id_civix_document_id_xml_search_search_string_get

    Retrieves a specific document from the BCLaws legislative repository with search text highlighted (XML format)
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/document/id/{aspect_id}/{civix_index_id}/{civix_document_id}/xml/search/{search_string}'.format(aspect_id=complete, civix_index_id='statreg', civix_document_id='01009_01', search_string='water'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

