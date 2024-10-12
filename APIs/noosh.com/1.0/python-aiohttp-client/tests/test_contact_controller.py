# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.contacts_list_vo import ContactsListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.user_details_expand_vo import UserDetailsExpandVO


pytestmark = pytest.mark.asyncio

async def test_get_billing_recipients(client):
    """Test case for get_billing_recipients

    List Billing Recipients
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/billingRecipients'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_list(client):
    """Test case for get_contact_list

    List the contacts
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/contacts'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contact_user_info(client):
    """Test case for get_contact_user_info

    Contact Info
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/contacts/{user_id}'.format(workgroup_id='workgroup_id_example', user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

