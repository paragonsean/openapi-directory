# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.structure_response_many import StructureResponseMany
from openapi_server.models.structure_response_one import StructureResponseOne


pytestmark = pytest.mark.asyncio

async def test_get_single_structure_structures_entry_id_get(client):
    """Test case for get_single_structure_structures_entry_id_get

    Get Single Structure
    """
    params = [('response_format', 'json'),
                    ('email_address', ''),
                    ('response_fields', ''),
                    ('include', 'references'),
                    ('api_hint', '')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/structures/{entry_id}'.format(entry_id='entry_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_structures_structures_get(client):
    """Test case for get_structures_structures_get

    Get Structures
    """
    params = [('filter', ''),
                    ('response_format', 'json'),
                    ('email_address', ''),
                    ('response_fields', ''),
                    ('sort', ''),
                    ('page_limit', 20),
                    ('page_offset', 0),
                    ('page_number', 0),
                    ('page_cursor', 0),
                    ('page_above', 0),
                    ('page_below', 0),
                    ('include', 'references'),
                    ('api_hint', '')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/structures',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

