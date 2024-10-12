# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server.models.update_account_request_body import UpdateAccountRequestBody


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Get account settings
    """
    params = [('include', 'masterUser')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/account',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account(client):
    """Test case for update_account

    Update account settings
    """
    body = {"externalDomain":"externalDomain","showReferralLinks":False,"brandingSettings":{"customEmail":"custom@example.com","companyName":"companyName","theme":"default"},"customSignature":"customSignature","emailContent":"Great news, your new account is ready! For your records, we've listed information you'll use to log in below: FTP Server: [[ftpserver]] Username (Web and FTP access): [[username]] [[setpassword]]","quota":{"noticeEnabled":True,"transactionsNoticeEnabled":True,"noticeThreshold":0,"transactionsNoticeThreshold":6},"allowedIpRanges":[{"ipEnd":"ipEnd","ipStart":"ipStart"},{"ipEnd":"ipEnd","ipStart":"ipStart"}],"secureOnly":False,"emailSubject":"ExaVault File Sharing Account","accountOnboarding":True,"complexPasswords":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'exampleaccount-zwSuWUZ8S38h33qPS8v0s',
        'ev_access_token': '19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/account',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

