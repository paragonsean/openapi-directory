# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.release_event_series_for_api_contract import ReleaseEventSeriesForApiContract
from openapi_server.models.release_event_series_for_api_contract_partial_find_result import ReleaseEventSeriesForApiContractPartialFindResult
from openapi_server.models.release_event_series_for_edit_for_api_contract import ReleaseEventSeriesForEditForApiContract
from openapi_server.models.release_event_series_optional_fields import ReleaseEventSeriesOptionalFields


pytestmark = pytest.mark.asyncio

async def test_api_release_event_series_get(client):
    """Test case for api_release_event_series_get

    
    """
    params = [('query', ''),
                    ('fields', openapi_server.ReleaseEventSeriesOptionalFields()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEventSeries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_event_series_id_delete(client):
    """Test case for api_release_event_series_id_delete

    
    """
    params = [('notes', ''),
                    ('hardDelete', False)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/releaseEventSeries/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_event_series_id_for_edit_get(client):
    """Test case for api_release_event_series_id_for_edit_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEventSeries/{id}/for-edit'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_release_event_series_id_get(client):
    """Test case for api_release_event_series_id_get

    
    """
    params = [('fields', openapi_server.ReleaseEventSeriesOptionalFields()),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/releaseEventSeries/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

