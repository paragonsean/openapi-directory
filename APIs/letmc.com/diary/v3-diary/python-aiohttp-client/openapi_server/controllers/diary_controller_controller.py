from typing import List, Dict
from aiohttp import web

from openapi_server.models.diary_appointment_details import DiaryAppointmentDetails
from openapi_server.models.diary_appointment_model import DiaryAppointmentModel
from openapi_server.models.diary_appointment_model_results import DiaryAppointmentModelResults
from openapi_server.models.diary_appointment_type_model_results import DiaryAppointmentTypeModelResults
from openapi_server.models.diary_booking_model import DiaryBookingModel
from openapi_server.models.feedback_submission_model import FeedbackSubmissionModel
from openapi_server.models.guest_diary_parameters_results_model import GuestDiaryParametersResultsModel
from openapi_server import util


async def diary_controller_add_feedback(request: web.Request, short_name, body) -> web.Response:
    """Submit appointment feedback

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param body: Feedback submission model
    :type body: dict | bytes

    """
    body = FeedbackSubmissionModel.from_dict(body)
    return web.Response(status=200)


async def diary_controller_cancel_appointment(request: web.Request, short_name, appointment_id) -> web.Response:
    """Cancel an existing appointment using its unique identifier

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param appointment_id: The unique appointment id
    :type appointment_id: str

    """
    return web.Response(status=200)


async def diary_controller_delete_appointment(request: web.Request, short_name, appointment_id) -> web.Response:
    """Delete an existing appointment using its unique identifier

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param appointment_id: The unique appointment id
    :type appointment_id: str

    """
    return web.Response(status=200)


async def diary_controller_get_allocations(request: web.Request, short_name, preferred_date, appointment_type, lettings=None, property_identifier=None, branch_id=None) -> web.Response:
    """Get a list of all available allocations for a date + 7 days for a specified appointment type

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param preferred_date: The date to search from
    :type preferred_date: str
    :param appointment_type: The unique appointment type identifier
    :type appointment_type: str
    :param lettings: Sales or Lettings property?
    :type lettings: bool
    :param property_identifier: The unique property identifier (Sales or Lettings) determines branch and property type
    :type property_identifier: str
    :param branch_id: Branch ID to check appointments (required if no property submitted)
    :type branch_id: str

    """
    preferred_date = util.deserialize_datetime(preferred_date)
    return web.Response(status=200)


async def diary_controller_get_appointment(request: web.Request, short_name, appointment_id) -> web.Response:
    """Get an appointment by ID

    

    :param short_name: Company short name
    :type short_name: str
    :param appointment_id: Appointment ID
    :type appointment_id: str

    """
    return web.Response(status=200)


async def diary_controller_get_appointment_types(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all diary appointment types

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def diary_controller_get_appointments_between_dates(request: web.Request, short_name, branch_id, start_date, end_date, appointment_types_to_search, offset, count) -> web.Response:
    """A collection of diary appointments linked to a company filtered between specific dates and by appointment type

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param start_date: The search from date
    :type start_date: str
    :param end_date: The search to date
    :type end_date: str
    :param appointment_types_to_search: The appointment IDs to search for
    :type appointment_types_to_search: List[str]
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def diary_controller_get_recurring_appointments(request: web.Request, short_name, branch_id, appointment_types_to_search, offset, count) -> web.Response:
    """Retrieves all recurring appointments:-

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str
    :param appointment_types_to_search: The appointment IDs to search for
    :type appointment_types_to_search: List[str]
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def diary_controller_post_appointment(request: web.Request, short_name, property_identifier, body, lettings=None) -> web.Response:
    """Post an appointment into a valid diary allocation

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param property_identifier: The unique property identifier (Sales or Lettings)
    :type property_identifier: List[str]
    :param body: The appointment details model
    :type body: dict | bytes
    :param lettings: Sales or Lettings property?
    :type lettings: bool

    """
    body = DiaryAppointmentDetails.from_dict(body)
    return web.Response(status=200)


async def diary_controller_put_appointment(request: web.Request, short_name, appointment_id, body, lettings=None, allow_marketing_correspondence=None) -> web.Response:
    """Update an existing appointment using its unique identifier

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param appointment_id: The unique appointment id
    :type appointment_id: str
    :param body: The appointment details model
    :type body: dict | bytes
    :param lettings: Sales or Lettings property?
    :type lettings: bool
    :param allow_marketing_correspondence: Sales or Lettings property?
    :type allow_marketing_correspondence: bool

    """
    body = DiaryAppointmentDetails.from_dict(body)
    return web.Response(status=200)


async def diary_controller_search_guest(request: web.Request, shortname, branch_id, forename, emailaddress, surname, offset, count) -> web.Response:
    """Match Guest Parameters with existing applicants

    

    :param shortname: 
    :type shortname: str
    :param branch_id: 
    :type branch_id: str
    :param forename: 
    :type forename: str
    :param emailaddress: 
    :type emailaddress: str
    :param surname: 
    :type surname: str
    :param offset: 
    :type offset: int
    :param count: 
    :type count: int

    """
    return web.Response(status=200)
