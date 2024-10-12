# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_public_v1_user_user_contact_methods_get200_response import ApiPublicV1UserUserContactMethodsGet200Response
from openapi_server.models.contact_device import ContactDevice
from openapi_server.models.contact_device_add import ContactDeviceAdd
from openapi_server.models.contact_email_add import ContactEmailAdd
from openapi_server.models.contact_phone_add import ContactPhoneAdd
from openapi_server.models.user_contact import UserContact


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_devices_contact_id_delete(client):
    """Test case for api_public_v1_user_user_contact_methods_devices_contact_id_delete

    Delete a contact device for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/user/{user}/contact-methods/devices/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_devices_contact_id_get(client):
    """Test case for api_public_v1_user_user_contact_methods_devices_contact_id_get

    Get the indicated contact device for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods/devices/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_user_user_contact_methods_devices_contact_id_put(client):
    """Test case for api_public_v1_user_user_contact_methods_devices_contact_id_put

    Update a contact device for a user
    """
    body = openapi_server.ContactDeviceAdd()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/api-public/v1/user/{user}/contact-methods/devices/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_devices_get(client):
    """Test case for api_public_v1_user_user_contact_methods_devices_get

    Get a list of all contact devices for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods/devices'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_emails_contact_id_delete(client):
    """Test case for api_public_v1_user_user_contact_methods_emails_contact_id_delete

    Delete a contact email for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/user/{user}/contact-methods/emails/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_emails_contact_id_get(client):
    """Test case for api_public_v1_user_user_contact_methods_emails_contact_id_get

    Get the indicated contact email for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods/emails/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_emails_get(client):
    """Test case for api_public_v1_user_user_contact_methods_emails_get

    Get a list of all contact emails for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods/emails'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_user_user_contact_methods_emails_post(client):
    """Test case for api_public_v1_user_user_contact_methods_emails_post

    Create a contact emails for a user
    """
    body = openapi_server.ContactEmailAdd()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/user/{user}/contact-methods/emails'.format(user='user_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_get(client):
    """Test case for api_public_v1_user_user_contact_methods_get

    Get a list of all contact methods for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_phones_contact_id_delete(client):
    """Test case for api_public_v1_user_user_contact_methods_phones_contact_id_delete

    Delete a contact phone for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/api-public/v1/user/{user}/contact-methods/phones/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_phones_contact_id_get(client):
    """Test case for api_public_v1_user_user_contact_methods_phones_contact_id_get

    Get the indicated contact phone for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods/phones/{contact_id}'.format(user='user_example', contact_id='contact_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_public_v1_user_user_contact_methods_phones_get(client):
    """Test case for api_public_v1_user_user_contact_methods_phones_get

    Get a list of all contact phones for a user
    """
    headers = { 
        'Accept': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api-public/v1/user/{user}/contact-methods/phones'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_api_public_v1_user_user_contact_methods_phones_post(client):
    """Test case for api_public_v1_user_user_contact_methods_phones_post

    Create a contact phones for a user
    """
    body = openapi_server.ContactPhoneAdd()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_vo_api_id': 'x_vo_api_id_example',
        'x_vo_api_key': 'x_vo_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/api-public/v1/user/{user}/contact-methods/phones'.format(user='user_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

