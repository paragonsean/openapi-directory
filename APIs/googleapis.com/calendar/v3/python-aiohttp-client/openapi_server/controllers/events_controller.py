from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.event import Event
from openapi_server.models.events import Events
from openapi_server import util


async def calendar_events_delete(request: web.Request, calendar_id, event_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, send_notifications=None, send_updates=None) -> web.Response:
    """calendar_events_delete

    Deletes an event.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param event_id: Event identifier.
    :type event_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param send_notifications: Deprecated. Please use sendUpdates instead.  Whether to send notifications about the deletion of the event. Note that some emails might still be sent even if you set the value to false. The default is false.
    :type send_notifications: bool
    :param send_updates: Guests who should receive notifications about the deletion of the event.
    :type send_updates: str

    """
    return web.Response(status=200)


async def calendar_events_get(request: web.Request, calendar_id, event_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, always_include_email=None, max_attendees=None, time_zone=None) -> web.Response:
    """calendar_events_get

    Returns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the events.list method using the iCalUID parameter.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param event_id: Event identifier.
    :type event_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param always_include_email: Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    :type always_include_email: bool
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param time_zone: Time zone used in the response. Optional. The default is the time zone of the calendar.
    :type time_zone: str

    """
    return web.Response(status=200)


async def calendar_events_import(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, conference_data_version=None, supports_attachments=None, body=None) -> web.Response:
    """calendar_events_import

    Imports an event. This operation is used to add a private copy of an existing event to a calendar.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param conference_data_version: Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    :type conference_data_version: int
    :param supports_attachments: Whether API client performing operation supports event attachments. Optional. The default is False.
    :type supports_attachments: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Event.from_dict(body)
    return web.Response(status=200)


async def calendar_events_insert(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, conference_data_version=None, max_attendees=None, send_notifications=None, send_updates=None, supports_attachments=None, body=None) -> web.Response:
    """calendar_events_insert

    Creates an event.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param conference_data_version: Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    :type conference_data_version: int
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param send_notifications: Deprecated. Please use sendUpdates instead.  Whether to send notifications about the creation of the new event. Note that some emails might still be sent even if you set the value to false. The default is false.
    :type send_notifications: bool
    :param send_updates: Whether to send notifications about the creation of the new event. Note that some emails might still be sent. The default is false.
    :type send_updates: str
    :param supports_attachments: Whether API client performing operation supports event attachments. Optional. The default is False.
    :type supports_attachments: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Event.from_dict(body)
    return web.Response(status=200)


async def calendar_events_instances(request: web.Request, calendar_id, event_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, always_include_email=None, max_attendees=None, max_results=None, original_start=None, page_token=None, show_deleted=None, time_max=None, time_min=None, time_zone=None) -> web.Response:
    """calendar_events_instances

    Returns instances of the specified recurring event.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param event_id: Recurring event identifier.
    :type event_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param always_include_email: Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    :type always_include_email: bool
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param max_results: Maximum number of events returned on one result page. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.
    :type max_results: int
    :param original_start: The original start time of the instance in the result. Optional.
    :type original_start: str
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param show_deleted: Whether to include deleted events (with status equals \&quot;cancelled\&quot;) in the result. Cancelled instances of recurring events will still be included if singleEvents is False. Optional. The default is False.
    :type show_deleted: bool
    :param time_max: Upper bound (exclusive) for an event&#39;s start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset.
    :type time_max: str
    :param time_min: Lower bound (inclusive) for an event&#39;s end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset.
    :type time_min: str
    :param time_zone: Time zone used in the response. Optional. The default is the time zone of the calendar.
    :type time_zone: str

    """
    return web.Response(status=200)


async def calendar_events_list(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, always_include_email=None, event_types=None, i_cal_uid=None, max_attendees=None, max_results=None, order_by=None, page_token=None, private_extended_property=None, q=None, shared_extended_property=None, show_deleted=None, show_hidden_invitations=None, single_events=None, sync_token=None, time_max=None, time_min=None, time_zone=None, updated_min=None) -> web.Response:
    """calendar_events_list

    Returns events on the specified calendar.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param always_include_email: Deprecated and ignored.
    :type always_include_email: bool
    :param event_types: Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. The default is [\&quot;default\&quot;, \&quot;focusTime\&quot;, \&quot;outOfOffice\&quot;].
    :type event_types: List[str]
    :param i_cal_uid: Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID.
    :type i_cal_uid: str
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param max_results: Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.
    :type max_results: int
    :param order_by: The order of the events returned in the result. Optional. The default is an unspecified, stable order.
    :type order_by: str
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param private_extended_property: Extended properties constraint specified as propertyName&#x3D;value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.
    :type private_extended_property: List[str]
    :param q: Free text search terms to find events that match these terms in the following fields:  - summary  - description  - location  - attendee&#39;s displayName  - attendee&#39;s email  - organizer&#39;s displayName  - organizer&#39;s email  - workingLocationProperties.officeLocation.buildingId  - workingLocationProperties.officeLocation.deskId  - workingLocationProperties.officeLocation.label  - workingLocationProperties.customLocation.label  These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for \&quot;Office\&quot; or \&quot;Bureau\&quot; returns working location events of type officeLocation, whereas searching for \&quot;Out of office\&quot; or \&quot;Abwesend\&quot; returns out-of-office events. Optional.
    :type q: str
    :param shared_extended_property: Extended properties constraint specified as propertyName&#x3D;value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.
    :type shared_extended_property: List[str]
    :param show_deleted: Whether to include deleted events (with status equals \&quot;cancelled\&quot;) in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.
    :type show_deleted: bool
    :param show_hidden_invitations: Whether to include hidden invitations in the result. Optional. The default is False.
    :type show_hidden_invitations: bool
    :param single_events: Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.
    :type single_events: bool
    :param sync_token: Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.  These are:  - iCalUID  - orderBy  - privateExtendedProperty  - q  - sharedExtendedProperty  - timeMin  - timeMax  - updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    :type sync_token: str
    :param time_max: Upper bound (exclusive) for an event&#39;s start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin.
    :type time_max: str
    :param time_min: Lower bound (exclusive) for an event&#39;s end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.
    :type time_min: str
    :param time_zone: Time zone used in the response. Optional. The default is the time zone of the calendar.
    :type time_zone: str
    :param updated_min: Lower bound for an event&#39;s last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.
    :type updated_min: str

    """
    return web.Response(status=200)


async def calendar_events_move(request: web.Request, calendar_id, event_id, destination, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, send_notifications=None, send_updates=None) -> web.Response:
    """calendar_events_move

    Moves an event to another calendar, i.e. changes an event&#39;s organizer. Note that only default events can be moved; outOfOffice, focusTime and workingLocation events cannot be moved.

    :param calendar_id: Calendar identifier of the source calendar where the event currently is on.
    :type calendar_id: str
    :param event_id: Event identifier.
    :type event_id: str
    :param destination: Calendar identifier of the target calendar where the event is to be moved to.
    :type destination: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param send_notifications: Deprecated. Please use sendUpdates instead.  Whether to send notifications about the change of the event&#39;s organizer. Note that some emails might still be sent even if you set the value to false. The default is false.
    :type send_notifications: bool
    :param send_updates: Guests who should receive notifications about the change of the event&#39;s organizer.
    :type send_updates: str

    """
    return web.Response(status=200)


async def calendar_events_patch(request: web.Request, calendar_id, event_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, always_include_email=None, conference_data_version=None, max_attendees=None, send_notifications=None, send_updates=None, supports_attachments=None, body=None) -> web.Response:
    """calendar_events_patch

    Updates an event. This method supports patch semantics.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param event_id: Event identifier.
    :type event_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param always_include_email: Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    :type always_include_email: bool
    :param conference_data_version: Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    :type conference_data_version: int
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param send_notifications: Deprecated. Please use sendUpdates instead.  Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false.
    :type send_notifications: bool
    :param send_updates: Guests who should receive notifications about the event update (for example, title changes, etc.).
    :type send_updates: str
    :param supports_attachments: Whether API client performing operation supports event attachments. Optional. The default is False.
    :type supports_attachments: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Event.from_dict(body)
    return web.Response(status=200)


async def calendar_events_quick_add(request: web.Request, calendar_id, text, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, send_notifications=None, send_updates=None) -> web.Response:
    """calendar_events_quick_add

    Creates an event based on a simple text string.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param text: The text describing the event to be created.
    :type text: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param send_notifications: Deprecated. Please use sendUpdates instead.  Whether to send notifications about the creation of the event. Note that some emails might still be sent even if you set the value to false. The default is false.
    :type send_notifications: bool
    :param send_updates: Guests who should receive notifications about the creation of the new event.
    :type send_updates: str

    """
    return web.Response(status=200)


async def calendar_events_update(request: web.Request, calendar_id, event_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, always_include_email=None, conference_data_version=None, max_attendees=None, send_notifications=None, send_updates=None, supports_attachments=None, body=None) -> web.Response:
    """calendar_events_update

    Updates an event.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param event_id: Event identifier.
    :type event_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param always_include_email: Deprecated and ignored. A value will always be returned in the email field for the organizer, creator and attendees, even if no real email address is available (i.e. a generated, non-working value will be provided).
    :type always_include_email: bool
    :param conference_data_version: Version number of conference data supported by the API client. Version 0 assumes no conference data support and ignores conference data in the event&#39;s body. Version 1 enables support for copying of ConferenceData as well as for creating new conferences using the createRequest field of conferenceData. The default is 0.
    :type conference_data_version: int
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param send_notifications: Deprecated. Please use sendUpdates instead.  Whether to send notifications about the event update (for example, description changes, etc.). Note that some emails might still be sent even if you set the value to false. The default is false.
    :type send_notifications: bool
    :param send_updates: Guests who should receive notifications about the event update (for example, title changes, etc.).
    :type send_updates: str
    :param supports_attachments: Whether API client performing operation supports event attachments. Optional. The default is False.
    :type supports_attachments: bool
    :param body: 
    :type body: dict | bytes

    """
    body = Event.from_dict(body)
    return web.Response(status=200)


async def calendar_events_watch(request: web.Request, calendar_id, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, always_include_email=None, event_types=None, i_cal_uid=None, max_attendees=None, max_results=None, order_by=None, page_token=None, private_extended_property=None, q=None, shared_extended_property=None, show_deleted=None, show_hidden_invitations=None, single_events=None, sync_token=None, time_max=None, time_min=None, time_zone=None, updated_min=None, body=None) -> web.Response:
    """calendar_events_watch

    Watch for changes to Events resources.

    :param calendar_id: Calendar identifier. To retrieve calendar IDs call the calendarList.list method. If you want to access the primary calendar of the currently logged in user, use the \&quot;primary\&quot; keyword.
    :type calendar_id: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param always_include_email: Deprecated and ignored.
    :type always_include_email: bool
    :param event_types: Event types to return. Optional. This parameter can be repeated multiple times to return events of different types. The default is [\&quot;default\&quot;, \&quot;focusTime\&quot;, \&quot;outOfOffice\&quot;].
    :type event_types: List[str]
    :param i_cal_uid: Specifies an event ID in the iCalendar format to be provided in the response. Optional. Use this if you want to search for an event by its iCalendar ID.
    :type i_cal_uid: str
    :param max_attendees: The maximum number of attendees to include in the response. If there are more than the specified number of attendees, only the participant is returned. Optional.
    :type max_attendees: int
    :param max_results: Maximum number of events returned on one result page. The number of events in the resulting page may be less than this value, or none at all, even if there are more events matching the query. Incomplete pages can be detected by a non-empty nextPageToken field in the response. By default the value is 250 events. The page size can never be larger than 2500 events. Optional.
    :type max_results: int
    :param order_by: The order of the events returned in the result. Optional. The default is an unspecified, stable order.
    :type order_by: str
    :param page_token: Token specifying which result page to return. Optional.
    :type page_token: str
    :param private_extended_property: Extended properties constraint specified as propertyName&#x3D;value. Matches only private properties. This parameter might be repeated multiple times to return events that match all given constraints.
    :type private_extended_property: List[str]
    :param q: Free text search terms to find events that match these terms in the following fields:  - summary  - description  - location  - attendee&#39;s displayName  - attendee&#39;s email  - organizer&#39;s displayName  - organizer&#39;s email  - workingLocationProperties.officeLocation.buildingId  - workingLocationProperties.officeLocation.deskId  - workingLocationProperties.officeLocation.label  - workingLocationProperties.customLocation.label  These search terms also match predefined keywords against all display title translations of working location, out-of-office, and focus-time events. For example, searching for \&quot;Office\&quot; or \&quot;Bureau\&quot; returns working location events of type officeLocation, whereas searching for \&quot;Out of office\&quot; or \&quot;Abwesend\&quot; returns out-of-office events. Optional.
    :type q: str
    :param shared_extended_property: Extended properties constraint specified as propertyName&#x3D;value. Matches only shared properties. This parameter might be repeated multiple times to return events that match all given constraints.
    :type shared_extended_property: List[str]
    :param show_deleted: Whether to include deleted events (with status equals \&quot;cancelled\&quot;) in the result. Cancelled instances of recurring events (but not the underlying recurring event) will still be included if showDeleted and singleEvents are both False. If showDeleted and singleEvents are both True, only single instances of deleted events (but not the underlying recurring events) are returned. Optional. The default is False.
    :type show_deleted: bool
    :param show_hidden_invitations: Whether to include hidden invitations in the result. Optional. The default is False.
    :type show_hidden_invitations: bool
    :param single_events: Whether to expand recurring events into instances and only return single one-off events and instances of recurring events, but not the underlying recurring events themselves. Optional. The default is False.
    :type single_events: bool
    :param sync_token: Token obtained from the nextSyncToken field returned on the last page of results from the previous list request. It makes the result of this list request contain only entries that have changed since then. All events deleted since the previous list request will always be in the result set and it is not allowed to set showDeleted to False. There are several query parameters that cannot be specified together with nextSyncToken to ensure consistency of the client state.  These are:  - iCalUID  - orderBy  - privateExtendedProperty  - q  - sharedExtendedProperty  - timeMin  - timeMax  - updatedMin All other query parameters should be the same as for the initial synchronization to avoid undefined behavior. If the syncToken expires, the server will respond with a 410 GONE response code and the client should clear its storage and perform a full synchronization without any syncToken. Learn more about incremental synchronization. Optional. The default is to return all entries.
    :type sync_token: str
    :param time_max: Upper bound (exclusive) for an event&#39;s start time to filter by. Optional. The default is not to filter by start time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMin is set, timeMax must be greater than timeMin.
    :type time_max: str
    :param time_min: Lower bound (exclusive) for an event&#39;s end time to filter by. Optional. The default is not to filter by end time. Must be an RFC3339 timestamp with mandatory time zone offset, for example, 2011-06-03T10:00:00-07:00, 2011-06-03T10:00:00Z. Milliseconds may be provided but are ignored. If timeMax is set, timeMin must be smaller than timeMax.
    :type time_min: str
    :param time_zone: Time zone used in the response. Optional. The default is the time zone of the calendar.
    :type time_zone: str
    :param updated_min: Lower bound for an event&#39;s last modification time (as a RFC3339 timestamp) to filter by. When specified, entries deleted since this time will always be included regardless of showDeleted. Optional. The default is not to filter by last modification time.
    :type updated_min: str
    :param body: 
    :type body: dict | bytes

    """
    body = Channel.from_dict(body)
    return web.Response(status=200)
