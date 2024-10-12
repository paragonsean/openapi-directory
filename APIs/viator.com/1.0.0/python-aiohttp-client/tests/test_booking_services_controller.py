# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.booking_availability200_response import BookingAvailability200Response
from openapi_server.models.booking_availability_dates200_response import BookingAvailabilityDates200Response
from openapi_server.models.booking_availability_request import BookingAvailabilityRequest
from openapi_server.models.booking_availability_tourgrades200_response import BookingAvailabilityTourgrades200Response
from openapi_server.models.booking_availability_tourgrades_pricingmatrix200_response import BookingAvailabilityTourgradesPricingmatrix200Response
from openapi_server.models.booking_availability_tourgrades_pricingmatrix_request import BookingAvailabilityTourgradesPricingmatrixRequest
from openapi_server.models.booking_availability_tourgrades_request import BookingAvailabilityTourgradesRequest
from openapi_server.models.booking_book200_response import BookingBook200Response
from openapi_server.models.booking_book_request import BookingBookRequest
from openapi_server.models.booking_calculateprice200_response import BookingCalculateprice200Response
from openapi_server.models.booking_calculateprice_request import BookingCalculatepriceRequest
from openapi_server.models.booking_hotels200_response import BookingHotels200Response
from openapi_server.models.booking_mybookings200_response import BookingMybookings200Response
from openapi_server.models.booking_pastbooking200_response import BookingPastbooking200Response
from openapi_server.models.booking_pricingmatrix200_response import BookingPricingmatrix200Response
from openapi_server.models.booking_pricingmatrix_request import BookingPricingmatrixRequest
from openapi_server.models.booking_status200_response import BookingStatus200Response
from openapi_server.models.booking_status_items200_response import BookingStatusItems200Response
from openapi_server.models.booking_status_items_request import BookingStatusItemsRequest
from openapi_server.models.booking_status_request import BookingStatusRequest
from openapi_server.models.booking_voucher200_response import BookingVoucher200Response
from openapi_server.models.cancel_booking400_response import CancelBooking400Response
from openapi_server.models.cancel_booking404_response import CancelBooking404Response
from openapi_server.models.cancel_booking_quote_response import CancelBookingQuoteResponse
from openapi_server.models.cancel_booking_response import CancelBookingResponse
from openapi_server.models.cancellation_reasons_response import CancellationReasonsResponse
from openapi_server.models.cancellation_request import CancellationRequest
from openapi_server.models.model401_unauthorized import Model401UNAUTHORIZED
from openapi_server.models.model406_notacceptable import Model406NOTACCEPTABLE
from openapi_server.models.model500_internalservererror import Model500INTERNALSERVERERROR
from openapi_server.models.model503_serviceunavailable import Model503SERVICEUNAVAILABLE


pytestmark = pytest.mark.asyncio

async def test_booking_availability(client):
    """Test case for booking_availability

    /booking/availability
    """
    body = {"ageBands":[{"bandId":1,"count":1}],"currencyCode":"AUD","month":"12","productCode":"5010SYDNEY","year":"2020"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/availability',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_availability_dates(client):
    """Test case for booking_availability_dates

    /booking/availability/dates
    """
    params = [('productCode', '2280AAHT')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/booking/availability/dates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_availability_tourgrades(client):
    """Test case for booking_availability_tourgrades

    /booking/availability/tourgrades
    """
    body = {"ageBands":[{"bandId":1,"count":1}],"bookingDate":"2020-12-28","currencyCode":"AUD","productCode":"5010SYDNEY"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/availability/tourgrades',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_availability_tourgrades_pricingmatrix(client):
    """Test case for booking_availability_tourgrades_pricingmatrix

    /booking/availability/tourgrades/pricingmatrix
    """
    body = {"currenctCode":"USD","month":"12","productCode":"2280AAHT","year":"2020"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/availability/tourgrades/pricingmatrix',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_book(client):
    """Test case for booking_book

    /booking/book
    """
    body = {"booker":{"email":"apitest@viator.com","firstname":"Homer Test","surname":"Simpson Test","title":"Mr"},"currencyCode":"USD","demo":true,"items":[{"bookingQuestionAnswers":[{"answer":"0123456789, 9876543210","questionId":5},{"answer":"Australia, Fiji","questionId":4},{"answer":"01 July 2022, 31 May 2022","questionId":3}],"hotelId":{"$ref":"#/components/examples/product-example-1/value/data/pas"},"languageOptionCode":"en/SERVICE_GUIDE","partnerItemDetail":{"distributorItemRef":"distroItemRef8348234535_1"},"pickupPoint":{"$ref":"#/components/examples/product-example-1/value/data/pas"},"productCode":"100022P1","specialRequirements":"","tourGradeCode":"TG1","travelDate":"2020-12-30","travellers":[{"bandId":1,"firstname":"Homer1","leadTraveller":true,"surname":"Simpson Test","title":"Mr"},{"bandId":1,"firstname":"Homer2","leadTraveller":true,"surname":"Simpson Test","title":"Mr"}]}],"partnerDetail":{"distributorRef":"distroRef34398534535"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/book',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_calculateprice(client):
    """Test case for booking_calculateprice

    /booking/calculateprice
    """
    body = {"currencyCode":"USD","items":[{"productCode":"5010SYDNEY","tourGradeCode":"24HOUR","travelDate":"2020-12-12","travellers":[{"bandId":1}]}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/calculateprice',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_hotels(client):
    """Test case for booking_hotels

    /booking/hotels
    """
    params = [('productCode', '2280AAHT'),
                    ('destId', 123)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/booking/hotels',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_mybookings(client):
    """Test case for booking_mybookings

    /booking/mybookings
    """
    params = [('voucherKey', '3299307:93c7f36a56b18ba1068787ba7fb7988da5c8ad08db77604110141ff21498603e:600033670'),
                    ('email', 'apitest@viator.com'),
                    ('itineraryOrItemId', '700179574')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/booking/mybookings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_pastbooking(client):
    """Test case for booking_pastbooking

    /booking/pastbooking
    """
    params = [('voucherKey', '1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678'),
                    ('email', 'apitest@viator.com'),
                    ('itemId', '580669678')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/booking/pastbooking',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_pricingmatrix(client):
    """Test case for booking_pricingmatrix

    /booking/pricingmatrix
    """
    body = {"bookingDate":"2020-12-12","currencyCode":"EUR","productCode":"5010SYDNEY","tourGradeCode":"24HOUR"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/pricingmatrix',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_status(client):
    """Test case for booking_status

    /booking/status
    """
    body = {"bookingDateFrom":"2020-12-21","bookingDateTo":"2020-12-31","distributorItemRefs":["itemRef1000000"],"itemIds":[580669678],"leadFirstName":"Homer test","leadSurname":"Simpson test","test":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/status',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_status_items(client):
    """Test case for booking_status_items

    /booking/status/items
    """
    body = {"bookingDateFrom":"2020-12-21","bookingDateTo":"2020-12-31","distributorItemRefs":["itemRef1000000"],"itemIds":[580669678],"leadFirstName":"Homer test","leadSurname":"Simpson test","test":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/booking/status/items',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_booking_voucher(client):
    """Test case for booking_voucher

    /booking/voucher
    """
    params = [('leadLastName', 'Simpson'),
                    ('itemId', 600033670),
                    ('embeddedResources', false),
                    ('voucherKey', '3299307:93c7f36a56b18ba1068787ba7fb7988da5c8ad08db77604110141ff21498603e:600033670'),
                    ('fullHTML', true),
                    ('mobileVoucher', true)]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/booking/voucher',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_booking(client):
    """Test case for cancel_booking

    /bookings/{booking-reference}/cancel
    """
    body = {"reasonCode":"Customer_Service.I_canceled_my_entire_trip"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/service/bookings/{booking_reference}/cancel'.format(booking_reference='booking_reference_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_booking_quote(client):
    """Test case for cancel_booking_quote

    /bookings/{booking-reference}/cancel-quote
    """
    headers = { 
        'Accept': 'application/json',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/bookings/{booking_reference}/cancel-quote'.format(booking_reference='booking_reference_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancellation_reasons(client):
    """Test case for cancellation_reasons

    /bookings/cancel-reasons
    """
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'en-US',
        'Legacy-API-key': 'special-key',
        'API-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/service/bookings/cancel-reasons',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

