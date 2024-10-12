# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_entry_for_api_contract_partial_find_result import ActivityEntryForApiContractPartialFindResult
from openapi_server.models.activity_entry_optional_fields import ActivityEntryOptionalFields
from openapi_server.models.activity_entry_sort_rule import ActivityEntrySortRule
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_edit_event import EntryEditEvent
from openapi_server.models.entry_optional_fields import EntryOptionalFields
from openapi_server.models.entry_type import EntryType


pytestmark = pytest.mark.asyncio

async def test_api_activity_entries_get(client):
    """Test case for api_activity_entries_get

    
    """
    params = [('before', '2013-10-20T19:20:30+01:00'),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('userId', 56),
                    ('editEvent', openapi_server.EntryEditEvent()),
                    ('entryType', openapi_server.EntryType()),
                    ('maxResults', 50),
                    ('getTotalCount', False),
                    ('fields', openapi_server.ActivityEntryOptionalFields()),
                    ('entryFields', openapi_server.EntryOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference()),
                    ('sortRule', openapi_server.ActivityEntrySortRule())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/activityEntries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

