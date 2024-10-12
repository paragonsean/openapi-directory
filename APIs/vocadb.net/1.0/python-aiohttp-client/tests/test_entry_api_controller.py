# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_for_api_contract_partial_find_result import EntryForApiContractPartialFindResult
from openapi_server.models.entry_optional_fields import EntryOptionalFields
from openapi_server.models.entry_sort_rule import EntrySortRule
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.entry_types import EntryTypes
from openapi_server.models.name_match_mode import NameMatchMode


pytestmark = pytest.mark.asyncio

async def test_api_entries_get(client):
    """Test case for api_entries_get

    
    """
    params = [('query', ''),
                    ('tagName[]', ['tag_name_example']),
                    ('tagId[]', [56]),
                    ('childTags', False),
                    ('entryTypes', openapi_server.EntryTypes()),
                    ('status', openapi_server.EntryStatus()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.EntrySortRule()),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('fields', openapi_server.EntryOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/entries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_entries_names_get(client):
    """Test case for api_entries_names_get

    
    """
    params = [('query', ''),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('maxResults', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/entries/names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

