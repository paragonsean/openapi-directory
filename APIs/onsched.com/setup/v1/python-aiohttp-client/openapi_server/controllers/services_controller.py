from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_input_model import AvailabilityInputModel
from openapi_server.models.resource_block_view_model import ResourceBlockViewModel
from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.service_allocation_input_model import ServiceAllocationInputModel
from openapi_server.models.service_allocation_list_view_model import ServiceAllocationListViewModel
from openapi_server.models.service_allocation_update_model import ServiceAllocationUpdateModel
from openapi_server.models.service_allocation_view_model import ServiceAllocationViewModel
from openapi_server.models.service_allocations_input_model import ServiceAllocationsInputModel
from openapi_server.models.service_availability_view_model import ServiceAvailabilityViewModel
from openapi_server.models.service_block_input_model import ServiceBlockInputModel
from openapi_server.models.service_block_list_view_model import ServiceBlockListViewModel
from openapi_server.models.service_block_update_model import ServiceBlockUpdateModel
from openapi_server.models.service_block_view_model import ServiceBlockViewModel
from openapi_server.models.service_calendar_input_model import ServiceCalendarInputModel
from openapi_server.models.service_calendar_view_model import ServiceCalendarViewModel
from openapi_server.models.service_image_input_model import ServiceImageInputModel
from openapi_server.models.service_input_model import ServiceInputModel
from openapi_server.models.service_list_view_model import ServiceListViewModel
from openapi_server.models.service_update_model import ServiceUpdateModel
from openapi_server.models.service_view_model import ServiceViewModel
from openapi_server import util


async def setup_v1_services_allocations_id_delete(request: web.Request, id) -> web.Response:
    """Delete Allocation

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a service allocation. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of serviceAllocation object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_allocations_id_get(request: web.Request, id) -> web.Response:
    """Get Allocation

    &lt;p&gt;Use this endpoint to &lt;b&gt;Get a Service Allocation&lt;/b&gt;. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of serviceAllocation object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_allocations_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Allocation

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a service allocation. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST /setup/v1/services/{id}/allocations&lt;/i&gt; endpoint for fields names and details.&lt;/p&gt;

    :param id: id of serviceAllocation object
    :type id: str
    :param body: Service allocation update model
    :type body: dict | bytes

    """
    body = ServiceAllocationUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_block_id_delete(request: web.Request, id) -> web.Response:
    """Delete Block

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Service Block. A valid &lt;b&gt;serviceBlock id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of serviceBlock object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_block_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Service Block. A valid &lt;b&gt;serviceBlock id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of serviceBlock object
    :type id: str
    :param body: Service Block update model
    :type body: dict | bytes

    """
    body = ServiceBlockUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_blocks_id_get(request: web.Request, id) -> web.Response:
    """Get Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Get a Service Block&lt;/b&gt;. A valid &lt;b&gt;serviceBlock id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of serviceBlock object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_calendar_id_delete(request: web.Request, id) -> web.Response:
    """Delete Service Links

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; service links from the calendar specified. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of calender to delete service links from
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_calendar_post(request: web.Request, body=None) -> web.Response:
    """Link Service to Calendar

    &lt;p&gt;Use this endpoint to &lt;b&gt;Link a Service&lt;/b&gt; to a calendar. &lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = ServiceCalendarInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_get(request: web.Request, location_id=None, service_group_id=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Services

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param service_group_id: Filter services by groupId
    :type service_group_id: int
    :param deleted: Filter by deleted status
    :type deleted: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_services_id_allocations_bulk_post(request: web.Request, id, body=None) -> web.Response:
    """Create Allocations Bulk

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; bulk service allocations. A valid &lt;b&gt;service id&lt;/b&gt; is required. Use this endpoint only if you need to POST multiple service allocations in one transaction. For details refer to: &lt;a href&#x3D;\&quot;POST ​/setup​/v1​/services​/{id}​/allocations\&quot;&gt;Post Service Allocation&lt;/a&gt;&lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ServiceAllocationsInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_id_allocations_get(request: web.Request, id, location_id=None, resource_id=None, start_date=None, end_date=None, offset=None, limit=None) -> web.Response:
    """List Service Allocations

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service Allocations&lt;/b&gt; for a specified service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Service allocations are used for &lt;b&gt;Event type services only&lt;/b&gt; where the events are offered on specific dates and times. Retrieve all allocations for a location by passing in 0 as the service id.&lt;/p&gt;  &lt;p&gt;The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of  service to list allocations for, 0 for all
    :type id: str
    :param location_id: The id of the location. Defaults to the primary location
    :type location_id: str
    :param resource_id: The id of the resource to filter on
    :type resource_id: str
    :param start_date: Format YYYY-MM-DD. Filter appointments by on/after startDate
    :type start_date: str
    :param end_date: Format YYYY-MM-DD. Filter appointments on/before endDate
    :type end_date: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def setup_v1_services_id_allocations_post(request: web.Request, id, body=None) -> web.Response:
    """Create Allocation

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a service allocation for a service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Service allocations are used for &lt;b&gt;Event type services only&lt;/b&gt;. Service allocations allow you to specify the time(s) a service is available as opposed to using weekly availability which represents a weekly schedule, ie: Mon-Fri 9am-5pm.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;. Service allocations can be set to specific time ranges or for the whole day by setting startTime&#x3D;0 and endTime&#x3D;2400. Service allocations can repeat for a specific date range instance or set to repeat at a specified frequency.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the allocation repeats. For example, an interval of 2 for a weekly allocation means that the allocation will repeat every 2nd week beginning at the day specified. A daily allocation with an interval of 10 means the allocation will repeat every 10 days. The interval property applies to all repeat frequencies.  &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY ALLOCATIONS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY ALLOCATIONS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;. You must specify the &lt;b&gt;“weekdays”&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;.  For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the allocation date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY ALLOCATIONS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly. &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want allocated.  If monthDay&#x3D;’15’ this means to allocate the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on.  For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits:  day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ServiceAllocationInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_id_availability_get(request: web.Request, id) -> web.Response:
    """Get Weekly Availability

    &lt;p&gt;Use this endpoint to return the &lt;b&gt;Weekly Service Availability&lt;/b&gt; for an appointment service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Weekly availability is returned for services where the Type &#x3D; 1. For event type services, where service Type &#x3D; 2, refer to the &lt;i&gt;GET ​/setup​/v1​/services​/{id}​/allocations&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of service object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_id_availability_put(request: web.Request, id, body=None) -> web.Response:
    """Update Weekly Availability

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; service weekly availability. A valid &lt;b&gt;service id&lt;/b&gt; is required. The availability day entries are created when a service object is created.&lt;/p&gt;  &lt;p&gt;To update weekly availability hours, all days of the week must be provided. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri&lt;/b&gt; and &lt;b&gt;sat&lt;/b&gt;. The &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; fields are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. We support 24-hour availability, set startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0.&lt;/p&gt;  &lt;p&gt;If you require times in between specified hours to be unavailable, use the resource blocks endpoints. Times entered represent the timezone of the business location.&lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param body: Service Availability Input Model
    :type body: dict | bytes

    """
    body = AvailabilityInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_id_block_post(request: web.Request, id, body=None) -> web.Response:
    """Create Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Service Block. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;Service blocks can be set to specific time ranges or for the whole day. To block a whole day set startTime to 0 and endTime to 2400.&lt;/p&gt;  &lt;p&gt;Service blocks can be for a specific date range instance or set to repeat at a specified frequency. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the block repeats. For example, an interval of 2 for a weekly block means that the block will repeat every 2nd week beginning at the day specified. A daily block with an interval of 10 means the block will repeat every 10 days. The interval property applies to all repeat frequencies. &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY BLOCKS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY BLOCKS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;.  You must specify the &lt;b&gt;weekdays&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;. For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the block date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY BLOCKS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly, &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want blocked.  If monthDay&#x3D;’15’ this means to block the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on. For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits: day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ServiceBlockInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_id_blocks_get(request: web.Request, id, start_date=None, end_date=None, offset=None, limit=None) -> web.Response:
    """List Service Blocks

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Blocks&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of service to list blocks for
    :type id: str
    :param start_date: Format YYYY-MM-DD. Filter blocks on/after startDate
    :type start_date: str
    :param end_date: Format YYYY-MM-DD. Filter on/before endDate
    :type end_date: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def setup_v1_services_id_calendar_get(request: web.Request, id, location_id=None) -> web.Response:
    """Get Linked Calendar

    &lt;p&gt;Use this endpoint to &lt;b&gt;Get the Linked Calendar&lt;/b&gt; for the service requested. A valid &lt;b&gt;service id&lt;/b&gt; is required. A service can only be linked to one calendar in a location.&lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param location_id: id of business location, defaults to primary business location
    :type location_id: str

    """
    return web.Response(status=200)


async def setup_v1_services_id_delete(request: web.Request, id) -> web.Response:
    """Delete Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a service object. A valid &lt;b&gt;service id&lt;/b&gt; is required. The service is not permanently deleted and can be recovered by using the &lt;i&gt;PUT /setup​/v1​/services​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of service object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_id_deleteimage_delete(request: web.Request, id) -> web.Response:
    """Delete Service Image

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a previously uploaded service image. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of service object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_id_get(request: web.Request, id) -> web.Response:
    """Get Service

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Service&lt;/b&gt; object. A valid &lt;b&gt;service id&lt;/b&gt; is required. Find service id&#39;s by using the &lt;i&gt;GET /setup/v1/services&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of service object
    :type id: int

    """
    return web.Response(status=200)


async def setup_v1_services_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a service object. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ServiceUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_id_recover_put(request: web.Request, id) -> web.Response:
    """Recover Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted service object. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_services_id_resources_get(request: web.Request, id, offset=None, limit=None, google_auth_return_url=None, outlook_auth_return_url=None) -> web.Response:
    """List Resources for Service

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resources&lt;/b&gt; that provide the requested service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int
    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str

    """
    return web.Response(status=200)


async def setup_v1_services_id_uploadimage_post(request: web.Request, id, body=None) -> web.Response:
    """Upload Service Image

    &lt;p&gt;Use this endpoint to &lt;b&gt;Upload&lt;/b&gt; an image to the service. A valid &lt;b&gt;service id&lt;/b&gt; is required. You must convert the image to a &lt;b&gt;base64 encoded string&lt;/b&gt; and pass that string as input along with your &lt;b&gt;filename&lt;/b&gt;.&lt;/p&gt;

    :param id: id of service object
    :type id: str
    :param body: Input model for image upload
    :type body: dict | bytes

    """
    body = ServiceImageInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_services_post(request: web.Request, body=None) -> web.Response:
    """Create Service

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new service. If not specified, the business location defaults to the primary business location. Note: Posting a service to the Primary Business Location will scope as company scoped and make the service available to all locations. If you want a service to only be available from a specific location, include the business location id.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;Name&lt;/b&gt; and &lt;b&gt;Duration&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;The service &lt;b&gt;Type&lt;/b&gt; is either, &lt;b&gt;1 &#x3D; Appointment&lt;/b&gt; or &lt;b&gt;2 &#x3D; Event&lt;/b&gt;. Default is 1 if not specified.&lt;/p&gt;  &lt;p&gt;For type &#x3D; 1, Appointments - Create an availability entry for each weekday to provide the service for. &lt;b&gt;All days of the week must be provided when adding service availability.&lt;/b&gt; Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri&lt;/b&gt; and &lt;b&gt;sat&lt;/b&gt;. Start and End Times are entered in military format. e.g., 800 is 8:00am, 2230 is 10:30pm. If not provided, it defaults to the primary location business hours.&lt;/p&gt;  &lt;p&gt;We support 24-hour availability, set startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0. If you require times in between specified hours to be unavailable, use the service block endpoint at: &lt;i&gt;POST ​/setup​/v1​/services​/{id}​/block&lt;/i&gt;.&lt;/p&gt;  &lt;p&gt;For type &#x3D; 2, Events - Create service allocations for their availability. Refer to the: &lt;i&gt;POST /setup​/v1​/services​/{id}​/allocations&lt;/i&gt; to set up service allocations for the event.&lt;/p&gt;  &lt;p&gt;Options are available for customer selected durations, for details: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/services-overview#variable-duration\&quot;&gt;Variable Duration Overview&lt;/a&gt;&lt;/p&gt;  &lt;p&gt;Additional parameters include but are not limited to bookingLimit, maxCapacity and maxGroupSize. For details: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/service-max-capacity\&quot;&gt;Service Limits Overview&lt;/a&gt;&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = ServiceInputModel.from_dict(body)
    return web.Response(status=200)
