from typing import List, Dict
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
from openapi_server import util


async def booking_availability(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/availability

    Get the tour-grade with the lowest price that is available for a product on each day of the specified month  This service: - returns  - useful when displaying a calendar of available tours - For more information, see: [Availability services](#section/Key-concepts/Availability-services) - **Notes:**    - [/booking/availability/dates](#operation/bookingAvailabilityDates) provides all availability in one call and is more suitable for calendars, etc.    - Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingAvailabilityRequest.from_dict(body)
    return web.Response(status=200)


async def booking_availability_dates(request: web.Request, accept_language, product_code=None) -> web.Response:
    """/booking/availability/dates

    Get dates on which a product is available  This service: - retrieves all available dates for a product, excluding days it does not operate and blocked-out dates - returns a multi-dimensional array of year-month -&amp;gt; days that have any availabile tour grade or traveler mix - useful to present the user with a list of dates for selection on which *this* product is available for booking - **Notes**:     - The user&#39;s desired traveler mix may not be eligible for booking; these details can be displayed when you retrieve its list of tour grades   - Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param product_code: **unique alphanumeric identifier** of the product
    :type product_code: str

    """
    return web.Response(status=200)


async def booking_availability_tourgrades(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/availability/tourgrades

    Get the tour grades of a product that are currently available  This service reports: - all tour grades for the specified product, on the specified day, that are available for the specified age bands - the pricing breakdown and the total depending on the travel date and traveler mix  **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingAvailabilityTourgradesRequest.from_dict(body)
    return web.Response(status=200)


async def booking_availability_tourgrades_pricingmatrix(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/availability/tourgrades/pricingmatrix

    Get a pricing matrix that includes availability and tour-grades for a product  Given a month, this service returns days with available tour grades only (i.e., days which have at least one tourgrade available), and the pricing matrix for that tour grade for that day.  - **Note**: Availability data is limited to a period of **12 months** into the future from the present time on the production server and **6 months** on the sandbox server.  

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingAvailabilityTourgradesPricingmatrixRequest.from_dict(body)
    return web.Response(status=200)


async def booking_book(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/book

    Make a booking  For more information, see:     - [Cancellation policy](#section/Key-concepts/Cancellation-policy)   - [Booking concepts](#section/Key-concepts/Booking-concepts)   - [Booking process flow](#section/Common-workflows-and-data-validation/Booking-process-flow)   - [Making a booking](#section/Common-workflows-and-data-validation/Making-a-booking)   - [Supplier communications](#section/Key-concepts/Supplier-communications) 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingBookRequest.from_dict(body)
    return web.Response(status=200)


async def booking_calculateprice(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/calculateprice

    Confirm the price of a tour / activity prior to booking  For more information, see: [Calculating prices](#section/Common-workflows-and-data-validation/Calculating-prices)    - **Note**: Availability and pricing data is limited to a period of **six months** into the future from the present time 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingCalculatepriceRequest.from_dict(body)
    return web.Response(status=200)


async def booking_hotels(request: web.Request, accept_language, product_code=None, dest_id=None) -> web.Response:
    """/booking/hotels

    Get hotel pick-ups Lists the hotel pickups available for either a product or a destination 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param product_code: **unique alphanumeric identifier** of the product
    :type product_code: str
    :param dest_id: **unique numeric identifier** of the destination
    :type dest_id: int

    """
    return web.Response(status=200)


async def booking_mybookings(request: web.Request, accept_language, voucher_key=None, email=None, itinerary_or_item_id=None) -> web.Response:
    """/booking/mybookings

    Get a user&#39;s bookings with travel dates in the future.   This service can also be used to check the status of a booking.   **Provide either:**  - A &#x60;voucherKey&#x60;, **or...**  - An email address (&#x60;email&#x60;) and a booking reference (&#x60;itineraryOrItemId&#x60;) ([Booking Reference](#section/Key-concepts/Booking-references)) 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param voucher_key: **voucher key** for the booking
    :type voucher_key: str
    :param email: **email address** of the booker for the booking
    :type email: str
    :param itinerary_or_item_id: The booking reference number of the item - **Note**: For more information, see [Booking references](#section/Key-concepts/Booking-references) 
    :type itinerary_or_item_id: str

    """
    return web.Response(status=200)


async def booking_pastbooking(request: web.Request, accept_language, voucher_key=None, email=None, item_id=None) -> web.Response:
    """/booking/pastbooking

    Get the details of a single specific past booking based on the &#x60;voucherKey&#x60; or &#x60;itemId&#x60; and email address sent in the request.  **Note**: this service will only return past bookings that were made with the same API key that was used to make the booking  **Sample query parameters**: - email&#x3D;apitest@viator.com&amp;amp;itemId&#x3D;580669678  **or** - voucherKey&#x3D;1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678  **email** - The email address passed must match the email address associated with the booking  **Departure details**  - Departure details such as the &#x60;departurePoint&#x60;, &#x60;departurePointAddress&#x60; and &#x60;departurePointDirections&#x60; is included in the response.  - These fields may contain HTML escape characters such as &amp;amp;amp; and special characters that are escaped by a backslash. Ensure that these fields are parsed after receiving the response as it will cause your JSON to be invalid.  For more information, see: [Reviewing bookings](#section/Common-workflows-and-data-validation/Reviewing-bookings) 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param voucher_key: **specifier** of past booking type (use *one* of: &#x60;itemId&#x60; (booking reference) *and* &#x60;&#39;voucherKey&#39;&#x60; *or* &#x60;&#39;email&#39;&#x60;)
    :type voucher_key: str
    :param email: **email address** by which to search for past bookings
    :type email: str
    :param item_id: Search for a booking with this **unique booking-reference number**. See [Booking references](#section/Key-concepts/Booking-references) for more information. 
    :type item_id: str

    """
    return web.Response(status=200)


async def booking_pricingmatrix(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/pricingmatrix

    Get the pricing matrix for tour-grades, product age bands and pax mixes  For more information, see: [Get the tour-grade pricing matrix](#section/Common-workflows-and-data-validation/Get-the-tour-grade-pricing-matrix) 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingPricingmatrixRequest.from_dict(body)
    return web.Response(status=200)


async def booking_status(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/status

    Get the booking status for multiple items based on different criteria  This service:  - is ideally be used in software for bulk updates of pending bookings - returns a maximum of 1000 bookings (narrow your search if you expect a greater number of results) - will return &amp;lt;u&amp;gt;both&amp;lt;/u&amp;gt; live &amp;lt;u&amp;gt;and&amp;lt;/u&amp;gt; test bookings - rate limited to &amp;lt;u&amp;gt;one request every 30 minutes&amp;lt;/u&amp;gt; - For more information, see: [Get the bookiing status for multiple items](#section/Common-workflows-and-data-validation/Get-the-booking-status-for-multiple-items)  **Exceeding the rate limit** - You will receive the following error message if you exceed the rate limit allowed for this service. Set &#x60;test&#x60; to &#x60;true&#x60; to bypass this limit: &#x60;&#x60;&#x60;javascript {     \&quot;data\&quot;: null     \&quot;vmid\&quot;: 221002     \&quot;errorMessage\&quot;: [\&quot;Access allowed every 30 minutes\&quot;]     \&quot;errorType\&quot;: \&quot;EXCEPTION\&quot;     \&quot;dateStamp\&quot;: \&quot;2013-03-26T10:28:51+0000\&quot;     \&quot;errorReference\&quot;: 55315512721712161381352771     \&quot;errorMessageText\&quot;: [\&quot;Access allowed every 30 minutes\&quot;]     \&quot;success\&quot;: false     \&quot;totalCount\&quot;: 1     \&quot;errorName\&quot;: \&quot;PollingDeniedException\&quot;   } &#x60;&#x60;&#x60; 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingStatusRequest.from_dict(body)
    return web.Response(status=200)


async def booking_status_items(request: web.Request, accept_language, body=None) -> web.Response:
    """/booking/status/items

    Get brief booking statuses  This service is similar to [/booking/status](#operation/bookingStatus) in that it: - retrieves the booking status for multiple items based on different criteria - has the same request parameters as [/booking/status](#operation/bookingStatus)  However, it differs in that it returns a multi-item array of booking items with less detail than what would be received from [/booking/status](#operation/bookingStatus). 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = BookingStatusItemsRequest.from_dict(body)
    return web.Response(status=200)


async def booking_voucher(request: web.Request, accept_language, lead_last_name=None, item_id=None, embedded_resources=None, voucher_key=None, full_html=None, mobile_voucher=None) -> web.Response:
    """/booking/voucher

    Get voucher details - Use this service to retrieve the voucher details of a booked item. - The data returned is HTML-formatted and can be wrapped in a header and/or footer.  **Sample query parameters** - leadLastName&#x3D;Simpson test&amp;amp;itemId&#x3D;580669678  **or**  - voucherKey&#x3D;1005851866:4af44c13ecf3f1a7d3f9ef2fc00c2257e08fa42ae20f877f3039ff9b52aba24e:580669678&amp;amp;fullHTML&#x3D;true&amp;amp;mobileVoucher&#x3D;true 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param lead_last_name: **surname** of *this* lead traveler
    :type lead_last_name: str
    :param item_id: Booking-reference number generated by Viator    - **Note**: For more information, see: [Booking references](#section/Key-concepts/Booking-references) 
    :type item_id: int
    :param embedded_resources: ignore (Viator only)
    :type embedded_resources: bool
    :param voucher_key: **identifier** for the voucher - **note**: use &amp;lt;u&amp;gt;either&amp;lt;/u&amp;gt; &#x60;voucherKey&#x60; &amp;lt;u&amp;gt;or&amp;lt;/u&amp;gt; the three separate parameters - if &#x60;voucherKey&#x60; is provided as well as the other parameters, then &#x60;voucherKey&#x60; overrides the other paramaters - &#x60;voucherKey&#x60; is obtained from [/booking/mybookings](#operation/bookingMybookings) or in the response from [/booking/book](#operation/bookingBook) when you make a booking 
    :type voucher_key: str
    :param full_html: **specifier**: - set to &#x60;true&#x60; if you wish to retrieve the full HTML-formatted voucher - set to &#x60;false&#x60; if you want the div fragment (optional) 
    :type full_html: bool
    :param mobile_voucher: **specifier**:  - if set to &#x60;true&#x60;, the service returns the mobile (cut down) HTML-formatted voucher - if &#x60;false&#x60; the full voucher HTML is returned (ignoring &#x60;fullHTML&#x60;) - default: &#x60;true&#x60;  - this field should only be enabled for products that have a &#x60;voucherOption&#x60; of &#x60;&#39;VOUCHER_E&#39;&#x60; - do not enable &#x60;mobileVouchers&#x60; for paper vouchers (&#x60;voucherOption&#x60; of &#x60;&#39;VOUCHER_PAPER_ONLY&#39;&#x60;) as no barcode is returned - the voucher information is available in the response from [/product](#operation/product), [/booking/book](#operation/bookingBook), [/booking/pastbooking](#operation/bookingPastbooking), [/booking/mybookings](#operation/bookingMybookings) (it is also displayed under the &#39;Redemption Info&#39; heading in this service) 
    :type mobile_voucher: bool

    """
    return web.Response(status=200)


async def cancel_booking(request: web.Request, booking_reference, accept_language, body=None) -> web.Response:
    """/bookings/{booking-reference}/cancel

    Submits a cancellation request for the specified booking  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/bookings/{booking-reference}/cancel&#x60; 

    :param booking_reference: The ID of the booking
    :type booking_reference: str
    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = CancellationRequest.from_dict(body)
    return web.Response(status=200)


async def cancel_booking_quote(request: web.Request, booking_reference) -> web.Response:
    """/bookings/{booking-reference}/cancel-quote

    Retrieves a quote for the cancellation of a booking  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/bookings/{booking-reference}/cancel-quote&#x60; 

    :param booking_reference: Unique numeric identifier of the booking for which to retrieve a cancellation quote
    :type booking_reference: str

    """
    return web.Response(status=200)


async def cancellation_reasons(request: web.Request, accept_language) -> web.Response:
    """/bookings/cancel-reasons

    Retrieves a dictionary of unique identification codes (&#x60;cancellationReasonCode&#x60;) and their associated natural-language descriptions (&#x60;cancellationReasonText&#x60;).  For information on how to use this service, see: [Cancellation API workflow](#section/Common-workflows-and-data-validation/Cancellation-API-workflow)  **Note**:     * This service &amp;lt;u&amp;gt;requires&amp;lt;/u&amp;gt; [exp-api-key](#section/Authentication/exp-api-key) to be included as a header parameter. Please speak to your account manager if you have not yet been issued an exp-api-key.   * The base URL for the server for this endpoint is different from the older endpoints described in this document. Use &#x60;https://api.sandbox.viator.com/partner/cancel-reasons&#x60; 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str

    """
    return web.Response(status=200)
