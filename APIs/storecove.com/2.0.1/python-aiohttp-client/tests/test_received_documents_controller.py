# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.received_document import ReceivedDocument
from openapi_server.models.received_document_create import ReceivedDocumentCreate


pytestmark = pytest.mark.asyncio

async def test_get_received_document(client):
    """Test case for get_received_document

    Get a new ReceivedDocument
    """
    params = [('syntax', json)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/received_documents/{guid}/{format}'.format(guid='guid_example', format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_receive_document(client):
    """Test case for receive_document

    Receive a new Document
    """
    body = {"document":"document","parseStrategy":"rfc822"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/legal_entities/{legal_entity_id}/received_documents'.format(legal_entity_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

