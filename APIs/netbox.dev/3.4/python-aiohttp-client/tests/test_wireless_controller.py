# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.wireless_lan import WirelessLAN
from openapi_server.models.wireless_lan_group import WirelessLANGroup
from openapi_server.models.wireless_link import WirelessLink
from openapi_server.models.wireless_wireless_lan_groups_list200_response import WirelessWirelessLanGroupsList200Response
from openapi_server.models.wireless_wireless_lans_list200_response import WirelessWirelessLansList200Response
from openapi_server.models.wireless_wireless_links_list200_response import WirelessWirelessLinksList200Response
from openapi_server.models.writable_wireless_lan import WritableWirelessLAN
from openapi_server.models.writable_wireless_lan_group import WritableWirelessLANGroup
from openapi_server.models.writable_wireless_link import WritableWirelessLink


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_bulk_delete(client):
    """Test case for wireless_wireless_lan_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/wireless/wireless-lan-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_bulk_partial_update(client):
    """Test case for wireless_wireless_lan_groups_bulk_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"wirelesslan_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/wireless/wireless-lan-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_bulk_update(client):
    """Test case for wireless_wireless_lan_groups_bulk_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"wirelesslan_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/wireless/wireless-lan-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_create(client):
    """Test case for wireless_wireless_lan_groups_create

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"wirelesslan_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/wireless/wireless-lan-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_delete(client):
    """Test case for wireless_wireless_lan_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/wireless/wireless-lan-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_list(client):
    """Test case for wireless_wireless_lan_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('parent_id', 'parent_id_example'),
                    ('parent', 'parent_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('parent__n', 'parent__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/wireless/wireless-lan-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_partial_update(client):
    """Test case for wireless_wireless_lan_groups_partial_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"wirelesslan_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/wireless/wireless-lan-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_read(client):
    """Test case for wireless_wireless_lan_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/wireless/wireless-lan-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lan_groups_update(client):
    """Test case for wireless_wireless_lan_groups_update

    
    """
    body = {"parent":1,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","_depth":0,"description":"description","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"wirelesslan_count":5,"name":"name","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/wireless/wireless-lan-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_bulk_delete(client):
    """Test case for wireless_wireless_lans_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/wireless/wireless-lans/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_bulk_partial_update(client):
    """Test case for wireless_wireless_lans_bulk_partial_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","vlan":5,"id":6,"tenant":1,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/wireless/wireless-lans/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_bulk_update(client):
    """Test case for wireless_wireless_lans_bulk_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","vlan":5,"id":6,"tenant":1,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/wireless/wireless-lans/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_create(client):
    """Test case for wireless_wireless_lans_create

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","vlan":5,"id":6,"tenant":1,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/wireless/wireless-lans/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_delete(client):
    """Test case for wireless_wireless_lans_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/wireless/wireless-lans/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_list(client):
    """Test case for wireless_wireless_lans_list

    
    """
    params = [('id', 'id_example'),
                    ('ssid', 'ssid_example'),
                    ('auth_psk', 'auth_psk_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('status', 'status_example'),
                    ('vlan_id', 'vlan_id_example'),
                    ('auth_type', 'auth_type_example'),
                    ('auth_cipher', 'auth_cipher_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('ssid__n', 'ssid__n_example'),
                    ('ssid__ic', 'ssid__ic_example'),
                    ('ssid__nic', 'ssid__nic_example'),
                    ('ssid__iew', 'ssid__iew_example'),
                    ('ssid__niew', 'ssid__niew_example'),
                    ('ssid__isw', 'ssid__isw_example'),
                    ('ssid__nisw', 'ssid__nisw_example'),
                    ('ssid__ie', 'ssid__ie_example'),
                    ('ssid__nie', 'ssid__nie_example'),
                    ('ssid__empty', 'ssid__empty_example'),
                    ('auth_psk__n', 'auth_psk__n_example'),
                    ('auth_psk__ic', 'auth_psk__ic_example'),
                    ('auth_psk__nic', 'auth_psk__nic_example'),
                    ('auth_psk__iew', 'auth_psk__iew_example'),
                    ('auth_psk__niew', 'auth_psk__niew_example'),
                    ('auth_psk__isw', 'auth_psk__isw_example'),
                    ('auth_psk__nisw', 'auth_psk__nisw_example'),
                    ('auth_psk__ie', 'auth_psk__ie_example'),
                    ('auth_psk__nie', 'auth_psk__nie_example'),
                    ('auth_psk__empty', 'auth_psk__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('status__n', 'status__n_example'),
                    ('vlan_id__n', 'vlan_id__n_example'),
                    ('auth_type__n', 'auth_type__n_example'),
                    ('auth_cipher__n', 'auth_cipher__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/wireless/wireless-lans/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_partial_update(client):
    """Test case for wireless_wireless_lans_partial_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","vlan":5,"id":6,"tenant":1,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/wireless/wireless-lans/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_read(client):
    """Test case for wireless_wireless_lans_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/wireless/wireless-lans/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_lans_update(client):
    """Test case for wireless_wireless_lans_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","vlan":5,"id":6,"tenant":1,"group":0,"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/wireless/wireless-lans/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_bulk_delete(client):
    """Test case for wireless_wireless_links_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/wireless/wireless-links/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_bulk_partial_update(client):
    """Test case for wireless_wireless_links_bulk_partial_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","interface_b":1,"interface_a":6,"id":0,"tenant":5,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/wireless/wireless-links/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_bulk_update(client):
    """Test case for wireless_wireless_links_bulk_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","interface_b":1,"interface_a":6,"id":0,"tenant":5,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/wireless/wireless-links/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_create(client):
    """Test case for wireless_wireless_links_create

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","interface_b":1,"interface_a":6,"id":0,"tenant":5,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/wireless/wireless-links/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_delete(client):
    """Test case for wireless_wireless_links_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/wireless/wireless-links/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_list(client):
    """Test case for wireless_wireless_links_list

    
    """
    params = [('id', 'id_example'),
                    ('ssid', 'ssid_example'),
                    ('auth_psk', 'auth_psk_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('interface_a_id', 'interface_a_id_example'),
                    ('interface_b_id', 'interface_b_id_example'),
                    ('status', 'status_example'),
                    ('auth_type', 'auth_type_example'),
                    ('auth_cipher', 'auth_cipher_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('ssid__n', 'ssid__n_example'),
                    ('ssid__ic', 'ssid__ic_example'),
                    ('ssid__nic', 'ssid__nic_example'),
                    ('ssid__iew', 'ssid__iew_example'),
                    ('ssid__niew', 'ssid__niew_example'),
                    ('ssid__isw', 'ssid__isw_example'),
                    ('ssid__nisw', 'ssid__nisw_example'),
                    ('ssid__ie', 'ssid__ie_example'),
                    ('ssid__nie', 'ssid__nie_example'),
                    ('ssid__empty', 'ssid__empty_example'),
                    ('auth_psk__n', 'auth_psk__n_example'),
                    ('auth_psk__ic', 'auth_psk__ic_example'),
                    ('auth_psk__nic', 'auth_psk__nic_example'),
                    ('auth_psk__iew', 'auth_psk__iew_example'),
                    ('auth_psk__niew', 'auth_psk__niew_example'),
                    ('auth_psk__isw', 'auth_psk__isw_example'),
                    ('auth_psk__nisw', 'auth_psk__nisw_example'),
                    ('auth_psk__ie', 'auth_psk__ie_example'),
                    ('auth_psk__nie', 'auth_psk__nie_example'),
                    ('auth_psk__empty', 'auth_psk__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('interface_a_id__n', 'interface_a_id__n_example'),
                    ('interface_a_id__lte', 'interface_a_id__lte_example'),
                    ('interface_a_id__lt', 'interface_a_id__lt_example'),
                    ('interface_a_id__gte', 'interface_a_id__gte_example'),
                    ('interface_a_id__gt', 'interface_a_id__gt_example'),
                    ('interface_b_id__n', 'interface_b_id__n_example'),
                    ('interface_b_id__lte', 'interface_b_id__lte_example'),
                    ('interface_b_id__lt', 'interface_b_id__lt_example'),
                    ('interface_b_id__gte', 'interface_b_id__gte_example'),
                    ('interface_b_id__gt', 'interface_b_id__gt_example'),
                    ('status__n', 'status__n_example'),
                    ('auth_type__n', 'auth_type__n_example'),
                    ('auth_cipher__n', 'auth_cipher__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/wireless/wireless-links/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_partial_update(client):
    """Test case for wireless_wireless_links_partial_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","interface_b":1,"interface_a":6,"id":0,"tenant":5,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/wireless/wireless-links/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_read(client):
    """Test case for wireless_wireless_links_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/wireless/wireless-links/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_wireless_wireless_links_update(client):
    """Test case for wireless_wireless_links_update

    
    """
    body = {"auth_type":"open","last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","ssid":"ssid","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"auth_cipher":"auto","auth_psk":"auth_psk","interface_b":1,"interface_a":6,"id":0,"tenant":5,"status":"connected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/wireless/wireless-links/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

