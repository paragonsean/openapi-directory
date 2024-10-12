# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.circuit import Circuit
from openapi_server.models.circuit_termination import CircuitTermination
from openapi_server.models.circuit_type import CircuitType
from openapi_server.models.circuits_circuit_terminations_list200_response import CircuitsCircuitTerminationsList200Response
from openapi_server.models.circuits_circuit_types_list200_response import CircuitsCircuitTypesList200Response
from openapi_server.models.circuits_circuits_list200_response import CircuitsCircuitsList200Response
from openapi_server.models.circuits_providers_list200_response import CircuitsProvidersList200Response
from openapi_server.models.provider import Provider
from openapi_server.models.writable_circuit import WritableCircuit
from openapi_server.models.writable_circuit_termination import WritableCircuitTermination


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_create(client):
    """Test case for circuits_circuit_terminations_create

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","port_speed":314780940,"circuit":0,"connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"description":"description","pp_info":"pp_info","xconnect_id":"xconnect_id","site":5,"upstream_speed":1210617418,"term_side":"A","id":6,"cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/circuits/circuit-terminations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_delete(client):
    """Test case for circuits_circuit_terminations_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/circuits/circuit-terminations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_list(client):
    """Test case for circuits_circuit_terminations_list

    
    """
    params = [('term_side', 'term_side_example'),
                    ('port_speed', 'port_speed_example'),
                    ('upstream_speed', 'upstream_speed_example'),
                    ('xconnect_id', 'xconnect_id_example'),
                    ('q', 'q_example'),
                    ('circuit_id', 'circuit_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('term_side__n', 'term_side__n_example'),
                    ('port_speed__n', 'port_speed__n_example'),
                    ('port_speed__lte', 'port_speed__lte_example'),
                    ('port_speed__lt', 'port_speed__lt_example'),
                    ('port_speed__gte', 'port_speed__gte_example'),
                    ('port_speed__gt', 'port_speed__gt_example'),
                    ('upstream_speed__n', 'upstream_speed__n_example'),
                    ('upstream_speed__lte', 'upstream_speed__lte_example'),
                    ('upstream_speed__lt', 'upstream_speed__lt_example'),
                    ('upstream_speed__gte', 'upstream_speed__gte_example'),
                    ('upstream_speed__gt', 'upstream_speed__gt_example'),
                    ('xconnect_id__n', 'xconnect_id__n_example'),
                    ('xconnect_id__ic', 'xconnect_id__ic_example'),
                    ('xconnect_id__nic', 'xconnect_id__nic_example'),
                    ('xconnect_id__iew', 'xconnect_id__iew_example'),
                    ('xconnect_id__niew', 'xconnect_id__niew_example'),
                    ('xconnect_id__isw', 'xconnect_id__isw_example'),
                    ('xconnect_id__nisw', 'xconnect_id__nisw_example'),
                    ('xconnect_id__ie', 'xconnect_id__ie_example'),
                    ('xconnect_id__nie', 'xconnect_id__nie_example'),
                    ('circuit_id__n', 'circuit_id__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/circuit-terminations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_partial_update(client):
    """Test case for circuits_circuit_terminations_partial_update

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","port_speed":314780940,"circuit":0,"connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"description":"description","pp_info":"pp_info","xconnect_id":"xconnect_id","site":5,"upstream_speed":1210617418,"term_side":"A","id":6,"cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/circuits/circuit-terminations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_read(client):
    """Test case for circuits_circuit_terminations_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/circuit-terminations/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_update(client):
    """Test case for circuits_circuit_terminations_update

    
    """
    body = {"connected_endpoint_type":"connected_endpoint_type","port_speed":314780940,"circuit":0,"connected_endpoint":{"key":"connected_endpoint"},"connection_status":True,"description":"description","pp_info":"pp_info","xconnect_id":"xconnect_id","site":5,"upstream_speed":1210617418,"term_side":"A","id":6,"cable":{"id":6,"label":"label","url":"https://openapi-generator.tech"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/circuits/circuit-terminations/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_types_create(client):
    """Test case for circuits_circuit_types_create

    
    """
    body = {"circuit_count":6,"name":"name","description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/circuits/circuit-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_types_delete(client):
    """Test case for circuits_circuit_types_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/circuits/circuit-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_types_list(client):
    """Test case for circuits_circuit_types_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('q', 'q_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/circuit-types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_types_partial_update(client):
    """Test case for circuits_circuit_types_partial_update

    
    """
    body = {"circuit_count":6,"name":"name","description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/circuits/circuit-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_types_read(client):
    """Test case for circuits_circuit_types_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/circuit-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_types_update(client):
    """Test case for circuits_circuit_types_update

    
    """
    body = {"circuit_count":6,"name":"name","description":"description","id":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/circuits/circuit-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuits_create(client):
    """Test case for circuits_circuits_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","description":"description","termination_a":"termination_a","type":5,"tags":["tags","tags"],"termination_z":"termination_z","commit_rate":171976544,"provider":1,"id":6,"install_date":"2000-01-23","tenant":5,"cid":"cid","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/circuits/circuits/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuits_delete(client):
    """Test case for circuits_circuits_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/circuits/circuits/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuits_list(client):
    """Test case for circuits_circuits_list

    
    """
    params = [('id', 'id_example'),
                    ('cid', 'cid_example'),
                    ('install_date', 'install_date_example'),
                    ('commit_rate', 'commit_rate_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('provider_id', 'provider_id_example'),
                    ('provider', 'provider_example'),
                    ('type_id', 'type_id_example'),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('cid__n', 'cid__n_example'),
                    ('cid__ic', 'cid__ic_example'),
                    ('cid__nic', 'cid__nic_example'),
                    ('cid__iew', 'cid__iew_example'),
                    ('cid__niew', 'cid__niew_example'),
                    ('cid__isw', 'cid__isw_example'),
                    ('cid__nisw', 'cid__nisw_example'),
                    ('cid__ie', 'cid__ie_example'),
                    ('cid__nie', 'cid__nie_example'),
                    ('install_date__n', 'install_date__n_example'),
                    ('install_date__lte', 'install_date__lte_example'),
                    ('install_date__lt', 'install_date__lt_example'),
                    ('install_date__gte', 'install_date__gte_example'),
                    ('install_date__gt', 'install_date__gt_example'),
                    ('commit_rate__n', 'commit_rate__n_example'),
                    ('commit_rate__lte', 'commit_rate__lte_example'),
                    ('commit_rate__lt', 'commit_rate__lt_example'),
                    ('commit_rate__gte', 'commit_rate__gte_example'),
                    ('commit_rate__gt', 'commit_rate__gt_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('provider_id__n', 'provider_id__n_example'),
                    ('provider__n', 'provider__n_example'),
                    ('type_id__n', 'type_id__n_example'),
                    ('type__n', 'type__n_example'),
                    ('status__n', 'status__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/circuits/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuits_partial_update(client):
    """Test case for circuits_circuits_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","description":"description","termination_a":"termination_a","type":5,"tags":["tags","tags"],"termination_z":"termination_z","commit_rate":171976544,"provider":1,"id":6,"install_date":"2000-01-23","tenant":5,"cid":"cid","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/circuits/circuits/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuits_read(client):
    """Test case for circuits_circuits_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/circuits/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuits_update(client):
    """Test case for circuits_circuits_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","description":"description","termination_a":"termination_a","type":5,"tags":["tags","tags"],"termination_z":"termination_z","commit_rate":171976544,"provider":1,"id":6,"install_date":"2000-01-23","tenant":5,"cid":"cid","status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/circuits/circuits/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_create(client):
    """Test case for circuits_providers_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":1,"created":"2000-01-23","custom_fields":"{}","admin_contact":"admin_contact","tags":["tags","tags"],"portal_url":"https://openapi-generator.tech","name":"name","noc_contact":"noc_contact","id":5,"asn":2147483647,"account":"account","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/circuits/providers/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_delete(client):
    """Test case for circuits_providers_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/circuits/providers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_graphs(client):
    """Test case for circuits_providers_graphs

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/providers/{id}/graphs'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_list(client):
    """Test case for circuits_providers_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('asn', 'asn_example'),
                    ('account', 'account_example'),
                    ('created', 'created_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__lte', 'created__lte_example'),
                    ('last_updated', 'last_updated_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('asn__n', 'asn__n_example'),
                    ('asn__lte', 'asn__lte_example'),
                    ('asn__lt', 'asn__lt_example'),
                    ('asn__gte', 'asn__gte_example'),
                    ('asn__gt', 'asn__gt_example'),
                    ('account__n', 'account__n_example'),
                    ('account__ic', 'account__ic_example'),
                    ('account__nic', 'account__nic_example'),
                    ('account__iew', 'account__iew_example'),
                    ('account__niew', 'account__niew_example'),
                    ('account__isw', 'account__isw_example'),
                    ('account__nisw', 'account__nisw_example'),
                    ('account__ie', 'account__ie_example'),
                    ('account__nie', 'account__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/providers/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_partial_update(client):
    """Test case for circuits_providers_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":1,"created":"2000-01-23","custom_fields":"{}","admin_contact":"admin_contact","tags":["tags","tags"],"portal_url":"https://openapi-generator.tech","name":"name","noc_contact":"noc_contact","id":5,"asn":2147483647,"account":"account","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/circuits/providers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_read(client):
    """Test case for circuits_providers_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/providers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_providers_update(client):
    """Test case for circuits_providers_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","circuit_count":1,"created":"2000-01-23","custom_fields":"{}","admin_contact":"admin_contact","tags":["tags","tags"],"portal_url":"https://openapi-generator.tech","name":"name","noc_contact":"noc_contact","id":5,"asn":2147483647,"account":"account","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/circuits/providers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

