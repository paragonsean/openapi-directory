from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_page import BatchPage
from openapi_server.models.batch_request import BatchRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.recipient import Recipient
from openapi_server.models.resource_id import ResourceId
from openapi_server.models.text import Text
from openapi_server.models.text_auto_reply import TextAutoReply
from openapi_server.models.text_auto_reply_page import TextAutoReplyPage
from openapi_server.models.text_broadcast import TextBroadcast
from openapi_server.models.text_broadcast_create_response import TextBroadcastCreateResponse
from openapi_server.models.text_broadcast_page import TextBroadcastPage
from openapi_server.models.text_broadcast_stats_dto import TextBroadcastStatsDto
from openapi_server.models.text_list import TextList
from openapi_server.models.text_page import TextPage
from openapi_server.models.text_recipient import TextRecipient
from openapi_server import util


async def add_text_broadcast_batch(request: web.Request, id, strict_validation=None, body=None) -> web.Response:
    """Add batches to a text broadcast

    Allows adding an extra batches to an already created text broadcast campaign. The batches which being  added pass the CallFire validation process (unlike in the recipients version of this API). That is why using of a scrubDuplicates flag remove duplicates from your batch. Batches may be added as a contact list id, a list of contact ids, or a list of numbers

    :param id: An id of a text broadcast
    :type id: int
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A request object
    :type body: dict | bytes

    """
    body = BatchRequest.from_dict(body)
    return web.Response(status=200)


async def add_text_broadcast_recipients(request: web.Request, id, fields=None, strict_validation=None, body=None) -> web.Response:
    """Add recipients to a text broadcast

    Use this API to add recipients to a text broadcast which is already created. Post a list of Recipient objects to be immediately added to the text broadcast campaign. These contacts will not go through validation process, and will be acted upon as they are added. Recipients may be added as a list of contact ids, or list of numbers

    :param id: An id of a text broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A list of the TextRecipient objects
    :type body: list | bytes

    """
    body = [TextRecipient.from_dict(d) for d in body]
    return web.Response(status=200)


async def archive_text_broadcast(request: web.Request, id) -> web.Response:
    """Archive text broadcast

    Archives a text broadcast (and hides it in the search results)

    :param id: An id of a text broadcast to archive
    :type id: int

    """
    return web.Response(status=200)


async def create_text_auto_reply(request: web.Request, body=None) -> web.Response:
    """Create an auto reply

    CallFire gives you possibility to set up auto reply messages for your numbers and keywords. You can set a general auto reply for anyone who texts your number, keyword, and/or include a text to match, so that the auto reply would be sent only to those who text the matched text

    :param body: TextAutoReply object, keyword or number should be specified with response message and text to match if needed
    :type body: dict | bytes

    """
    body = TextAutoReply.from_dict(body)
    return web.Response(status=200)


async def create_text_broadcast(request: web.Request, start=None, strict_validation=None, body=None) -> web.Response:
    """Create a text broadcast

    Creates a text broadcast campaign using the Text Broadcast API. Send a TextBroadcast object in the message body to detail a text broadcast campaign. A campaign can be created without contacts and with bare minimum configuration, but contacts have to be added further on to use the campaign. It supports scheduling, retry logic, pattern-based messages.

    :param start: If true then starts the campaign immediately (not required).
    :type start: bool
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A TextBroadcast object
    :type body: dict | bytes

    """
    body = TextBroadcast.from_dict(body)
    return web.Response(status=200)


async def delete_text_auto_reply(request: web.Request, id) -> web.Response:
    """Delete an auto reply

    Deletes a text auto reply and removes the configuration. Can not delete a TextAutoReply which is currently active for a campaign

    :param id: An id of a text auto reply
    :type id: int

    """
    return web.Response(status=200)


async def find_text_auto_replys(request: web.Request, fields=None, limit=None, offset=None, number=None) -> web.Response:
    """Find auto replies

    Find all text autoreplies created by user. Returns a paged list of TextAutoReply

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param number: Phone number in E.164 format (11-digit) which contains a TextAutoReply. Example: 12132000384. If number is empty then operator returns all autoreplies configured for the user&#39;s account
    :type number: str

    """
    return web.Response(status=200)


async def find_text_broadcasts(request: web.Request, name=None, label=None, running=None, scheduled=None, interval_begin=None, interval_end=None, limit=None, offset=None, fields=None) -> web.Response:
    """Find text broadcasts

    Searches for all text broadcasts created by user. Can query on label, name, and the current running status of the campaign. Returns a paged list of text broadcasts

    :param name: A name of text broadcast
    :type name: str
    :param label: A label of a text broadcast
    :type label: str
    :param running: Returns broadcasts only in running state.
    :type running: bool
    :param scheduled: Specify whether the campaigns should be scheduled or not
    :type scheduled: bool
    :param interval_begin: Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type interval_begin: int
    :param interval_end: End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type interval_end: int
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_texts(request: web.Request, id=None, campaign_id=None, batch_id=None, from_number=None, to_number=None, label=None, states=None, results=None, inbound=None, interval_begin=None, interval_end=None, limit=None, offset=None, fields=None) -> web.Response:
    """Find texts

    Searches for texts sent or received by user. Use \&quot;campaignId&#x3D;0\&quot; parameter to query for all texts sent through the POST /texts API. See [call states and results](https://developers.callfire.com/results-responses-errors.html)

    :param id: List of Text ids to search for, if ids specified other query params ignored
    :type id: List[int]
    :param campaign_id: An id of a campaign, queries for texts inside a particular campaign. Specify null to list texts of all campaigns or 0 for a default campaign
    :type campaign_id: int
    :param batch_id: An Id of a contact batch, queries for texts which are used in the particular contact batch
    :type batch_id: int
    :param from_number: A phone number in E.164 format (11-digit). Example: 12132000384, 67076
    :type from_number: str
    :param to_number: A phone number in E.164 format (11-digit). Example: 12132000384, 67076
    :type to_number: str
    :param label: A label of a text message
    :type label: str
    :param states: Expected text statuses in comma separated string, available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    :type states: str
    :param results: Expected text results in comma separated string, available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    :type results: str
    :param inbound: Specify true for inbound or false for outbounds. Do not specify this parameter if you need to get both inbound and outbound texts listed in response
    :type inbound: bool
    :param interval_begin: Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    :type interval_begin: int
    :param interval_end: End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
    :type interval_end: int
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_text(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific text

    Returns a single Text instance for a given text id

    :param id: An id of a text
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_text_auto_reply(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific auto reply

    Returns a single TextAutoReply instance for a given text auto reply id

    :param id: An id of a text auto reply
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_text_broadcast(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific text broadcast

    Returns a single TextBroadcast instance for a given text broadcast id

    :param id: An id of a text broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_text_broadcast_batches(request: web.Request, id, fields=None, limit=None, offset=None) -> web.Response:
    """Find batches in a text broadcast

    This endpoint will enable the user to page through all of the batches for a particular text broadcast campaign

    :param id: An id of a text broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int

    """
    return web.Response(status=200)


async def get_text_broadcast_stats(request: web.Request, id, fields=None, begin=None, end=None) -> web.Response:
    """Get statistics on text broadcast

    Returns the broadcast statistics. Example: total number of the sent/received actions, total cost, number of remaining outbound actions, error count, etc

    :param id: An id of a text broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param begin: Start of a search find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type begin: int
    :param end: End of a search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type end: int

    """
    return web.Response(status=200)


async def get_text_broadcast_texts(request: web.Request, id, batch_id=None, fields=None, limit=None, offset=None) -> web.Response:
    """Find texts in a text broadcast

    This endpoint will enable the user to page through all of the texts for a particular text broadcast campaign

    :param id: An id of a text broadcast
    :type id: int
    :param batch_id: ~
    :type batch_id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int

    """
    return web.Response(status=200)


async def send_texts(request: web.Request, fields=None, campaign_id=None, default_message=None, strict_validation=None, body=None) -> web.Response:
    """Send texts

    Use the /texts API to send individual texts quickly. By default all texts are going out from CallFire&#39;s dedicated short code. Example: 67076, 818818 etc

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param campaign_id: Specifies a campaignId to send texts through a previously created campaign
    :type campaign_id: int
    :param default_message: Text message can be overridden by TextRecipient.message field. If multiple recipients have the same text message to a different recipients it is better to specify a single default message and do not duplicate it in each recipient.
    :type default_message: str
    :param strict_validation: Turns on strict validation for recipients
    :type strict_validation: bool
    :param body: List of TextRecipient objects. By recipient we mean either phone number or contact with user-defined attributes added to action. Text messaging supports media files, provide a list of ids of media files for recipient to attach media to the message.
    :type body: list | bytes

    """
    body = [TextRecipient.from_dict(d) for d in body]
    return web.Response(status=200)


async def start_text_broadcast(request: web.Request, id) -> web.Response:
    """Start text broadcast

    Starts a text broadcast

    :param id: An id of a text broadcast to start
    :type id: int

    """
    return web.Response(status=200)


async def stop_text_broadcast(request: web.Request, id) -> web.Response:
    """Stop text broadcast

    Stops a text broadcast

    :param id: An Id of a text broadcast. To stop the broadcast
    :type id: int

    """
    return web.Response(status=200)


async def toggle_text_broadcast_recipients_status(request: web.Request, id, enable=None, body=None) -> web.Response:
    """Disable/enable undialed recipients in broadcast

    This operation lets the user to disable/enable undialed contacts in created broadcast

    :param id: An id of a text broadcast
    :type id: int
    :param enable: Flag which indicate what to do with texts (true will enable texts in DISABLED status and vice versa)
    :type enable: bool
    :param body: List of Recipient objects. By recipient we mean either phone number or contact id.
    :type body: list | bytes

    """
    body = [Recipient.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_text_broadcast(request: web.Request, id, strict_validation=None, body=None) -> web.Response:
    """Update a text broadcast

    Allows modifying the configuration of existing text broadcast campaign. See TextBroadcast for more information on what can/can&#39;t be updated on this API

    :param id: An id of a text broadcast
    :type id: int
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A TextBroadcast object
    :type body: dict | bytes

    """
    body = TextBroadcast.from_dict(body)
    return web.Response(status=200)
