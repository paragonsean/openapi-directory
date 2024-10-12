# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_autocomplete_school_result import APIAutocompleteSchoolResult


pytestmark = pytest.mark.asyncio

async def test_autocomplete_get_schools(client):
    """Test case for autocomplete_get_schools

    Returns a simple and quick list of schools for use in a client-typed autocomplete
    """
    params = [('q', 'q_example'),
                    ('qSearchCityStateName', True),
                    ('st', 'st_example'),
                    ('level', 'level_example'),
                    ('boxLatitudeNW', 3.4),
                    ('boxLongitudeNW', 3.4),
                    ('boxLatitudeSE', 3.4),
                    ('boxLongitudeSE', 3.4),
                    ('returnCount', 56),
                    ('appID', 'app_id_example'),
                    ('appKey', 'app_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2.0/autocomplete/schools',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

