# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.security_contact import SecurityContact
from openapi_server.models.security_contact_list import SecurityContactList


pytestmark = pytest.mark.asyncio

async def test_security_contacts_create(client):
    """Test case for security_contacts_create

    
    """
    security_contact = {"properties":{"phone":"phone","alertNotifications":"On","alertsToAdmins":"On","email":"email"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/securityContacts/{security_contact_name}'.format(subscription_id='subscription_id_example', security_contact_name='security_contact_name_example'),
        headers=headers,
        json=security_contact,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_contacts_delete(client):
    """Test case for security_contacts_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/securityContacts/{security_contact_name}'.format(subscription_id='subscription_id_example', security_contact_name='security_contact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_contacts_get(client):
    """Test case for security_contacts_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/securityContacts/{security_contact_name}'.format(subscription_id='subscription_id_example', security_contact_name='security_contact_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_contacts_list(client):
    """Test case for security_contacts_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/securityContacts'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_security_contacts_update(client):
    """Test case for security_contacts_update

    
    """
    security_contact = {"properties":{"phone":"phone","alertNotifications":"On","alertsToAdmins":"On","email":"email"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Security/securityContacts/{security_contact_name}'.format(subscription_id='subscription_id_example', security_contact_name='security_contact_name_example'),
        headers=headers,
        json=security_contact,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

