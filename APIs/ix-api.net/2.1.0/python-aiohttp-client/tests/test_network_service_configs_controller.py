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
from openapi_server.models.network_service_config import NetworkServiceConfig
from openapi_server.models.network_service_config_request import NetworkServiceConfigRequest
from openapi_server.models.network_service_config_update import NetworkServiceConfigUpdate
from openapi_server.models.network_service_config_update_partial import NetworkServiceConfigUpdatePartial
from openapi_server.models.network_service_configs_destroy400_response import NetworkServiceConfigsDestroy400Response


pytestmark = pytest.mark.asyncio

async def test_network_service_config_cancellation_policy_read(client):
    """Test case for network_service_config_cancellation_policy_read

    
    """
    params = [('decommission_at', 'decommission_at_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-service-configs/{id}/cancellation-policy'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_configs_create(client):
    """Test case for network_service_configs_create

    
    """
    body = {"consuming_account":"2381982","managing_account":"238189294","network_service":"network_service","product_offering":"product_offering","contract_ref":"contract:31824","type":"exchange_lan","ips":["ips","ips"],"capacity":1,"role_assignments":["c-impl:123","c-noc:331"],"listed":True,"purchase_order":"Project: DC Moon","external_ref":"IX:Service:23042","macs":["macs","macs"],"network_feature_configs":["12356","43829"],"asns":[343953088,343953088],"connection":"connection","vlan_config":{"vlan":23,"vlan_ethertype":"0x8100","vlan_type":"dot1q"},"billing_account":"billing_account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/network-service-configs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_configs_destroy(client):
    """Test case for network_service_configs_destroy

    
    """
    body = {"decommission_at":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/network-service-configs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_configs_list(client):
    """Test case for network_service_configs_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('state', 'state_example'),
                    ('state__is_not', 'state__is_not_example'),
                    ('managing_account', 'managing_account_example'),
                    ('consuming_account', 'consuming_account_example'),
                    ('external_ref', 'external_ref_example'),
                    ('type', 'type_example'),
                    ('inner_vlan', 56),
                    ('outer_vlan', 56),
                    ('capacity', 56),
                    ('network_service', 'network_service_example'),
                    ('connection', 'connection_example'),
                    ('product_offering', 'product_offering_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-service-configs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_configs_partial_update(client):
    """Test case for network_service_configs_partial_update

    
    """
    body = openapi_server.NetworkServiceConfigUpdatePartial()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/network-service-configs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_configs_read(client):
    """Test case for network_service_configs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-service-configs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_service_configs_update(client):
    """Test case for network_service_configs_update

    
    """
    body = {"consuming_account":"2381982","managing_account":"238189294","contract_ref":"contract:31824","type":"exchange_lan","ips":["ips","ips"],"capacity":1,"role_assignments":["c-impl:123","c-noc:331"],"listed":True,"purchase_order":"Project: DC Moon","external_ref":"IX:Service:23042","macs":["macs","macs"],"network_feature_configs":["12356","43829"],"asns":[343953088,343953088],"connection":"connection","vlan_config":{"vlan":23,"vlan_ethertype":"0x8100","vlan_type":"dot1q"},"billing_account":"billing_account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/network-service-configs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

