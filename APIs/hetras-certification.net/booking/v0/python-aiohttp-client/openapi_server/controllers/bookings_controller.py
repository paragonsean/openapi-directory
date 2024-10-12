from typing import List, Dict
from aiohttp import web

from openapi_server.models.assign_room_criteria import AssignRoomCriteria
from openapi_server.models.assign_room_response import AssignRoomResponse
from openapi_server.models.authorization_request import AuthorizationRequest
from openapi_server.models.base_response import BaseResponse
from openapi_server.models.booking_list_response import BookingListResponse
from openapi_server.models.cancellation_response import CancellationResponse
from openapi_server.models.check_in_details import CheckInDetails
from openapi_server.models.operation_reservation_patchable_model import OperationReservationPatchableModel
from openapi_server.models.reservation import Reservation
from openapi_server.models.reservation_confirmation import ReservationConfirmation
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server.models.reservations_response import ReservationsResponse
from openapi_server.models.terminal_authorization_request import TerminalAuthorizationRequest
from openapi_server.models.total_count_response import TotalCountResponse
from openapi_server import util


async def bookings_cancel_reservation(request: web.Request, app_id, app_key, confirmation_id, reservation_number, send_confirmation=None) -> web.Response:
    """Cancel one reservation.

    This request will cancel one specific reservation. It will show up in the hetras UI in the Cancellation and NoShow              processing screen and it will be up to the hotel staff to either charge or waive the cancellation fee.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation to cancel.
    :type reservation_number: int
    :param send_confirmation: Whether to send a confirmation email to the primary guest
    :type send_confirmation: bool

    """
    return web.Response(status=200)


async def bookings_check_in(request: web.Request, app_id, app_key, confirmation_id, reservation_number, check_in_details) -> web.Response:
    """Performs a check in operation for a reservation.

    With this call you can set a reservation to the status inhouse. It allows only single room reservations to be checked in.              The reservation must have assigned a vacant and clean room.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation to be checked in.
    :type reservation_number: int
    :param check_in_details: Specifies checkIn details, for example Client Identity.
    :type check_in_details: dict | bytes

    """
    check_in_details = CheckInDetails.from_dict(check_in_details)
    return web.Response(status=200)


async def bookings_check_out(request: web.Request, app_id, app_key, confirmation_id, reservation_number) -> web.Response:
    """Performs a check out operation for a reservation.

    With this call you can set a reservation to the checkout status. It allows only single room reservations to be checked out.              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation to be checked out.
    :type reservation_number: int

    """
    return web.Response(status=200)


async def bookings_create_booking(request: web.Request, app_id, app_key, reservation, send_confirmation=None) -> web.Response:
    """Create a new booking.

    Create a new booking as defined in the requests payload. You can get more information about the payload if you check out the              documentation for the reservation request model.&lt;br /&gt;              Please also have a look at the &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/tutorials\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Tutorials&lt;/a&gt;.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param reservation: Specifies the details of the booking to be created.
    :type reservation: dict | bytes
    :param send_confirmation: Whether to send a confirmation email to the primary guest
    :type send_confirmation: bool

    """
    reservation = Reservation.from_dict(reservation)
    return web.Response(status=200)


async def bookings_get_booking(request: web.Request, app_id, app_key, confirmation_id, expand=None, exclude=None) -> web.Response:
    """Load all reservations for one booking by confirmation id.

    A booking groups all reservations done in one single request and can be identified by the confirmation id.              Guests usually use the confirmation id to check in at the kiosk, on the website or mobile device. In hetras              all reservations of one booking share the room type, rate plan and number of guests per room.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking to load.
    :type confirmation_id: str
    :param expand: Specifies the expand type.
    :type expand: str
    :param exclude: Specifies the exclude type.
    :type exclude: str

    """
    return web.Response(status=200)


async def bookings_get_bookings(request: web.Request, app_id, app_key, hotel_id=None, cancellation_id=None, reservation_number=None, customer_name=None, customer_email=None, customer_id=None, room_number=None, external_id=None, company_name=None, company_id=None, company_email=None, block_code=None, reservation_statuses=None, market_codes=None, channel_codes=None, sub_channel_codes=None, room_types=None, rate_plan_codes=None, labels=None, _from=None, to=None, date_filter=None, exclude=None, skip=None, top=None, inlinecount=None) -> web.Response:
    """Find bookings matching the given filter criteria.

    Here you can easily find bookings matching various criteria. The booking you are looking for has to fullfill all the specified criteria              at the same time. So if you specify a customer name and a channel code you will get all bookings where the firstname or lastname of a guest or a               contact contains the specified value and that have been done through the defined channel.              A booking can consist of multiple reservations, so even if you are looking for a specific reservation which is part of a multi-room booking you will get              all reservations for this booking returned.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Only return bookings for this specific hotel.
    :type hotel_id: int
    :param cancellation_id: Return bookings for this cancellation id.
    :type cancellation_id: str
    :param reservation_number: Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels.
    :type reservation_number: int
    :param customer_name: Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type customer_name: str
    :param customer_email: Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type customer_email: str
    :param customer_id: Return all bookings the id of one of the guests or the contact matches the specified value.
    :type customer_id: str
    :param room_number: Return all bookings having the specified room number assigned.
    :type room_number: str
    :param external_id: Return all bookings exactly matching the specified external id. This filter is case sensitive.
    :type external_id: str
    :param company_name: Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type company_name: str
    :param company_id: Return all bookings the id of the company or travel agent profile matches the specified value.
    :type company_id: str
    :param company_email: Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type company_email: str
    :param block_code: Return all bookings where the block code matches the specified value.
    :type block_code: str
    :param reservation_statuses: Return all bookings where the reservation status is one of the specified values.
    :type reservation_statuses: List[str]
    :param market_codes: Return all bookings where the market code is one of the specified values.
    :type market_codes: List[str]
    :param channel_codes: Return all bookings where the channel code is one of the specified values.
    :type channel_codes: List[str]
    :param sub_channel_codes: Return all bookings where the subchannel code is one of the specified values.
    :type sub_channel_codes: List[str]
    :param room_types: Return all bookings where the room type is one of the specified values.
    :type room_types: List[str]
    :param rate_plan_codes: Return all bookings where the rate plan code is one of the specified values.
    :type rate_plan_codes: List[str]
    :param labels: Return all reservations with at least one of the specified labels.
    :type labels: List[str]
    :param _from: Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later.
    :type _from: str
    :param to: End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier.
    :type to: str
    :param date_filter: Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range.
    :type date_filter: str
    :param exclude: To be able to request reservations without personal data based on GDPR.
    :type exclude: str
    :param skip: Amount of items to skip.
    :type skip: int
    :param top: Amount of items to select.
    :type top: int
    :param inlinecount: Return total number of items for a given filter criteria.
    :type inlinecount: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def bookings_get_bookings_count(request: web.Request, app_id, app_key, hotel_id=None, cancellation_id=None, reservation_number=None, customer_name=None, customer_email=None, customer_id=None, room_number=None, external_id=None, company_name=None, company_id=None, company_email=None, block_code=None, reservation_statuses=None, market_codes=None, channel_codes=None, sub_channel_codes=None, room_types=None, rate_plan_codes=None, labels=None, _from=None, to=None, date_filter=None, exclude=None) -> web.Response:
    """Get total count of bookings matchung the given filter criteria.

    Get the count of all bookings matching your criteria. The bookings have to fullfill all the specified criteria              at the same time. So if you specify a customer name and a channel code you will get the count for all bookings where the firstname or lastname               of a guest or a contact contains the specified value and that have been done through the defined channel.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: Only return bookings for this specific hotel.
    :type hotel_id: int
    :param cancellation_id: Return bookings for this cancellation id.
    :type cancellation_id: str
    :param reservation_number: Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels.
    :type reservation_number: int
    :param customer_name: Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type customer_name: str
    :param customer_email: Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type customer_email: str
    :param customer_id: Return all bookings the id of one of the guests or the contact matches the specified value.
    :type customer_id: str
    :param room_number: Return all bookings having the specified room number assigned.
    :type room_number: str
    :param external_id: Return all bookings exactly matching the specified external id. This filter is case sensitive.
    :type external_id: str
    :param company_name: Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type company_name: str
    :param company_id: Return all bookings the id of the company or travel agent profile matches the specified value.
    :type company_id: str
    :param company_email: Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces.
    :type company_email: str
    :param block_code: Return all bookings where the block code matches the specified value.
    :type block_code: str
    :param reservation_statuses: Return all bookings where the reservation status is one of the specified values.
    :type reservation_statuses: List[str]
    :param market_codes: Return all bookings where the market code is one of the specified values.
    :type market_codes: List[str]
    :param channel_codes: Return all bookings where the channel code is one of the specified values.
    :type channel_codes: List[str]
    :param sub_channel_codes: Return all bookings where the subchannel code is one of the specified values.
    :type sub_channel_codes: List[str]
    :param room_types: Return all bookings where the room type is one of the specified values.
    :type room_types: List[str]
    :param rate_plan_codes: Return all bookings where the rate plan code is one of the specified values.
    :type rate_plan_codes: List[str]
    :param labels: Return all reservations with at least one of the specified labels.
    :type labels: List[str]
    :param _from: Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later.
    :type _from: str
    :param to: End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier.
    :type to: str
    :param date_filter: Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range.
    :type date_filter: str
    :param exclude: To be able to request reservations without personal data based on GDPR.
    :type exclude: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def bookings_get_reservation(request: web.Request, app_id, app_key, confirmation_id, reservation_number, expand=None, exclude=None) -> web.Response:
    """Load a specific reservation from a booking.

    With this request you can load one specific reservation done with one booking request.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation to load.
    :type reservation_number: int
    :param expand: Specifies the expand type.
    :type expand: str
    :param exclude: Specifies the exclude type.
    :type exclude: str

    """
    return web.Response(status=200)


async def bookings_patch(request: web.Request, app_id, app_key, confirmation_id, reservation_number, patch_request) -> web.Response:
    """Partially updates a reservation.

    The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call allows to update the following fields:              external_id, market_code, channel_code, subchannel_code, guarantee_type, comment, addon_services, labels, guests, contact and company.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/addon_services\&quot;, \&quot;value\&quot;: [\&quot;BREAKFAST\&quot;, \&quot;PARKING\&quot;]                },                {                  \&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/labels/-\&quot;, \&quot;value\&quot;: \&quot;MOBILE\&quot;                },                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/guests/SHOW-1234\&quot;, \&quot;value\&quot;: { \&quot;customer_id\&quot;: \&quot;SHOW-1234\&quot;, \&quot;primary\&quot;: false }                },                {                  \&quot;op\&quot;: \&quot;add\&quot;, \&quot;path\&quot;: \&quot;/guests/-\&quot;, \&quot;value\&quot;: { \&quot;customer_id\&quot;: \&quot;SHOW-5678\&quot;, \&quot;primary\&quot;: true }                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation that has to be updated.
    :type reservation_number: int
    :param patch_request: A set of JSON Patch operations
    :type patch_request: list | bytes

    """
    patch_request = [OperationReservationPatchableModel.from_dict(d) for d in patch_request]
    return web.Response(status=200)


async def bookings_payment_token(request: web.Request, app_id, app_key, confirmation_id, reservation_number, authorization_request) -> web.Response:
    """Post a payment token for a reservation.

    TBD.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation to be checked in.
    :type reservation_number: int
    :param authorization_request: 
    :type authorization_request: dict | bytes

    """
    authorization_request = AuthorizationRequest.from_dict(authorization_request)
    return web.Response(status=200)


async def bookings_post_room_assignment(request: web.Request, app_id, app_key, confirmation_id, reservation_number, assigning_criteria=None) -> web.Response:
    """Assign a room to a reservation.

    By default this API call assigns a random room, which has the proper room type, is not already assigned              to another reservation or has any maintenance status set for the stay period of the underlying reservation. If the              arrival date for the underlying reservation is the current business day dirty rooms are excluded by default. For reservation              arriving on any latter day the room condition is not taken into account.&lt;br /&gt;              By specifiying the room selection criteria in the request body you can influence which room will be assigned. See the request model              for further details.&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation the room should be assigned to.
    :type reservation_number: int
    :param assigning_criteria: Specifies the criteria for the room selection.
    :type assigning_criteria: dict | bytes

    """
    assigning_criteria = AssignRoomCriteria.from_dict(assigning_criteria)
    return web.Response(status=200)


async def bookings_terminal_authorization(request: web.Request, app_id, app_key, confirmation_id, reservation_number, authorization_request) -> web.Response:
    """Performs a chip and pin credit card authorization for a reservation.

    With this call you can trigger a terminal authorization prompt for a reservation guest.               For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param confirmation_id: The confirmation id for the booking the reservation was made.
    :type confirmation_id: str
    :param reservation_number: Specifies the reservation number for the reservation to be checked in.
    :type reservation_number: int
    :param authorization_request: Specifies authorization details, such as amount and client identity.
    :type authorization_request: dict | bytes

    """
    authorization_request = TerminalAuthorizationRequest.from_dict(authorization_request)
    return web.Response(status=200)
