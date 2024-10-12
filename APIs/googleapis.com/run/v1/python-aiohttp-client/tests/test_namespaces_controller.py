# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.domain_mapping import DomainMapping
from openapi_server.models.execution import Execution
from openapi_server.models.job import Job
from openapi_server.models.list_authorized_domains_response import ListAuthorizedDomainsResponse
from openapi_server.models.list_configurations_response import ListConfigurationsResponse
from openapi_server.models.list_domain_mappings_response import ListDomainMappingsResponse
from openapi_server.models.list_executions_response import ListExecutionsResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_revisions_response import ListRevisionsResponse
from openapi_server.models.list_routes_response import ListRoutesResponse
from openapi_server.models.list_services_response import ListServicesResponse
from openapi_server.models.list_tasks_response import ListTasksResponse
from openapi_server.models.run_job_request import RunJobRequest
from openapi_server.models.service import Service
from openapi_server.models.status import Status
from openapi_server.models.task import Task


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_authorizeddomains_list(client):
    """Test case for run_namespaces_authorizeddomains_list

    
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
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/domains.cloudrun.com/v1/{parent}/authorizeddomains'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_configurations_list(client):
    """Test case for run_namespaces_configurations_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/serving.knative.dev/v1/{parent}/configurations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_domainmappings_create(client):
    """Test case for run_namespaces_domainmappings_create

    
    """
    body = {"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"apiVersion":"apiVersion","kind":"kind","spec":{"certificateMode":"CERTIFICATE_MODE_UNSPECIFIED","forceOverride":True,"routeName":"routeName"},"status":{"mappedRouteName":"mappedRouteName","resourceRecords":[{"rrdata":"rrdata","name":"name","type":"RECORD_TYPE_UNSPECIFIED"},{"rrdata":"rrdata","name":"name","type":"RECORD_TYPE_UNSPECIFIED"}],"conditions":[{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"},{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"}],"observedGeneration":1,"url":"url"}}
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
                    ('dryRun', 'dry_run_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/domains.cloudrun.com/v1/{parent}/domainmappings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_domainmappings_delete(client):
    """Test case for run_namespaces_domainmappings_delete

    
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
                    ('apiVersion', 'api_version_example'),
                    ('dryRun', 'dry_run_example'),
                    ('kind', 'kind_example'),
                    ('propagationPolicy', 'propagation_policy_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/domains.cloudrun.com/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_domainmappings_get(client):
    """Test case for run_namespaces_domainmappings_get

    
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
        path='/apis/domains.cloudrun.com/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_domainmappings_list(client):
    """Test case for run_namespaces_domainmappings_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/domains.cloudrun.com/v1/{parent}/domainmappings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_executions_cancel(client):
    """Test case for run_namespaces_executions_cancel

    
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
        path='/apis/run.googleapis.com/v1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_executions_list(client):
    """Test case for run_namespaces_executions_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/run.googleapis.com/v1/{parent}/executions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_create(client):
    """Test case for run_namespaces_jobs_create

    
    """
    body = {"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"apiVersion":"apiVersion","kind":"kind","spec":{"template":{"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"spec":{"template":{"spec":{"maxRetries":1,"serviceAccountName":"serviceAccountName","volumes":[{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}},{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}}],"timeoutSeconds":"timeoutSeconds","containers":[{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]},{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]}]}},"taskCount":6,"parallelism":0}}},"status":{"executionCount":0,"conditions":[{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"},{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"}],"latestCreatedExecution":{"completionTimestamp":"completionTimestamp","creationTimestamp":"creationTimestamp","name":"name"},"observedGeneration":6}}
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
        path='/apis/run.googleapis.com/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_delete(client):
    """Test case for run_namespaces_jobs_delete

    
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
                    ('apiVersion', 'api_version_example'),
                    ('kind', 'kind_example'),
                    ('propagationPolicy', 'propagation_policy_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/run.googleapis.com/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_list(client):
    """Test case for run_namespaces_jobs_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/run.googleapis.com/v1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_replace_job(client):
    """Test case for run_namespaces_jobs_replace_job

    
    """
    body = {"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"apiVersion":"apiVersion","kind":"kind","spec":{"template":{"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"spec":{"template":{"spec":{"maxRetries":1,"serviceAccountName":"serviceAccountName","volumes":[{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}},{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}}],"timeoutSeconds":"timeoutSeconds","containers":[{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]},{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]}]}},"taskCount":6,"parallelism":0}}},"status":{"executionCount":0,"conditions":[{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"},{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"}],"latestCreatedExecution":{"completionTimestamp":"completionTimestamp","creationTimestamp":"creationTimestamp","name":"name"},"observedGeneration":6}}
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
        method='PUT',
        path='/apis/run.googleapis.com/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_run(client):
    """Test case for run_namespaces_jobs_run

    
    """
    body = {"overrides":{"taskCount":0,"containerOverrides":[{"args":["args","args"],"name":"name","env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"clearArgs":True},{"args":["args","args"],"name":"name","env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"clearArgs":True}],"timeoutSeconds":6}}
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
        path='/apis/run.googleapis.com/v1/{nameru}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_revisions_list(client):
    """Test case for run_namespaces_revisions_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/serving.knative.dev/v1/{parent}/revisions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_routes_list(client):
    """Test case for run_namespaces_routes_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/serving.knative.dev/v1/{parent}/routes'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_services_create(client):
    """Test case for run_namespaces_services_create

    
    """
    body = {"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"apiVersion":"apiVersion","kind":"kind","spec":{"template":{"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"spec":{"containerConcurrency":0,"enableServiceLinks":True,"serviceAccountName":"serviceAccountName","imagePullSecrets":[{"name":"name"},{"name":"name"}],"volumes":[{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}},{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}}],"timeoutSeconds":6,"containers":[{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]},{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]}]}},"traffic":[{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"},{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"}]},"status":{"address":{"url":"url"},"latestCreatedRevisionName":"latestCreatedRevisionName","conditions":[{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"},{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"}],"latestReadyRevisionName":"latestReadyRevisionName","observedGeneration":5,"url":"url","traffic":[{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"},{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"}]}}
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
                    ('dryRun', 'dry_run_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/apis/serving.knative.dev/v1/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_services_delete(client):
    """Test case for run_namespaces_services_delete

    
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
                    ('apiVersion', 'api_version_example'),
                    ('dryRun', 'dry_run_example'),
                    ('kind', 'kind_example'),
                    ('propagationPolicy', 'propagation_policy_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/apis/serving.knative.dev/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_services_get(client):
    """Test case for run_namespaces_services_get

    
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
        path='/apis/serving.knative.dev/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_services_list(client):
    """Test case for run_namespaces_services_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/serving.knative.dev/v1/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_services_replace_service(client):
    """Test case for run_namespaces_services_replace_service

    
    """
    body = {"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"apiVersion":"apiVersion","kind":"kind","spec":{"template":{"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"spec":{"containerConcurrency":0,"enableServiceLinks":True,"serviceAccountName":"serviceAccountName","imagePullSecrets":[{"name":"name"},{"name":"name"}],"volumes":[{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}},{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]},"emptyDir":{"sizeLimit":"sizeLimit","medium":"medium"},"csi":{"driver":"driver","readOnly":True,"volumeAttributes":{"key":"volumeAttributes"}},"name":"name","nfs":{"path":"path","server":"server","readOnly":True},"secret":{"secretName":"secretName","defaultMode":6,"optional":True,"items":[{"mode":1,"path":"path","key":"key"},{"mode":1,"path":"path","key":"key"}]}}],"timeoutSeconds":6,"containers":[{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]},{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":7},"startupProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":4},{"protocol":"protocol","name":"name","containerPort":4}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":1,"periodSeconds":7,"tcpSocket":{"port":3,"host":"host"},"timeoutSeconds":2,"successThreshold":9,"initialDelaySeconds":2,"exec":{"command":["command","command"]},"grpc":{"port":5,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","port":5,"host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]}]}},"traffic":[{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"},{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"}]},"status":{"address":{"url":"url"},"latestCreatedRevisionName":"latestCreatedRevisionName","conditions":[{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"},{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"}],"latestReadyRevisionName":"latestReadyRevisionName","observedGeneration":5,"url":"url","traffic":[{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"},{"revisionName":"revisionName","configurationName":"configurationName","tag":"tag","latestRevision":True,"percent":1,"url":"url"}]}}
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
                    ('dryRun', 'dry_run_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/apis/serving.knative.dev/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_tasks_get(client):
    """Test case for run_namespaces_tasks_get

    
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
        path='/apis/run.googleapis.com/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_tasks_list(client):
    """Test case for run_namespaces_tasks_list

    
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
                    ('continue', '_continue_example'),
                    ('fieldSelector', 'field_selector_example'),
                    ('includeUninitialized', True),
                    ('labelSelector', 'label_selector_example'),
                    ('limit', 56),
                    ('resourceVersion', 'resource_version_example'),
                    ('watch', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/apis/run.googleapis.com/v1/{parent}/tasks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

