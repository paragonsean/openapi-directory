# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.org_classification import OrgClassification
from openapi_server.models.person_include import PersonInclude
from openapi_server.models.person_list import PersonList


pytestmark = pytest.mark.asyncio

async def test_people_geo_people_geo_get(client):
    """Test case for people_geo_people_geo_get

    People Geo
    """
    params = [('lat', 3.4),
                    ('lng', 3.4),
                    ('include', []),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/people.geo',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_people_search_people_get(client):
    """Test case for people_search_people_get

    People Search
    """
    params = [('jurisdiction', 'jurisdiction_example'),
                    ('name', 'name_example'),
                    ('id', []),
                    ('org_classification', openapi_server.OrgClassification()),
                    ('district', 'district_example'),
                    ('include', []),
                    ('page', 1),
                    ('per_page', 10),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/people',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

