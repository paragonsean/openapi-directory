# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.applicant import Applicant
from openapi_server.models.applicants_filter import ApplicantsFilter
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_applicant_response import CreateApplicantResponse
from openapi_server.models.delete_applicant_response import DeleteApplicantResponse
from openapi_server.models.get_applicant_response import GetApplicantResponse
from openapi_server.models.get_applicants_response import GetApplicantsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_applicant_response import UpdateApplicantResponse


pytestmark = pytest.mark.asyncio

async def test_applicants_add(client):
    """Test case for applicants_add

    Create Applicant
    """
    body = {"birthday":"2000-08-12","addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"sources":["Job site"],"owner_id":"54321","social_links":[{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"},{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"}],"anonymized":True,"created_at":"2020-09-30T07:43:32Z","deleted_by":"12345","title":"CEO","custom_mappings":"{}","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"archived":False,"cover_letter":"I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...","record_url":"https://app.intercom.io/contacts/12345","updated_at":"2020-09-30T07:43:32Z","id":"12345","photo_url":"https://unavatar.io/elon-musk","first_name":"Elon","headline":"PepsiCo, Inc, Central Perk","confidential":False,"rejected_at":"2020-09-30T07:43:32Z","application_ids":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"initials":"EM","stage_id":"12345","last_name":"Musk","sourced_by":"12345","recruiter_id":"12345","middle_name":"D.","created_by":"12345","deleted_at":"2020-09-30T07:43:32Z","tags":["New"],"phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"deleted":True,"followers":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"last_interaction_at":"2020-09-30T07:43:32Z","cv_url":"https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/36615291/pdf_cv_38swhu4w42k1.pdf?response-content-disposition=inline&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYHB7CA5RLR4Y3ON%2F20220514%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20220514T235654Z&X-Amz-Expires=36000&X-Amz-SignedHeaders=host&X-Amz-Signature=72c0621f5976db75b54de487eb821a8e73480d7f2a6a4a9713ab997944b0561f","name":"Elon Musk","updated_by":"12345","websites":[{"id":"12345","type":"primary","url":"http://example.com"},{"id":"12345","type":"primary","url":"http://example.com"}],"source_id":"12345","coordinator_id":"12345","job_url":"https://democompany.recruitee.com/o/example-talent-pool","applications":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"position_id":"123"}
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
        path='/ats/applicants',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applicants_all(client):
    """Test case for applicants_all

    List Applicants
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.ApplicantsFilter()),
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
        path='/ats/applicants',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applicants_delete(client):
    """Test case for applicants_delete

    Delete Applicant
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
        path='/ats/applicants/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applicants_one(client):
    """Test case for applicants_one

    Get Applicant
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
        path='/ats/applicants/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applicants_update(client):
    """Test case for applicants_update

    Update Applicant
    """
    body = {"birthday":"2000-08-12","addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"sources":["Job site"],"owner_id":"54321","social_links":[{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"},{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"}],"anonymized":True,"created_at":"2020-09-30T07:43:32Z","deleted_by":"12345","title":"CEO","custom_mappings":"{}","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"archived":False,"cover_letter":"I submit this application to express my sincere interest in the API developer position. In the previous role, I was responsible for leadership and ...","record_url":"https://app.intercom.io/contacts/12345","updated_at":"2020-09-30T07:43:32Z","id":"12345","photo_url":"https://unavatar.io/elon-musk","first_name":"Elon","headline":"PepsiCo, Inc, Central Perk","confidential":False,"rejected_at":"2020-09-30T07:43:32Z","application_ids":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"initials":"EM","stage_id":"12345","last_name":"Musk","sourced_by":"12345","recruiter_id":"12345","middle_name":"D.","created_by":"12345","deleted_at":"2020-09-30T07:43:32Z","tags":["New"],"phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"deleted":True,"followers":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"last_interaction_at":"2020-09-30T07:43:32Z","cv_url":"https://recruitee-main.s3.eu-central-1.amazonaws.com/candidates/36615291/pdf_cv_38swhu4w42k1.pdf?response-content-disposition=inline&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYHB7CA5RLR4Y3ON%2F20220514%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20220514T235654Z&X-Amz-Expires=36000&X-Amz-SignedHeaders=host&X-Amz-Signature=72c0621f5976db75b54de487eb821a8e73480d7f2a6a4a9713ab997944b0561f","name":"Elon Musk","updated_by":"12345","websites":[{"id":"12345","type":"primary","url":"http://example.com"},{"id":"12345","type":"primary","url":"http://example.com"}],"source_id":"12345","coordinator_id":"12345","job_url":"https://democompany.recruitee.com/o/example-talent-pool","applications":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"position_id":"123"}
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
        path='/ats/applicants/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

