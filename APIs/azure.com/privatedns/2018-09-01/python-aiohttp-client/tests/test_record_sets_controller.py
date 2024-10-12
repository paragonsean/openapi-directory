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
    parameters = {"name":"name","etag":"etag","id":"id","type":"type","properties":{"aRecords":[{"ipv4Address":"ipv4Address"},{"ipv4Address":"ipv4Address"}],"cnameRecord":{"cname":"cname"},"txtRecords":[{"value":["value","value"]},{"value":["value","value"]}],"metadata":{"key":"metadata"},"fqdn":"fqdn","isAutoRegistered":True,"mxRecords":[{"preference":0,"exchange":"exchange"},{"preference":0,"exchange":"exchange"}],"aaaaRecords":[{"ipv6Address":"ipv6Address"},{"ipv6Address":"ipv6Address"}],"srvRecords":[{"port":7,"weight":3,"priority":9,"target":"target"},{"port":7,"weight":3,"priority":9,"target":"target"}],"ptrRecords":[{"ptrdname":"ptrdname"},{"ptrdname":"ptrdname"}],"ttl":2,"soaRecord":{"expireTime":6,"serialNumber":2,"minimumTtl":1,"refreshTime":5,"host":"host","retryTime":5,"email":"email"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'if_none_match': 'if_none_match_example',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', record_type='record_type_example', relative_record_set_name='relative_record_set_name_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', record_type='record_type_example', relative_record_set_name='relative_record_set_name_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', record_type='record_type_example', relative_record_set_name='relative_record_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_list(client):
    """Test case for record_sets_list

    
    """
    params = [('$top', 56),
                    ('$recordsetnamesuffix', 'recordsetnamesuffix_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/ALL'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', subscription_id='subscription_id_example'),
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/{record_type}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', record_type='record_type_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_sets_update(client):
    """Test case for record_sets_update

    
    """
    parameters = {"name":"name","etag":"etag","id":"id","type":"type","properties":{"aRecords":[{"ipv4Address":"ipv4Address"},{"ipv4Address":"ipv4Address"}],"cnameRecord":{"cname":"cname"},"txtRecords":[{"value":["value","value"]},{"value":["value","value"]}],"metadata":{"key":"metadata"},"fqdn":"fqdn","isAutoRegistered":True,"mxRecords":[{"preference":0,"exchange":"exchange"},{"preference":0,"exchange":"exchange"}],"aaaaRecords":[{"ipv6Address":"ipv6Address"},{"ipv6Address":"ipv6Address"}],"srvRecords":[{"port":7,"weight":3,"priority":9,"target":"target"},{"port":7,"weight":3,"priority":9,"target":"target"}],"ptrRecords":[{"ptrdname":"ptrdname"},{"ptrdname":"ptrdname"}],"ttl":2,"soaRecord":{"expireTime":6,"serialNumber":2,"minimumTtl":1,"refreshTime":5,"host":"host","retryTime":5,"email":"email"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/privateDnsZones/{private_zone_name}/{record_type}/{relative_record_set_name}'.format(resource_group_name='resource_group_name_example', private_zone_name='private_zone_name_example', record_type='record_type_example', relative_record_set_name='relative_record_set_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

