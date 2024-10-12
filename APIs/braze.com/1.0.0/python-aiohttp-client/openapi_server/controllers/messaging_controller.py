from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedule_api_triggered_canvases_request import ScheduleApiTriggeredCanvasesRequest
from openapi_server import util


async def get_upcoming_scheduled_campaigns_and_canvases(request: web.Request, end_time=None) -> web.Response:
    """Get Upcoming Scheduled Campaigns and Canvases

    You can view a JSON list of upcoming and scheduled Campaigns and Canvases using the following information and parameters. The endpoint will return information about scheduled Campaigns and entry Canvases between now and the designated end_time (ISO 8601 format) specified in the request. Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint are only for Campaigns and Canvases created and scheduled in Braze.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;scheduled_broadcasts\&quot;: [       # Example Canvas       {         \&quot;name\&quot; &#x3D;&gt; String,         \&quot;id\&quot; &#x3D;&gt; String,         \&quot;type\&quot; &#x3D;&gt; \&quot;Canvas\&quot;,         \&quot;tags\&quot; &#x3D;&gt; [String tag names],         \&quot;next_send_time\&quot; &#x3D;&gt; \&quot;YYYY-MM-DD HH:mm:ss\&quot; (may also include time zone if not local/intelligent delivery)         \&quot;schedule_type\&quot; &#x3D;&gt; one of \&quot;local_time_zones\&quot;, \&quot;intelligent_delivery\&quot;, or the name of your company&#39;s time zone       },       # Example Campaign       {         \&quot;name\&quot; &#x3D;&gt; String,         \&quot;id\&quot; &#x3D;&gt; String,         \&quot;type\&quot; &#x3D;&gt; \&quot;Campaign\&quot;,         \&quot;tags\&quot; &#x3D;&gt; [String tag names],         \&quot;next_send_time\&quot; &#x3D;&gt; \&quot;YYYY-MM-DD HH:mm:ss\&quot; (may also include time zone if not local/intelligent delivery)         \&quot;schedule_type\&quot; &#x3D;&gt; one of \&quot;local_time_zones\&quot;, \&quot;intelligent_delivery\&quot;, or the name of your company&#39;s time zone       },     ] } &#x60;&#x60;&#x60;

    :param end_time: (Required) String in ISO 8601 format  End date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API.
    :type end_time: str

    """
    return web.Response(status=200)


async def schedule_api_triggered_canvases(request: web.Request, body=None) -> web.Response:
    """Schedule API Triggered Canvases

    Use this endpoint to trigger API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in &#x60;canvas_entry_properties&#x60; that will be templated into the messages sent by the first steps of the Canvas.  This endpoint allows you to schedule Canvas messages (up to 90 days in advance) via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a Canvas.  ### Request Parameters  | Parameter | Required | Data Type | Description | | --------- | ---------| --------- | ----------- | |&#x60;canvas_id&#x60;|Required|String| See canvas identifier| |&#x60;send_id&#x60; | Optional | String | See send identifier | |&#x60;recipients&#x60; | Optional | Array of recipient objects | See recipients object | |&#x60;audience&#x60; | Optional | Connected audience object | See connected audience | |&#x60;broadcast&#x60; | Optional | Boolean | See broadcast -- defaults to false on 8/31/17, must be set to true if \&quot;recipients\&quot; object is omitted | | &#x60;trigger_properties&#x60; | Optional | Object | Personalization key value pairs for all users in this send; see trigger properties | | &#x60;schedule&#x60; | Required | Schedule object | See schedule object |  ## Request Components - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/) - [Recipients](https://www.braze.com/docs/api/objects_filters/recipient_object/) - [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/) - [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast) - [Trigger Properties](https://www.braze.com/docs/api/objects_filters/trigger_properties_object/) - [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)

    :param body: 
    :type body: dict | bytes

    """
    body = ScheduleApiTriggeredCanvasesRequest.from_dict(body)
    return web.Response(status=200)
