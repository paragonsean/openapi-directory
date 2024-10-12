# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_snmpv3 import ConfigSNMPv3


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_access_add(client):
    """Test case for protocol_snmpv3_access_add

    Adds a new access entry with the specified parameters.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/access/add/{group_name}/{prefix}/{security_model}/{security_level}/{context_match}/{read_view}/{write_view}/{notify_view}'.format(agent_num=56, group_name='group_name_example', prefix='prefix_example', security_model='security_model_example', security_level='security_level_example', context_match='context_match_example', read_view='read_view_example', write_view='write_view_example', notify_view='notify_view_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_access_clear(client):
    """Test case for protocol_snmpv3_access_clear

    Clears all access entries.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/access/clear'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_access_del(client):
    """Test case for protocol_snmpv3_access_del

    Deletes the specified access entry.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/access/del/{access_name}'.format(agent_num=56, access_name='access_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_access_list(client):
    """Test case for protocol_snmpv3_access_list

    Returns the current acccess entries as an array of strings.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/access/list'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_get_config(client):
    """Test case for protocol_snmpv3_get_config

    Returns the SNMPv3 configuration.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/get/config'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_get_context_engineid(client):
    """Test case for protocol_snmpv3_get_context_engineid

    Retrieves the contextEngineID for the agent instance.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/get/context_engineid'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_get_engineboots(client):
    """Test case for protocol_snmpv3_get_engineboots

    Retrieves the number of times the agent has been restarted.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/get/engineboots'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_get_engineid(client):
    """Test case for protocol_snmpv3_get_engineid

    For started agents, retrieves the current engineID in use by the snmpv3 module.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/get/engineid'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_get_enginetime(client):
    """Test case for protocol_snmpv3_get_enginetime

    Retrieves the time in seconds for which the agent has been running.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/get/enginetime'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_group_add(client):
    """Test case for protocol_snmpv3_group_add

    Adds a new group entry with the specified parameters.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/group/add/{group_name}/{security_model}/{security_name}'.format(agent_num=56, group_name='group_name_example', security_model='security_model_example', security_name='security_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_group_clear(client):
    """Test case for protocol_snmpv3_group_clear

    Clears all group entries.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/group/clear'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_group_del(client):
    """Test case for protocol_snmpv3_group_del

    Deletes the specified group entry.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/group/del/{group_name}'.format(agent_num=56, group_name='group_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_group_list(client):
    """Test case for protocol_snmpv3_group_list

    Returns the current group entries as an array of strings.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/group/list'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_set_config(client):
    """Test case for protocol_snmpv3_set_config

    Changes the SNMPv3 configuration.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/set/config/{parameter}/{value}'.format(agent_num=56, parameter='parameter_example', value='value_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_user_add(client):
    """Test case for protocol_snmpv3_user_add

    Adds a new user entry with the specified parameters.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/user/add/{user_name}/{security_name}/{auth_protocol}/{auth_key}/{priv_protocol}/{priv_key}'.format(agent_num=56, user_name='user_name_example', security_name='security_name_example', auth_protocol='auth_protocol_example', auth_key='auth_key_example', priv_protocol='priv_protocol_example', priv_key='priv_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_user_clear(client):
    """Test case for protocol_snmpv3_user_clear

    Clears all user entries.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/user/clear'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_user_del(client):
    """Test case for protocol_snmpv3_user_del

    Deletes the specified user entry.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/user/del/{user_name}'.format(agent_num=56, user_name='user_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_user_list(client):
    """Test case for protocol_snmpv3_user_list

    Returns the current user entries as a Tcl list.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/user/list'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_usm_save(client):
    """Test case for protocol_snmpv3_usm_save

    Saves current user settings in the currently loaded USM config file.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/usm/save'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_usm_saveas(client):
    """Test case for protocol_snmpv3_usm_saveas

    Saves current user settings in the specified USM config file.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/usm/saveas/{filename}'.format(agent_num=56, filename='filename_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_vacm_save(client):
    """Test case for protocol_snmpv3_vacm_save

    Saves current group, access, view settings in the currently loaded VACM config file.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/vacm/save'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_vacm_saveas(client):
    """Test case for protocol_snmpv3_vacm_saveas

    Saves current group, access, view settings in the specified VACM config file.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/vacm/saveas/{filename}'.format(agent_num=56, filename='filename_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_view_add(client):
    """Test case for protocol_snmpv3_view_add

    Adds a new view entry with the specified parameters.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/view/add/{view_name}/{view_type}/{subtree}/{mask}'.format(agent_num=56, view_name='view_name_example', view_type='view_type_example', subtree='subtree_example', mask='mask_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_view_clear(client):
    """Test case for protocol_snmpv3_view_clear

    Clears all view entries.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/view/clear'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_view_del(client):
    """Test case for protocol_snmpv3_view_del

    Deletes the specified view entry.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/view/del/{view_name}'.format(agent_num=56, view_name='view_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_protocol_snmpv3_view_list(client):
    """Test case for protocol_snmpv3_view_list

    Returns the current view entries as an array of strings.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/mimic/agent/{agent_num}/protocol/msg/snmpv3/view/list'.format(agent_num=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

