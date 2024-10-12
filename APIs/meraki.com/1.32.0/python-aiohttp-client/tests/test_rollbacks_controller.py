# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_firmware_upgrades_rollback200_response import CreateNetworkFirmwareUpgradesRollback200Response
from openapi_server.models.create_network_firmware_upgrades_rollback_request import CreateNetworkFirmwareUpgradesRollbackRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_firmware_upgrades_rollback_2(client):
    """Test case for create_network_firmware_upgrades_rollback_2

    Rollback a Firmware Upgrade For A Network
    """
    body = openapi_server.CreateNetworkFirmwareUpgradesRollbackRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/firmwareUpgrades/rollbacks'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

