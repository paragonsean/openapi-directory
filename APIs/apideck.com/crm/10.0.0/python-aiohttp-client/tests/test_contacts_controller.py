# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.contact import Contact
from openapi_server.models.contacts_filter import ContactsFilter
from openapi_server.models.contacts_sort import ContactsSort
from openapi_server.models.create_contact_response import CreateContactResponse
from openapi_server.models.delete_contact_response import DeleteContactResponse
from openapi_server.models.get_contact_response import GetContactResponse
from openapi_server.models.get_contacts_response import GetContactsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_contact_response import UpdateContactResponse


pytestmark = pytest.mark.asyncio

async def test_contacts_add(client):
    """Test case for contacts_add

    Create contact
    """
    body = {"birthday":"2000-08-12","addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"gender":"female","owner_id":"54321","prefix":"Mr.","social_links":[{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"},{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"}],"lead_source":"Cold Call","created_at":"2017-08-12T20:43:21.291Z","description":"Internal champion","first_call_at":"2020-09-30T07:43:32Z","language":"EN","suffix":"PhD","title":"CEO","type":"personal","custom_mappings":"{}","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"updated_at":"2017-08-12T20:43:21.291Z","last_activity_at":"2020-09-30T07:43:32Z","current_balance":10.5,"first_email_at":"2020-09-30T07:43:32Z","id":"12345","photo_url":"https://unavatar.io/elon-musk","department":"Engineering","fax":"+12129876543","first_name":"Elon","lead_id":"34567","image":"https://unavatar.io/elon-musk","company_id":"23456","custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"active":True,"last_name":"Musk","middle_name":"D.","tags":["New"],"phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"company_name":"23456","name":"Elon Musk","email_domain":"gmail.com","websites":[{"id":"12345","type":"primary","url":"http://example.com"},{"id":"12345","type":"primary","url":"http://example.com"}],"status":"open"}
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
        path='/crm/contacts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_all(client):
    """Test case for contacts_all

    List contacts
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.ContactsFilter()),
                    ('sort', openapi_server.ContactsSort()),
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
        path='/crm/contacts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_delete(client):
    """Test case for contacts_delete

    Delete contact
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
        path='/crm/contacts/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_one(client):
    """Test case for contacts_one

    Get contact
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
        path='/crm/contacts/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contacts_update(client):
    """Test case for contacts_update

    Update contact
    """
    body = {"birthday":"2000-08-12","addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"gender":"female","owner_id":"54321","prefix":"Mr.","social_links":[{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"},{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"}],"lead_source":"Cold Call","created_at":"2017-08-12T20:43:21.291Z","description":"Internal champion","first_call_at":"2020-09-30T07:43:32Z","language":"EN","suffix":"PhD","title":"CEO","type":"personal","custom_mappings":"{}","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"updated_at":"2017-08-12T20:43:21.291Z","last_activity_at":"2020-09-30T07:43:32Z","current_balance":10.5,"first_email_at":"2020-09-30T07:43:32Z","id":"12345","photo_url":"https://unavatar.io/elon-musk","department":"Engineering","fax":"+12129876543","first_name":"Elon","lead_id":"34567","image":"https://unavatar.io/elon-musk","company_id":"23456","custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"active":True,"last_name":"Musk","middle_name":"D.","tags":["New"],"phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"company_name":"23456","name":"Elon Musk","email_domain":"gmail.com","websites":[{"id":"12345","type":"primary","url":"http://example.com"},{"id":"12345","type":"primary","url":"http://example.com"}],"status":"open"}
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
        path='/crm/contacts/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

