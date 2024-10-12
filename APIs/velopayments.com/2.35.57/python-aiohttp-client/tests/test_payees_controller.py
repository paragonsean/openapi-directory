# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.paged_payee_response_v3 import PagedPayeeResponseV3
from openapi_server.models.paged_payee_response_v4 import PagedPayeeResponseV4
from openapi_server.models.payee_delta_response_v3 import PayeeDeltaResponseV3
from openapi_server.models.payee_delta_response_v4 import PayeeDeltaResponseV4
from openapi_server.models.payee_detail_response_v3 import PayeeDetailResponseV3
from openapi_server.models.payee_detail_response_v4 import PayeeDetailResponseV4
from openapi_server.models.update_payee_details_request_v3 import UpdatePayeeDetailsRequestV3
from openapi_server.models.update_payee_details_request_v4 import UpdatePayeeDetailsRequestV4
from openapi_server.models.update_remote_id_request_v3 import UpdateRemoteIdRequestV3
from openapi_server.models.update_remote_id_request_v4 import UpdateRemoteIdRequestV4


pytestmark = pytest.mark.asyncio

async def test_delete_payee_by_id_v3(client):
    """Test case for delete_payee_by_id_v3

    Delete Payee by Id
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/payees/{payee_id}'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payee_by_id_v4(client):
    """Test case for delete_payee_by_id_v4

    Delete Payee by Id
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v4/payees/{payee_id}'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payee_by_id_v3(client):
    """Test case for get_payee_by_id_v3

    Get Payee by Id
    """
    params = [('sensitive', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payees/{payee_id}'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payee_by_id_v4(client):
    """Test case for get_payee_by_id_v4

    Get Payee by Id
    """
    params = [('sensitive', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/payees/{payee_id}'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payee_changes_v3(client):
    """Test case for list_payee_changes_v3

    List Payee Changes
    """
    params = [('payorId', 'payor_id_example'),
                    ('updatedSince', '2013-10-20T19:20:30+01:00'),
                    ('page', 1),
                    ('pageSize', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payees/deltas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payee_changes_v4(client):
    """Test case for list_payee_changes_v4

    List Payee Changes
    """
    params = [('payorId', 'payor_id_example'),
                    ('updatedSince', '2013-10-20T19:20:30+01:00'),
                    ('page', 1),
                    ('pageSize', 100)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/payees/deltas',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payees_v3(client):
    """Test case for list_payees_v3

    List Payees
    """
    params = [('payorId', 'payor_id_example'),
                    ('watchlistStatus', 'watchlist_status_example'),
                    ('disabled', True),
                    ('onboardedStatus', 'onboarded_status_example'),
                    ('email', 'bob@example.com'),
                    ('displayName', 'Bob Smith'),
                    ('remoteId', 'remoteId123'),
                    ('payeeType', 'payee_type_example'),
                    ('payeeCountry', 'US'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'displayName:asc')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/payees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_payees_v4(client):
    """Test case for list_payees_v4

    List Payees
    """
    params = [('payorId', 'payor_id_example'),
                    ('watchlistStatus', 'watchlist_status_example'),
                    ('disabled', True),
                    ('onboardedStatus', 'onboarded_status_example'),
                    ('email', 'bob@example.com'),
                    ('displayName', 'Bob Smith'),
                    ('remoteId', 'remoteId123'),
                    ('payeeType', 'payee_type_example'),
                    ('payeeCountry', 'US'),
                    ('ofacStatus', 'ofac_status_example'),
                    ('page', 1),
                    ('pageSize', 25),
                    ('sort', 'displayName:asc')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/payees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payee_details_update_v3(client):
    """Test case for payee_details_update_v3

    Update Payee Details
    """
    body = {"address":{"city":"Key West","country":"US","countyOrProvince":"FL","line1":"500 Duval St","line2":"line2","line3":"line3","line4":"line4","zipOrPostcode":"33945"},"challenge":{"description":"challenge description","value":"challenge test"},"company":{"name":"ABC Group Plc","operatingName":"ABC Co","taxId":"123123123"},"email":"bob@example.com","individual":{"dateOfBirth":"1985-01-01","name":{"firstName":"Bob","lastName":"Smith","otherNames":"A","title":"Mr"},"nationalIdentification":"AB123456C"},"language":"en-US"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payees/{payee_id}/payeeDetailsUpdate'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payee_details_update_v4(client):
    """Test case for payee_details_update_v4

    Update Payee Details
    """
    body = {"address":{"city":"Key West","country":"US","countyOrProvince":"FL","line1":"500 Duval St","line2":"line2","line3":"line3","line4":"line4","zipOrPostcode":"33945"},"challenge":{"description":"challenge description","value":"11984567"},"company":{"name":"ABC Group Plc","operatingName":"ABC Co","taxId":"123123123"},"contactSmsNumber":"11235555555","email":"bob@example.com","individual":{"dateOfBirth":"1985-01-01","name":{"firstName":"Bob","lastName":"Smith","otherNames":"A","title":"Mr"},"nationalIdentification":"AB123456C"},"language":"en-US"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/payees/{payee_id}/payeeDetailsUpdate'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v3_payees_payee_id_remote_id_update_post(client):
    """Test case for v3_payees_payee_id_remote_id_update_post

    Update Payee Remote Id
    """
    body = {"payorId":"9ac75325-5dcd-42d5-b992-175d7e0a035e","remoteId":"remoteId123"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/payees/{payee_id}/remoteIdUpdate'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v4_payees_payee_id_remote_id_update_post(client):
    """Test case for v4_payees_payee_id_remote_id_update_post

    Update Payee Remote Id
    """
    body = {"payorId":"9ac75325-5dcd-42d5-b992-175d7e0a035e","remoteId":"remoteId123"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v4/payees/{payee_id}/remoteIdUpdate'.format(payee_id='2aa5d7e0-2ecb-403f-8494-1865ed0454e9'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

