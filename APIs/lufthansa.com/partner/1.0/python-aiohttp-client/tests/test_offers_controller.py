# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_all_fares(client):
    """Test case for all_fares

    All Fares
    """
    params = [('catalogues', 'catalogues_example'),
                    ('origin', 'origin_example'),
                    ('destination', 'destination_example'),
                    ('travel-date', 'travel_date_example'),
                    ('return-date', 'return_date_example'),
                    ('cabin-class', 'economy'),
                    ('travelers', 'travelers_example'),
                    ('fare-family', 'smart'),
                    ('trackingid', 'trackingid_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/allfares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_best_fares(client):
    """Test case for best_fares

    Best Fares
    """
    params = [('catalogues', 'catalogues_example'),
                    ('origin', 'origin_example'),
                    ('destination', 'destination_example'),
                    ('travel-date', 'travel_date_example'),
                    ('trip-duration', 'trip_duration_example'),
                    ('range', 'range_example'),
                    ('cabin-class', 'cabin_class_example'),
                    ('country', 'country_example'),
                    ('trackingid', 'trackingid_example'),
                    ('fare-family', 'fare_family_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/bestfares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deep_links(client):
    """Test case for deep_links

    Deep Links
    """
    params = [('catalogues', 'catalogues_example'),
                    ('trackingid', 'trackingid_example'),
                    ('country', 'country_example'),
                    ('lang', 'lang_example'),
                    ('origin', 'origin_example'),
                    ('origin-name', 'origin_name_example'),
                    ('destination', 'destination_example'),
                    ('destination-name', 'destination_name_example'),
                    ('travel-date', 'travel_date_example'),
                    ('return-date', 'return_date_example'),
                    ('cabin-class', 'cabin_class_example'),
                    ('outbound-segments', 'outbound_segments_example'),
                    ('return-segments', 'return_segments_example'),
                    ('travelers', 'travelers_example'),
                    ('fare', 'fare_example'),
                    ('net-fare', 'net_fare_example'),
                    ('fare-currency', 'fare_currency_example'),
                    ('partnerid', 'partnerid_example'),
                    ('encryption-key', 'encryption_key_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/deeplink',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fares(client):
    """Test case for fares

    Fares
    """
    params = [('catalogues', 'catalogues_example'),
                    ('segments', 'segments_example'),
                    ('carriers', 'carriers_example'),
                    ('travelers', 'travelers_example'),
                    ('fare-types', 'basic')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/fares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fares_subscriptions(client):
    """Test case for fares_subscriptions

    Fares Subscriptions
    """
    params = [('origin', 'origin_example'),
                    ('destination', 'destination_example'),
                    ('cabin-class', 'cabin_class_example'),
                    ('trip-duration', 'trip_duration_example'),
                    ('email', 'email_example'),
                    ('lang', 'lang_example'),
                    ('country', 'country_example'),
                    ('trackingid', 'trackingid_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_l_h_deep_links_ffp(client):
    """Test case for l_h_deep_links_ffp

    LH Deep Links - FFP
    """
    params = [('catalogues', 'catalogues_example'),
                    ('origin', 'origin_example'),
                    ('destination', 'destination_example'),
                    ('travel-date', 'travel_date_example'),
                    ('trackingid', 'trackingid_example'),
                    ('country', 'country_example'),
                    ('lang', 'lang_example'),
                    ('return-date', 'return_date_example'),
                    ('cabin-class', 'cabin_class_example'),
                    ('travelers', 'travelers_example'),
                    ('partnerid', 'partnerid_example'),
                    ('encryption-key', 'encryption_key_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/deeplink/ffp',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_l_h_deep_links_itco(client):
    """Test case for l_h_deep_links_itco

    LH Deep Links - ITCO
    """
    params = [('catalogues', 'catalogues_example'),
                    ('origin', 'origin_example'),
                    ('destination', 'destination_example'),
                    ('travel-date', 'travel_date_example'),
                    ('outbound-segments', 'outbound_segments_example'),
                    ('fare', 'fare_example'),
                    ('fare-currency', 'fare_currency_example'),
                    ('trackingid', 'trackingid_example'),
                    ('country', 'country_example'),
                    ('lang', 'lang_example'),
                    ('return-date', 'return_date_example'),
                    ('cabin-class', 'cabin_class_example'),
                    ('return-segments', 'return_segments_example'),
                    ('travelers', 'travelers_example'),
                    ('net-fare', 'net_fare_example'),
                    ('partnerid', 'partnerid_example'),
                    ('encryption-key', 'encryption_key_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/deeplink/itco',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lowest_fares(client):
    """Test case for lowest_fares

    Lowest Fares
    """
    params = [('catalogues', 'catalogues_example'),
                    ('origin', 'origin_example'),
                    ('destination', 'destination_example'),
                    ('travel-date', 'travel_date_example'),
                    ('return-date', 'return_date_example'),
                    ('cabin-class', 'cabin_class_example'),
                    ('travelers', 'travelers_example'),
                    ('fare-family', 'basic'),
                    ('country', 'country_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/fares/lowestfares',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_o_nd_route(client):
    """Test case for o_nd_route

    OND Route
    """
    params = [('catalogues', 'LH'),
                    ('limit', 'limit_example'),
                    ('offset', 'offset_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/ond/route/{origin}/{destination}'.format(origin='origin_example', destination='destination_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_o_nd_status(client):
    """Test case for o_nd_status

    OND Status
    """
    params = [('catalogues', 'LH'),
                    ('new-routes', 'new_routes_example'),
                    ('old-routes', 'old_routes_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/ond/status',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top_ond(client):
    """Test case for top_ond

    Top OND
    """
    params = [('catalogues', 'LH'),
                    ('origin', 'origin_example')]
    headers = { 
        'Accept': 'application/json',
        'accept': 'accept_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offers/ond/top',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

