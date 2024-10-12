# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.merchant_session import MerchantSession
from openapi_server.models.session import Session
from openapi_server.models.session_create import SessionCreate
from openapi_server.models.session_read import SessionRead


pytestmark = pytest.mark.asyncio

async def test_create_credit_session(client):
    """Test case for create_credit_session

    Create a new payment session
    """
    body = openapi_server.SessionCreate()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/payments/v1/sessions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_credit_session(client):
    """Test case for read_credit_session

    Read an existing payment session
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/payments/v1/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_credit_session(client):
    """Test case for update_credit_session

    Update an existing payment session
    """
    body = openapi_server.Session()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/payments/v1/sessions/{session_id}'.format(session_id='session_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

