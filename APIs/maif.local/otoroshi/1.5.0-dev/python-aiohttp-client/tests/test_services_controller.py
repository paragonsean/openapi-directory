# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.deleted import Deleted
from openapi_server.models.error_template import ErrorTemplate
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.service import Service
from openapi_server.models.target import Target


pytestmark = pytest.mark.asyncio

async def test_all_services(client):
    """Test case for all_services

    Get all services
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_service(client):
    """Test case for create_service

    Create a new service descriptor
    """
    body = {"metadata":{"key":"value"},"cors":{"excludedPatterns":["a string value","a string value"],"allowMethods":["a string value","a string value"],"allowHeaders":["a string value","a string value"],"exposeHeaders":["a string value","a string value"],"maxAge":123123,"allowCredentials":True,"enabled":True,"allowOrigin":"a string value"},"forceHttps":True,"matchingRoot":"a string value","buildMode":True,"chaosConfig":{"badResponsesFaultConfig":{"responses":[{"headers":{"key":"value"},"body":"a string value","status":123123},{"headers":{"key":"value"},"body":"a string value","status":123123}],"ratio":42.2},"largeResponseFaultConfig":{"additionalRequestSize":123123,"ratio":42.2},"latencyInjectionFaultConfig":{"from":123123,"to":123123,"ratio":42.2},"largeRequestFaultConfig":{"additionalRequestSize":123123,"ratio":42.2},"enabled":True},"secComSettings":{"size":123123,"secret":"a string value","type":"a string value"},"targets":[{"scheme":"a string value","host":"www.google.com"},{"scheme":"a string value","host":"www.google.com"}],"enabled":True,"localHost":"a string value","root":"a string value","additionalHeaders":{"key":"value"},"api":{"exposeApi":True,"openApiDescriptorUrl":"http://www.google.com"},"id":"110e8400-e29b-11d4-a716-446655440000","ipFiltering":{"blacklist":["192.192.192.192","192.192.192.192"],"whitelist":["192.192.192.192","192.192.192.192"]},"sendOtoroshiHeadersBack":True,"redirection":{"code":123123,"to":"a string value","enabled":True},"headersVerification":{"key":"value"},"redirectToLocal":True,"userFacing":True,"authConfigRef":"a string value","secComExcludedPatterns":["a string value","a string value"],"xForwardedHeaders":True,"transformerRef":"a string value","Canary":{"root":"a string value","targets":[{"scheme":"a string value","host":"www.google.com"},{"scheme":"a string value","host":"www.google.com"}],"enabled":True,"traffic":123123},"groups":["a string value"],"privatePatterns":["a string value","a string value"],"gzip":{"excludedPatterns":["a string value","a string value"],"blackList":["a string value","a string value"],"whiteList":["a string value","a string value"],"chunkedThreshold":123,"compressionLevel":123123,"enabled":True,"bufferSize":123},"clientConfig":{"retries":123123,"sampleInterval":123123,"useCircuitBreaker":True,"backoffFactor":123123,"maxErrors":123123,"retryInitialDelay":123123,"callTimeout":123123,"globalTimeout":123123},"env":"a string value","enforceSecureCommunication":True,"jwtVerifier":{"algoSettings":{"size":123123,"secret":"a string value","type":"a string value"},"source":{"name":"a string value","type":"a string value"},"strategy":{"verificationSettings":{"mappingSettings":{"values":{"key":"value"},"map":{"key":"value"},"remove":["a string value","a string value"]},"fields":{"key":"value"}},"type":"a string value"},"strict":True,"type":"a string value","enabled":True},"clientValidatorRef":"a string value","publicPatterns":["a string value","a string value"],"localScheme":"a string value","privateApp":True,"domain":"a string value","healthCheck":{"enabled":True,"url":"http://www.google.com"},"name":"a string value","statsdConfig":{"port":123123,"datadog":True,"host":"a string value"},"matchingHeaders":{"key":"value"},"subdomain":"a string value","overrideHost":True,"maintenanceMode":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/services',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_service_template(client):
    """Test case for create_service_template

    Create a service descriptor error template
    """
    body = {"templateMaintenance":"a string value","templateBuild":"a string value","messages":{"key":"value"},"template50x":"a string value","template40x":"a string value","serviceId":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/services/{service_id}/template'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service(client):
    """Test case for delete_service

    Delete a service descriptor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_service_template(client):
    """Test case for delete_service_template

    Delete a service descriptor error template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/services/{service_id}/template'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_service(client):
    """Test case for patch_service

    Update a service descriptor with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service(client):
    """Test case for service

    Get a service descriptor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_add_target(client):
    """Test case for service_add_target

    Add a target to a service descriptor
    """
    body = {"scheme":"a string value","host":"www.google.com"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/services/{service_id}/targets'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_delete_target(client):
    """Test case for service_delete_target

    Delete a service descriptor target
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/services/{service_id}/targets'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_group_services(client):
    """Test case for service_group_services

    Get all services descriptor for a group
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/groups/{service_group_id}/services'.format(service_group_id='service_group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_targets(client):
    """Test case for service_targets

    Get a service descriptor targets
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}/targets'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_service_template(client):
    """Test case for service_template

    Get a service descriptor error template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/services/{service_id}/template'.format(service_id='service_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_service(client):
    """Test case for update_service

    Update a service descriptor
    """
    body = {"metadata":{"key":"value"},"cors":{"excludedPatterns":["a string value","a string value"],"allowMethods":["a string value","a string value"],"allowHeaders":["a string value","a string value"],"exposeHeaders":["a string value","a string value"],"maxAge":123123,"allowCredentials":True,"enabled":True,"allowOrigin":"a string value"},"forceHttps":True,"matchingRoot":"a string value","buildMode":True,"chaosConfig":{"badResponsesFaultConfig":{"responses":[{"headers":{"key":"value"},"body":"a string value","status":123123},{"headers":{"key":"value"},"body":"a string value","status":123123}],"ratio":42.2},"largeResponseFaultConfig":{"additionalRequestSize":123123,"ratio":42.2},"latencyInjectionFaultConfig":{"from":123123,"to":123123,"ratio":42.2},"largeRequestFaultConfig":{"additionalRequestSize":123123,"ratio":42.2},"enabled":True},"secComSettings":{"size":123123,"secret":"a string value","type":"a string value"},"targets":[{"scheme":"a string value","host":"www.google.com"},{"scheme":"a string value","host":"www.google.com"}],"enabled":True,"localHost":"a string value","root":"a string value","additionalHeaders":{"key":"value"},"api":{"exposeApi":True,"openApiDescriptorUrl":"http://www.google.com"},"id":"110e8400-e29b-11d4-a716-446655440000","ipFiltering":{"blacklist":["192.192.192.192","192.192.192.192"],"whitelist":["192.192.192.192","192.192.192.192"]},"sendOtoroshiHeadersBack":True,"redirection":{"code":123123,"to":"a string value","enabled":True},"headersVerification":{"key":"value"},"redirectToLocal":True,"userFacing":True,"authConfigRef":"a string value","secComExcludedPatterns":["a string value","a string value"],"xForwardedHeaders":True,"transformerRef":"a string value","Canary":{"root":"a string value","targets":[{"scheme":"a string value","host":"www.google.com"},{"scheme":"a string value","host":"www.google.com"}],"enabled":True,"traffic":123123},"groups":["a string value"],"privatePatterns":["a string value","a string value"],"gzip":{"excludedPatterns":["a string value","a string value"],"blackList":["a string value","a string value"],"whiteList":["a string value","a string value"],"chunkedThreshold":123,"compressionLevel":123123,"enabled":True,"bufferSize":123},"clientConfig":{"retries":123123,"sampleInterval":123123,"useCircuitBreaker":True,"backoffFactor":123123,"maxErrors":123123,"retryInitialDelay":123123,"callTimeout":123123,"globalTimeout":123123},"env":"a string value","enforceSecureCommunication":True,"jwtVerifier":{"algoSettings":{"size":123123,"secret":"a string value","type":"a string value"},"source":{"name":"a string value","type":"a string value"},"strategy":{"verificationSettings":{"mappingSettings":{"values":{"key":"value"},"map":{"key":"value"},"remove":["a string value","a string value"]},"fields":{"key":"value"}},"type":"a string value"},"strict":True,"type":"a string value","enabled":True},"clientValidatorRef":"a string value","publicPatterns":["a string value","a string value"],"localScheme":"a string value","privateApp":True,"domain":"a string value","healthCheck":{"enabled":True,"url":"http://www.google.com"},"name":"a string value","statsdConfig":{"port":123123,"datadog":True,"host":"a string value"},"matchingHeaders":{"key":"value"},"subdomain":"a string value","overrideHost":True,"maintenanceMode":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/services/{service_id}'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_service_targets(client):
    """Test case for update_service_targets

    Update a service descriptor targets
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/services/{service_id}/targets'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_service_template(client):
    """Test case for update_service_template

    Update an error template to a service descriptor
    """
    body = {"templateMaintenance":"a string value","templateBuild":"a string value","messages":{"key":"value"},"template50x":"a string value","template40x":"a string value","serviceId":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/services/{service_id}/template'.format(service_id='service_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

