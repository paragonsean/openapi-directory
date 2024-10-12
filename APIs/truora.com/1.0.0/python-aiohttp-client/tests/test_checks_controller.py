# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_details_output import CheckDetailsOutput
from openapi_server.models.check_output import CheckOutput
from openapi_server.models.checks_output import ChecksOutput
from openapi_server.models.database import Database
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_check(client):
    """Test case for create_check

    Create a background check
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'truora_priority': 'truora_priority_example',
        'api-key': 'special-key',
    }
    data = {
        'birth_certificate': 'birth_certificate_example',
        'company_name': 'company_name_example',
        'country': 'country_example',
        'date_of_birth': '2013-10-20',
        'diplomatic_id': 'diplomatic_id_example',
        'driver_license': 'driver_license_example',
        'escrow': 'escrow_example',
        'first_name': 'first_name_example',
        'force_creation': True,
        'foreign_id': 'foreign_id_example',
        'issue_date': '2013-10-20',
        'last_name': 'last_name_example',
        'license_plate': 'license_plate_example',
        'national_id': 'national_id_example',
        'native_country': 'native_country_example',
        'owner_document_id': 'owner_document_id_example',
        'owner_document_type': 'owner_document_type_example',
        'passport': 'passport_example',
        'payment_date': '2013-10-20',
        'pep': 'pep_example',
        'phone_number': 'phone_number_example',
        'professional_card': 'professional_card_example',
        'ptp': 'ptp_example',
        'region': 'region_example',
        'report_id': 'report_id_example',
        'state_id': 'state_id_example',
        'tax_id': 'tax_id_example',
        'type': 'type_example',
        'user_authorized': True,
        'vehicle_id': 'vehicle_id_example',
        'verification_code': 'verification_code_example',
        'watch': 'watch_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/checks',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_check(client):
    """Test case for get_check

    Get Background Check
    """
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/checks/{check_id}'.format(check_id='check_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health_dashboard(client):
    """Test case for get_health_dashboard

    Get Health Dashboard
    """
    params = [('country', 'country_example'),
                    ('unixTimestampSeconds', 'unix_timestamp_seconds_example'),
                    ('unixtimezoneOffsetSeconds', 'unixtimezone_offset_seconds_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/checks/health',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_check_details(client):
    """Test case for list_check_details

    List Check Details
    """
    params = [('start_key', 'start_key_example'),
                    ('lang', 'lang_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/checks/{check_id}/details'.format(check_id='check_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_checks(client):
    """Test case for list_checks

    List Checks
    """
    params = [('start_key', 'start_key_example'),
                    ('report_id', 'report_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/checks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

