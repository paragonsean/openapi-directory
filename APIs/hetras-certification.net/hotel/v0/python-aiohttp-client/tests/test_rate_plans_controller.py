# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.extended_rateplan_entry import ExtendedRateplanEntry
from openapi_server.models.operation_rate_patch_request import OperationRatePatchRequest
from openapi_server.models.rate_response import RateResponse
from openapi_server.models.rateplans_list_response import RateplansListResponse
from openapi_server.models.rates_batch_update_request_item import RatesBatchUpdateRequestItem
from openapi_server.models.rates_response import RatesResponse
from openapi_server.models.total_count_response import TotalCountResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rate_plans_batch_update_rates(client):
    """Test case for rate_plans_batch_update_rates

    Update a list of base rateplans for a given period and a given base price for single occupancy.
    """
    request = {"rateplan":"rateplan","base_price":0.8008281904610115,"from":"2000-01-23T04:56:07.000+00:00","to":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/batch/$rates'.format(hotel_id=56),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_plans_get_rate(client):
    """Test case for rate_plans_get_rate

    Get the setup of a daily rate for a specific business day and rateplan.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/{rateplan_code}/rates/{business_day}'.format(hotel_id=56, rateplan_code='rateplan_code_example', business_day='2013-10-20T19:20:30+01:00'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_plans_get_rateplan(client):
    """Test case for rate_plans_get_rateplan

    Get all the details for a specific rateplan in the hotel.
    """
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/{rateplan_code}'.format(hotel_id=56, rateplan_code='rateplan_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_plans_get_rateplans(client):
    """Test case for rate_plans_get_rateplans

    Get a list of rateplans for the specified hotel id matching the filter criteria.
    """
    params = [('sellingStatus', 'selling_status_example'),
                    ('commissionable', True),
                    ('group', 'group_example'),
                    ('baseRateplan', 'base_rateplan_example'),
                    ('channelGroup', 'channel_group_example'),
                    ('channelCode', 'channel_code_example'),
                    ('marketCodes', ['market_codes_example']),
                    ('roomTypes', ['room_types_example']),
                    ('includedServices', ['included_services_example']),
                    ('skip', 56),
                    ('top', 56),
                    ('inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans'.format(hotel_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_plans_get_rateplans_count(client):
    """Test case for rate_plans_get_rateplans_count

    Get the count of all rateplans in the hotel matching the given filter criteria.
    """
    params = [('sellingStatus', 'selling_status_example'),
                    ('commissionable', True),
                    ('group', 'group_example'),
                    ('baseRateplan', 'base_rateplan_example'),
                    ('channelGroup', 'channel_group_example'),
                    ('channelCode', 'channel_code_example'),
                    ('marketCodes', ['market_codes_example']),
                    ('roomTypes', ['room_types_example']),
                    ('includedServices', ['included_services_example'])]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/$count'.format(hotel_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_plans_get_rates(client):
    """Test case for rate_plans_get_rates

    Get the setup of the daily rates for a specific rateplan and a defined timeperiod.
    """
    params = [('expand', 'expand_example'),
                    ('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00'),
                    ('skip', 56),
                    ('top', 56),
                    ('inlinecount', 'inlinecount_example')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/{rateplan_code}/rates'.format(hotel_id=56, rateplan_code='rateplan_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rate_plans_get_rates_count(client):
    """Test case for rate_plans_get_rates_count

    Get the count of all active and loaded daily rates for the defined rateplan in a specified time period.
    """
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/{rateplan_code}/rates/$count'.format(hotel_id=56, rateplan_code='rateplan_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rate_plans_patch_rate(client):
    """Test case for rate_plans_patch_rate

    Partially update a rate of the specified rateplan for a defined business day.
    """
    patch_request = [openapi_server.OperationRatePatchRequest()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/{rateplan_code}/rates/{business_day}'.format(hotel_id=56, rateplan_code='rateplan_code_example', business_day='2013-10-20T19:20:30+01:00'),
        headers=headers,
        json=patch_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_rate_plans_patch_rates(client):
    """Test case for rate_plans_patch_rates

    Partially update a rate of the specified rateplan for the defined time period.
    """
    patch_request = [openapi_server.OperationRatePatchRequest()]
    params = [('from', '2013-10-20T19:20:30+01:00'),
                    ('to', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'app_id': 'app_id_example',
        'app_key': 'app_key_example',
    }
    response = await client.request(
        method='PATCH',
        path='/api/hotel/v0/hotels/{hotel_id}/rateplans/{rateplan_code}/rates'.format(hotel_id=56, rateplan_code='rateplan_code_example'),
        headers=headers,
        json=patch_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

