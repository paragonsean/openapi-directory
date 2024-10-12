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

async def test_circuits_choices_list(client):
    """Test case for circuits_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_choices_read(client):
    """Test case for circuits_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/circuits/_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_circuits_circuit_terminations_create(client):
    """Test case for circuits_circuit_terminations_create

    
    """
    body = {"xconnect_id":"xconnect_id","port_speed":1280358508,"site":5,"upstream_speed":494379917,"circuit":0,"pp_info":"pp_info","term_side":"A","id":6,"interface":1}
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
                    ('port_speed', 3.4),
                    ('upstream_speed', 3.4),
                    ('xconnect_id', 'xconnect_id_example'),
                    ('q', 'q_example'),
                    ('circuit_id', 'circuit_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
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
    body = {"xconnect_id":"xconnect_id","port_speed":1280358508,"site":5,"upstream_speed":494379917,"circuit":0,"pp_info":"pp_info","term_side":"A","id":6,"interface":1}
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
    body = {"xconnect_id":"xconnect_id","port_speed":1280358508,"site":5,"upstream_speed":494379917,"circuit":0,"pp_info":"pp_info","term_side":"A","id":6,"interface":1}
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"name":"name","id":6,"slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","description":"description","type":2,"tags":["tags","tags"],"commit_rate":171976544,"provider":1,"id":6,"install_date":"2000-01-23","tenant":5,"cid":"cid","status":5}
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
    params = [('cid', 'cid_example'),
                    ('install_date', 'install_date_example'),
                    ('commit_rate', 3.4),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('provider_id', 'provider_id_example'),
                    ('provider', 'provider_example'),
                    ('type_id', 'type_id_example'),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","description":"description","type":2,"tags":["tags","tags"],"commit_rate":171976544,"provider":1,"id":6,"install_date":"2000-01-23","tenant":5,"cid":"cid","status":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","description":"description","type":2,"tags":["tags","tags"],"commit_rate":171976544,"provider":1,"id":6,"install_date":"2000-01-23","tenant":5,"cid":"cid","status":5}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","admin_contact":"admin_contact","tags":["tags","tags"],"portal_url":"https://openapi-generator.tech","name":"name","noc_contact":"noc_contact","id":1,"asn":2147483647,"account":"account","slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('asn', 3.4),
                    ('account', 'account_example'),
                    ('id__in', 'id__in_example'),
                    ('q', 'q_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('tag', 'tag_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","admin_contact":"admin_contact","tags":["tags","tags"],"portal_url":"https://openapi-generator.tech","name":"name","noc_contact":"noc_contact","id":1,"asn":2147483647,"account":"account","slug":"slug"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23","custom_fields":"{}","admin_contact":"admin_contact","tags":["tags","tags"],"portal_url":"https://openapi-generator.tech","name":"name","noc_contact":"noc_contact","id":1,"asn":2147483647,"account":"account","slug":"slug"}
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

