# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.number_config import NumberConfig
from openapi_server.models.number_config_page import NumberConfigPage
from openapi_server.models.number_lease import NumberLease
from openapi_server.models.number_lease_page import NumberLeasePage
from openapi_server.models.number_list import NumberList
from openapi_server.models.region_page import RegionPage


pytestmark = pytest.mark.asyncio

async def test_find_number_lease_configs(client):
    """Test case for find_number_lease_configs

    Find lease configs
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('prefix', 'prefix_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('zipcode', 'zipcode_example'),
                    ('labelName', 'label_name_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/leases/configs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_number_leases(client):
    """Test case for find_number_leases

    Find leases
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('prefix', 'prefix_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('zipcode', 'zipcode_example'),
                    ('labelName', 'label_name_example'),
                    ('tollFree', True),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/leases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_number_regions(client):
    """Test case for find_number_regions

    Find number regions
    """
    params = [('limit', 100),
                    ('offset', 0),
                    ('prefix', 'prefix_example'),
                    ('city', 'city_example'),
                    ('cityPrefix', 'city_prefix_example'),
                    ('state', 'state_example'),
                    ('zipcode', 'zipcode_example'),
                    ('country', 'country_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/regions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_numbers_local(client):
    """Test case for find_numbers_local

    Find local numbers
    """
    params = [('limit', 100),
                    ('prefix', 'prefix_example'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('zipcode', 'zipcode_example'),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/local',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_numbers_tollfree(client):
    """Test case for find_numbers_tollfree

    Find tollfree numbers
    """
    params = [('pattern', 'pattern_example'),
                    ('limit', 100),
                    ('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/tollfree',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_lease(client):
    """Test case for get_number_lease

    Find a specific lease
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/leases/{number}'.format(number='number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_lease_config(client):
    """Test case for get_number_lease_config

    Find a specific lease config
    """
    params = [('fields', 'fields_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/numbers/leases/configs/{number}'.format(number='number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_number_lease(client):
    """Test case for update_number_lease

    Update a lease
    """
    body = {"leaseBegin":5,"type":"PLAN","callFeatureStatus":"UNSUPPORTED","labels":["labels","labels"],"number":"number","textFeatureStatus":"UNSUPPORTED","autoRenew":True,"sendEmailOnCreate":True,"leaseEnd":5,"nationalFormat":"nationalFormat","region":{"zipcode":"zipcode","country":"country","city":"city","prefix":"prefix","latitude":2.302136,"timeZone":"timeZone","state":"state","longitude":7.0614014},"tollFree":True,"status":"PENDING"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/numbers/leases/{number}'.format(number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_number_lease_config(client):
    """Test case for update_number_lease_config

    Update a lease config
    """
    body = {"number":"number","callTrackingConfig":{"voicemailSoundId":2,"failedTransferSoundId":5,"googleAnalytics":{"googleAccountId":"googleAccountId","domain":"domain","category":"category"},"voicemail":True,"weeklySchedule":{"stopTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6},"timeZone":"timeZone","daysOfWeek":["daysOfWeek","daysOfWeek"],"startTimeOfDay":{"hour":5,"nano":9,"minute":9,"second":6}},"transferNumbers":["transferNumbers","transferNumbers"],"introSoundId":5,"screen":True,"recorded":True,"whisperSoundId":7},"ivrInboundConfig":{"dialplanXml":"dialplanXml"},"configType":"IVR","textInboundConfig":{"forwardNumber":"forwardNumber","forwardEnabled":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/v2/numbers/leases/configs/{number}'.format(number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

