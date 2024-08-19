# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.device_output import DeviceOutput
from openapi_server.models.family_output import FamilyOutput
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.os_output import OSOutput
from openapi_server.models.type_output import TypeOutput
from openapi_server.models.ua_collection_output import UACollectionOutput
from openapi_server.models.ua_output import UAOutput
from openapi_server.models.vendor_output import VendorOutput


pytestmark = pytest.mark.asyncio

async def test_parse_user_agent_v1_ua_user_agent_urlencoded_get(client):
    """Test case for parse_user_agent_v1_ua_user_agent_urlencoded_get

    Get the information found in an User Agent.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ua/{user_agent_urlencoded}'.format(user_agent_urlencoded='user_agent_urlencoded_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_parse_user_agents_csv_v1_ua_csv_post(client):
    """Test case for parse_user_agents_csv_v1_ua_csv_post

    Get the information found in the set of User Agents uploaded.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('csv_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/ua/csv',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_user_agents_v1_ua_post(client):
    """Test case for parse_user_agents_v1_ua_post

    Get the information found in a set of User Agents.
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/ua',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_device_by_code_v1_ua_device_code_get(client):
    """Test case for query_device_by_code_v1_ua_device_code_get

    Get the information of the device of a user agent.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ua/device/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_family_by_code_v1_ua_family_code_get(client):
    """Test case for query_family_by_code_v1_ua_family_code_get

    Get the information of the family of a user agent.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ua/family/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_os_by_code_v1_ua_os_code_get(client):
    """Test case for query_os_by_code_v1_ua_os_code_get

    Get the information of the Operating System of a user agent.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ua/os/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_type_by_code_v1_ua_type_code_get(client):
    """Test case for query_type_by_code_v1_ua_type_code_get

    Get the information of the type of a user agent.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ua/type/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_vendor_by_code_v1_ua_vendor_code_get(client):
    """Test case for query_vendor_by_code_v1_ua_vendor_code_get

    Get the information of the vendor of a user agent.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/ua/vendor/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

