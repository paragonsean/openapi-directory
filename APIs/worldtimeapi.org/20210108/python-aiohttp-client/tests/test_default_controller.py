# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.date_time_json_response import DateTimeJsonResponse
from openapi_server.models.error_json_response import ErrorJsonResponse


pytestmark = pytest.mark.asyncio

async def test_ip_get(client):
    """Test case for ip_get

    request the current time based on the ip of the request. note: this is a \"best guess\" obtained from open-source data.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ip',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_ipv4_get(client):
    """Test case for ip_ipv4_get

    request the current time based on the ip of the request. note: this is a \"best guess\" obtained from open-source data.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/ip/{ipv4}'.format(ipv4='ipv4_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_ipv4_txt_get(client):
    """Test case for ip_ipv4_txt_get

    request the current time based on the ip of the request. note: this is a \"best guess\" obtained from open-source data.
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/ip/{ipv4_tx}'.format(ipv4='ipv4_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_txt_get(client):
    """Test case for ip_txt_get

    request the current time based on the ip of the request. note: this is a \"best guess\" obtained from open-source data.
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/ip.txt',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_area_get(client):
    """Test case for timezone_area_get

    a listing of all timezones available for that area.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone/{area}'.format(area='area_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_area_location_get(client):
    """Test case for timezone_area_location_get

    request the current time for a timezone.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone/{area}/{location}'.format(area='area_example', location='location_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_area_location_region_get(client):
    """Test case for timezone_area_location_region_get

    request the current time for a timezone.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone/{area}/{location}/{region}'.format(area='area_example', location='location_example', region='region_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_area_location_region_txt_get(client):
    """Test case for timezone_area_location_region_txt_get

    request the current time for a timezone.
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone/{area}/{location}/{region_tx}'.format(area='area_example', location='location_example', region='region_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_area_location_txt_get(client):
    """Test case for timezone_area_location_txt_get

    request the current time for a timezone.
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone/{area}/{location_tx}'.format(area='area_example', location='location_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_area_txt_get(client):
    """Test case for timezone_area_txt_get

    a listing of all timezones available for that area.
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone/{area_tx}'.format(area='area_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_get(client):
    """Test case for timezone_get

    a listing of all timezones.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_txt_get(client):
    """Test case for timezone_txt_get

    a listing of all timezones.
    """
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/api/timezone.txt',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

