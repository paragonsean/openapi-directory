# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_info import AccountInfo
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_email_request import ChangeEmailRequest
from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.company_info import CompanyInfo
from openapi_server.models.credit_card_info import CreditCardInfo
from openapi_server.models.credit_card_info_response import CreditCardInfoResponse
from openapi_server.models.personal_info import PersonalInfo
from openapi_server.models.profile_picture_info import ProfilePictureInfo
from openapi_server.models.profile_picture_info_response import ProfilePictureInfoResponse


pytestmark = pytest.mark.asyncio

async def test_activate_user_account(client):
    """Test case for activate_user_account

    Activate the user account
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/account/activate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_email(client):
    """Test case for change_email

    Change user email
    """
    body = openapi_server.ChangeEmailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/account/changeEmail',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_password(client):
    """Test case for change_password

    Change user password
    """
    body = openapi_server.ChangePasswordRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/account/changePassword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_credit_card_info(client):
    """Test case for get_credit_card_info

    Get credit card information
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/account/creditCardInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_picture_info(client):
    """Test case for get_profile_picture_info

    Get profile picture information
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/account/profilePictureInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_account_info(client):
    """Test case for get_user_account_info

    Get user account information
    """
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/customer/account',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_email_activation(client):
    """Test case for resend_email_activation

    Resend email activation
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/customer/account/resendEmailActivation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_company_info(client):
    """Test case for save_company_info

    Change company information
    """
    body = openapi_server.CompanyInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/customer/account/companyInfo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_credit_card_info(client):
    """Test case for save_credit_card_info

    Save user credit card info
    """
    body = openapi_server.CreditCardInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/customer/account/creditCardInfo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_personal_info(client):
    """Test case for save_personal_info

    Save user personal information
    """
    body = openapi_server.PersonalInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/customer/account/personalInfo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_profile_picture_info(client):
    """Test case for save_profile_picture_info

    Change user picture information
    """
    body = openapi_server.ProfilePictureInfo()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v2/user/customer/account/profilePictureInfo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

