# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call import Call
from openapi_server.models.call_create import CallCreate
from openapi_server.models.call_transfer import CallTransfer
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events_count import EventsCount


pytestmark = pytest.mark.asyncio

async def test_call_answer(client):
    """Test case for call_answer

    Answer call (On supported devices)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/t/vbc.prod/vis/v1/self/calls/{id}/answer'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call_hold(client):
    """Test case for call_hold

    Put call on hold
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/t/vbc.prod/vis/v1/self/calls/{id}/hold'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call_transfer(client):
    """Test case for call_transfer

    Transfer call
    """
    body = {"phoneNumber":"phoneNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/t/vbc.prod/vis/v1/self/calls/{id}/transfer'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call_unold(client):
    """Test case for call_unold

    Unhold
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/t/vbc.prod/vis/v1/self/calls/{id}/hold'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call_vm_transfer(client):
    """Test case for call_vm_transfer

    Send call to voicemail
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/t/vbc.prod/vis/v1/self/calls/{id}/vmtransfer'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_call(client):
    """Test case for create_call

    Place a call
    """
    body = {"phoneNumber":"phoneNumber"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/t/vbc.prod/vis/v1/self/calls',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_call(client):
    """Test case for destroy_call

    End a call
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/t/vbc.prod/vis/v1/self/calls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_calls_count(client):
    """Test case for get_calls_count

    Get calls count
    """
    params = [('fromDate', 56),
                    ('toDate', 56),
                    ('direction', 'INBOUND,OUTBOUND'),
                    ('states', ACTIVE)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/calls/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_roles(client):
    """Test case for get_roles

    Get a call
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/calls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_calls(client):
    """Test case for list_calls

    List active calls
    """
    params = [('fromDate', 56),
                    ('toDate', 56),
                    ('direction', 'INBOUND,OUTBOUND'),
                    ('states', ACTIVE),
                    ('offset', 56),
                    ('size', 20),
                    ('order', ASC),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/vis/v1/self/calls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

