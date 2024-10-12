# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer import Customer
from openapi_server.models.jwt_response import JwtResponse
from openapi_server.models.login_user import LoginUser
from openapi_server.models.problem import Problem
from openapi_server.models.response_status import ResponseStatus


pytestmark = pytest.mark.asyncio

async def test_authenticate_user(client):
    """Test case for authenticate_user

    Get Token
    """
    login_user = {"password":"password","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0.0/authentication/customer/token',
        headers=headers,
        json=login_user,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register(client):
    """Test case for register

    Customer Registration
    """
    register = {"zip":"zip","country":"country","lastName":"lastName","city":"city","companyDescription":"companyDescription","companyName":"companyName","faceRecognitionType":"AWS or AZURE","firstName":"firstName","password":"password","phone":"phone","streetAddress":"streetAddress","state":"state","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1.0.0/authentication/customer/registration',
        headers=headers,
        json=register,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

