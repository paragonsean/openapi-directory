# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_content_aspect_id_civix_document_id_get(client):
    """Test case for content_aspect_id_civix_document_id_get

    Lists the metadata available for the specified index or directory from the BCLaws legislative respository
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/content/{aspect_id}/{civix_document_id}'.format(aspect_id=complete, civix_document_id='statreg'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_content_aspect_id_get(client):
    """Test case for content_aspect_id_get

    Describes the documents and directories available within a specific 'aspect' (content group) of the BCLaws library
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/civix/content/{aspect_id}'.format(aspect_id=complete),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

