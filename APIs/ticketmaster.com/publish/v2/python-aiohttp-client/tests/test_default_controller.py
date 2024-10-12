# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attraction import Attraction
from openapi_server.models.augmentation_data import AugmentationData
from openapi_server.models.entitlement import Entitlement
from openapi_server.models.event import Event
from openapi_server.models.extension_data import ExtensionData
from openapi_server.models.ingestion_result import IngestionResult
from openapi_server.models.venue import Venue
from openapi_server.models.video import Video


pytestmark = pytest.mark.asyncio

async def test_patch_attraction(client):
    """Test case for patch_attraction

    Publish a patch on an attraction
    """
    body = {"score":0.8008282,"changes":[{"op":"add","path":"path","from":"from","value":"{}"},{"op":"add","path":"path","from":"from","value":"{}"}],"relatedEntityId":"relatedEntityId","relatedEntityType":"event","source":"source","versionNumber":6}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='PATCH',
        path='/publish/v2/publish/v2/attractions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_event(client):
    """Test case for patch_event

    Publish a patch on an event
    """
    body = {"score":0.8008282,"changes":[{"op":"add","path":"path","from":"from","value":"{}"},{"op":"add","path":"path","from":"from","value":"{}"}],"relatedEntityId":"relatedEntityId","relatedEntityType":"event","source":"source","versionNumber":6}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='PATCH',
        path='/publish/v2/publish/v2/events/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_venue(client):
    """Test case for patch_venue

    Publish a patch on a venue
    """
    body = {"score":0.8008282,"changes":[{"op":"add","path":"path","from":"from","value":"{}"},{"op":"add","path":"path","from":"from","value":"{}"}],"relatedEntityId":"relatedEntityId","relatedEntityType":"event","source":"source","versionNumber":6}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='PATCH',
        path='/publish/v2/publish/v2/venues/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_attraction(client):
    """Test case for publish_attraction

    Publish an attractions
    """
    body = {"additionalInfos":"en-us: additionalInfo","images":[{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"},{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"}],"references":"sourceName: id","test":False,"active":False,"source":{"name":"name","id":"id"},"type":"event","descriptions":"en-us: description","version":1,"url":"url","classifications":[{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False},{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False}],"relationships":[null,null],"names":"en-us: name","discoverable":False}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/attractions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_attraction_videos(client):
    """Test case for publish_attraction_videos

    Publish a video on an attraction
    """
    body = {"embedUrl":"embedUrl","source":{"name":"name","id":"id"},"licensingInformation":{"license":"license","regionRestriction":{"allowed":["allowed","allowed"]}},"url":"url"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/attractions/{id}/videos'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_entitlements(client):
    """Test case for publish_entitlements

    Publish entitlements on an entity
    """
    body = {"data":"{}","relatedEntityId":"relatedEntityId","relatedEntityType":"event","source":"ticketmaster","versionNumber":0,"relatedEntitySource":{"name":"name","id":"id"}}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/entitlements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_event(client):
    """Test case for publish_event

    Publish an event
    """
    body = {"venue":{"country":{"names":"en-us: name","countryCode":"countryCode"},"distance":1.4894159098541704,"references":"sourceName: id","city":{"names":"en-us: name"},"timezone":"timezone","postalCode":"postalCode","source":{"name":"name","id":"id"},"units":"units","type":"event","descriptions":"en-us: description","relationships":[null,null],"currency":"currency","state":{"names":"en-us: name","stateCode":"stateCode"},"accessibleSeatingDetails":"en-us:seatingDetails","additionalInfos":"en-us: additionalInfo","images":[{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"},{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"}],"address":{"line1s":"en-us: line1","line3s":"en-us:line3","line2s":"en-us:line2"},"test":False,"social":{"twitter":{"hashtags":"#hashtag example #hashtag another example","handle":"@a Twitter handle exampe"}},"active":False,"generalInfo":{"childRules":"en-us: rule","generalRules":"en-us: rule"},"boxOfficeInfo":{"openHoursDetails":"en-us:openHours","acceptedPaymentDetails":"en-us:paymentDetails","phoneNumberDetails":"en-us:phoneNumbers","willCallDetails":"en-us:willCall"},"version":7,"url":"url","markets":[{"id":"id"},{"id":"id"}],"names":"en-us: name","discoverable":False,"dma":[{"id":6},{"id":6}],"location":{"latitude":4.145608029883936,"longitude":7.386281948385884},"parkingDetails":"en-us:parkingDetails"},"distance":2.027123023002322,"references":"sourceName: id","publicVisibility":{"startDateTime":"2000-01-23T04:56:07.000+00:00","visible":False,"endDateTime":"2000-01-23T04:56:07.000+00:00"},"priceRanges":[{"min":1.0246457001441578,"max":1.2315135367772556,"currency":"currency","type":"standard"},{"min":1.0246457001441578,"max":1.2315135367772556,"currency":"currency","type":"standard"}],"source":{"name":"name","id":"id"},"units":"units","type":"event","descriptions":"en-us: description","sales":{"public":{"startDateTime":"2000-01-23T04:56:07.000+00:00","startTBD":False,"endDateTime":"2000-01-23T04:56:07.000+00:00"},"presales":[{"names":"en-us: name","startDateTime":"2000-01-23T04:56:07.000+00:00","endDateTime":"2000-01-23T04:56:07.000+00:00","descriptions":"en-us: description","url":"url"},{"names":"en-us: name","startDateTime":"2000-01-23T04:56:07.000+00:00","endDateTime":"2000-01-23T04:56:07.000+00:00","descriptions":"en-us: description","url":"url"}]},"relationships":[null,null],"pleaseNotes":"en-us: note","promoter":{"names":"en-us: name","id":"id","descriptions":"en-us: description"},"attractions":[{"additionalInfos":"en-us: additionalInfo","images":[{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"},{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"}],"references":"sourceName: id","test":False,"active":False,"source":{"name":"name","id":"id"},"type":"event","descriptions":"en-us: description","version":1,"url":"url","classifications":[{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False},{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False}],"relationships":[null,null],"names":"en-us: name","discoverable":False},{"additionalInfos":"en-us: additionalInfo","images":[{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"},{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"}],"references":"sourceName: id","test":False,"active":False,"source":{"name":"name","id":"id"},"type":"event","descriptions":"en-us: description","version":1,"url":"url","classifications":[{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False},{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False}],"relationships":[null,null],"names":"en-us: name","discoverable":False}],"place":{"area":{"names":"en-us: name"},"country":{"names":"en-us: name","countryCode":"countryCode"},"address":{"line1s":"en-us: line1","line3s":"en-us:line3","line2s":"en-us:line2"},"names":"en-us: name","city":{"names":"en-us: name"},"postalCode":"postalCode","location":{"latitude":4.145608029883936,"longitude":7.386281948385884},"state":{"names":"en-us: name","stateCode":"stateCode"}},"additionalInfos":"en-us: additionalInfo","images":[{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"},{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"}],"test":False,"active":False,"dates":{"access":{"startApproximate":False,"startDateTime":"2000-01-23T04:56:07.000+00:00","endApproximate":False,"endDateTime":"2000-01-23T04:56:07.000+00:00"},"timezone":"timezone","start":{"dateTime":"2000-01-23T04:56:07.000+00:00","localTime":{"fieldTypes":[{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}},{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}}],"values":[3,3],"hourOfDay":5,"chronology":{"zone":{"fixed":False,"id":"id"}},"fields":[{"minimumValue":1,"leapDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"name":"name","durationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"rangeDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"type":{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}},"maximumValue":6,"lenient":False,"supported":False},{"minimumValue":1,"leapDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"name":"name","durationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"rangeDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"type":{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}},"maximumValue":6,"lenient":False,"supported":False}],"minuteOfHour":7,"secondOfMinute":9,"millisOfDay":5,"millisOfSecond":2},"dateTBA":False,"noSpecificTime":False,"timeTBA":False,"localDate":"2000-01-23","dateTBD":False},"end":{"dateTime":"2000-01-23T04:56:07.000+00:00","localTime":{"fieldTypes":[{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}},{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}}],"values":[3,3],"hourOfDay":5,"chronology":{"zone":{"fixed":False,"id":"id"}},"fields":[{"minimumValue":1,"leapDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"name":"name","durationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"rangeDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"type":{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}},"maximumValue":6,"lenient":False,"supported":False},{"minimumValue":1,"leapDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"name":"name","durationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"rangeDurationField":{"name":"name","precise":False,"type":{"name":"name"},"unitMillis":0,"supported":False},"type":{"rangeDurationType":{"name":"name"},"name":"name","durationType":{"name":"name"}},"maximumValue":6,"lenient":False,"supported":False}],"minuteOfHour":7,"secondOfMinute":9,"millisOfDay":5,"millisOfSecond":2},"approximate":False},"status":{"code":"onsale"}},"version":1,"url":"url","classifications":[{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False},{"subGenre":{"names":{"key":"names"},"id":"id"},"segment":{"names":{"key":"names"},"id":"id"},"genre":{"names":{"key":"names"},"id":"id"},"subType":{"names":{"key":"names"},"id":"id"},"type":{"names":{"key":"names"},"id":"id"},"primary":False}],"names":"en-us: name","discoverable":False,"location":{"latitude":4.145608029883936,"longitude":7.386281948385884},"infos":"en-us: info"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/events',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_event_videos(client):
    """Test case for publish_event_videos

    Publish a video on an event
    """
    body = {"embedUrl":"embedUrl","source":{"name":"name","id":"id"},"licensingInformation":{"license":"license","regionRestriction":{"allowed":["allowed","allowed"]}},"url":"url"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/events/{id}/videos'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_extension(client):
    """Test case for publish_extension

    Publish extension on an entity
    """
    body = {"data":"{}","relatedEntityId":"relatedEntityId","relatedEntityType":"event","source":"source","type":"type","versionNumber":0,"relatedEntitySource":{"name":"name","id":"id"}}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/extensions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_venue(client):
    """Test case for publish_venue

    Publish a venue
    """
    body = {"country":{"names":"en-us: name","countryCode":"countryCode"},"distance":1.4894159098541704,"references":"sourceName: id","city":{"names":"en-us: name"},"timezone":"timezone","postalCode":"postalCode","source":{"name":"name","id":"id"},"units":"units","type":"event","descriptions":"en-us: description","relationships":[null,null],"currency":"currency","state":{"names":"en-us: name","stateCode":"stateCode"},"accessibleSeatingDetails":"en-us:seatingDetails","additionalInfos":"en-us: additionalInfo","images":[{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"},{"attribution":"attribution","width":6,"domains":["domains","domains"],"fallback":False,"url":"url","height":0,"ratio":"169"}],"address":{"line1s":"en-us: line1","line3s":"en-us:line3","line2s":"en-us:line2"},"test":False,"social":{"twitter":{"hashtags":"#hashtag example #hashtag another example","handle":"@a Twitter handle exampe"}},"active":False,"generalInfo":{"childRules":"en-us: rule","generalRules":"en-us: rule"},"boxOfficeInfo":{"openHoursDetails":"en-us:openHours","acceptedPaymentDetails":"en-us:paymentDetails","phoneNumberDetails":"en-us:phoneNumbers","willCallDetails":"en-us:willCall"},"version":7,"url":"url","markets":[{"id":"id"},{"id":"id"}],"names":"en-us: name","discoverable":False,"dma":[{"id":6},{"id":6}],"location":{"latitude":4.145608029883936,"longitude":7.386281948385884},"parkingDetails":"en-us:parkingDetails"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'tmps_correlation_id': '',
    }
    response = await client.request(
        method='POST',
        path='/publish/v2/publish/v2/venues',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

