# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_create_instance_request import GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateInstanceRequest
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_create_worker_pool_request import GoogleDevtoolsRemotebuildexecutionAdminV1alphaCreateWorkerPoolRequest
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_list_instances_response import GoogleDevtoolsRemotebuildexecutionAdminV1alphaListInstancesResponse
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_list_worker_pools_response import GoogleDevtoolsRemotebuildexecutionAdminV1alphaListWorkerPoolsResponse
from openapi_server.models.google_devtools_remotebuildexecution_admin_v1alpha_update_worker_pool_request import GoogleDevtoolsRemotebuildexecutionAdminV1alphaUpdateWorkerPoolRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_create(client):
    """Test case for remotebuildexecution_projects_instances_create

    
    """
    body = {"parent":"parent","instance":{"loggingEnabled":True,"featurePolicy":{"linuxExecution":"LINUX_EXECUTION_UNSPECIFIED","actionHermeticity":"ACTION_HERMETICITY_UNSPECIFIED","vmVerification":"VM_VERIFICATION_UNSPECIFIED","dockerChrootPath":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"dockerSiblingContainers":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"actionIsolation":"ACTION_ISOLATION_UNSPECIFIED","dockerRuntime":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"windowsExecution":"WINDOWS_EXECUTION_UNSPECIFIED","macExecution":"MAC_EXECUTION_UNSPECIFIED","dockerNetwork":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"linuxIsolation":"LINUX_ISOLATION_UNSPECIFIED","containerImageSources":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"dockerPrivileged":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"dockerUlimits":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"dockerRunAsRoot":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"dockerAddCapabilities":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"},"dockerRunAsContainerProvidedUser":{"allowedValues":["allowedValues","allowedValues"],"policy":"POLICY_UNSPECIFIED"}},"name":"name","location":"location","state":"STATE_UNSPECIFIED","schedulerNotificationConfig":{"topic":"topic"}},"instanceId":"instanceId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_list(client):
    """Test case for remotebuildexecution_projects_instances_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{parent}/instances'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_test_notify(client):
    """Test case for remotebuildexecution_projects_instances_test_notify

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{nametest_notif}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_workerpools_create(client):
    """Test case for remotebuildexecution_projects_instances_workerpools_create

    
    """
    body = {"parent":"parent","poolId":"poolId","workerPool":{"workerCount":"workerCount","hostOs":"hostOs","channel":"channel","name":"name","state":"STATE_UNSPECIFIED","autoscale":{"minIdleWorkers":"minIdleWorkers","maxSize":"maxSize","minSize":"minSize"},"workerConfig":{"soleTenantNodeType":"soleTenantNodeType","accelerator":{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount"},"attachedDisks":{"localSsd":{"sizeGb":"sizeGb","count":"count"},"dockerRootDisk":{"diskType":"diskType","sourceImage":"sourceImage","diskSizeGb":"diskSizeGb"}},"zones":["zones","zones"],"labels":{"key":"labels"},"maxConcurrentActions":"maxConcurrentActions","networkAccess":"networkAccess","vmImage":"vmImage","minCpuPlatform":"minCpuPlatform","reserved":True,"diskType":"diskType","userServiceAccounts":["userServiceAccounts","userServiceAccounts"],"machineType":"machineType","diskSizeGb":"diskSizeGb"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1alpha/{parent}/workerpools'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_workerpools_delete(client):
    """Test case for remotebuildexecution_projects_instances_workerpools_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_workerpools_list(client):
    """Test case for remotebuildexecution_projects_instances_workerpools_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{parent}/workerpools'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_instances_workerpools_patch(client):
    """Test case for remotebuildexecution_projects_instances_workerpools_patch

    
    """
    body = {"updateMask":"updateMask","workerPool":{"workerCount":"workerCount","hostOs":"hostOs","channel":"channel","name":"name","state":"STATE_UNSPECIFIED","autoscale":{"minIdleWorkers":"minIdleWorkers","maxSize":"maxSize","minSize":"minSize"},"workerConfig":{"soleTenantNodeType":"soleTenantNodeType","accelerator":{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount"},"attachedDisks":{"localSsd":{"sizeGb":"sizeGb","count":"count"},"dockerRootDisk":{"diskType":"diskType","sourceImage":"sourceImage","diskSizeGb":"diskSizeGb"}},"zones":["zones","zones"],"labels":{"key":"labels"},"maxConcurrentActions":"maxConcurrentActions","networkAccess":"networkAccess","vmImage":"vmImage","minCpuPlatform":"minCpuPlatform","reserved":True,"diskType":"diskType","userServiceAccounts":["userServiceAccounts","userServiceAccounts"],"machineType":"machineType","diskSizeGb":"diskSizeGb"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('loggingEnabled', True),
                    ('name1', 'name1_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remotebuildexecution_projects_operations_get(client):
    """Test case for remotebuildexecution_projects_operations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1alpha/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

