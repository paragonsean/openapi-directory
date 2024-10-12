# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_payee_v3_request import CreatePayeeV3Request
from openapi_server.models.create_payees_csv_response_v3 import CreatePayeesCSVResponseV3
from openapi_server.models.create_payees_csv_response_v4 import CreatePayeesCSVResponseV4
from openapi_server.models.create_payees_request_v3 import CreatePayeesRequestV3
from openapi_server.models.create_payees_request_v4 import CreatePayeesRequestV4
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.invite_payee_request_v3 import InvitePayeeRequestV3
from openapi_server.models.invite_payee_request_v4 import InvitePayeeRequestV4
from openapi_server.models.paged_payee_invitation_status_response_v3 import PagedPayeeInvitationStatusResponseV3
from openapi_server.models.paged_payee_invitation_status_response_v4 import PagedPayeeInvitationStatusResponseV4
from openapi_server.models.query_batch_response_v3 import QueryBatchResponseV3
from openapi_server.models.query_batch_response_v4 import QueryBatchResponseV4
from openapi_server.models.v4_create_payee_request import V4CreatePayeeRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_payee_v3(client):
    """Test case for create_payee_v3

    Initiate Payee Creation
    """
    body = {"payees":[{"address":{"city":"Key West","country":"US","countyOrProvince":"FL","line1":"500 Duval St","line2":"line2","line3":"line3","line4":"line4","zipOrPostcode":"33945"},"challenge":{"description":"challenge description","value":"challenge test"},"company":{"name":"ABC Group Plc","operatingName":"ABC Co","taxId":"123123123"},"email":"bob@example.com","individual":{"dateOfBirth":"1970-05-20T00:00:00.000+0000","name":{"firstName":"Bob","lastName":"Smith","otherNames":"H","title":"Mr"},"nationalIdentification":"SA211123K"},"language":"en-US","payeeId":"2aa5d7e0-2ecb-403f-8494-1865ed0454e9","paymentChannel":{"accountName":"My account","accountNumber":"XXXXXX5678","countryCode":"US","currency":"USD","iban":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234","paymentChannelName":"My Payment Channel","routingNumber":"XXXXX6789"},"payorRefs":[{"invitationStatus":"invitationStatus","invitationStatusTimestamp":"2019-01-20T09:00:00Z","payableIssues":[{"code":"3","message":"payee-disabled"},{"code":"3","message":"payee-disabled"}],"payableStatus":True,"paymentChannelId":"70faaff7-2c32-4b44-b27f-f0b6c484e6f3","payorId":"ba08877f-9d96-41e4-9c26-44a872d856ae","remoteId":"uniqueIdForRemoteEntity"},{"invitationStatus":"invitationStatus","invitationStatusTimestamp":"2019-01-20T09:00:00Z","payableIssues":[{"code":"3","message":"payee-disabled"},{"code":"3","message":"payee-disabled"}],"payableStatus":True,"paymentChannelId":"70faaff7-2c32-4b44-b27f-f0b6c484e6f3","payorId":"ba08877f-9d96-41e4-9c26-44a872d856ae","remoteId":"uniqueIdForRemoteEntity"}],"remoteId":"Remote ID","type":"type"},{"address":{"city":"Key West","country":"US","countyOrProvince":"FL","line1":"500 Duval St","line2":"line2","line3":"line3","line4":"line4","zipOrPostcode":"33945"},"challenge":{"description":"challenge description","value":"challenge test"},"company":{"name":"ABC Group Plc","operatingName":"ABC Co","taxId":"123123123"},"email":"bob@example.com","individual":{"dateOfBirth":"1970-05-20T00:00:00.000+0000","name":{"firstName":"Bob","lastName":"Smith","otherNames":"H","title":"Mr"},"nationalIdentification":"SA211123K"},"language":"en-US","payeeId":"2aa5d7e0-2ecb-403f-8494-1865ed0454e9","paymentChannel":{"accountName":"My account","accountNumber":"XXXXXX5678","countryCode":"US","currency":"USD","iban":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234","paymentChannelName":"My Payment Channel","routingNumber":"XXXXX6789"},"payorRefs":[{"invitationStatus":"invitationStatus","invitationStatusTimestamp":"2019-01-20T09:00:00Z","payableIssues":[{"code":"3","message":"payee-disabled"},{"code":"3","message":"payee-disabled"}],"payableStatus":True,"paymentChannelId":"70faaff7-2c32-4b44-b27f-f0b6c484e6f3","payorId":"ba08877f-9d96-41e4-9c26-44a872d856ae","remoteId":"uniqueIdForRemoteEntity"},{"invitationStatus":"invitationStatus","invitationStatusTimestamp":"2019-01-20T09:00:00Z","payableIssues":[{"code":"3","message":"payee-disabled"},{"code":"3","message":"payee-disabled"}],"payableStatus":True,"paymentChannelId":"70faaff7-2c32-4b44-b27f-f0b6c484e6f3","payorId":"ba08877f-9d96-41e4-9c26-44a872d856ae","remoteId":"uniqueIdForRemoteEntity"}],"remoteId":"Remote ID","type":"type"}],"payorId":"9ac75325-5dcd-42d5-b992-175d7e0a035e"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payees_invitation_status_v3(client):
    """Test case for get_payees_invitation_status_v3

    Get Payee Invitation Status
    """
    params = [('payeeId', '2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
                    ('invitationStatus', 'invitation_status_example'),
                    ('page', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payees/payors/{payor_id}/invitationStatus'.format(payor_id='9ac75325-5dcd-42d5-b992-175d7e0a035e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payees_invitation_status_v4(client):
    """Test case for get_payees_invitation_status_v4

    Get Payee Invitation Status
    """
    params = [('payeeId', '2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
                    ('invitationStatus', 'invitation_status_example'),
                    ('page', 1),
                    ('pageSize', 25)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/payees/payors/{payor_id}/invitationStatus'.format(payor_id='9ac75325-5dcd-42d5-b992-175d7e0a035e'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_batch_status_v3(client):
    """Test case for query_batch_status_v3

    Query Batch Status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payees/batch/{batch_id}'.format(batch_id='batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_batch_status_v4(client):
    """Test case for query_batch_status_v4

    Query Batch Status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/payees/batch/{batch_id}'.format(batch_id='batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_payee_invite_v3(client):
    """Test case for resend_payee_invite_v3

    Resend Payee Invite
    """
    body = {"payorId":"9ac75325-5dcd-42d5-b992-175d7e0a035e"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payees/{payee_id}/invite'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_payee_invite_v4(client):
    """Test case for resend_payee_invite_v4

    Resend Payee Invite
    """
    body = {"payorId":"9ac75325-5dcd-42d5-b992-175d7e0a035e"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/payees/{payee_id}/invite'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v4_create_payee(client):
    """Test case for v4_create_payee

    Initiate Payee Creation
    """
    body = {"payees":[{"address":{"city":"Key West","country":"US","countyOrProvince":"FL","line1":"500 Duval St","line2":"line2","line3":"line3","line4":"line4","zipOrPostcode":"33945"},"challenge":{"description":"challenge description","value":"11984567"},"company":{"name":"ABC Group Plc","operatingName":"ABC Co","taxId":"123123123"},"email":"bob@example.com","individual":{"dateOfBirth":"1970-05-20T00:00:00.000+0000","name":{"firstName":"Bob","lastName":"Smith","otherNames":"H","title":"Mr"},"nationalIdentification":"SA211123K"},"language":"en-US","paymentChannel":{"accountName":"My account","accountNumber":"XXXXXX5678","countryCode":"US","currency":"USD","iban":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234","paymentChannelName":"My Payment Channel","routingNumber":"XXXXX6789"},"remoteId":"Remote ID"},{"address":{"city":"Key West","country":"US","countyOrProvince":"FL","line1":"500 Duval St","line2":"line2","line3":"line3","line4":"line4","zipOrPostcode":"33945"},"challenge":{"description":"challenge description","value":"11984567"},"company":{"name":"ABC Group Plc","operatingName":"ABC Co","taxId":"123123123"},"email":"bob@example.com","individual":{"dateOfBirth":"1970-05-20T00:00:00.000+0000","name":{"firstName":"Bob","lastName":"Smith","otherNames":"H","title":"Mr"},"nationalIdentification":"SA211123K"},"language":"en-US","paymentChannel":{"accountName":"My account","accountNumber":"XXXXXX5678","countryCode":"US","currency":"USD","iban":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234","paymentChannelName":"My Payment Channel","routingNumber":"XXXXX6789"},"remoteId":"Remote ID"}],"payorId":"9ac75325-5dcd-42d5-b992-175d7e0a035e"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/payees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

