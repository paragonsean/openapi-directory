# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.offering_user import OfferingUser
from openapi_server.models.offering_user_add_response import OfferingUserAddResponse
from openapi_server.models.offering_user_response import OfferingUserResponse
from openapi_server.models.offerings_offering_id_users_post207_response_inner import OfferingsOfferingIdUsersPost207ResponseInner
from openapi_server.models.transfer_request import TransferRequest


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_get(client):
    """Test case for offerings_offering_id_users_get

    Find offering's users
    """
    params = [('facilitators', true),
                    ('learners', true),
                    ('markers', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/users'.format(offering_id='offering_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_marker_email_marks_delete(client):
    """Test case for offerings_offering_id_users_marker_email_marks_delete

    Remove learners from coach's marking list
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/offerings/{offering_id}/users/{marker_email}/marks'.format(offering_id='offering_id_example', marker_email='marker_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_marker_email_marks_get(client):
    """Test case for offerings_offering_id_users_marker_email_marks_get

    Find Learners marked by a coach
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/offerings/{offering_id}/users/{marker_email}/marks'.format(offering_id='offering_id_example', marker_email='marker_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_marker_email_marks_post(client):
    """Test case for offerings_offering_id_users_marker_email_marks_post

    Add learners to be marked by a coach
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/users/{marker_email}/marks'.format(offering_id='offering_id_example', marker_email='marker_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_post(client):
    """Test case for offerings_offering_id_users_post

    Adds user to the offering
    """
    body = {"firstName":"firstName","lastName":"lastName","isReadonly":False,"metadata":{"tags":["tags","tags"]},"sendInvite":True,"profile":{"displayName":"displayName"},"isFacilitator":False,"personId":"personId","sendNotificationEmail":True,"isMarker":False,"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/offerings/{offering_id}/users'.format(offering_id='offering_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_offerings_offering_id_users_user_email_delete(client):
    """Test case for offerings_offering_id_users_user_email_delete

    Removes user from the offering
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/offerings/{offering_id}/users/{user_email}'.format(offering_id='offering_id_example', user_email='user_email_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_user_email_transfer_patch(client):
    """Test case for users_user_email_transfer_patch

    Transfer a user between offerings
    """
    body = {"sendInvite":True,"fromOfferingId":"fromOfferingId","toOfferingId":"toOfferingId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/users/{user_email}/transfer'.format(user_email='user_email_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

