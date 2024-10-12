from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_day_view_model import AvailabilityDayViewModel
from openapi_server.models.availability_view_model import AvailabilityViewModel
from openapi_server.models.unavailable_time_list_view_model import UnavailableTimeListViewModel
from openapi_server import util


async def consumer_v1_availability_service_id_start_date_end_date_days_get(request: web.Request, service_id, start_date, end_date, location_id=None, resource_id=None, tz_offset=None) -> web.Response:
    """Get Available Days

    &lt;p&gt;This endpoint will return &lt;b&gt;Day Level Availability&lt;/b&gt; for the range of dates requested. For example, if the business is closed, or there is a public holiday this endpoint will return that the \&quot;Day is unavailable\&quot;.&lt;/p&gt;  &lt;p&gt;Day Availability is a high-level check for Holidays and Open/Available hours of a location, service and/or resource and should be used to restrict your choices of days available in your application to improve usability and performance.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;The locationId is optional, however if not supplied it defaults to the Primary Business Location for open/closed hours information. It is recommended you always provide the locationId.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;resourceId&lt;/b&gt; is optional. If used the available days will be return day availability for the resource specified.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;tzOffset&lt;/b&gt; parameter should be used if the appointment requester, the end user, is in a different timezone than the location or resource.&lt;/p&gt;

    :param service_id: Service Id for day availability search
    :type service_id: str
    :param start_date: Format YYYY-MM-DD: Start Date for availability search
    :type start_date: str
    :param end_date: Format YYYY-MM-DD: End Date for availability search
    :type end_date: str
    :param location_id: Id of business location, defaults to primary business location
    :type location_id: str
    :param resource_id: Resource Id to filter on
    :type resource_id: str
    :param tz_offset: Timezone offset to view availability for
    :type tz_offset: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def consumer_v1_availability_service_id_start_date_end_date_get(request: web.Request, service_id, start_date, end_date, start_time=None, end_time=None, location_id=None, resource_id=None, resource_group_id=None, resource_ids=None, round_robin=None, duration=None, interval=None, timezone_name=None, tz_offset=None, destination=None, day_availability_start_date=None, day_availability=None, first_day_available=None) -> web.Response:
    """Get Available Times

    &lt;p&gt;    &lt;b&gt;Choose your search criteria carefully. Availability is an expensive call.&lt;/b&gt; If you search availability for all resources, you should only do so for a single date. If you search availability for multiple dates, you should only do so for a specific resource by specifying the optional resourceId parameter.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;resourceId&lt;/b&gt; is optional, it is recommended if known at the time of availability call.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;timezoneName&lt;/b&gt; is optional, it allows you to specify the IANA formatted name for the end user&#39;s timezone to view availability. e.g., &lt;i&gt;America/New_York&lt;/i&gt;. &lt;b&gt;NOTE: This is the recommended approach for your implementation.&lt;/b&gt;  The \&quot;tzOffset\&quot; parameter remains for backward compatibility.  For JavaScript, use moment.js in your client for ease of timezone detection and selection. For iOS, use the name property of the NSTimeZone returned from the localTimeZone method. For .NET, consider NodaTime or TimeZoneConverter via NuGet. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;duration&lt;/b&gt; should only be populated if you allow the end user to select a duration, otherwise the service&#39;s duration will be used.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; are optional and are specified in &lt;b&gt;military time e.g., 800 &#x3D; 8:00am, 2230 &#x3D; 10:30pm&lt;/b&gt;. Note: You will only see availability within the boundary of your business location start and end times.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;dayAvailability&lt;/b&gt; will return day level availability for the number of days requested from the start date. See &lt;i&gt;GET /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/days&lt;/i&gt; for details.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;firstDayAvailable&lt;/b&gt; only works with day availability. If set to true it will look for the first day available within the range specified by the dayAvailability parameter. The two parameters together can be a clever way to display availability for a week or month. Tip - pass in the beginning of the week or month, and available times are displayed for the first available date if exists.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;tzOffset&lt;/b&gt; allows you to pass in the timezone offset for the end user&#39;s timezone of choice, e.g., (-240) for EST. If you use this option, your application should be timezone aware. The requested timezone is specified as an offset (plus or minus) from GMT time.&lt;/p&gt;  &lt;p&gt;Availability can be complex. For further troubleshooting refer to the: &lt;i&gt;&lt;b&gt;GET /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/unavailable&lt;/b&gt;&lt;/i&gt; endpoint. This endpoint will show you all unavailable times for a given date range. Available times are created from any unblocked time periods. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/availability-overview\&quot;&gt;Availability Overview&lt;/a&gt;&lt;/p&gt;

    :param service_id: Service Id for availability search
    :type service_id: str
    :param start_date: Format YYYY-MM-DD: Start Date for availability search
    :type start_date: str
    :param end_date: Format YYYY-MM-DD: End Date for availability search
    :type end_date: str
    :param start_time: Format Military Time Start Time for availability search. Defaults to Business Hours Start
    :type start_time: int
    :param end_time: Format Military Time. End Time for availability search. Defaults to Business Hours End
    :type end_time: int
    :param location_id: Id of business location, defaults to primary business location
    :type location_id: str
    :param resource_id: Resource Id for availability search
    :type resource_id: str
    :param resource_group_id: Resource Group Id for availability search
    :type resource_group_id: str
    :param resource_ids: Comma separated Resource Id&#39;s for availability search
    :type resource_ids: str
    :param round_robin: Round robin choice 0&#x3D;none, 1&#x3D;random, 2&#x3D;balanced
    :type round_robin: str
    :param duration: Duration of the service if different from default
    :type duration: int
    :param interval: Booking Interval if different than the default
    :type interval: int
    :param timezone_name: Requested IANA timezone Id to view availability
    :type timezone_name: str
    :param tz_offset: Request timezone offset to view availability
    :type tz_offset: int
    :param destination: For calculating travel based availability, requires distance scope
    :type destination: str
    :param day_availability_start_date: Format YYYY-DD-YY: Start date for day availability, defaults to startDate
    :type day_availability_start_date: str
    :param day_availability: Number of days of day availability to return
    :type day_availability: int
    :param first_day_available: Return available times for the first available day
    :type first_day_available: bool

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    day_availability_start_date = util.deserialize_datetime(day_availability_start_date)
    return web.Response(status=200)


async def consumer_v1_availability_service_id_start_date_end_date_unavailable_get(request: web.Request, service_id, start_date, end_date, location_id=None, resource_id=None, duration=None, tz_offset=None, skip_time_past_unavailability=None) -> web.Response:
    """Get Unavailable Times

    &lt;p&gt;This endpoint is used to show &lt;b&gt;Unavailable&lt;/b&gt; times and provides valuable information as to why a time slot is unavailable. If you question your availability results, populate the same parameters to this endpoint to find out why.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Location hours, holidays, services, resources, blocks, allocations, and appointments are just some of variables that may cause time slots to become unavailable. Use this endpoint to understand why you don&#39;t see availability.&lt;/p&gt;

    :param service_id: Service Id for availability search
    :type service_id: str
    :param start_date: Format YYYY-MM-DD: Start Date for unavailable time search
    :type start_date: str
    :param end_date: Format YYYY-MM-DD: End Date for unavailable time search
    :type end_date: str
    :param location_id: Id of business location, defaults to primary business location
    :type location_id: str
    :param resource_id: Resource Id to filter on
    :type resource_id: str
    :param duration: Duration of the service if different from default
    :type duration: int
    :param tz_offset: Request timezone offset to view unavailable times
    :type tz_offset: int
    :param skip_time_past_unavailability: Set as true to remove Time Past (TP) blocks in the response
    :type skip_time_past_unavailability: bool

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
