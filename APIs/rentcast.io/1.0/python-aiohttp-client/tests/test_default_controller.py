# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.market_statistics200_response import MarketStatistics200Response
from openapi_server.models.property_records200_response_inner import PropertyRecords200ResponseInner
from openapi_server.models.property_records_random200_response_inner import PropertyRecordsRandom200ResponseInner
from openapi_server.models.rent_estimate_long_term200_response import RentEstimateLongTerm200Response
from openapi_server.models.rental_listing_long_term_by_id200_response import RentalListingLongTermById200Response
from openapi_server.models.rental_listings_long_term200_response_inner import RentalListingsLongTerm200ResponseInner
from openapi_server.models.sale_listing_by_id200_response import SaleListingById200Response
from openapi_server.models.sale_listings200_response_inner import SaleListings200ResponseInner
from openapi_server.models.value_estimate200_response import ValueEstimate200Response


pytestmark = pytest.mark.asyncio

async def test_market_statistics(client):
    """Test case for market_statistics

    Market Statistics
    """
    params = [('zipCode', '29611'),
                    ('historyRange', 6)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/markets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_record_by_id(client):
    """Test case for property_record_by_id

    Property Record by Id
    """
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/properties/{id}'.format(id='5500-Grand-Lake-Dr,-San-Antonio,-TX-78244'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_records(client):
    """Test case for property_records

    Property Records
    """
    params = [('address', '5500 Grand Lake Dr, San Antonio, TX, 78244'),
                    ('city', 'city_example'),
                    ('state', 'state_example'),
                    ('zipCode', 'zip_code_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 3.4),
                    ('propertyType', 'property_type_example'),
                    ('bedrooms', 3.4),
                    ('bathrooms', 3.4),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_property_records_random(client):
    """Test case for property_records_random

    Random Property Records
    """
    params = [('limit', 5)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/properties/random',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rent_estimate_long_term(client):
    """Test case for rent_estimate_long_term

    Rent Estimate
    """
    params = [('address', '5500 Grand Lake Drive, San Antonio, TX, 78244'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('propertyType', Single Family),
                    ('bedrooms', 4),
                    ('bathrooms', 2),
                    ('squareFootage', 1600),
                    ('maxRadius', 3.4),
                    ('daysOld', 3.4),
                    ('compCount', 5)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avm/rent/long-term',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rental_listing_long_term_by_id(client):
    """Test case for rental_listing_long_term_by_id

    Rental Listing by Id
    """
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/listings/rental/long-term/{id}'.format(id='1702-Cherry-Orchard-Dr,-Austin,-TX-78745'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rental_listings_long_term(client):
    """Test case for rental_listings_long_term

    Rental Listings
    """
    params = [('address', 'address_example'),
                    ('city', 'Austin'),
                    ('state', 'TX'),
                    ('zipCode', 'zip_code_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 3.4),
                    ('propertyType', 'property_type_example'),
                    ('bedrooms', 3.4),
                    ('bathrooms', 3.4),
                    ('status', Active),
                    ('daysOld', 3.4),
                    ('limit', 5),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/listings/rental/long-term',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sale_listing_by_id(client):
    """Test case for sale_listing_by_id

    Sale Listing by Id
    """
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/listings/sale/{id}'.format(id='1702-Cherry-Orchard-Dr,-Austin,-TX-78745'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sale_listings(client):
    """Test case for sale_listings

    Sale Listings
    """
    params = [('address', 'address_example'),
                    ('city', 'Austin'),
                    ('state', 'TX'),
                    ('zipCode', 'zip_code_example'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('radius', 3.4),
                    ('propertyType', 'property_type_example'),
                    ('bedrooms', 3.4),
                    ('bathrooms', 3.4),
                    ('status', Active),
                    ('daysOld', 3.4),
                    ('limit', 5),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/listings/sale',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_value_estimate(client):
    """Test case for value_estimate

    Value Estimate
    """
    params = [('address', '5500 Grand Lake Drive, San Antonio, TX, 78244'),
                    ('latitude', 3.4),
                    ('longitude', 3.4),
                    ('propertyType', Single Family),
                    ('bedrooms', 4),
                    ('bathrooms', 2),
                    ('squareFootage', 1600),
                    ('maxRadius', 3.4),
                    ('daysOld', 3.4),
                    ('compCount', 5)]
    headers = { 
        'Accept': 'application/json',
        'sec0': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/avm/value',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

