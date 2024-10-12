# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_addresses_output_format_get(client):
    """Test case for addresses_output_format_get

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

async def test_sites_near_output_format_get(client):
    """Test case for sites_near_output_format_get

    Find sites near to a geographic point
    """
    params = [('point', '-122.377,50.121'),
                    ('maxDistance', 56),
                    ('outputSRS', 4326),
                    ('maxResults', 1),
                    ('locationDescriptor', any),
                    ('setBack', 0),
                    ('brief', False),
                    ('excludeUnits', False),
                    ('onlyCivic', False)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sites/near.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_nearest_output_format_get(client):
    """Test case for sites_nearest_output_format_get

    Find the site nearest to a geographic point
    """
    params = [('point', '-122.377,50.121'),
                    ('maxDistance', 56),
                    ('outputSRS', 4326),
                    ('locationDescriptor', any),
                    ('setBack', 0),
                    ('brief', False),
                    ('excludeUnits', False),
                    ('onlyCivic', False)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sites/nearest.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_site_id_output_format_get(client):
    """Test case for sites_site_id_output_format_get

    Get a site by its unique ID
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
        path='/sites/{site_id_output_format}'.format(site_id='site_id_example', output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_site_id_subsites_output_format_get(client):
    """Test case for sites_site_id_subsites_output_format_get

    Represents all subsites of a given site
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
        path='/sites/{site_id}/subsites.{outputFormat}'.format(site_id='site_id_example', output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sites_within_output_format_get(client):
    """Test case for sites_within_output_format_get

    Find sites in a geographic area
    """
    params = [('bbox', '-119.51,49.48,-119.53,49.50'),
                    ('outputSRS', 4326),
                    ('maxResults', 1),
                    ('locationDescriptor', any),
                    ('setBack', 0),
                    ('brief', False),
                    ('excludeUnits', False),
                    ('onlyCivic', False)]
    headers = { 
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/sites/within.{outputFormat}'.format(output_format=json),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

