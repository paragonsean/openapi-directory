# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_automatic_provisioning_controller_create_account_container import RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_automatic_provisioning_create_account(client):
    """Test case for automatic_provisioning_create_account

    Creates a new Billbee user account with the data passed
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiAutomaticProvisioningControllerCreateAccountContainer()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/automaticprovision/createaccount',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automatic_provisioning_terms_info(client):
    """Test case for automatic_provisioning_terms_info

    Returns infos about Billbee terms and conditions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/automaticprovision/termsinfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

