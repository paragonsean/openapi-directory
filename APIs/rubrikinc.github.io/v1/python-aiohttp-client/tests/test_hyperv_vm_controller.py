# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hyperv_virtual_machine_force_full_request import HypervVirtualMachineForceFullRequest
from openapi_server.models.hyperv_virtual_machine_force_full_response import HypervVirtualMachineForceFullResponse


pytestmark = pytest.mark.asyncio

async def test_get_hyperv_virtual_machine_force_full_spec(client):
    """Test case for get_hyperv_virtual_machine_force_full_spec

    Retrieve the configuration which has been set for forcing a full snapshot for a Hyper-V Virtual Machine
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/hyperv/vm/{id}/request/force_full_snapshot'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_hyperv_virtual_machine_force_full_snapshot(client):
    """Test case for request_hyperv_virtual_machine_force_full_snapshot

    Request a full snapshot during next backup job of a Hyper-V virtual machine
    """
    body = {"virtualDiskInfos":[{"shouldDedupe":True,"virtualDiskId":"virtualDiskId"},{"shouldDedupe":True,"virtualDiskId":"virtualDiskId"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hyperv/vm/{id}/request/force_full_snapshot'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

