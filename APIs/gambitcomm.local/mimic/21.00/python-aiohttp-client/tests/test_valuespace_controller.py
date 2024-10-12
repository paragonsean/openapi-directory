# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_add(client):
    """Test case for add

    Add an entry to a table.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/value/add/{object}/{instance}'.format(agent_num=56, object='object_example', instance='instance_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eval_value(client):
    """Test case for eval_value

    Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/eval/{object}/{instance}'.format(agent_num=56, object='object_example', instance='instance_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_info(client):
    """Test case for get_info

    Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/info/{object}'.format(agent_num=56, object='object_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instances(client):
    """Test case for get_instances

    Display the MIB object instances for the specified object.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/instances/{object}'.format(agent_num=56, object='object_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_mib(client):
    """Test case for get_mib

    Return the MIB that defines the specified object.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/mib/{object}'.format(agent_num=56, object='object_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_name(client):
    """Test case for get_name

    Return the symbolic name of the specified object identifier.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/name/{oid}'.format(agent_num=56, oid='oid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_objects(client):
    """Test case for get_objects

    Display the MIB objects below the current position
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/list/{oid}'.format(agent_num=56, oid='oid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_oid(client):
    """Test case for get_oid

    Return the numeric OID of the specified object.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/oid/{object}'.format(agent_num=56, object='object_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_state(client):
    """Test case for get_state

    Get the state of a MIB object object.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/state/get/{object}'.format(agent_num=56, object='object_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_value(client):
    """Test case for get_value

    Get a variable in the Value Space.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/get/{object}/{instance}/{variable}'.format(agent_num=56, object='object_example', instance='instance_example', variable='variable_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_variables(client):
    """Test case for get_variables

    Display the variables for the specified instance instance for the specified MIB object object
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/variables/{object}/{instance}'.format(agent_num=56, object='object_example', instance='instance_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_meval_value(client):
    """Test case for meval_value

    Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/meval/{obj_ins_array}'.format(agent_num=56, obj_ins_array=[openapi_server.List[str]()]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mget_value(client):
    """Test case for mget_value

    Get multiple variables in the Value Space.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/mget/{obj_ins_var_array}'.format(agent_num=56, obj_ins_var_array=[openapi_server.List[str]()]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mset_value(client):
    """Test case for mset_value

    Set multiple variables in the Value Space.
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/value/mset'.format(agent_num=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_munset_value(client):
    """Test case for munset_value

    Unset multiple variables in the Value Space
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/value/munset'.format(agent_num=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove(client):
    """Test case for remove

    Remove an entry from a table.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/value/remove/{object}/{instance}'.format(agent_num=56, object='object_example', instance='instance_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_state(client):
    """Test case for set_state

    Set the state of a MIB object object
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/value/state/set/{object}/{state}'.format(agent_num=56, object='object_example', state=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_value(client):
    """Test case for set_value

    Set a variable in the Value Space.
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/value/set/{object}/{instance}/{variable}'.format(agent_num=56, object='object_example', instance='instance_example', variable='variable_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_split_oid(client):
    """Test case for split_oid

    Split the numerical OID into the object OID and instance OID.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/value/split/{oid}'.format(agent_num=56, oid='oid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unset_value(client):
    """Test case for unset_value

    Unset a variable in the Value Space in order to free its memory.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/value/unset/{object}/{instance}/{variable}'.format(agent_num=56, object='object_example', instance='instance_example', variable='variable_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

