# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_ip_geolocation_with_confidence_area_and_hazard_report_api(client):
    """Test case for ip_geolocation_with_confidence_area_and_hazard_report_api

    IP Geolocation with Confidence Area and Hazard Report API
    """
    params = [('ip', '193.114.112.122'),
                    ('localityLanguage', 'en'),
                    ('key', '{{API KEY}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data/ip-geolocation-full',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ip_geolocation_with_confidence_area_api(client):
    """Test case for ip_geolocation_with_confidence_area_api

    IP Geolocation with Confidence Area API
    """
    params = [('ip', '193.114.112.122'),
                    ('localityLanguage', 'en'),
                    ('key', '{{API KEY}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/data/ip-geolocation-with-confidence',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

