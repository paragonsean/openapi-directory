from typing import List, Dict
from aiohttp import web

from openapi_server.models.diary_allocation_model import DiaryAllocationModel
from openapi_server.models.diary_allocation_model_results import DiaryAllocationModelResults
from openapi_server.models.diary_appointment_model import DiaryAppointmentModel
from openapi_server.models.diary_appointment_model_results import DiaryAppointmentModelResults
from openapi_server.models.diary_appointment_type_model import DiaryAppointmentTypeModel
from openapi_server.models.diary_appointment_type_model_results import DiaryAppointmentTypeModelResults
from openapi_server import util


async def v2_tier2_short_name_diary_allocations_diary_allocation_idget(request: web.Request, short_name, diary_allocation_id) -> web.Response:
    """Get a specific diary allocation given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param diary_allocation_id: The unique ID of the DiaryAllocation
    :type diary_allocation_id: str

    """
    return web.Response(status=200)


async def v2_tier2_short_name_diary_allocations_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all diary allocations

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier2_short_name_diary_appointments_diary_appointment_idget(request: web.Request, short_name, diary_appointment_id) -> web.Response:
    """Get a specific diary appointment given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param diary_appointment_id: The unique ID of the DiaryAppointment
    :type diary_appointment_id: str

    """
    return web.Response(status=200)


async def v2_tier2_short_name_diary_appointments_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all diary appointments

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier2_short_name_diary_appointmenttypes_diary_appointment_type_idget(request: web.Request, short_name, diary_appointment_type_id) -> web.Response:
    """Get a specific diary appointment type given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param diary_appointment_type_id: The unique ID of the DiaryAppointmentType
    :type diary_appointment_type_id: str

    """
    return web.Response(status=200)


async def v2_tier2_short_name_diary_appointmenttypes_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all diary appointment types

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)
