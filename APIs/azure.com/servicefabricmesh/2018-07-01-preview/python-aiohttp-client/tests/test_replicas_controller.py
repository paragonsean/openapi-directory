# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.service_replica_description import ServiceReplicaDescription
from openapi_server.models.service_replica_list import ServiceReplicaList


pytestmark = pytest.mark.asyncio

async def test_replica_get(client):
    """Test case for replica_get

    Gets a specific replica of a given service.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}/services/{service_name}/replicas/{replica_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', service_name='service_name_example', replica_name='replica_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replica_list_by_service_name(client):
    """Test case for replica_list_by_service_name

    Gets replicas of a given service.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}/services/{service_name}/replicas'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example', service_name='service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

