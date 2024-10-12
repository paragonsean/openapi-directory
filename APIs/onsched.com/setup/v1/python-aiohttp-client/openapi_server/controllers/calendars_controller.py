from typing import List, Dict
from aiohttp import web

from openapi_server.models.calendar_block_input_model import CalendarBlockInputModel
from openapi_server.models.calendar_block_list_view_model import CalendarBlockListViewModel
from openapi_server.models.calendar_block_update_model import CalendarBlockUpdateModel
from openapi_server.models.calendar_block_view_model import CalendarBlockViewModel
from openapi_server.models.resource_block_view_model import ResourceBlockViewModel
from openapi_server.models.schedule_input_model import ScheduleInputModel
from openapi_server.models.schedule_list_view_model import ScheduleListViewModel
from openapi_server.models.schedule_update_model import ScheduleUpdateModel
from openapi_server.models.schedule_view_model import ScheduleViewModel
from openapi_server.models.service_list_view_model import ServiceListViewModel
from openapi_server import util


async def setup_v1_calendars_block_id_delete(request: web.Request, id) -> web.Response:
    """Delete Calendar Block

    &lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a calendar block. A valid &lt;b&gt;calendarBlock id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of a calendarBlock object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_calendars_block_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Calendar Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Calendar Block. A valid &lt;b&gt;calendarBlock id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST ​/setup​/v1​/calendars​/{id}​/block&lt;/i&gt; endpoint for fieldnames and details.&lt;/p&gt;

    :param id: id of calendarBlock object
    :type id: str
    :param body: Resource Block input model
    :type body: dict | bytes

    """
    body = CalendarBlockUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_calendars_blocks_id_get(request: web.Request, id) -> web.Response:
    """Get Calendar Block

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Calendar Block&lt;/b&gt;. A valid &lt;b&gt;calendarBlock id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of calendarBlock object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_calendars_get(request: web.Request, location_id=None, deleted=None, offset=None, limit=None) -> web.Response:
    """List Calendars

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Calendars&lt;/b&gt; from the requested location. If not specified, the business location defaults to the primary business location. &lt;/p&gt;

    :param location_id: id of business location, defaults to primary business location
    :type location_id: str
    :param deleted: Filter by deleted status
    :type deleted: bool
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_calendars_id_block_post(request: web.Request, id, body=None) -> web.Response:
    """Create Calendar Block

    &lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Calendar Block. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;Calendar blocks can be set to specific time ranges or for the whole day. Th block a whole day set the startTime to 0 and endTime to 2400.&lt;/p&gt;  &lt;p&gt;Calendar blocks can be for a specific date range instance or set to repeat at a specified frequency.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the block repeats. For example, an interval of 2 for a weekly block means that the block will repeat every 2nd week beginning at the day specified. A daily block with an interval of 10 means the block will repeat every 10 days. The interval property applies to all repeat frequencies. &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY BLOCKS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY BLOCKS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt;  is required and should be set to &lt;b&gt;“W”&lt;/b&gt;.  You must specify the &lt;b&gt;weekdays&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;. For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the block date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY BLOCKS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly, &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want blocked.  If monthDay&#x3D;’15’ this means to block the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on. For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits: day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

    :param id: id of calendar object
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CalendarBlockInputModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_calendars_id_blocks_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """List Calendar Blocks

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Calendar Blocks&lt;/b&gt; for the requested calendar. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. &lt;/p&gt;

    :param id: id of calendar to list blocks
    :type id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_calendars_id_delete(request: web.Request, id) -> web.Response:
    """Delete Calendar

    &lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. The calendar is not permanently deleted and can be recovered by using the &lt;i&gt;PUT ​/setup​/v1​/calendars​/{id}​/recover &lt;/i&gt;endpoint.&lt;/p&gt;

    :param id: id of calendar object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_calendars_id_get(request: web.Request, id) -> web.Response:
    """Get Calendar

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;Calendar&lt;/b&gt; object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of calendar object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_calendars_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update Calendar

    &lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. When your company was created a calendar object was automatically created with 24-hour weekly availability. Its &lt;b&gt;name &#x3D; Main&lt;/b&gt;, the &lt;b&gt;type &#x3D; resource&lt;/b&gt; and by default the &lt;b&gt;interval &#x3D; 30 mins&lt;/b&gt;. We are currently supporting resource calendar type. Other types were part of our Legacy Application and has no relevance in the API product.&lt;/p&gt;

    :param id: id of calendar object
    :type id: str
    :param body: Input model for the calendar object
    :type body: dict | bytes

    """
    body = ScheduleUpdateModel.from_dict(body)
    return web.Response(status=200)


async def setup_v1_calendars_id_recover_put(request: web.Request, id) -> web.Response:
    """Recover Calendar

    &lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a previously deleted calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;

    :param id: id of calendar object
    :type id: str

    """
    return web.Response(status=200)


async def setup_v1_calendars_id_services_get(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """List Calendar Services

    &lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Linked Services&lt;/b&gt; of a calendar object. A valid &lt;b&gt;calendar id&lt;/b&gt; is required. Find calendar id&#39;s by using the &lt;i&gt;GET /setup/v1/calendars&lt;/i&gt; endpoint.&lt;/p&gt;

    :param id: id of calendar object
    :type id: str
    :param offset: Starting row of page, default 0
    :type offset: int
    :param limit: Page limit default 20, max 100
    :type limit: int

    """
    return web.Response(status=200)


async def setup_v1_calendars_post(request: web.Request, body=None) -> web.Response:
    """DEPRECATING: Create

    &lt;p&gt;    &lt;b&gt;DEPRECATING:&lt;/b&gt; Create Calendar&lt;/p&gt;  &lt;p&gt;We are no longer supporting Multiple Calendar Functionality as it is part of our Legacy Application and has no relevance in the API.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes

    """
    body = ScheduleInputModel.from_dict(body)
    return web.Response(status=200)
