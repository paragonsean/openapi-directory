# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_password_request import ChangePasswordRequest
from openapi_server.models.change_recovery_question_request import ChangeRecoveryQuestionRequest
from openapi_server.models.set_recovery_credential_request import SetRecoveryCredentialRequest


pytestmark = pytest.mark.asyncio

async def test_change_password(client):
    """Test case for change_password

    Change Password
    """
    body = {"newPassword":{"value":"uTVM,TPw55"},"oldPassword":{"value":"{{password}}"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/credentials/change_password'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_recovery_question(client):
    """Test case for change_recovery_question

    Change Recovery Question
    """
    body = {"password":{"value":"{{password}}"},"recovery_question":{"answer":"My recovery credentials are updated","question":"What happens when I update my question"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/credentials/change_recovery_question'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_forgot_password_one_time_code(client):
    """Test case for forgot_password_one_time_code

    Forgot Password (One Time Code)
    """
    params = [('sendEmail', 'false')]
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/credentials/forgot_password'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_recovery_credential(client):
    """Test case for set_recovery_credential

    Set Recovery Credential
    """
    body = {"credentials":{"recovery_question":{"answer":"Annie Oakley","question":"Who's a major player in the cowboy scene?"}}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

