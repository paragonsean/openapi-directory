from typing import List, Dict
from aiohttp import web

from openapi_server.models.appointment_view_model import AppointmentViewModel
from openapi_server.models.availability_input_model import AvailabilityInputModel
from openapi_server.models.calendar_auth_view_model import CalendarAuthViewModel
from openapi_server.models.resource_allocation_input_model import ResourceAllocationInputModel
from openapi_server.models.resource_allocation_list_view_model import ResourceAllocationListViewModel
from openapi_server.models.resource_allocation_update_model import ResourceAllocationUpdateModel
from openapi_server.models.resource_allocation_view_model import ResourceAllocationViewModel
from openapi_server.models.resource_availability_view_model import ResourceAvailabilityViewModel
from openapi_server.models.resource_block_input_model import ResourceBlockInputModel
from openapi_server.models.resource_block_list_view_model import ResourceBlockListViewModel
from openapi_server.models.resource_block_update_model import ResourceBlockUpdateModel
from openapi_server.models.resource_block_view_model import ResourceBlockViewModel
from openapi_server.models.resource_image_input_model import ResourceImageInputModel
from openapi_server.models.resource_input_model import ResourceInputModel
from openapi_server.models.resource_list_view_model import ResourceListViewModel
from openapi_server.models.resource_update_model import ResourceUpdateModel
from openapi_server.models.resource_view_model import ResourceViewModel
from openapi_server.models.resources_input_model import ResourcesInputModel
from openapi_server.models.resources_update_model import ResourcesUpdateModel
from openapi_server.models.system_timezone_view_model import SystemTimezoneViewModel
from openapi_server import util


async def setup_v1_resources_allocations_id_delete(request: web.Request, id) -> web.Response:
    """Delete Allocation

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Resource Allocation. A valid &lt;b&gt;resourceAllocation id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resourceAllocation object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_allocations_id_get(request: web.Request, id) -> web.Response:
    """Get Allocation

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Allocation&lt;/b&gt;. A valid &lt;b&gt;resourceAllocation id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of resourceAllocation object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_allocations_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Allocation

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resource allocation. A valid &lt;b&gt;resourceAllocation id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST /setup/v1/resources/{id}/allocations&lt;/i&gt; endpoint for details.&lt;/p&gt;

    :param id: id of resourceAllocation object
    :type id: str
    :param body: Resource allocation update model
    :type body: dict | bytes

    """
    body = ResourceAllocationUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_block_id_delete(request: web.Request, id) -> web.Response:
    """Delete Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resourceBlock id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resourceBlock object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_block_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resourceBlock id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/block&lt;/i&gt; endpoint for fieldnames and details.&lt;/p&gt;

    :param id: id of resourceBlock object
    :type id: str
    :param body: Resource Block update model
    :type body: dict | bytes

    """
    body = ResourceBlockUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_blocks_id_get(request: web.Request, id) -> web.Response:
    """Get Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Get&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resourceBlock id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resourceBlock object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_bulk_post(request: web.Request, google_auth_return_url=None, outlook_auth_return_url=None, body=None) -> web.Response:
    """Create Resources Bulk

    &lt;p&gt;Use this endpoint to &lt;b&gt;Bulk Create&lt;/b&gt; resources. Valid &lt;b&gt;resource ids&lt;/b&gt; are required. The posted list of resources cannot exceed 100 resource objects per transaction for performance purposes.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str
    :param body: Resources input model
    :type body: dict | bytes

    """
    body = ResourcesInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_bulk_put(request: web.Request, google_auth_return_url=None, outlook_auth_return_url=None, body=None) -> web.Response:
    """Update Resources Bulk

    &lt;p&gt;Use this endpoint to &lt;b&gt;Bulk Update&lt;/b&gt; resources. Valid &lt;b&gt;resource id&#39;s&lt;/b&gt; are required. The list of resources cannot exceed 100 resource objects per transaction for performance purposes.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str
    :param body: Resources update model
    :type body: dict | bytes

    """
    body = ResourcesUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_get(request: web.Request, location_id=None, resource_group_id=None, email=None, name=None, deleted=None, google_auth_return_url=None, outlook_auth_return_url=None, offset=None, limit=None) -> web.Response:
    """List Resources

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Resources&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param resource_group_id: Filter by group Id
    :type resource_group_id: str
    :param email: Filter by email address
    :type email: str
    :param name: Search by name
    :type name: str
    :param deleted: Show by deleted status, default is false
    :type deleted: bool
    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max is 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_resources_id_allocations_get(request: web.Request, id, start_date=None, end_date=None, offset=None, limit=None) -> web.Response:
    """List Resource Allocations

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Allocations&lt;/b&gt; for a specified resource. We recommend using allocations if a resource&#39;s schedule changes frequently from day to day or week to week. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of resource to list allocations for
    :type id: str
    :param start_date: yyyy-mm-dd, filter allocations on/after startDate
    :type start_date: str
    :param end_date: yyyy-mm-dd, filter on/before endDate
    :type end_date: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def setup_v1_resources_id_allocations_post(request: web.Request, id, body=None) -> web.Response:
    """Create Allocation

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a resource allocation for a resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;. Resource allocations can be set to specific time ranges or for the whole day by setting startTime&#x3D;0 and endTime&#x3D;2400. They can repeat for a specific date range instance or set to repeat at a specified frequency.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M &lt;/b&gt;for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the allocation repeats. For example, an interval of 2 for a weekly allocation means that the allocation will repeat every 2nd week beginning at the day specified. A daily allocation with an interval of 10 means the allocation will repeat every 10 days. The interval property applies to all repeat frequencies.  &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY ALLOCATIONS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY ALLOCATIONS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;. You must specify the &lt;b&gt;“weekdays”&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;.  For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the allocation date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY ALLOCATIONS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly. &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want allocated.  If monthDay&#x3D;’15’ this means to allocate the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on.  For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits:  day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResourceAllocationInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_id_availability_get(request: web.Request, id) -> web.Response:
    """List Weekly Availability

    &lt;p&gt;Use this endpoint to view the &lt;b&gt;Weekly Availability&lt;/b&gt; for a resource. The displayed available times are represented in the resource&#39;s timezone. The resource timezone can be set to any world timezone. If not provided, by default it is set to the Business timezone.&lt;/p&gt;

    :param id: id of resource object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_availability_put(request: web.Request, id, body=None) -> web.Response:
    """Update Weekly Availability

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; resource weekly availability. A valid &lt;b&gt;resource id&lt;/b&gt; is required. The availability day entries are created when a resource object is created.&lt;/p&gt;  &lt;p&gt;To update weekly availability hours, all days of the week must be provided. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri&lt;/b&gt; and &lt;b&gt;sat&lt;/b&gt;. The &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; fields are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. We support 24-hour availability, set startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0.&lt;/p&gt;  &lt;p&gt;If you require times in between specified hours to be unavailable, use the resource blocks endpoints. Times entered represent the timezone of the resource. Resources can be set to any world timezone. &lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param body: Resource Availability Input Model
    :type body: dict | bytes

    """
    body = AvailabilityInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_id_block_post(request: web.Request, id, body=None) -> web.Response:
    """Create Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Resource Block. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;Resource blocks can be set to specific time ranges or for the whole day. Use the &lt;b&gt;AllDay&lt;/b&gt; setting to create an all-day block. &lt;b&gt;AllDay&lt;/b&gt; will automatically set startTime to 0 and endTime to 2400.&lt;/p&gt;  &lt;p&gt;Resource blocks can be for a specific date range instance or set to repeat at a specified frequency. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the block repeats. For example, an interval of 2 for a weekly block means that the block will repeat every 2nd week beginning at the day specified. A daily block with an interval of 10 means the block will repeat every 10 days. The interval property applies to all repeat frequencies. &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY BLOCKS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY BLOCKS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;.  You must specify the &lt;b&gt;weekdays&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;. For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the block date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY BLOCKS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly, &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want blocked.  If monthDay&#x3D;’15’ this means to block the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on. For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits: day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResourceBlockInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_id_blocks_get(request: web.Request, id, start_date=None, end_date=None, offset=None, limit=None) -> web.Response:
    """List Resource Blocks

    &lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Blocks&lt;/b&gt;. A valid &lt;b&gt;resource id&lt;/b&gt; is required. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

    :param id: id of resource to list blocks for
    :type id: str
    :param start_date: YYYY-MM-DD, filter blocks on/after startDate
    :type start_date: str
    :param end_date: YYYY-MM-DD, filter on/before endDate
    :type end_date: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def setup_v1_resources_id_calendar_auth_google_google_email_address_get(request: web.Request, id, google_email_address, google_auth_return_url=None) -> web.Response:
    """Get Resource Google URL

    &lt;p&gt;Use this endpoint to return the &lt;b&gt;Resources Google Calendar Authorization URL&lt;/b&gt;. A valid &lt;b&gt;resource id&lt;/b&gt; and &lt;b&gt;Google Email Address&lt;/b&gt; are required.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param google_email_address: Email address of Google Calendar
    :type google_email_address: str
    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_calendar_auth_outlook_outlook_email_address_get(request: web.Request, id, outlook_email_address, outlook_auth_return_url=None) -> web.Response:
    """Get Resource Outlook URL

    &lt;p&gt;Use this endpoint to return the &lt;b&gt;Resources Outlook Calendar Authorization URL&lt;/b&gt;. A valid &lt;b&gt;resource id&lt;/b&gt; and &lt;b&gt;Outlook Email Address&lt;/b&gt; are required.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param outlook_email_address: Email address of Outlook Calendar
    :type outlook_email_address: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_delete(request: web.Request, id) -> web.Response:
    """Delete Resource

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a resource. The resource is not permanently deleted and can be recovered. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resource object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_deleteimage_delete(request: web.Request, id) -> web.Response:
    """Delete Resource Image

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a previously uploaded resource image. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resource object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_get(request: web.Request, id, google_auth_return_url=None, outlook_auth_return_url=None) -> web.Response:
    """Get Resource

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource&lt;/b&gt; object. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Find resource id&#39;s by using the: &lt;i&gt;GET /setup/v1/resources&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_put(request: web.Request, id, google_auth_return_url=None, outlook_auth_return_url=None, body=None) -> web.Response:
    """Update Resource

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str
    :param body: Resource Update Model
    :type body: dict | bytes

    """
    body = ResourceUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_id_reassign_appointments_resource_id_put(request: web.Request, id, resource_id, start_date=None, end_date=None, calendar_id=None) -> web.Response:
    """Reassign Resource

    &lt;p&gt;Use this endpoint to &lt;b&gt;Reassign&lt;/b&gt; appointments from one resource to another. If the startDate is not supplied, the default is today&#39;s date + 1 day; If the endDate is not supplied, all future appointments from the start date will be reassigned. If the calendar id is not supplied the default is the primary calendar of the location.&lt;/p&gt;

    :param id: id of the original resource
    :type id: str
    :param resource_id: id of the target resource
    :type resource_id: str
    :param start_date: YYYY-MM-DD, Appt range start date
    :type start_date: str
    :param end_date: YYYY-MM-DD, Appt range end date
    :type end_date: str
    :param calendar_id: CalendarId of calendar containing appointments
    :type calendar_id: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def setup_v1_resources_id_recover_put(request: web.Request, id, google_auth_return_url=None, outlook_auth_return_url=None) -> web.Response:
    """Recover Resource

    &lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_services_delete(request: web.Request, id) -> web.Response:
    """Delete Linked Services

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; linked services from a Resource, i.e. unlink the services. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Once deleted, all services become available to the resource.&lt;/p&gt;

    :param id: id of resource object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_resources_id_services_post(request: web.Request, id, body=None) -> web.Response:
    """Create Linked Services

    &lt;p&gt;Use this endpoint to explicitly &lt;b&gt;Link Services&lt;/b&gt; to a Resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Note:&lt;/b&gt; By default, the services array is empty which signifies that all services are provided by the resource. Linking services here will add to the linked service(s) array available to this resource. This will limit the services available to the resource.&lt;/p&gt;  &lt;p&gt;You cannot post services that already exist in the array, you can only add new ones. Use the &lt;i&gt;PUT ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint to update the entire list.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param body: Array of valid service object id&#39;s
    :type body: List[str]

    """
    return web.Response(status=200)


async def setup_v1_resources_id_services_put(request: web.Request, id, body=None) -> web.Response:
    """Update Linked Services

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; the linked services of a Resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Updating services with this endpoint will update the linked services available to the resource. Only those services will be available to the resource.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Note:&lt;/b&gt; This is a destructive process, any existing linked services will be removed and replaced with the list of services supplied here. Provide the resources complete list of services when using this endpoint.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param body: Array of valid service object id&#39;s
    :type body: List[str]

    """
    return web.Response(status=200)


async def setup_v1_resources_id_uploadimage_post(request: web.Request, id, body=None) -> web.Response:
    """Upload Resource Image

    &lt;p&gt;Use this endpoint to &lt;b&gt;Upload&lt;/b&gt; a resource image to the resource. A valid &lt;b&gt;resource id&lt;/b&gt; is required. You must convert the image to a &lt;b&gt;base64 encoded string&lt;/b&gt; and pass that string as input along with your &lt;b&gt;filename&lt;/b&gt;.&lt;/p&gt;

    :param id: id of resource object
    :type id: str
    :param body: Input model for image upload
    :type body: dict | bytes

    """
    body = ResourceImageInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_post(request: web.Request, google_auth_return_url=None, outlook_auth_return_url=None, body=None) -> web.Response:
    """Create Resource

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new resource.&lt;/p&gt;  &lt;p&gt;Required Fields: &lt;b&gt;Email Address&lt;/b&gt; and &lt;b&gt;Name&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Providing a single or many serviceId(s) in the service array will result the resource explicitly being available to provide those services only. While passing in an empty array will result in all services being available to the resources. This includes all company and business scoped services. See the &lt;i&gt;POST ​/setup​/v1​/resources​/{id}​/services&lt;/i&gt; endpoint for details about explicitly linking services.&lt;/p&gt;  &lt;p&gt;Set the resource availability type by using the &lt;b&gt;recurringAvailability&lt;/b&gt; flag. Set recurringAvailability to &lt;b&gt;True&lt;/b&gt; for &lt;b&gt;Weekly Availability&lt;/b&gt; or &lt;b&gt;False&lt;/b&gt; for &lt;b&gt;Resource Allocations&lt;/b&gt;.&lt;/p&gt;

    :param google_auth_return_url: Google calendar authorization return url
    :type google_auth_return_url: str
    :param outlook_auth_return_url: Outlook calendar authorization return url
    :type outlook_auth_return_url: str
    :param body: Resource input model
    :type body: dict | bytes

    """
    body = ResourceInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_resources_timezones_get(request: web.Request, ) -> web.Response:
    """Get Time Zones

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Time Zones&lt;/b&gt;.&lt;/p&gt;


    """
    return web.Response(status=200)
