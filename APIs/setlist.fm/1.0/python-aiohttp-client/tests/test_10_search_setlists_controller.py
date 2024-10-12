# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.json_setlists import JsonSetlists


pytestmark = pytest.mark.asyncio

async def test_resource10_search_setlists_get_setlists_get(client):
    """Test case for resource10_search_setlists_get_setlists_get

    Search for setlists.
    """
    params = [('artistMbid', 'artist_mbid_example'),
                    ('artistName', 'artist_name_example'),
                    ('artistTmid', 56),
                    ('cityId', 'city_id_example'),
                    ('cityName', 'city_name_example'),
                    ('countryCode', 'country_code_example'),
                    ('date', '_date_example'),
                    ('lastFm', 56),
                    ('lastUpdated', 'last_updated_example'),
                    ('p', 1),
                    ('state', 'state_example'),
                    ('stateCode', 'state_code_example'),
                    ('tourName', 'tour_name_example'),
                    ('venueId', 'venue_id_example'),
                    ('venueName', 'venue_name_example'),
                    ('year', 'year_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/1.0/search/setlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

