# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.pv_for_song_contract_partial_find_result import PVForSongContractPartialFindResult
from openapi_server.models.pv_service import PVService


pytestmark = pytest.mark.asyncio

async def test_api_pvs_for_songs_get(client):
    """Test case for api_pvs_for_songs_get

    
    """
    params = [('name', 'name_example'),
                    ('author', 'author_example'),
                    ('service', openapi_server.PVService()),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('lang', openapi_server.ContentLanguagePreference())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/pvs/for-songs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

