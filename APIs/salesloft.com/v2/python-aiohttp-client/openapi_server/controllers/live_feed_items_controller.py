from typing import List, Dict
from aiohttp import web

from openapi_server.models.live_feed_item import LiveFeedItem
from openapi_server import util


async def v2_third_party_live_feed_items_post(request: web.Request, event_occurred_at, idempotency_key, message, subject_id, subject_type, user_guid) -> web.Response:
    """Create a live feed item

    Creates a live feed item that can be sent to users. May only be used by whitelisted Frontend Integrations. Reference the Salesloft App Directory and Frontend Integrations sections for additional details.

    :param event_occurred_at: Equality filters that are applied to the event_occurred_at field. A single filter can be used by itself or combined with other filters to create a range. ---CUSTOM--- {\\\&quot;keys\\\&quot;:[{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;gt\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;},{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;gte\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;},{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;lt\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;},{\\\&quot;description\\\&quot;:\\\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;lte\\\&quot;,\\\&quot;type\\\&quot;:\\\&quot;iso8601 string\\\&quot;}],\\\&quot;type\\\&quot;:\\\&quot;object\\\&quot;} 
    :type event_occurred_at: str
    :param idempotency_key: Uniquely provided string specific to this event. This should be a value which can&#39;t be duplicated between external systems, meaning that an id is not sufficient.
    :type idempotency_key: str
    :param message: The message that relates to the subject. This message should start with a lower-case past-tense verb and end with a period (e.g. \\\&quot;received a package.\\\&quot;). When live feed items are displayed to users, the subject&#39;s name is concatenated with the message and a joining space. Only &lt;a&gt; HTML tags with an \\\&quot;href\\\&quot; attribute are allowed. Other attributes and tags will be stripped.
    :type message: str
    :param subject_id: The ID of the subject of the live feed item (i.e. the \\\&quot;person\\\&quot; id).
    :type subject_id: int
    :param subject_type: The type of the subject of the live feed item. Currently only \\\&quot;person\\\&quot; is supported.
    :type subject_type: str
    :param user_guid: The guid for the user that this live feed item should be shown to.
    :type user_guid: str

    """
    return web.Response(status=200)
