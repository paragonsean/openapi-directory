# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activities_filter import ActivitiesFilter
from openapi_server.models.activity import Activity
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_activity_response import CreateActivityResponse
from openapi_server.models.delete_activity_response import DeleteActivityResponse
from openapi_server.models.get_activities_response import GetActivitiesResponse
from openapi_server.models.get_activity_response import GetActivityResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_activity_response import UpdateActivityResponse


pytestmark = pytest.mark.asyncio

async def test_activities_add(client):
    """Test case for activities_add

    Create activity
    """
    body = {"video_conference_url":"https://us02web.zoom.us/j/88120759396","end_datetime":"2021-05-01T12:30:00.000Z","start_datetime":"2021-05-01T12:00:00.000Z","contract_id":"12345","owner_id":"12345","asset_id":"12345","all_day_event":False,"show_as":"busy","type":"meeting","solution_id":"12345","custom_mappings":"{}","product_id":"12345","case_id":"12345","downstream_id":"12345","id":"12345","recurrent":False,"campaign_id":"12345","location_address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"attendees":[{"prefix":"Mr.","created_at":"2017-08-12T20:43:21.291Z","is_organizer":True,"last_name":"Musk","contact_id":"12345","middle_name":"D.","suffix":"PhD","email_address":"elon@musk.com","updated_at":"2017-08-12T20:43:21.291Z","user_id":"12345","name":"Elon Musk","id":"12345","first_name":"Elon","status":"accepted"},{"prefix":"Mr.","created_at":"2017-08-12T20:43:21.291Z","is_organizer":True,"last_name":"Musk","contact_id":"12345","middle_name":"D.","suffix":"PhD","email_address":"elon@musk.com","updated_at":"2017-08-12T20:43:21.291Z","user_id":"12345","name":"Elon Musk","id":"12345","first_name":"Elon","status":"accepted"}],"custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"event_sub_type":"debrief","reminder_datetime":"2021-05-01T17:00:00.000Z","created_by":"12345","done":False,"group_event":True,"opportunity_id":"12345","user_id":"12345","updated_by":"12345","video_conference_id":"zoom:88120759396","activity_datetime":"2021-05-01T12:00:00.000Z","child":False,"reminder_set":False,"end_date":"2021-05-01","note":"An internal note about the meeting","custom_object_id":"12345","private":True,"created_at":"2020-09-30T07:43:32.000Z","description":"More info about the meeting","group_event_type":"Proposed","contact_id":"12345","title":"Meeting","archived":False,"updated_at":"2020-09-30T07:43:32.000Z","lead_id":"12345","duration_seconds":1800,"company_id":"12345","activity_date":"2021-05-01","account_id":"12345","deleted":False,"duration_minutes":30,"location":"Space"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/crm/activities',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_all(client):
    """Test case for activities_all

    List activities
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.ActivitiesFilter()),
                    ('pass_through', None),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/activities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_delete(client):
    """Test case for activities_delete

    Delete activity
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/crm/activities/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_one(client):
    """Test case for activities_one

    Get activity
    """
    params = [('raw', False),
                    ('fields', 'id,updated_at')]
    headers = { 
        'Accept': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crm/activities/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activities_update(client):
    """Test case for activities_update

    Update activity
    """
    body = {"video_conference_url":"https://us02web.zoom.us/j/88120759396","end_datetime":"2021-05-01T12:30:00.000Z","start_datetime":"2021-05-01T12:00:00.000Z","contract_id":"12345","owner_id":"12345","asset_id":"12345","all_day_event":False,"show_as":"busy","type":"meeting","solution_id":"12345","custom_mappings":"{}","product_id":"12345","case_id":"12345","downstream_id":"12345","id":"12345","recurrent":False,"campaign_id":"12345","location_address":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"attendees":[{"prefix":"Mr.","created_at":"2017-08-12T20:43:21.291Z","is_organizer":True,"last_name":"Musk","contact_id":"12345","middle_name":"D.","suffix":"PhD","email_address":"elon@musk.com","updated_at":"2017-08-12T20:43:21.291Z","user_id":"12345","name":"Elon Musk","id":"12345","first_name":"Elon","status":"accepted"},{"prefix":"Mr.","created_at":"2017-08-12T20:43:21.291Z","is_organizer":True,"last_name":"Musk","contact_id":"12345","middle_name":"D.","suffix":"PhD","email_address":"elon@musk.com","updated_at":"2017-08-12T20:43:21.291Z","user_id":"12345","name":"Elon Musk","id":"12345","first_name":"Elon","status":"accepted"}],"custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"event_sub_type":"debrief","reminder_datetime":"2021-05-01T17:00:00.000Z","created_by":"12345","done":False,"group_event":True,"opportunity_id":"12345","user_id":"12345","updated_by":"12345","video_conference_id":"zoom:88120759396","activity_datetime":"2021-05-01T12:00:00.000Z","child":False,"reminder_set":False,"end_date":"2021-05-01","note":"An internal note about the meeting","custom_object_id":"12345","private":True,"created_at":"2020-09-30T07:43:32.000Z","description":"More info about the meeting","group_event_type":"Proposed","contact_id":"12345","title":"Meeting","archived":False,"updated_at":"2020-09-30T07:43:32.000Z","lead_id":"12345","duration_seconds":1800,"company_id":"12345","activity_date":"2021-05-01","account_id":"12345","deleted":False,"duration_minutes":30,"location":"Space"}
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_apideck_consumer_id': 'x_apideck_consumer_id_example',
        'x_apideck_app_id': 'dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX',
        'x_apideck_service_id': 'x_apideck_service_id_example',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/crm/activities/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

