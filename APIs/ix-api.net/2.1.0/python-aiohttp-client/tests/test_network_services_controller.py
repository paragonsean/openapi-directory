# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.cancellation_policy import CancellationPolicy
from openapi_server.models.cancellation_request import CancellationRequest
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.network_service import NetworkService
from openapi_server.models.network_service_change_request import NetworkServiceChangeRequest
from openapi_server.models.network_service_configs_destroy400_response import NetworkServiceConfigsDestroy400Response
from openapi_server.models.network_service_request import NetworkServiceRequest
from openapi_server.models.network_service_request_partial import NetworkServiceRequestPartial


pytestmark = pytest.mark.asyncio

async def test_network_service_cancellation_policy_read(client):
    """Test case for network_service_cancellation_policy_read

    
    """
    params = [('decommission_at', 'decommission_at_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-services/{id}/cancellation-policy'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_change_request_create(client):
    """Test case for network_service_change_request_create

    
    """
    body = {"product_offering":"product_offering","capacity":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/network-services/{id}/change-request'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_change_request_destroy(client):
    """Test case for network_service_change_request_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/network-services/{id}/change-request'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_change_request_read(client):
    """Test case for network_service_change_request_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-services/{id}/change-request'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_services_create(client):
    """Test case for network_services_create

    
    """
    body = {"consuming_account":"2381982","joining_member_account":"231829","managing_account":"238189294","purchase_order":"Project: DC Moon","external_ref":"IX:Service:23042","product_offering":"product_offering","contract_ref":"contract:31824","type":"p2p_vc","billing_account":"billing_account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/network-services',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_services_destroy(client):
    """Test case for network_services_destroy

    
    """
    body = {"decommission_at":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/network-services/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_services_list(client):
    """Test case for network_services_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('state', 'state_example'),
                    ('state__is_not', 'state__is_not_example'),
                    ('managing_account', 'managing_account_example'),
                    ('consuming_account', 'consuming_account_example'),
                    ('external_ref', 'external_ref_example'),
                    ('type', 'type_example'),
                    ('pop', 'pop_example'),
                    ('product_offering', 'product_offering_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-services',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_services_partial_update(client):
    """Test case for network_services_partial_update

    
    """
    body = openapi_server.NetworkServiceRequestPartial()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/network-services/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_services_read(client):
    """Test case for network_services_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-services/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_services_update(client):
    """Test case for network_services_update

    
    """
    body = {"consuming_account":"2381982","joining_member_account":"231829","managing_account":"238189294","purchase_order":"Project: DC Moon","external_ref":"IX:Service:23042","product_offering":"product_offering","contract_ref":"contract:31824","type":"p2p_vc","billing_account":"billing_account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/network-services/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

