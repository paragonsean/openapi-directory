# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_servicebroker_v1beta1_binding import GoogleCloudServicebrokerV1beta1Binding
from openapi_server.models.google_cloud_servicebroker_v1beta1_broker import GoogleCloudServicebrokerV1beta1Broker
from openapi_server.models.google_cloud_servicebroker_v1beta1_create_binding_response import GoogleCloudServicebrokerV1beta1CreateBindingResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_create_service_instance_response import GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_delete_binding_response import GoogleCloudServicebrokerV1beta1DeleteBindingResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_get_binding_response import GoogleCloudServicebrokerV1beta1GetBindingResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_list_bindings_response import GoogleCloudServicebrokerV1beta1ListBindingsResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_list_brokers_response import GoogleCloudServicebrokerV1beta1ListBrokersResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_list_catalog_response import GoogleCloudServicebrokerV1beta1ListCatalogResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_list_service_instances_response import GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse
from openapi_server.models.google_cloud_servicebroker_v1beta1_operation import GoogleCloudServicebrokerV1beta1Operation
from openapi_server.models.google_cloud_servicebroker_v1beta1_service_instance import GoogleCloudServicebrokerV1beta1ServiceInstance
from openapi_server.models.google_cloud_servicebroker_v1beta1_update_service_instance_response import GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_create(client):
    """Test case for servicebroker_projects_brokers_create

    
    """
    body = openapi_server.GoogleCloudServicebrokerV1beta1Broker()
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/brokers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_instances_bindings_list(client):
    """Test case for servicebroker_projects_brokers_instances_bindings_list

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/bindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_instances_list(client):
    """Test case for servicebroker_projects_brokers_instances_list

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_list(client):
    """Test case for servicebroker_projects_brokers_list

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/brokers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_catalog_list(client):
    """Test case for servicebroker_projects_brokers_v2_catalog_list

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/v2/catalog'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_create(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_create

    
    """
    body = openapi_server.GoogleCloudServicebrokerV1beta1ServiceInstance()
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('acceptsIncomplete', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1beta1/{parent}/v2/service_instances/{instance_id}'.format(parent='parent_example', instance_id='instance_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_patch(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_patch

    
    """
    body = openapi_server.GoogleCloudServicebrokerV1beta1ServiceInstance()
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('acceptsIncomplete', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_service_bindings_create(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_service_bindings_create

    
    """
    body = openapi_server.GoogleCloudServicebrokerV1beta1Binding()
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('acceptsIncomplete', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1beta1/{parent}/service_bindings/{binding_id}'.format(parent='parent_example', binding_id='binding_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_service_bindings_delete(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_service_bindings_delete

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('acceptsIncomplete', True),
                    ('planId', 'plan_id_example'),
                    ('serviceId', 'service_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_service_bindings_get(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_service_bindings_get

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('planId', 'plan_id_example'),
                    ('serviceId', 'service_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_service_bindings_get_last_operation(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_service_bindings_get_last_operation

    
    """
    params = [('fields', 'fields_example'),
                    ('uploadType', 'upload_type_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('access_token', 'access_token_example'),
                    ('key', 'key_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('operation', 'operation_example'),
                    ('planId', 'plan_id_example'),
                    ('serviceId', 'service_id_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/last_operation'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

