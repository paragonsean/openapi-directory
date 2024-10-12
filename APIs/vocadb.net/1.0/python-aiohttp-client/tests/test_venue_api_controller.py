# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.content_language_preference import ContentLanguagePreference
from openapi_server.models.distance_unit import DistanceUnit
from openapi_server.models.name_match_mode import NameMatchMode
from openapi_server.models.venue_for_api_contract_partial_find_result import VenueForApiContractPartialFindResult
from openapi_server.models.venue_optional_fields import VenueOptionalFields
from openapi_server.models.venue_report_type import VenueReportType
from openapi_server.models.venue_sort_rule import VenueSortRule


pytestmark = pytest.mark.asyncio

async def test_api_venues_get(client):
    """Test case for api_venues_get

    
    """
    params = [('query', ''),
                    ('fields', openapi_server.VenueOptionalFields()),
                    ('start', 0),
                    ('maxResults', 10),
                    ('getTotalCount', False),
                    ('nameMatchMode', openapi_server.NameMatchMode()),
                    ('lang', openapi_server.ContentLanguagePreference()),
                    ('sortRule', openapi_server.VenueSortRule()),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 3.4),
                    ('distanceUnit', openapi_server.DistanceUnit())]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/venues',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_venues_id_delete(client):
    """Test case for api_venues_id_delete

    
    """
    params = [('notes', ''),
                    ('hardDelete', False)]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/venues/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_venues_id_reports_post(client):
    """Test case for api_venues_id_reports_post

    
    """
    params = [('reportType', openapi_server.VenueReportType()),
                    ('notes', 'notes_example'),
                    ('versionNumber', 56)]
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/venues/{id}/reports'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

