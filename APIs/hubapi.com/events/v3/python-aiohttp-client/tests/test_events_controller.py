# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_response_external_unified_event import CollectionResponseExternalUnifiedEvent
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_events_v3_events_get_page(client):
    """Test case for get_events_v3_events_get_page

    
    """
    params = [('objectType', 'object_type_example'),
                    ('eventType', 'event_type_example'),
                    ('occurredAfter', '2013-10-20T19:20:30+01:00'),
                    ('occurredBefore', '2013-10-20T19:20:30+01:00'),
                    ('objectId', 56),
                    ('indexTableName', 'index_table_name_example'),
                    ('indexSpecificMetadata', 'index_specific_metadata_example'),
                    ('after', 'after_example'),
                    ('before', 'before_example'),
                    ('limit', 56),
                    ('sort', ['sort_example']),
                    ('objectProperty.{propname}', None),
                    ('property.{propname}', None),
                    ('id', ['id_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'private_apps_legacy': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/events/v3/events/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

