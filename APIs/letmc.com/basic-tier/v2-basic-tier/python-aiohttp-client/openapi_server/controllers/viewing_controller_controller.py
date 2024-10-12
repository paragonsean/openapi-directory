from typing import List, Dict
from aiohttp import web

from openapi_server.models.viewing_booking_model import ViewingBookingModel
from openapi_server import util


async def viewing_controller_get_bookings(request: web.Request, short_name, preferred_date, property_ids_to_view) -> web.Response:
    """Gets a list of available viewing slots for one or more properties

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param preferred_date: The preferred date for a viewing
    :type preferred_date: str
    :param property_ids_to_view: An array of unique IDs of properties to view
    :type property_ids_to_view: List[str]

    """
    preferred_date = util.deserialize_datetime(preferred_date)
    return web.Response(status=200)


async def viewing_controller_make_booking(request: web.Request, short_name, forename, surname, mobile_phone, email_address, property_ids_to_view, selected_viewing_slot, want_room_in_shared_property=None, alert_min_rent=None, alert_max_rent=None, alert_number_of_beds=None, alert_area_id=None, alert_tenant_type=None, subscribe_to_email_alerts=None, subscribe_to_sms_alerts=None) -> web.Response:
    """Book an appointment for a viewing slot returned from the GET verb

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param forename: The forename of the prospect
    :type forename: str
    :param surname: The surname of the prospect
    :type surname: str
    :param mobile_phone: The mobile phone number of the prospect
    :type mobile_phone: str
    :param email_address: The email address of the prospect
    :type email_address: str
    :param property_ids_to_view: An array of unique IDs of properties to view
    :type property_ids_to_view: List[str]
    :param selected_viewing_slot: The prospect&#39;s selected viewing slot
    :type selected_viewing_slot: dict | bytes
    :param want_room_in_shared_property: Whether the prospect wants a shared property
    :type want_room_in_shared_property: bool
    :param alert_min_rent: The minimum rent amount the prospect is looking for
    :type alert_min_rent: float
    :param alert_max_rent: The maximum rent amount the prospect is looking for
    :type alert_max_rent: float
    :param alert_number_of_beds: The minimum number of beds the prospect is looking for
    :type alert_number_of_beds: int
    :param alert_area_id: The unique ID of the area the prospect is looking for
    :type alert_area_id: str
    :param alert_tenant_type: The tenanct type the prospect is looking for
    :type alert_tenant_type: str
    :param subscribe_to_email_alerts: Whether to subscribe the prospect to email alerts
    :type subscribe_to_email_alerts: bool
    :param subscribe_to_sms_alerts: Whether to subscribe the prospect to SMS alerts
    :type subscribe_to_sms_alerts: bool

    """
    selected_viewing_slot = ViewingBookingModel.from_dict(selected_viewing_slot)
    return web.Response(status=200)
