# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_subject_right_cancel_delete_request_request import DataSubjectRightCancelDeleteRequestRequest
from openapi_server.models.data_subject_right_delete_request202_response import DataSubjectRightDeleteRequest202Response
from openapi_server.models.data_subject_right_delete_status_request200_response import DataSubjectRightDeleteStatusRequest200Response
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_data_subject_right_cancel_delete_request(client):
    """Test case for data_subject_right_cancel_delete_request

    
    """
    body = openapi_server.DataSubjectRightCancelDeleteRequestRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/dsr/delete/{token}/cancel'.format(token='token_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_subject_right_cancel_export_request(client):
    """Test case for data_subject_right_cancel_export_request

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/dsr/export/{token}/cancel'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_subject_right_delete_request(client):
    """Test case for data_subject_right_delete_request

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/dsr/delete',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_subject_right_delete_status_request(client):
    """Test case for data_subject_right_delete_status_request

    
    """
    params = [('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/dsr/delete/{token}'.format(token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_subject_right_export_request(client):
    """Test case for data_subject_right_export_request

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/user/dsr/export',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_subject_right_export_status_request(client):
    """Test case for data_subject_right_export_status_request

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/user/dsr/export/{token}'.format(token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

