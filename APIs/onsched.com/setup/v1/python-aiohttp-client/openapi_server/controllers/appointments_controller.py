from typing import List, Dict
from aiohttp import web

from openapi_server.models.appointment_list_view_model import AppointmentListViewModel
from openapi_server.models.appointment_view_model import AppointmentViewModel
from openapi_server import util


async def setup_v1_appointments_get(request: web.Request, location_id=None, email=None, lastname=None, service_id=None, calendar_id=None, resource_id=None, customer_id=None, service_allocation_id=None, start_date=None, end_date=None, status=None, booked_by=None, offset=None, limit=None) -> web.Response:
    """List Appointments

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Appointments&lt;/b&gt;. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param email: Filter appointments by email address
    :type email: str
    :param lastname: Filter appointments by lastname or part of
    :type lastname: str
    :param service_id: Filter appointments by service
    :type service_id: str
    :param calendar_id: Filter appointments by calendar
    :type calendar_id: str
    :param resource_id: Filter appointments by resource
    :type resource_id: str
    :param customer_id: Filter appointments by customer
    :type customer_id: str
    :param service_allocation_id: Filter appointments by service allocation
    :type service_allocation_id: str
    :param start_date: Format YYYY-MM-DD: Filter appointments by on/after startDate
    :type start_date: str
    :param end_date: Format YYYY-MM-DD: Filter appointments on/before endDate
    :type end_date: str
    :param status: Filter appointments by status: IN, BK, CN, RE, RS
    :type status: str
    :param booked_by: Filter appointments by user email who booked
    :type booked_by: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def setup_v1_appointments_id_get(request: web.Request, id) -> web.Response:
    """Get Appointment

    &lt;p&gt;Use this endpoint to return an &lt;b&gt;Appointment&lt;/b&gt; object. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. Find appointment id&#39;s by using the &lt;i&gt;GET​/setup​/v1​/appointments&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of appointment object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_appointments_id_reassign_resource_resource_id_put(request: web.Request, id, resource_id) -> web.Response:
    """Reassign Appointment

    &lt;p&gt;Use this endpoint to &lt;b&gt;Reassign&lt;/b&gt; an appointment from one resource to another. The result returned is a single appointment that was reassigned to the target resource. A valid &lt;b&gt;appointment id&lt;/b&gt; and &lt;b&gt;resource id&lt;/b&gt; is required. Find appointment id&#39;s by using the &lt;i&gt;GET /setup/v1/appointments&lt;/i&gt; endpoint, find resource id&#39;s by using the &lt;i&gt;GET ​/setup​/v1​/resources&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of appointment object
    :type id: str
    :param resource_id: id of target resource
    :type resource_id: str

    """
    return web.Response(status=200)
