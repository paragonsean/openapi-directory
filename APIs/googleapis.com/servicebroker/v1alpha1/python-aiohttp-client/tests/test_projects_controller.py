# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_servicebroker_v1alpha1_binding import GoogleCloudServicebrokerV1alpha1Binding
from openapi_server.models.google_cloud_servicebroker_v1alpha1_create_binding_response import GoogleCloudServicebrokerV1alpha1CreateBindingResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_delete_service_instance_response import GoogleCloudServicebrokerV1alpha1DeleteServiceInstanceResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_list_bindings_response import GoogleCloudServicebrokerV1alpha1ListBindingsResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_list_catalog_response import GoogleCloudServicebrokerV1alpha1ListCatalogResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_list_service_instances_response import GoogleCloudServicebrokerV1alpha1ListServiceInstancesResponse
from openapi_server.models.google_cloud_servicebroker_v1alpha1_operation import GoogleCloudServicebrokerV1alpha1Operation
from openapi_server.models.google_cloud_servicebroker_v1alpha1_service_instance import GoogleCloudServicebrokerV1alpha1ServiceInstance


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_instances_service_bindings_list(client):
    """Test case for servicebroker_projects_brokers_instances_service_bindings_list

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/service_bindings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_service_instances_list(client):
    """Test case for servicebroker_projects_brokers_service_instances_list

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/service_instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_catalog_list(client):
    """Test case for servicebroker_projects_brokers_v2_catalog_list

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{parent}/v2/catalog'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_delete(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_delete

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
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
        path='/v1alpha1/{parent}/v2/service_instances/{instance_id}'.format(parent='parent_example', instance_id='instance_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_get(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_get

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_get_last_operation(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_get_last_operation

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
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
        path='/v1alpha1/{parent}/v2/service_instances/{instance_id}/last_operation'.format(parent='parent_example', instance_id='instance_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_service_bindings_create(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_service_bindings_create

    
    """
    body = openapi_server.GoogleCloudServicebrokerV1alpha1Binding()
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
                    ('acceptsIncomplete', True)]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1alpha1/{parent}/v2/service_instances/{instance_id}/service_bindings/{binding_id}'.format(parent='parent_example', instance_id='instance_id_example', binding_id='binding_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servicebroker_projects_brokers_v2_service_instances_service_bindings_get_last_operation(client):
    """Test case for servicebroker_projects_brokers_v2_service_instances_service_bindings_get_last_operation

    
    """
    params = [('upload_protocol', 'upload_protocol_example'),
                    ('quotaUser', 'quota_user_example'),
                    ('prettyPrint', True),
                    ('uploadType', 'upload_type_example'),
                    ('fields', 'fields_example'),
                    ('callback', 'param_callback_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('$.xgafv', 'xgafv_example'),
                    ('alt', json),
                    ('key', 'key_example'),
                    ('access_token', 'access_token_example'),
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
        path='/v1alpha1/{parent}/v2/service_instances/{instance_id}/service_bindings/{binding_id}/last_operation'.format(parent='parent_example', instance_id='instance_id_example', binding_id='binding_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

