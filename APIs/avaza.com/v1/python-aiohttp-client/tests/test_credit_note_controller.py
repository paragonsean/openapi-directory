# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credit_note import CreditNote
from openapi_server.models.credit_note_list import CreditNoteList


pytestmark = pytest.mark.asyncio

async def test_credit_note_get(client):
    """Test case for credit_note_get

    Gets list of CreditNotes
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/CreditNote',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_credit_note_get_by_id(client):
    """Test case for credit_note_get_by_id

    Gets Credit Note by CreditNoteID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/CreditNote/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

