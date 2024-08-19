# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_addresses_output_format_get_0(client):
    """Test case for addresses_output_format_get_0

    Geocode an address
    """
    params = [('addressString', '525 Superior Street, Victoria, BC'),
                    ('locationDescriptor', any),
                    ('maxResults', 1),
                    ('interpolation', adaptive),
                    ('echo', True),
                    ('brief', False),
                    ('autoComplete', False),
                    ('setBack', 0),
                    ('outputSRS', 4326),
                    ('minScore', 1),
                    ('matchPrecision', 'match_precision_example'),
                    ('matchPrecisionNot', 'match_precision_not_example'),
                    ('siteName', 'site_name_example'),
                    ('unitDesignator', 'unit_designator_example'),
                    ('unitNumber', 'unit_number_example'),
                    ('unitNumberSuffix', 'unit_number_suffix_example'),
                    ('civicNumber', 'civic_number_example'),
                    ('civicNumberSuffix', 'civic_number_suffix_example'),
                    ('streetName', 'street_name_example'),
                    ('streetType', 'street_type_example'),
                    ('streetDirection', 'street_direction_example'),
                    ('streetQualifier', 'street_qualifier_example'),
                    ('localityName', 'locality_name_example'),
                    ('provinceCode', 'BC'),
                    ('localities', 'localities_example'),
                    ('notLocalities', 'not_localities_example'),
                    ('bbox', 'bbox_example'),
                    ('centre', 'centre_example'),
                    ('maxDistance', 3.4),
                    ('extrapolate', True),
                    ('parcelPoint', 'parcel_point_example')]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/addresses.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_intersections_intersection_id_output_format_get(client):
    """Test case for intersections_intersection_id_output_format_get

    Get an intersection by its unique ID
    """
    params = [('outputSRS', 4326)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/intersections/{intersection_id_output_format}'.format(intersection_id='intersection_id_example', output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_intersections_near_output_format_get(client):
    """Test case for intersections_near_output_format_get

    Find intersections near to a geographic point
    """
    params = [('point', '-122.377,50.121'),
                    ('maxDistance', 56),
                    ('outputSRS', 4326),
                    ('maxResults', 1),
                    ('minDegree', 2),
                    ('maxDegree', 100)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/intersections/near.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_intersections_nearest_output_format_get(client):
    """Test case for intersections_nearest_output_format_get

    Find nearest intersection to a geographic point
    """
    params = [('point', '-122.377,50.121'),
                    ('maxDistance', 56),
                    ('outputSRS', 4326),
                    ('minDegree', 2),
                    ('maxDegree', 100)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/intersections/nearest.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_intersections_within_output_format_get(client):
    """Test case for intersections_within_output_format_get

    Find intersections in a geographic area
    """
    params = [('bbox', '-119.51,49.48,-119.53,49.50'),
                    ('outputSRS', 4326),
                    ('maxResults', 200),
                    ('minDegree', 2),
                    ('maxDegree', 100)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/intersections/within.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

