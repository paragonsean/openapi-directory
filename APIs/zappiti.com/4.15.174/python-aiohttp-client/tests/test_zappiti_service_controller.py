# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.check_zappiti_service_request import CheckZappitiServiceRequest
from openapi_server.models.check_zappiti_service_result import CheckZappitiServiceResult
from openapi_server.models.install_zappiti_service_request import InstallZappitiServiceRequest
from openapi_server.models.install_zappiti_service_result import InstallZappitiServiceResult
from openapi_server.models.start_zappiti_service_request import StartZappitiServiceRequest
from openapi_server.models.start_zappiti_service_result import StartZappitiServiceResult


pytestmark = pytest.mark.asyncio

async def test_check_zappiti_service_post(client):
    """Test case for check_zappiti_service_post

    Check if Zappiti Service app status on the player
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/CheckZappitiService',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_install_zappiti_service_post(client):
    """Test case for install_zappiti_service_post

    Open a popup that allow the user to install Zappiti Service, if not already installed
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/InstallZappitiService',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_zappiti_service_post(client):
    """Test case for start_zappiti_service_post

    Start Zappiti Service if not started yet
    """
    body = {"ApiKey":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/StartZappitiService',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

