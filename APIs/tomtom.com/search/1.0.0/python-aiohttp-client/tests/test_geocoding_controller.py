# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_search_version_number_geocode_query_ext_get(client):
    """Test case for search_version_number_geocode_query_ext_get

    Geocode
    """
    params = [('storeResult', False),
                    ('typeahead', False),
                    ('limit', 10),
                    ('ofs', 0),
                    ('countrySet', 'FR'),
                    ('lat', 37.337),
                    ('lon', -121.89),
                    ('radius', 56),
                    ('topLeft', '37.553,-122.453'),
                    ('btmRight', '37.4,-122.55'),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example'),
                    ('view', Unified)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/geocode/{query_ext}'.format(version_number=56, query='4 north 2nd street san jose', ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_version_number_structured_geocode_ext_get(client):
    """Test case for search_version_number_structured_geocode_ext_get

    Structured Geocode
    """
    params = [('countryCode', 'NL'),
                    ('limit', 10),
                    ('ofs', 0),
                    ('streetNumber', 'street_number_example'),
                    ('streetName', 'street_name_example'),
                    ('crossStreet', 'cross_street_example'),
                    ('municipality', 'Amsterdam'),
                    ('municipalitySubdivision', 'municipality_subdivision_example'),
                    ('countryTertiarySubdivision', 'country_tertiary_subdivision_example'),
                    ('countrySecondarySubdivision', 'country_secondary_subdivision_example'),
                    ('countrySubdivision', 'country_subdivision_example'),
                    ('postalCode', 'postal_code_example'),
                    ('language', 'language_example'),
                    ('extendedPostalCodesFor', 'extended_postal_codes_for_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/search/{version_number}/structuredGeocode.{ext}'.format(version_number=56, ext='xml'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

