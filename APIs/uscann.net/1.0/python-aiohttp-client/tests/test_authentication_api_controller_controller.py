# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.email_model import EmailModel
from openapi_server.models.forgot_mail_token import ForgotMailToken
from openapi_server.models.jwt_response import JwtResponse
from openapi_server.models.login_user import LoginUser
from openapi_server.models.mail_token import MailToken
from openapi_server.models.problem import Problem
from openapi_server.models.registration_model import RegistrationModel
from openapi_server.models.response_status import ResponseStatus


pytestmark = pytest.mark.asyncio

async def test_authenticate_user(client):
    """Test case for authenticate_user

    authenticate the user and returns the token
    """
    login_user = {"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/apiv1/authentication/token',
        headers=headers,
        json=login_user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_forgot_password(client):
    """Test case for forgot_password

    forgotPassword
    """
    forgot_password = {"email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/apiv1/authentication/forgotPassword',
        headers=headers,
        json=forgot_password,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    register
    """
    register = {"zip":"zip","country":"country","lastName":"lastName","city":"city","companyDescription":"companyDescription","companyName":"companyName","number3":1,"date3":"date3","number1":0,"date2":"date2","number2":6,"storage":"storage","date1":"date1","firstName":"firstName","password":"password","string3":"string3","phone":"phone","streetAddress":"streetAddress","string1":"string1","string2":"string2","state":"state","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/apiv1/authentication/register',
        headers=headers,
        json=register,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_forgot_password(client):
    """Test case for set_forgot_password

    validates the mail token and set new password
    """
    token = {"password":"password","activity":"activity","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/apiv1/authentication/setForgotPassword',
        headers=headers,
        json=token,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_mail_token(client):
    """Test case for validate_mail_token

    validates the mail token
    """
    token = {"activity":"activity","token":"token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'content_type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/apiv1/authentication/validateMailToken',
        headers=headers,
        json=token,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

