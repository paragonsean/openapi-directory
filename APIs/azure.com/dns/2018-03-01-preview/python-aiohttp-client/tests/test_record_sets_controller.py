# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.record_set import RecordSet
from openapi_server.models.record_set_list_result import RecordSetListResult


pytestmark = pytest.mark.asyncio

async def test_record_sets_create_or_update(client):
    """Test case for record_sets_create_or_update

    
    """
    parameters = {"name":"name","etag":"etag","id":"id","type":"type","properties":{"AAAARecords":[{"ipv6Address":"ipv6Address"},{"ipv6Address":"ipv6Address"}],"metadata":{"key":"metadata"},"fqdn":"fqdn","NSRecords":[{"nsdname":"nsdname"},{"nsdname":"nsdname"}],"MXRecords":[{"preference":0,"exchange":"exchange"},{"preference":0,"exchange":"exchange"}],"SRVRecords":[{"port":7,"weight":3,"priority":9,"target":"target"},{"port":7,"weight":3,"priority":9,"target":"target"}],"ARecords":[{"ipv4Address":"ipv4Address"},{"ipv4Address":"ipv4Address"}],"TTL":2,"CNAMERecord":{"cname":"cname"},"PTRRecords":[{"ptrdname":"ptrdname"},{"ptrdname":"ptrdname"}],"TXTRecords":[{"value":["value","value"]},{"value":["value","value"]}],"caaRecords":[{"flags":4,"tag":"tag","value":"value"},{"flags":4,"tag":"tag","value":"value"}],"SOARecord":{"expireTime":6,"serialNumber":2,"minimumTTL":1,"refreshTime":5,"host":"host","retryTime":5,"email":"email"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', relative_record_set_name='relative_record_set_name_example', record_type='record_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_delete(client):
    """Test case for record_sets_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', relative_record_set_name='relative_record_set_name_example', record_type='record_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_get(client):
    """Test case for record_sets_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', relative_record_set_name='relative_record_set_name_example', record_type='record_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_list_all_by_dns_zone(client):
    """Test case for record_sets_list_all_by_dns_zone

    
    """
    params = [('$top', 56),
                    ('$recordsetnamesuffix', 'recordsetnamesuffix_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/all'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_list_by_dns_zone(client):
    """Test case for record_sets_list_by_dns_zone

    
    """
    params = [('$top', 56),
                    ('$recordsetnamesuffix', 'recordsetnamesuffix_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/recordsets'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_list_by_type(client):
    """Test case for record_sets_list_by_type

    
    """
    params = [('$top', 56),
                    ('$recordsetnamesuffix', 'recordsetnamesuffix_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/{record_type}'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', record_type='record_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_update(client):
    """Test case for record_sets_update

    
    """
    parameters = {"name":"name","etag":"etag","id":"id","type":"type","properties":{"AAAARecords":[{"ipv6Address":"ipv6Address"},{"ipv6Address":"ipv6Address"}],"metadata":{"key":"metadata"},"fqdn":"fqdn","NSRecords":[{"nsdname":"nsdname"},{"nsdname":"nsdname"}],"MXRecords":[{"preference":0,"exchange":"exchange"},{"preference":0,"exchange":"exchange"}],"SRVRecords":[{"port":7,"weight":3,"priority":9,"target":"target"},{"port":7,"weight":3,"priority":9,"target":"target"}],"ARecords":[{"ipv4Address":"ipv4Address"},{"ipv4Address":"ipv4Address"}],"TTL":2,"CNAMERecord":{"cname":"cname"},"PTRRecords":[{"ptrdname":"ptrdname"},{"ptrdname":"ptrdname"}],"TXTRecords":[{"value":["value","value"]},{"value":["value","value"]}],"caaRecords":[{"flags":4,"tag":"tag","value":"value"},{"flags":4,"tag":"tag","value":"value"}],"SOARecord":{"expireTime":6,"serialNumber":2,"minimumTTL":1,"refreshTime":5,"host":"host","retryTime":5,"email":"email"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/dnsZones/{zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', zone_name='zone_name_example', relative_record_set_name='relative_record_set_name_example', record_type='record_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

