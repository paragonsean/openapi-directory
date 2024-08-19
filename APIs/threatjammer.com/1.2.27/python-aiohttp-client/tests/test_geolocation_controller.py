# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.geo_ip_collection_output import GeoIPCollectionOutput
from openapi_server.models.geo_ip_output import GeoIPOutput
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_assess_ip_set_csv_v1_geo_csv_post(client):
    """Test case for assess_ip_set_csv_v1_geo_csv_post

    Get the geolocation data of all the IP addresses uploaded.
    """
    params = [('strict_parse', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('csv_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/geo/csv',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geolocate_ip_set_v1_geo_post(client):
    """Test case for geolocate_ip_set_v1_geo_post

    Get the geolocation data of the IP addresses set.
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/geo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_geolocate_ip_v1_geo_ip_address_get(client):
    """Test case for geolocate_ip_v1_geo_ip_address_get

    Get the geo location data of the IP address.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/geo/{ip_address}'.format(ip_address='ip_address_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

