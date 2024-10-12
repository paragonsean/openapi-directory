# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.contacts_destroy400_response import ContactsDestroy400Response
from openapi_server.models.network_feature_config import NetworkFeatureConfig
from openapi_server.models.network_feature_config_request import NetworkFeatureConfigRequest
from openapi_server.models.network_feature_config_update import NetworkFeatureConfigUpdate
from openapi_server.models.network_feature_config_update_partial import NetworkFeatureConfigUpdatePartial


pytestmark = pytest.mark.asyncio

async def test_network_feature_configs_create(client):
    """Test case for network_feature_configs_create

    
    """
    body = {"network_feature":"network_feature","consuming_account":"2381982","managing_account":"238189294","insert_ixp_asn":True,"ip":"ip","bgp_session_type":"passive","contract_ref":"contract:31824","network_service_config":"network_service_config","type":"route_server","as_set_v6":"MOON-AS@RIPE","as_set_v4":"MOON-AS@RIPE","role_assignments":["c-impl:123","c-noc:331"],"password":"bgp-session-test-23","purchase_order":"Project: DC Moon","external_ref":"IX:Service:23042","max_prefix_v4":5000,"session_mode":"public","max_prefix_v6":5000,"asn":4200000023,"billing_account":"billing_account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/network-feature-configs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_feature_configs_destroy(client):
    """Test case for network_feature_configs_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/network-feature-configs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_feature_configs_list(client):
    """Test case for network_feature_configs_list

    
    """
    params = [('id', ['id1,id2,id3']),
                    ('state', 'state_example'),
                    ('state__is_not', 'state__is_not_example'),
                    ('managing_account', 'managing_account_example'),
                    ('consuming_account', 'consuming_account_example'),
                    ('external_ref', 'external_ref_example'),
                    ('type', 'type_example'),
                    ('service_config', 'service_config_example'),
                    ('network_feature', 'network_feature_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-feature-configs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_feature_configs_partial_update(client):
    """Test case for network_feature_configs_partial_update

    
    """
    body = openapi_server.NetworkFeatureConfigUpdatePartial()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/merge-patch+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/network-feature-configs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_feature_configs_read(client):
    """Test case for network_feature_configs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/network-feature-configs/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_feature_configs_update(client):
    """Test case for network_feature_configs_update

    
    """
    body = {"consuming_account":"2381982","managing_account":"238189294","insert_ixp_asn":True,"ip":"ip","bgp_session_type":"passive","type":"route_server","as_set_v6":"MOON-AS@RIPE","as_set_v4":"MOON-AS@RIPE","password":"bgp-session-test-23","external_ref":"IX:Service:23042","max_prefix_v4":5000,"session_mode":"public","max_prefix_v6":5000,"asn":4200000023}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/network-feature-configs/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

