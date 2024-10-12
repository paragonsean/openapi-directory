# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.job import Job
from openapi_server.models.list_jobs_response import ListJobsResponse


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_create(client):
    """Test case for run_namespaces_jobs_create

    
    """
    body = {"metadata":{"generation":6,"finalizers":["finalizers","finalizers"],"resourceVersion":"resourceVersion","annotations":{"key":"annotations"},"generateName":"generateName","deletionTimestamp":"deletionTimestamp","labels":{"key":"labels"},"ownerReferences":[{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True},{"uid":"uid","controller":True,"apiVersion":"apiVersion","kind":"kind","name":"name","blockOwnerDeletion":True}],"selfLink":"selfLink","deletionGracePeriodSeconds":0,"uid":"uid","clusterName":"clusterName","creationTimestamp":"creationTimestamp","name":"name","namespace":"namespace"},"apiVersion":"apiVersion","kind":"kind","spec":{"template":{"spec":{"terminationGracePeriodSeconds":"terminationGracePeriodSeconds","serviceAccountName":"serviceAccountName","volumes":[{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":6,"path":"path","key":"key"},{"mode":6,"path":"path","key":"key"}]},"name":"name","secret":{"secretName":"secretName","defaultMode":7,"optional":True,"items":[{"mode":6,"path":"path","key":"key"},{"mode":6,"path":"path","key":"key"}]}},{"configMap":{"defaultMode":1,"name":"name","optional":True,"items":[{"mode":6,"path":"path","key":"key"},{"mode":6,"path":"path","key":"key"}]},"name":"name","secret":{"secretName":"secretName","defaultMode":7,"optional":True,"items":[{"mode":6,"path":"path","key":"key"},{"mode":6,"path":"path","key":"key"}]}}],"containers":[{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":2,"periodSeconds":3,"tcpSocket":{"port":4,"host":"host"},"timeoutSeconds":7,"successThreshold":2,"initialDelaySeconds":9,"exec":{"command":["command","command"]},"grpc":{"port":7,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":1},"startupProbe":{"failureThreshold":2,"periodSeconds":3,"tcpSocket":{"port":4,"host":"host"},"timeoutSeconds":7,"successThreshold":2,"initialDelaySeconds":9,"exec":{"command":["command","command"]},"grpc":{"port":7,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":1},{"protocol":"protocol","name":"name","containerPort":1}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":2,"periodSeconds":3,"tcpSocket":{"port":4,"host":"host"},"timeoutSeconds":7,"successThreshold":2,"initialDelaySeconds":9,"exec":{"command":["command","command"]},"grpc":{"port":7,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]},{"image":"image","imagePullPolicy":"imagePullPolicy","livenessProbe":{"failureThreshold":2,"periodSeconds":3,"tcpSocket":{"port":4,"host":"host"},"timeoutSeconds":7,"successThreshold":2,"initialDelaySeconds":9,"exec":{"command":["command","command"]},"grpc":{"port":7,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"terminationMessagePolicy":"terminationMessagePolicy","terminationMessagePath":"terminationMessagePath","workingDir":"workingDir","resources":{"requests":{"key":"requests"},"limits":{"key":"limits"}},"securityContext":{"runAsUser":1},"startupProbe":{"failureThreshold":2,"periodSeconds":3,"tcpSocket":{"port":4,"host":"host"},"timeoutSeconds":7,"successThreshold":2,"initialDelaySeconds":9,"exec":{"command":["command","command"]},"grpc":{"port":7,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"env":[{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}},{"name":"name","value":"value","valueFrom":{"secretKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"},"configMapKeyRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True,"key":"key"}}}],"ports":[{"protocol":"protocol","name":"name","containerPort":1},{"protocol":"protocol","name":"name","containerPort":1}],"command":["command","command"],"volumeMounts":[{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"},{"mountPath":"mountPath","name":"name","readOnly":True,"subPath":"subPath"}],"args":["args","args"],"name":"name","readinessProbe":{"failureThreshold":2,"periodSeconds":3,"tcpSocket":{"port":4,"host":"host"},"timeoutSeconds":7,"successThreshold":2,"initialDelaySeconds":9,"exec":{"command":["command","command"]},"grpc":{"port":7,"service":"service"},"httpGet":{"path":"path","scheme":"scheme","host":"host","httpHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}]}},"envFrom":[{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}},{"configMapRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True},"prefix":"prefix","secretRef":{"localObjectReference":{"name":"name"},"name":"name","optional":True}}]}],"restartPolicy":"restartPolicy","activeDeadlineSeconds":"activeDeadlineSeconds"}},"backoffLimit":1,"parallelism":5,"completions":5,"activeDeadlineSeconds":"activeDeadlineSeconds","ttlSecondsAfterFinished":1},"status":{"completionTime":"completionTime","instances":[{"completionTime":"completionTime","restarted":6,"lastExitCode":9,"index":9,"startTime":"startTime","failed":9,"lastAttemptResult":{"exitCode":6,"status":{"code":8,"details":[{"key":""},{"key":""}],"message":"message"}},"succeeded":3},{"completionTime":"completionTime","restarted":6,"lastExitCode":9,"index":9,"startTime":"startTime","failed":9,"lastAttemptResult":{"exitCode":6,"status":{"code":8,"details":[{"key":""},{"key":""}],"message":"message"}},"succeeded":3}],"active":4,"startTime":"startTime","failed":5,"conditions":[{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"},{"severity":"severity","reason":"reason","lastTransitionTime":"lastTransitionTime","message":"message","type":"type","status":"status"}],"observedGeneration":6,"imageDigest":"imageDigest","succeeded":1}}
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
        path='/apis/run.googleapis.com/v1alpha1/{parent}/jobs'.format(parent='parent_example'),
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
        path='/apis/run.googleapis.com/v1alpha1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_namespaces_jobs_get(client):
    """Test case for run_namespaces_jobs_get

    
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
        path='/apis/run.googleapis.com/v1alpha1/{name}'.format(name='name_example'),
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
        path='/apis/run.googleapis.com/v1alpha1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

