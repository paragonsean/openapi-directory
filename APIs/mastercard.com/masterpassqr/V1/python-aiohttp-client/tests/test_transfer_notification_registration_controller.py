# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accountregistration167_wrapper import Accountregistration167Wrapper
from openapi_server.models.accountregistration168_wrapper import Accountregistration168Wrapper
from openapi_server.models.accountregistration169_wrapper import Accountregistration169Wrapper
from openapi_server.models.accountregistration170_wrapper import Accountregistration170Wrapper
from openapi_server.models.accountregistration171_wrapper import Accountregistration171Wrapper
from openapi_server.models.accountregistration172_wrapper import Accountregistration172Wrapper


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_transfer_notification_registration(client):
    """Test case for create_transfer_notification_registration

    This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.
    """
    accountregistration = openapi_server.Accountregistration167Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/send/v1/partners/{partner_id}/notification-registries'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9'),
        headers=headers,
        json=accountregistration,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transfer_notification_registration(client):
    """Test case for delete_transfer_notification_registration

    This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/send/v1/partners/{partner_id}/notification-registries/{account_reg_ref}'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9', account_reg_ref='areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notification_registration_api_read_by(client):
    """Test case for notification_registration_api_read_by

    This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider's information for a registered PAN for notifications. 
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/send/v1/partners/{partner_id}/notification-registries/{account_reg_ref}'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9', account_reg_ref='areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_notification_registration_api_update(client):
    """Test case for notification_registration_api_update

    This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.
    """
    accountregistration = openapi_server.Accountregistration169Wrapper()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/send/v1/partners/{partner_id}/notification-registries/{account_reg_ref}'.format(partner_id='ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9', account_reg_ref='areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF'),
        headers=headers,
        json=accountregistration,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

