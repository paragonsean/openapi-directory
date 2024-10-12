from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_webinars_response import AccountWebinarsResponse
from openapi_server.models.attendee import Attendee
from openapi_server.models.audio import Audio
from openapi_server.models.audio_update import AudioUpdate
from openapi_server.models.created_webinar import CreatedWebinar
from openapi_server.models.date_time_range import DateTimeRange
from openapi_server.models.historical_webinar import HistoricalWebinar
from openapi_server.models.session_performance import SessionPerformance
from openapi_server.models.upcoming_webinar import UpcomingWebinar
from openapi_server.models.webinar import Webinar
from openapi_server.models.webinar_by_key import WebinarByKey
from openapi_server.models.webinar_req_create import WebinarReqCreate
from openapi_server.models.webinar_req_update import WebinarReqUpdate
from openapi_server import util


async def cancel_webinar(request: web.Request, authorization, organizer_key, webinar_key, send_cancellation_emails=None) -> web.Response:
    """Cancel webinar

    Cancels a specific webinar. If the webinar is a series or sequence, this call deletes all scheduled sessions. To send cancellation emails to registrants set sendCancellationEmails&#x3D;true in the request. When the cancellation emails are sent, the default generated message is used in the cancellation email body.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param send_cancellation_emails: Indicates whether cancellation notice emails should be sent. The default value is false
    :type send_cancellation_emails: bool

    """
    return web.Response(status=200)


async def create_webinar(request: web.Request, authorization, organizer_key, body) -> web.Response:
    """Create webinar

    Creates a single session webinar, a sequence of webinars or a series of webinars depending on the type field in the body: \&quot;single_session\&quot; creates a single webinar session, \&quot;sequence\&quot; creates a webinar with multiple meeting times where attendees are expected to be the same for all sessions, and \&quot;series\&quot; creates a webinar with multiple meetings times where attendees choose only one to attend. The default, if no type is declared, is single_session. A sequence webinar requires a \&quot;recurrenceStart\&quot; object consisting of a \&quot;startTime\&quot; and \&quot;endTime\&quot; key for the first webinar of the sequence, a \&quot;recurrencePattern\&quot; of \&quot;daily\&quot;, \&quot;weekly\&quot;, \&quot;monthly\&quot;, and a \&quot;recurrenceEnd\&quot; which is the last date of the sequence (for example, 2016-12-01). A series webinar requires a \&quot;times\&quot; array with a discrete \&quot;startTime\&quot; and \&quot;endTime\&quot; for each webinar in the series. The call requires a webinar subject and description. The \&quot;isPasswordProtected\&quot; sets whether the webinar requires a password for attendees to join. If set to True, the organizer must go to Registration Settings at My Webinars (https://global.gotowebinar.com/webinars.tmpl) and add the password to the webinar, and send the password to the registrants. The response provides a numeric webinarKey in string format for the new webinar. Once a webinar has been created with this method, you can accept registrations.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param body: The webinar details
    :type body: dict | bytes

    """
    body = WebinarReqCreate.from_dict(body)
    return web.Response(status=200)


async def get_all_account_webinars(request: web.Request, authorization, account_key, from_time, to_time, page=None, size=None) -> web.Response:
    """Get all webinars for an account

    Retrieves the list of webinars for an account within a given date range. __*Page*__ and __*size*__ parameters are optional. Default __*page*__ is 0 and default __*size*__ is 20. For technical reasons, this call cannot be executed from this documentation. Please use the curl command to execute it.

    :param authorization: Access token
    :type authorization: str
    :param account_key: The key of the account
    :type account_key: int
    :param from_time: A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
    :type from_time: str
    :param to_time: A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
    :type to_time: str
    :param page: The page number to be displayed. The first page is 0.
    :type page: int
    :param size: The size of the page.
    :type size: int

    """
    from_time = util.deserialize_datetime(from_time)
    to_time = util.deserialize_datetime(to_time)
    return web.Response(status=200)


async def get_all_webinars(request: web.Request, authorization, organizer_key) -> web.Response:
    """Get all webinars

    Returns webinars scheduled for the future for a specified organizer.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int

    """
    return web.Response(status=200)


async def get_attendees_for_all_webinar_sessions(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get attendees for all webinar sessions

    Returns all attendees for all sessions of the specified webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def get_audio_information(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get audio information

    Retrieves the audio/conferencing information for a specific webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def get_historical_webinars(request: web.Request, authorization, organizer_key, from_time, to_time) -> web.Response:
    """Get historical webinars

    Returns details for completed webinars for the specified organizer and completed webinars of other organizers where the specified organizer is a co-organizer.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param from_time: A required start of datetime range in ISO8601 UTC format, e.g. 2015-07-13T10:00:00Z
    :type from_time: str
    :param to_time: A required end of datetime range in ISO8601 UTC format, e.g. 2015-07-13T22:00:00Z
    :type to_time: str

    """
    from_time = util.deserialize_datetime(from_time)
    to_time = util.deserialize_datetime(to_time)
    return web.Response(status=200)


async def get_performance_for_all_webinar_sessions(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get performance for all webinar sessions

    Gets performance details for all sessions of a specific webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def get_upcoming_webinars(request: web.Request, authorization, organizer_key) -> web.Response:
    """Get upcoming webinars

    Returns webinars scheduled for the future for the specified organizer and webinars of other organizers where the specified organizer is a co-organizer.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int

    """
    return web.Response(status=200)


async def get_webinar(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get webinar

    Retrieve information on a specific webinar. If the type of the webinar is &#39;sequence&#39;, a sequence of future times will be provided. Webinars of type &#39;series&#39; are treated the same as normal webinars - each session in the webinar series has a different webinarKey. If an organizer cancels a webinar, then a request to get that webinar would return a &#39;404 Not Found&#39; error.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def get_webinar_meeting_times(request: web.Request, authorization, organizer_key, webinar_key) -> web.Response:
    """Get webinar meeting times

    Retrieves the meeting times for a webinar.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int

    """
    return web.Response(status=200)


async def update_audio_information(request: web.Request, authorization, organizer_key, webinar_key, body, notify_participants=None) -> web.Response:
    """Update audio information

    Updates the audio/conferencing settings for a specific webinar

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param body: The audio/conferencing settings
    :type body: dict | bytes
    :param notify_participants: Defines whether to send notifications to participants
    :type notify_participants: bool

    """
    body = AudioUpdate.from_dict(body)
    return web.Response(status=200)


async def update_webinar(request: web.Request, authorization, organizer_key, webinar_key, body, notify_participants=None) -> web.Response:
    """Update webinar

    Updates a webinar. The call requires at least one of the parameters in the request body. The request completely replaces the existing session, series, or sequence and so must include the full definition of each as for the Create call. Set notifyParticipants&#x3D;true to send update emails to registrants.

    :param authorization: Access token
    :type authorization: str
    :param organizer_key: The key of the organizer
    :type organizer_key: int
    :param webinar_key: The key of the webinar
    :type webinar_key: int
    :param body: The webinar details
    :type body: dict | bytes
    :param notify_participants: Defines whether to send notifications to participants
    :type notify_participants: bool

    """
    body = WebinarReqUpdate.from_dict(body)
    return web.Response(status=200)
