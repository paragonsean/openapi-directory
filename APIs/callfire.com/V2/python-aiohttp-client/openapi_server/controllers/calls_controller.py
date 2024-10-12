from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_page import BatchPage
from openapi_server.models.batch_request import BatchRequest
from openapi_server.models.call import Call
from openapi_server.models.call_broadcast import CallBroadcast
from openapi_server.models.call_broadcast_page import CallBroadcastPage
from openapi_server.models.call_broadcast_stats import CallBroadcastStats
from openapi_server.models.call_list import CallList
from openapi_server.models.call_page import CallPage
from openapi_server.models.call_recipient import CallRecipient
from openapi_server.models.call_recording import CallRecording
from openapi_server.models.call_recording_list import CallRecordingList
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.recipient import Recipient
from openapi_server.models.resource_id import ResourceId
from openapi_server import util


async def add_call_broadcast_batch(request: web.Request, id, strict_validation=None, body=None) -> web.Response:
    """Add batches to a call broadcast

    The &#39;add batch&#39; API allows user to add additional batches to an already created voice broadcast campaign. The added batch will go through the CallFire validation process, unlike in the recipients version of this API. That is why you can use the scrubDuplicates flag to remove duplicates from your batch. Batches may be added as a contact list id, a list of contact ids, or a list of numbers

    :param id: An id of a call broadcast
    :type id: int
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A request object
    :type body: dict | bytes

    """
    body = BatchRequest.from_dict(body)
    return web.Response(status=200)


async def add_call_broadcast_recipients(request: web.Request, id, fields=None, strict_validation=None, body=None) -> web.Response:
    """Add recipients to a call broadcast

    Use this API to add the recipients to an existing voice broadcast. Post a list of Recipient objects to be added to the voice broadcast campaign. These contacts will not go through validation process, and will be acted upon as they are added. Recipients may be added as a list of contact ids, or list of numbers

    :param id: An id of a call broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A list of CallRecipient objects
    :type body: list | bytes

    """
    body = [Recipient.from_dict(d) for d in body]
    return web.Response(status=200)


async def archive_voice_broadcast(request: web.Request, id) -> web.Response:
    """Archive voice broadcast

    Archives a voice broadcast (voice broadcast will be hidden in search results)

    :param id: An id of a voice broadcast to archive
    :type id: int

    """
    return web.Response(status=200)


async def create_call_broadcast(request: web.Request, start=None, strict_validation=None, body=None) -> web.Response:
    """Create a call broadcast

    Creates a call broadcast campaign using the Call Broadcast API. Send a CallBroadcast in the message body to add details in a voice broadcast campaign. The campaign can be created without contacts and bare minimum configuration, but contacts will have to be added further on to use the campaign

    :param start: Specify whether to immediately start this campaign (not required)
    :type start: bool
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A CallBroadcast object
    :type body: dict | bytes

    """
    body = CallBroadcast.from_dict(body)
    return web.Response(status=200)


async def find_call_broadcasts(request: web.Request, fields=None, limit=None, offset=None, label=None, name=None, running=None, scheduled=None, interval_begin=None, interval_end=None) -> web.Response:
    """Find call broadcasts

    Searches for all voice broadcasts created by user. Can query on label, name, and the current running status of the campaign. Returns a paged list of voice broadcasts

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param label: A label of a voice broadcast
    :type label: str
    :param name: A name of voice broadcast
    :type name: str
    :param running: Specify whether the campaigns should be running or not
    :type running: bool
    :param scheduled: Specify whether the campaigns should be scheduled or not
    :type scheduled: bool
    :param interval_begin: Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type interval_begin: int
    :param interval_end: End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type interval_end: int

    """
    return web.Response(status=200)


async def find_calls(request: web.Request, fields=None, limit=None, offset=None, id=None, campaign_id=None, batch_id=None, from_number=None, to_number=None, label=None, states=None, results=None, inbound=None, interval_begin=None, interval_end=None) -> web.Response:
    """Find calls

    To search for all calls sent or received by the user. Use \&quot;id&#x3D;0\&quot; for the campaignId parameter to query for all calls sent through the POST /calls API. See [call states and results](https://developers.callfire.com/results-responses-errors.html)

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param id: Lists the Call ids to search for. If calls ids are specified then other query parameters can be ignored
    :type id: List[int]
    :param campaign_id: An id of a campaign, queries for calls included to a particular campaign. Specify null for all campaigns and 0 for default campaign
    :type campaign_id: int
    :param batch_id: An id of a contact batch, queries for calls of a particular contact batch
    :type batch_id: int
    :param from_number: Phone number in E.164 format (11-digit) that call was from. Example: 12132000384
    :type from_number: str
    :param to_number: Phone number in E.164 format (11-digit) that call was sent to. Example: 12132000384
    :type to_number: str
    :param label: A label for a specific call
    :type label: str
    :param states: Searches for all calls which correspond to statuses listed in a comma separated string. Available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    :type states: str
    :param results: Searches for all calls with statuses listed in a comma separated string. Available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
    :type results: str
    :param inbound: Filters inbound calls for \&quot;true\&quot; value and outbound calls for \&quot;false\&quot; value
    :type inbound: bool
    :param interval_begin: Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type interval_begin: int
    :param interval_end: End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type interval_end: int

    """
    return web.Response(status=200)


async def get_call(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific call

    Returns a single Call instance for a given call id.

    :param id: An id of a call
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_call_broadcast(request: web.Request, id, fields=None) -> web.Response:
    """Find a specific call broadcast

    Returns a single CallBroadcast instance for a given call broadcast campaign id

    :param id: An id of a CallBroadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_call_broadcast_batches(request: web.Request, id, fields=None, limit=None, offset=None) -> web.Response:
    """Find batches in a call broadcast

    This endpoint will enable the user to page through all of the batches for a particular voice broadcast campaign

    :param id: An id of a call broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int

    """
    return web.Response(status=200)


async def get_call_broadcast_calls(request: web.Request, id, batch_id=None, fields=None, limit=None, offset=None) -> web.Response:
    """Find calls in a call broadcast

    This endpoint will enable the user to page through all calls for a particular call broadcast campaign

    :param id: An Id of a call broadcast
    :type id: int
    :param batch_id: An id of a particular batch associated with broadcast
    :type batch_id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int

    """
    return web.Response(status=200)


async def get_call_broadcast_stats(request: web.Request, id, fields=None, begin=None, end=None) -> web.Response:
    """Get statistics on call broadcast

    Returns broadcast statistics like total number of sent/received actions, total cost, number of remaining outbound actions, error count, etc

    :param id: An id of a call broadcast
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param begin: Start of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type begin: int
    :param end: End of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
    :type end: int

    """
    return web.Response(status=200)


async def get_call_recording(request: web.Request, id, fields=None) -> web.Response:
    """Get call recording by id

    Returns metadata of recording of a particular call. Metadata contains a link to a MP3 recording

    :param id: ~
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_call_recording_by_name(request: web.Request, id, name, fields=None) -> web.Response:
    """Get call recording by name

    Returns recording metadata of particular call. Metadata contains link to a MP3 recording

    :param id: An id of a call
    :type id: int
    :param name: A name of a recording
    :type name: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_call_recording_mp3(request: web.Request, id) -> web.Response:
    """Get call recording in mp3 format

    Returns an MP3 recording of particular call, response contains binary data, content type is &#39;audio/mpeg&#39;

    :param id: An id of a call
    :type id: int

    """
    return web.Response(status=200)


async def get_call_recording_mp3_by_name(request: web.Request, id, name) -> web.Response:
    """Get call mp3 recording by name

    Returns a MP3 recording of a particular call, response contains binary data, content type is &#39;audio/mpeg&#39;

    :param id: An id of a call
    :type id: int
    :param name: A name of a recording
    :type name: str

    """
    return web.Response(status=200)


async def get_call_recordings(request: web.Request, id, fields=None) -> web.Response:
    """Get call recordings for a call

    Returns a list of recordings metadata of particular call. Metadata contains link to a MP3 recording

    :param id: An id of a call
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def send_calls(request: web.Request, fields=None, campaign_id=None, default_live_message=None, default_machine_message=None, default_live_message_sound_id=None, default_machine_message_sound_id=None, default_voice=None, strict_validation=None, body=None) -> web.Response:
    """Send calls

    Use the /calls API to send individual calls quickly. A verified Caller ID and sufficient credits are required to make a call. CallRecipient represents a single recipient identified by phone number or contact id in CallFire system. You can attach user-defined attributes to a Call action via CallRecipient.attributes property, attributes are available in Call action response

    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str
    :param campaign_id: Specifies a campaignId to send calls quickly on a previously created campaign
    :type campaign_id: int
    :param default_live_message: Text to be turned into a sound, this text will be played when the phone is answered. Parameter can be overridden for any particular CallRecipient
    :type default_live_message: str
    :param default_machine_message: Text to be turned into a sound, this text will be played when answering machine is detected. Parameter can be overridden for any particular CallRecipient
    :type default_machine_message: str
    :param default_live_message_sound_id: Id of sound file to play if phone is answered. Parameter can be overridden for any particular CallRecipient
    :type default_live_message_sound_id: int
    :param default_machine_message_sound_id: An id of a sound file to play if answering machine is detected. Parameter can be overridden for any particular CallRecipient
    :type default_machine_message_sound_id: int
    :param default_voice: The voice set by default for all text-to-speech messages defined in CallRecipient objects or as default *Message properties
    :type default_voice: str
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: An array of CallRecipient objects.  Limitations: 1. Max number of CallRecipient objects is 10 
    :type body: list | bytes

    """
    body = [CallRecipient.from_dict(d) for d in body]
    return web.Response(status=200)


async def start_voice_broadcast(request: web.Request, id) -> web.Response:
    """Start voice broadcast

    Start a voice broadcast

    :param id: An id of voice broadcast to start
    :type id: int

    """
    return web.Response(status=200)


async def stop_voice_broadcast(request: web.Request, id) -> web.Response:
    """Stop voice broadcast

    Stop a voice broadcast

    :param id: An id of voice broadcast to stop
    :type id: int

    """
    return web.Response(status=200)


async def toggle_call_broadcast_recipients_status(request: web.Request, id, enable=None, body=None) -> web.Response:
    """Disable/enable undialed recipients in broadcast

    This operation lets the user to disable/enable undialed recipients in created broadcast

    :param id: An id of a voice broadcast
    :type id: int
    :param enable: Flag which indicate what to do with calls (true will enable call in DISABLED status and vice versa)
    :type enable: bool
    :param body: List of Recipient objects. By recipient we mean either phone number or contact id.
    :type body: list | bytes

    """
    body = [Recipient.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_call_broadcast(request: web.Request, id, strict_validation=None, body=None) -> web.Response:
    """Update a call broadcast

    This operation lets the user modify the configuration of a voice broadcast campaign after call broadcast campaign is created. See CallBroadcast for more information on what can/can&#39;t be updated on this API

    :param id: An id of a voice broadcast
    :type id: int
    :param strict_validation: Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation
    :type strict_validation: bool
    :param body: A CallBroadcast object
    :type body: dict | bytes

    """
    body = CallBroadcast.from_dict(body)
    return web.Response(status=200)
