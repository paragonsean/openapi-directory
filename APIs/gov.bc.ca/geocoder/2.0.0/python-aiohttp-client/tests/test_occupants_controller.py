# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_occupants_addresses_output_format_get(client):
    """Test case for occupants_addresses_output_format_get

    Geocode an address and identify site occupants
    """
    params = [('addressString', 'Sir James Douglas Elementary'),
                    ('tags', 'tags_example'),
                    ('locationDescriptor', any),
                    ('maxResults', 1),
                    ('interpolation', adaptive),
                    ('echo', False),
                    ('brief', False),
                    ('autoComplete', False),
                    ('setBack', 0),
                    ('outputSRS', 4326),
                    ('minScore', 1),
                    ('matchPrecision', 'OCCUPANT'),
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
        path='/occupants/addresses.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupants_near_output_format_get(client):
    """Test case for occupants_near_output_format_get

    Find occupants of sites near to a geographic point
    """
    params = [('point', '-122.377,50.121'),
                    ('tags', 'tags_example'),
                    ('maxDistance', 56),
                    ('outputSRS', 4326),
                    ('maxResults', 1),
                    ('locationDescriptor', any),
                    ('brief', False),
                    ('setBack', 0)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/occupants/near.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupants_nearest_output_format_get(client):
    """Test case for occupants_nearest_output_format_get

    Find occupants of the site nearest to a geographic point
    """
    params = [('point', '-122.377,50.121'),
                    ('maxDistance', 56),
                    ('tags', 'tags_example'),
                    ('outputSRS', 4326),
                    ('locationDescriptor', any),
                    ('brief', False),
                    ('setBack', 0)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/occupants/nearest.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupants_occupant_id_output_format_get(client):
    """Test case for occupants_occupant_id_output_format_get

    Get an occupant (of a site) by its unique ID
    """
    params = [('outputSRS', 4326),
                    ('locationDescriptor', any),
                    ('brief', False),
                    ('setBack', 0)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/occupants/{occupant_id_output_format}'.format(occupant_id='occupant_id_example', output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_occupants_within_output_format_get(client):
    """Test case for occupants_within_output_format_get

    Find occupants of sites in a geographic area
    """
    params = [('bbox', '-123.14,49.28,-123.13,49.29'),
                    ('tags', 'tags_example'),
                    ('outputSRS', 4326),
                    ('maxResults', 200),
                    ('locationDescriptor', any),
                    ('brief', False),
                    ('setBack', 0)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/occupants/within.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

