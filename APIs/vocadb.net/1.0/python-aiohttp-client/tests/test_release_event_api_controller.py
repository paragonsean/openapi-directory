# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album_for_api_contract import AlbumForApiContract
from openapi_server.models.album_optional_fields import AlbumOptionalFields
from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.event_category import EventCategory
from openapi_server.models.event_report_type import EventReportType
from openapi_server.models.event_sort_rule import EventSortRule
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.release_event_for_api_contract import ReleaseEventForApiContract
from openapi_server.models.release_event_for_api_contract_partial_find_result import ReleaseEventForApiContractPartialFindResult
from openapi_server.models.release_event_optional_fields import ReleaseEventOptionalFields
from openapi_server.models.song_for_api_contract import SongForApiContract
from openapi_server.models.song_optional_fields import SongOptionalFields
from openapi_server.models.sort_direction import SortDirection


pytestmark = pytest.mark.asyncio

async def test_api_release_events_event_id_albums_get(client):
    """Test case for api_release_events_event_id_albums_get

    
    """
    params = [('fields', openapi_server.AlbumOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEvents/{event_id}/albums'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_events_event_id_published_songs_get(client):
    """Test case for api_release_events_event_id_published_songs_get

    
    """
    params = [('fields', openapi_server.SongOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEvents/{event_id}/published-songs'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_events_event_id_reports_post(client):
    """Test case for api_release_events_event_id_reports_post

    
    """
    params = [('reportType', openapi_server.EventReportType()),
                    ('notes', 'notes_example'),
                    ('versionNumber', 56)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/releaseEvents/{event_id}/reports'.format(event_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_events_get(client):
    """Test case for api_release_events_get

    
    """
    params = [('query', ''),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('seriesId', 0),
                    ('afterDate', '2013-10-20T19:20:30+01:00'),
                    ('beforeDate', '2013-10-20T19:20:30+01:00'),
                    ('category', openapi_server.EventCategory()),
                    ('userCollectionId', 56),
                    ('tagId[]', [56]),
                    ('childTags', False),
                    ('artistId[]', [56]),
                    ('childVoicebanks', False),
                    ('includeMembers', False),
                    ('status', openapi_server.EntryStatus()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('sort', openapi_server.EventSortRule()),
                    ('fields', openapi_server.ReleaseEventOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference()),
                    ('sortDirection', openapi_server.SortDirection())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEvents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_events_id_delete(client):
    """Test case for api_release_events_id_delete

    
    """
    params = [('notes', ''),
                    ('hardDelete', False)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/releaseEvents/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_events_id_get(client):
    """Test case for api_release_events_id_get

    
    """
    params = [('fields', openapi_server.ReleaseEventOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEvents/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_events_names_get(client):
    """Test case for api_release_events_names_get

    
    """
    params = [('query', ''),
                    ('maxResults', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEvents/names',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

