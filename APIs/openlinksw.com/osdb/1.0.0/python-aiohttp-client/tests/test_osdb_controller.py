# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_help_response import ActionHelpResponse
from openapi_server.models.describe_action_response import DescribeActionResponse
from openapi_server.models.describe_service_response import DescribeServiceResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.exec_body import ExecBody
from openapi_server.models.list_actions_response import ListActionsResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.load_service200_response import LoadService200Response
from openapi_server.models.load_service_request import LoadServiceRequest
from openapi_server.models.login_response import LoginResponse
from openapi_server.models.logout_response import LogoutResponse


pytestmark = pytest.mark.asyncio

async def test_action_help(client):
    """Test case for action_help

    Action help
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/actions/{service_id}/{action_id}/help'.format(service_id='service_id_example', action_id='action_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_action(client):
    """Test case for describe_action

    Describe action
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/actions/{service_id}/{action_id}'.format(service_id='service_id_example', action_id='action_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_service(client):
    """Test case for describe_service

    Describe service
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_execute_action(client):
    """Test case for execute_action

    Execute action
    """
    body = {"osdb:response_format":"osdb:response_format","action_specific_property1":"action_specific_property1","osdb:body_data_src_url":"https://openapi-generator.tech","action_specific_property2":"action_specific_property2","osdb:body_data_encoding":"osdb:body_data_encoding","osdb:output_type":"url_only","osdb:body_data_raw":"osdb:body_data_raw"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/osdb/api/v1/actions/{service_id}/{action_id}/exec'.format(service_id='service_id_example', action_id='action_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_actions(client):
    """Test case for list_actions

    List actions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/actions/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_services(client):
    """Test case for list_services

    List services
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/services',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_load_service(client):
    """Test case for load_service

    Load service
    """
    body = {"service_description_url":"http://ods-qa.openlinksw.com:8896/DAV/home/nobody/csv_extractor_svc.ods-qa.170109.ttl","service_moniker":"csv_extractor"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/osdb/api/v1/services',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_login(client):
    """Test case for login

    Login
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/login',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logout(client):
    """Test case for logout

    Logout
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/osdb/api/v1/logout',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unload_service(client):
    """Test case for unload_service

    Unload service
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/osdb/api/v1/services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

