# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_employee_response import CreateEmployeeResponse
from openapi_server.models.delete_employee_response import DeleteEmployeeResponse
from openapi_server.models.employee import Employee
from openapi_server.models.employees_filter import EmployeesFilter
from openapi_server.models.employees_sort import EmployeesSort
from openapi_server.models.get_employee_response import GetEmployeeResponse
from openapi_server.models.get_employees_response import GetEmployeesResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_employee_response import UpdateEmployeeResponse


pytestmark = pytest.mark.asyncio

async def test_employees_add(client):
    """Test case for employees_add

    Create Employee
    """
    body = {"addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"direct_reports":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"employment_role":{"sub_type":"full_time","type":"contractor"},"nationalities":["US","US"],"probation_period":{"end_date":"2021-11-28","start_date":"2021-10-01"},"source":"lever","custom_mappings":"{}","division":"Europe","id":"12345","photo_url":"https://unavatar.io/elon-musk","compensations":[{"effective_date":"2021-06-11","flsa_status":"nonexempt","id":"3404301363494309004","job_id":"3490439050957906679","payment_unit":"hour","rate":50},{"effective_date":"2021-06-11","flsa_status":"nonexempt","id":"3404301363494309004","job_id":"3490439050957906679","payment_unit":"hour","rate":50}],"employment_start_date":"2021-10-26","custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"initials":"EM","division_id":"12345","display_name":"Technoking","created_by":"12345","tax_id":"234-32-0000","tags":["New"],"company_name":"SpaceX","updated_by":"12345","employee_number":"123456-AB","pronouns":"she,her","salutation":"Mr","preferred_name":"Elon Musk","birthday":"2000-08-12","ethnicity":"African American","gender":"male","social_links":[{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"},{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"}],"timezone":"Europe/London","created_at":"2020-09-30T07:43:32Z","description":"A description","title":"CEO","works_remote":True,"employment_end_date":"2028-10-26","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"dietary_preference":"Veggie","record_url":"https://app.intercom.io/contacts/12345","food_allergies":["No allergies"],"updated_at":"2020-09-30T07:43:32Z","country_of_birth":"US","social_security_number":"123456789","employment_status":"active","department":"R&D","first_name":"Elon","preferred_language":"EN","deceased_on":"2000-08-12","company_id":"23456","languages":["EN","EN"],"manager":{"name":"Elon Musk","last_name":"Musk","employment_status":"active","id":"12345","first_name":"Elon","email":"elon@musk.com"},"department_id":"12345","department_name":"12345","jobs":[{"end_date":"2020-08-12","role":"Sales","compensation_rate":72000,"is_primary":True,"employee_id":"12345","currency":"USD","location":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"id":"12345","payment_unit":"year","title":"CEO","hired_at":"2020-08-12","start_date":"2020-08-12"},{"end_date":"2020-08-12","role":"Sales","compensation_rate":72000,"is_primary":True,"employee_id":"12345","currency":"USD","location":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"id":"12345","payment_unit":"year","title":"CEO","hired_at":"2020-08-12","start_date":"2020-08-12"}],"last_name":"Musk","team":{"name":"Full Stack Engineers","id":"1234"},"middle_name":"D.","phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"marital_status":"married","tax_code":"1111","deleted":True,"partner":{"birthday":"2000-08-12","gender":"male","initials":"EM","last_name":"Musk","id":"12345","middle_name":"D.","first_name":"Elon","custom_mappings":"{}","deceased_on":"2000-08-12"},"row_version":"1-12345","bank_accounts":[{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"},{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"}],"source_id":"12345","leaving_reason":"resigned"}
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
        path='/hris/employees',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_employees_all(client):
    """Test case for employees_all

    List Employees
    """
    params = [('raw', False),
                    ('cursor', 'cursor_example'),
                    ('limit', 20),
                    ('filter', openapi_server.EmployeesFilter()),
                    ('sort', openapi_server.EmployeesSort()),
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
        path='/hris/employees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_employees_delete(client):
    """Test case for employees_delete

    Delete Employee
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
        path='/hris/employees/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_employees_one(client):
    """Test case for employees_one

    Get Employee
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
        path='/hris/employees/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_employees_update(client):
    """Test case for employees_update

    Update Employee
    """
    body = {"addresses":[{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"}],"direct_reports":["a0d636c6-43b3-4bde-8c70-85b707d992f4","a98lfd96-43b3-4bde-8c70-85b707d992e6"],"employment_role":{"sub_type":"full_time","type":"contractor"},"nationalities":["US","US"],"probation_period":{"end_date":"2021-11-28","start_date":"2021-10-01"},"source":"lever","custom_mappings":"{}","division":"Europe","id":"12345","photo_url":"https://unavatar.io/elon-musk","compensations":[{"effective_date":"2021-06-11","flsa_status":"nonexempt","id":"3404301363494309004","job_id":"3490439050957906679","payment_unit":"hour","rate":50},{"effective_date":"2021-06-11","flsa_status":"nonexempt","id":"3404301363494309004","job_id":"3490439050957906679","payment_unit":"hour","rate":50}],"employment_start_date":"2021-10-26","custom_fields":[{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"},{"name":"employee_level","description":"Employee Level","id":"2389328923893298","value":"Uses Salesforce and Marketo"}],"initials":"EM","division_id":"12345","display_name":"Technoking","created_by":"12345","tax_id":"234-32-0000","tags":["New"],"company_name":"SpaceX","updated_by":"12345","employee_number":"123456-AB","pronouns":"she,her","salutation":"Mr","preferred_name":"Elon Musk","birthday":"2000-08-12","ethnicity":"African American","gender":"male","social_links":[{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"},{"id":"12345","type":"twitter","url":"https://www.twitter.com/apideck"}],"timezone":"Europe/London","created_at":"2020-09-30T07:43:32Z","description":"A description","title":"CEO","works_remote":True,"employment_end_date":"2028-10-26","emails":[{"id":"123","type":"primary","email":"elon@musk.com"},{"id":"123","type":"primary","email":"elon@musk.com"}],"dietary_preference":"Veggie","record_url":"https://app.intercom.io/contacts/12345","food_allergies":["No allergies"],"updated_at":"2020-09-30T07:43:32Z","country_of_birth":"US","social_security_number":"123456789","employment_status":"active","department":"R&D","first_name":"Elon","preferred_language":"EN","deceased_on":"2000-08-12","company_id":"23456","languages":["EN","EN"],"manager":{"name":"Elon Musk","last_name":"Musk","employment_status":"active","id":"12345","first_name":"Elon","email":"elon@musk.com"},"department_id":"12345","department_name":"12345","jobs":[{"end_date":"2020-08-12","role":"Sales","compensation_rate":72000,"is_primary":True,"employee_id":"12345","currency":"USD","location":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"id":"12345","payment_unit":"year","title":"CEO","hired_at":"2020-08-12","start_date":"2020-08-12"},{"end_date":"2020-08-12","role":"Sales","compensation_rate":72000,"is_primary":True,"employee_id":"12345","currency":"USD","location":{"country":"US","contact_name":"Elon Musk","website":"https://elonmusk.com","line4":"delivery instructions","notes":"Address notes or delivery instructions.","string":"25 Spring Street, Blackburn, VIC 3130","city":"San Francisco","latitude":"40.759211","county":"Santa Clara","type":"primary","row_version":"1-12345","name":"HQ US","street_number":"25","phone_number":"111-111-1111","id":"123","salutation":"Mr","state":"CA","fax":"122-111-1111","line3":"Suite #","postal_code":"94104","line2":"apt #","email":"elon@musk.com","line1":"Main street","longitude":"-73.984638"},"id":"12345","payment_unit":"year","title":"CEO","hired_at":"2020-08-12","start_date":"2020-08-12"}],"last_name":"Musk","team":{"name":"Full Stack Engineers","id":"1234"},"middle_name":"D.","phone_numbers":[{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"},{"country_code":"1","number":"111-111-1111","extension":"105","area_code":"323","id":"12345","type":"primary"}],"marital_status":"married","tax_code":"1111","deleted":True,"partner":{"birthday":"2000-08-12","gender":"male","initials":"EM","last_name":"Musk","id":"12345","middle_name":"D.","first_name":"Elon","custom_mappings":"{}","deceased_on":"2000-08-12"},"row_version":"1-12345","bank_accounts":[{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"},{"bsb_number":"062-001","account_number":"123465","bank_code":"BNH","account_type":"credit_card","account_name":"SPACEX LLC","iban":"CH2989144532982975332","bank_name":"Monzo","currency":"USD","routing_number":"012345678","bic":"AUDSCHGGXXX","branch_identifier":"001"}],"source_id":"12345","leaving_reason":"resigned"}
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
        path='/hris/employees/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

