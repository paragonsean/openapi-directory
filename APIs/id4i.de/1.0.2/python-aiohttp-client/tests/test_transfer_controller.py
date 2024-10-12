# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.transfer_receive_info import TransferReceiveInfo
from openapi_server.models.transfer_send_info import TransferSendInfo


pytestmark = pytest.mark.asyncio

async def test_get_send_info(client):
    """Test case for get_send_info

    Show transfer preparation information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/transfers/{id4n}/sendInfo'.format(id4n='id4n_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_prepare(client):
    """Test case for prepare

    Prepare an object for transfer
    """
    body = {"recipientOrganizationIds":["de.acme","com.porsche","de.bluerain"],"openForClaims":False,"ownerOrganizationId":"de.bluerain","holderOrganizationId":"de.id4i","keepOwnership":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transfers/{id4n}/sendInfo'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_receive(client):
    """Test case for receive

    Transfer a GUID or collection, obtaining it (i.e. becoming the holder) and if allowed also taking ownership
    """
    body = {"organizationId":"de.id4i"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/transfers/{id4n}/receiveInfo'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

