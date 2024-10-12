# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.file_needs_vendor import FileNeedsVendor
from openapi_server.models.vendor_invitation_list import VendorInvitationList


pytestmark = pytest.mark.asyncio

async def test_get_invitation_vendors(client):
    """Test case for get_invitation_vendors

    Get vendor list for compiled invitation needs
    """
    body = {"reason":"reason","taskType":["taskType","taskType"],"targetLanguage":["targetLanguage","targetLanguage"],"guid":"guid","projectId":6,"fileId":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/invitation/vendors',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

