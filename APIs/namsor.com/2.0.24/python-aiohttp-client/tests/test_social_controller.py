# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_first_last_name_phone_coded_out import BatchFirstLastNamePhoneCodedOut
from openapi_server.models.batch_first_last_name_phone_number_geo_in import BatchFirstLastNamePhoneNumberGeoIn
from openapi_server.models.batch_first_last_name_phone_number_in import BatchFirstLastNamePhoneNumberIn
from openapi_server.models.first_last_name_phone_coded_out import FirstLastNamePhoneCodedOut


pytestmark = pytest.mark.asyncio

async def test_phone_code(client):
    """Test case for phone_code

    [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, given a personal name and formatted / unformatted phone number.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/phoneCode/{first_name}/{last_name}/{phone_number}'.format(first_name='first_name_example', last_name='last_name_example', phone_number='phone_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phone_code_batch(client):
    """Test case for phone_code_batch

    [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, detecting automatically the local context given a name and formatted / unformatted phone number.
    """
    body = {"personalNamesWithPhoneNumbers":[{"firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","id":"id"},{"firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/phoneCodeBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phone_code_geo(client):
    """Test case for phone_code_geo

    [USES 11 UNITS PER NAME] Infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/phoneCodeGeo/{first_name}/{last_name}/{phone_number}/{country_iso2}'.format(first_name='first_name_example', last_name='last_name_example', phone_number='phone_number_example', country_iso2='country_iso2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phone_code_geo_batch(client):
    """Test case for phone_code_geo_batch

    [USES 11 UNITS PER NAME] Infer the likely country and phone prefix, of up to 100 personal names, with a local context (ISO2 country of residence).
    """
    body = {"personalNamesWithPhoneNumbers":[{"firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","countryIso2Alt":"countryIso2Alt","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","phoneNumber":"phoneNumber","countryIso2Alt":"countryIso2Alt","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/phoneCodeGeoBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_phone_code_geo_feedback_loop(client):
    """Test case for phone_code_geo_feedback_loop

    [CREDITS 1 UNIT] Feedback loop to better infer the likely phone prefix, given a personal name and formatted / unformatted phone number, with a local context (ISO2 country of residence).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/phoneCodeGeoFeedbackLoop/{first_name}/{last_name}/{phone_number}/{phone_number_e164}/{country_iso2}'.format(first_name='first_name_example', last_name='last_name_example', phone_number='phone_number_example', phone_number_e164='phone_number_e164_example', country_iso2='country_iso2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

