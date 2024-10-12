# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.event import Event
from openapi_server.models.events import Events


pytestmark = pytest.mark.asyncio

async def test_calendar_events_delete(client):
    """Test case for calendar_events_delete

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('sendNotifications', True),
                    ('sendUpdates', 'send_updates_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/calendar/v3/calendars/{calendar_id}/events/{event_id}'.format(calendar_id='calendar_id_example', event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_get(client):
    """Test case for calendar_events_get

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('alwaysIncludeEmail', True),
                    ('maxAttendees', 56),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar/v3/calendars/{calendar_id}/events/{event_id}'.format(calendar_id='calendar_id_example', event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_import(client):
    """Test case for calendar_events_import

    
    """
    body = {"reminders":{"overrides":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"useDefault":True},"attachments":[{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"},{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"}],"workingLocationProperties":{"officeLocation":{"floorId":"floorId","floorSectionId":"floorSectionId","label":"label","deskId":"deskId","buildingId":"buildingId"},"homeOffice":"","customLocation":{"label":"label"},"type":"type"},"gadget":{"preferences":{"key":"preferences"},"iconLink":"iconLink","display":"display","link":"link","width":5,"title":"title","type":"type","height":1},"colorId":"colorId","hangoutLink":"hangoutLink","attendeesOmitted":False,"description":"description","focusTimeProperties":{"chatStatus":"chatStatus","declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"source":{"title":"title","url":"url"},"extendedProperties":{"shared":{"key":"shared"},"private":{"key":"private"}},"guestsCanModify":False,"recurringEventId":"recurringEventId","endTimeUnspecified":False,"guestsCanSeeOtherGuests":True,"end":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"id":"id","locked":False,"anyoneCanAddSelf":False,"summary":"summary","creator":{"displayName":"displayName","self":False,"id":"id","email":"email"},"privateCopy":False,"visibility":"default","attendees":[{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"},{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"}],"created":"2000-01-23T04:56:07.000+00:00","htmlLink":"htmlLink","kind":"calendar#event","iCalUID":"iCalUID","start":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"originalStartTime":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"eventType":"default","recurrence":["recurrence","recurrence"],"sequence":5,"organizer":{"displayName":"displayName","self":False,"id":"id","email":"email"},"transparency":"opaque","conferenceData":{"entryPoints":[{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"},{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"}],"notes":"notes","conferenceId":"conferenceId","createRequest":{"requestId":"requestId","conferenceSolutionKey":{"type":"type"},"status":{"statusCode":"statusCode"}},"signature":"signature","conferenceSolution":{"name":"name","iconUri":"iconUri","key":{"type":"type"}},"parameters":{"addOnParameters":{"parameters":{"key":"parameters"}}}},"etag":"etag","location":"location","guestsCanInviteOthers":True,"outOfOfficeProperties":{"declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"updated":"2000-01-23T04:56:07.000+00:00","status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('conferenceDataVersion', 56),
                    ('supportsAttachments', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/calendars/{calendar_id}/events/import'.format(calendar_id='calendar_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_insert(client):
    """Test case for calendar_events_insert

    
    """
    body = {"reminders":{"overrides":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"useDefault":True},"attachments":[{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"},{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"}],"workingLocationProperties":{"officeLocation":{"floorId":"floorId","floorSectionId":"floorSectionId","label":"label","deskId":"deskId","buildingId":"buildingId"},"homeOffice":"","customLocation":{"label":"label"},"type":"type"},"gadget":{"preferences":{"key":"preferences"},"iconLink":"iconLink","display":"display","link":"link","width":5,"title":"title","type":"type","height":1},"colorId":"colorId","hangoutLink":"hangoutLink","attendeesOmitted":False,"description":"description","focusTimeProperties":{"chatStatus":"chatStatus","declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"source":{"title":"title","url":"url"},"extendedProperties":{"shared":{"key":"shared"},"private":{"key":"private"}},"guestsCanModify":False,"recurringEventId":"recurringEventId","endTimeUnspecified":False,"guestsCanSeeOtherGuests":True,"end":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"id":"id","locked":False,"anyoneCanAddSelf":False,"summary":"summary","creator":{"displayName":"displayName","self":False,"id":"id","email":"email"},"privateCopy":False,"visibility":"default","attendees":[{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"},{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"}],"created":"2000-01-23T04:56:07.000+00:00","htmlLink":"htmlLink","kind":"calendar#event","iCalUID":"iCalUID","start":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"originalStartTime":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"eventType":"default","recurrence":["recurrence","recurrence"],"sequence":5,"organizer":{"displayName":"displayName","self":False,"id":"id","email":"email"},"transparency":"opaque","conferenceData":{"entryPoints":[{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"},{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"}],"notes":"notes","conferenceId":"conferenceId","createRequest":{"requestId":"requestId","conferenceSolutionKey":{"type":"type"},"status":{"statusCode":"statusCode"}},"signature":"signature","conferenceSolution":{"name":"name","iconUri":"iconUri","key":{"type":"type"}},"parameters":{"addOnParameters":{"parameters":{"key":"parameters"}}}},"etag":"etag","location":"location","guestsCanInviteOthers":True,"outOfOfficeProperties":{"declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"updated":"2000-01-23T04:56:07.000+00:00","status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('conferenceDataVersion', 56),
                    ('maxAttendees', 56),
                    ('sendNotifications', True),
                    ('sendUpdates', 'send_updates_example'),
                    ('supportsAttachments', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/calendars/{calendar_id}/events'.format(calendar_id='calendar_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_instances(client):
    """Test case for calendar_events_instances

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('alwaysIncludeEmail', True),
                    ('maxAttendees', 56),
                    ('maxResults', 56),
                    ('originalStart', 'original_start_example'),
                    ('pageToken', 'page_token_example'),
                    ('showDeleted', True),
                    ('timeMax', 'time_max_example'),
                    ('timeMin', 'time_min_example'),
                    ('timeZone', 'time_zone_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar/v3/calendars/{calendar_id}/events/{event_id}/instances'.format(calendar_id='calendar_id_example', event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_list(client):
    """Test case for calendar_events_list

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('alwaysIncludeEmail', True),
                    ('eventTypes', ['event_types_example']),
                    ('iCalUID', 'i_cal_uid_example'),
                    ('maxAttendees', 56),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('privateExtendedProperty', ['private_extended_property_example']),
                    ('q', 'q_example'),
                    ('sharedExtendedProperty', ['shared_extended_property_example']),
                    ('showDeleted', True),
                    ('showHiddenInvitations', True),
                    ('singleEvents', True),
                    ('syncToken', 'sync_token_example'),
                    ('timeMax', 'time_max_example'),
                    ('timeMin', 'time_min_example'),
                    ('timeZone', 'time_zone_example'),
                    ('updatedMin', 'updated_min_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendar/v3/calendars/{calendar_id}/events'.format(calendar_id='calendar_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_move(client):
    """Test case for calendar_events_move

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('destination', 'destination_example'),
                    ('sendNotifications', True),
                    ('sendUpdates', 'send_updates_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/calendars/{calendar_id}/events/{event_id}/move'.format(calendar_id='calendar_id_example', event_id='event_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_patch(client):
    """Test case for calendar_events_patch

    
    """
    body = {"reminders":{"overrides":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"useDefault":True},"attachments":[{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"},{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"}],"workingLocationProperties":{"officeLocation":{"floorId":"floorId","floorSectionId":"floorSectionId","label":"label","deskId":"deskId","buildingId":"buildingId"},"homeOffice":"","customLocation":{"label":"label"},"type":"type"},"gadget":{"preferences":{"key":"preferences"},"iconLink":"iconLink","display":"display","link":"link","width":5,"title":"title","type":"type","height":1},"colorId":"colorId","hangoutLink":"hangoutLink","attendeesOmitted":False,"description":"description","focusTimeProperties":{"chatStatus":"chatStatus","declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"source":{"title":"title","url":"url"},"extendedProperties":{"shared":{"key":"shared"},"private":{"key":"private"}},"guestsCanModify":False,"recurringEventId":"recurringEventId","endTimeUnspecified":False,"guestsCanSeeOtherGuests":True,"end":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"id":"id","locked":False,"anyoneCanAddSelf":False,"summary":"summary","creator":{"displayName":"displayName","self":False,"id":"id","email":"email"},"privateCopy":False,"visibility":"default","attendees":[{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"},{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"}],"created":"2000-01-23T04:56:07.000+00:00","htmlLink":"htmlLink","kind":"calendar#event","iCalUID":"iCalUID","start":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"originalStartTime":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"eventType":"default","recurrence":["recurrence","recurrence"],"sequence":5,"organizer":{"displayName":"displayName","self":False,"id":"id","email":"email"},"transparency":"opaque","conferenceData":{"entryPoints":[{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"},{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"}],"notes":"notes","conferenceId":"conferenceId","createRequest":{"requestId":"requestId","conferenceSolutionKey":{"type":"type"},"status":{"statusCode":"statusCode"}},"signature":"signature","conferenceSolution":{"name":"name","iconUri":"iconUri","key":{"type":"type"}},"parameters":{"addOnParameters":{"parameters":{"key":"parameters"}}}},"etag":"etag","location":"location","guestsCanInviteOthers":True,"outOfOfficeProperties":{"declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"updated":"2000-01-23T04:56:07.000+00:00","status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('alwaysIncludeEmail', True),
                    ('conferenceDataVersion', 56),
                    ('maxAttendees', 56),
                    ('sendNotifications', True),
                    ('sendUpdates', 'send_updates_example'),
                    ('supportsAttachments', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/calendar/v3/calendars/{calendar_id}/events/{event_id}'.format(calendar_id='calendar_id_example', event_id='event_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_quick_add(client):
    """Test case for calendar_events_quick_add

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('text', 'text_example'),
                    ('sendNotifications', True),
                    ('sendUpdates', 'send_updates_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/calendars/{calendar_id}/events/quickAdd'.format(calendar_id='calendar_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_update(client):
    """Test case for calendar_events_update

    
    """
    body = {"reminders":{"overrides":[{"method":"method","minutes":0},{"method":"method","minutes":0}],"useDefault":True},"attachments":[{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"},{"iconLink":"iconLink","fileUrl":"fileUrl","mimeType":"mimeType","title":"title","fileId":"fileId"}],"workingLocationProperties":{"officeLocation":{"floorId":"floorId","floorSectionId":"floorSectionId","label":"label","deskId":"deskId","buildingId":"buildingId"},"homeOffice":"","customLocation":{"label":"label"},"type":"type"},"gadget":{"preferences":{"key":"preferences"},"iconLink":"iconLink","display":"display","link":"link","width":5,"title":"title","type":"type","height":1},"colorId":"colorId","hangoutLink":"hangoutLink","attendeesOmitted":False,"description":"description","focusTimeProperties":{"chatStatus":"chatStatus","declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"source":{"title":"title","url":"url"},"extendedProperties":{"shared":{"key":"shared"},"private":{"key":"private"}},"guestsCanModify":False,"recurringEventId":"recurringEventId","endTimeUnspecified":False,"guestsCanSeeOtherGuests":True,"end":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"id":"id","locked":False,"anyoneCanAddSelf":False,"summary":"summary","creator":{"displayName":"displayName","self":False,"id":"id","email":"email"},"privateCopy":False,"visibility":"default","attendees":[{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"},{"additionalGuests":6,"resource":False,"displayName":"displayName","organizer":True,"self":False,"comment":"comment","optional":False,"id":"id","responseStatus":"responseStatus","email":"email"}],"created":"2000-01-23T04:56:07.000+00:00","htmlLink":"htmlLink","kind":"calendar#event","iCalUID":"iCalUID","start":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"originalStartTime":{"date":"2000-01-23","dateTime":"2000-01-23T04:56:07.000+00:00","timeZone":"timeZone"},"eventType":"default","recurrence":["recurrence","recurrence"],"sequence":5,"organizer":{"displayName":"displayName","self":False,"id":"id","email":"email"},"transparency":"opaque","conferenceData":{"entryPoints":[{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"},{"entryPointFeatures":["entryPointFeatures","entryPointFeatures"],"password":"password","regionCode":"regionCode","pin":"pin","entryPointType":"entryPointType","accessCode":"accessCode","meetingCode":"meetingCode","label":"label","uri":"uri","passcode":"passcode"}],"notes":"notes","conferenceId":"conferenceId","createRequest":{"requestId":"requestId","conferenceSolutionKey":{"type":"type"},"status":{"statusCode":"statusCode"}},"signature":"signature","conferenceSolution":{"name":"name","iconUri":"iconUri","key":{"type":"type"}},"parameters":{"addOnParameters":{"parameters":{"key":"parameters"}}}},"etag":"etag","location":"location","guestsCanInviteOthers":True,"outOfOfficeProperties":{"declineMessage":"declineMessage","autoDeclineMode":"autoDeclineMode"},"updated":"2000-01-23T04:56:07.000+00:00","status":"status"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('alwaysIncludeEmail', True),
                    ('conferenceDataVersion', 56),
                    ('maxAttendees', 56),
                    ('sendNotifications', True),
                    ('sendUpdates', 'send_updates_example'),
                    ('supportsAttachments', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/calendar/v3/calendars/{calendar_id}/events/{event_id}'.format(calendar_id='calendar_id_example', event_id='event_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendar_events_watch(client):
    """Test case for calendar_events_watch

    
    """
    body = {"resourceId":"resourceId","address":"address","payload":True,"kind":"api#channel","expiration":"expiration","id":"id","resourceUri":"resourceUri","params":{"key":"params"},"type":"type","token":"token"}
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('alwaysIncludeEmail', True),
                    ('eventTypes', ['event_types_example']),
                    ('iCalUID', 'i_cal_uid_example'),
                    ('maxAttendees', 56),
                    ('maxResults', 56),
                    ('orderBy', 'order_by_example'),
                    ('pageToken', 'page_token_example'),
                    ('privateExtendedProperty', ['private_extended_property_example']),
                    ('q', 'q_example'),
                    ('sharedExtendedProperty', ['shared_extended_property_example']),
                    ('showDeleted', True),
                    ('showHiddenInvitations', True),
                    ('singleEvents', True),
                    ('syncToken', 'sync_token_example'),
                    ('timeMax', 'time_max_example'),
                    ('timeMin', 'time_min_example'),
                    ('timeZone', 'time_zone_example'),
                    ('updatedMin', 'updated_min_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/calendar/v3/calendars/{calendar_id}/events/watch'.format(calendar_id='calendar_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

