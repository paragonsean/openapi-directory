# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_bit_locker_keys_response import GetBitLockerKeysResponse
from openapi_server.models.job_response import JobResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.location import Location
from openapi_server.models.locations_response import LocationsResponse
from openapi_server.models.put_job_parameters import PutJobParameters
from openapi_server.models.update_job_parameters import UpdateJobParameters


pytestmark = pytest.mark.asyncio

async def test_bit_locker_keys_list(client):
    """Test case for bit_locker_keys_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ImportExport/jobs/{job_name}/listBitLockerKeys'.format(job_name='job_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_create(client):
    """Test case for jobs_create

    
    """
    body = {"location":"location","properties":{"storageAccountId":"storageAccountId","incompleteBlobListUri":"incompleteBlobListUri","percentComplete":5,"provisioningState":"provisioningState","returnAddress":{"countryOrRegion":"countryOrRegion","stateOrProvince":"stateOrProvince","city":"city","phone":"phone","postalCode":"postalCode","streetAddress1":"streetAddress1","recipientName":"recipientName","streetAddress2":"streetAddress2","email":"email"},"returnPackage":{"carrierName":"carrierName","driveCount":0,"shipDate":"shipDate","trackingNumber":"trackingNumber"},"deliveryPackage":{"carrierName":"carrierName","driveCount":0,"shipDate":"shipDate","trackingNumber":"trackingNumber"},"logLevel":"logLevel","returnShipping":{"carrierName":"carrierName","carrierAccountNumber":"carrierAccountNumber"},"diagnosticsPath":"diagnosticsPath","driveList":[{"manifestFile":"manifestFile","driveId":"driveId","bitLockerKey":"bitLockerKey","manifestHash":"manifestHash","bytesSucceeded":6,"driveHeaderHash":"driveHeaderHash","manifestUri":"manifestUri","percentComplete":1,"state":"Specified","copyStatus":"copyStatus","errorLogUri":"errorLogUri","verboseLogUri":"verboseLogUri"},{"manifestFile":"manifestFile","driveId":"driveId","bitLockerKey":"bitLockerKey","manifestHash":"manifestHash","bytesSucceeded":6,"driveHeaderHash":"driveHeaderHash","manifestUri":"manifestUri","percentComplete":1,"state":"Specified","copyStatus":"copyStatus","errorLogUri":"errorLogUri","verboseLogUri":"verboseLogUri"}],"shippingInformation":{"countryOrRegion":"countryOrRegion","stateOrProvince":"stateOrProvince","city":"city","phone":"phone","postalCode":"postalCode","streetAddress1":"streetAddress1","recipientName":"recipientName","streetAddress2":"streetAddress2"},"backupDriveManifest":True,"state":"state","cancelRequested":True,"jobType":"jobType","export":{"blobListblobPath":"blobListblobPath","blobList":{"blobPathPrefix":["blobPathPrefix","blobPathPrefix"],"blobPath":["blobPath","blobPath"]}}},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'x_ms_client_tenant_id': 'x_ms_client_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ImportExport/jobs/{job_name}'.format(job_name='job_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_delete(client):
    """Test case for jobs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ImportExport/jobs/{job_name}'.format(job_name='job_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ImportExport/jobs/{job_name}'.format(job_name='job_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_by_resource_group(client):
    """Test case for jobs_list_by_resource_group

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ImportExport/jobs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_by_subscription(client):
    """Test case for jobs_list_by_subscription

    
    """
    params = [('$top', 56),
                    ('$filter', 'filter_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ImportExport/jobs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_update(client):
    """Test case for jobs_update

    
    """
    body = {"properties":{"deliveryPackage":{"carrierName":"carrierName","driveCount":0,"shipDate":"shipDate","trackingNumber":"trackingNumber"},"logLevel":"logLevel","returnShipping":{"carrierName":"carrierName","carrierAccountNumber":"carrierAccountNumber"},"driveList":[{"manifestFile":"manifestFile","driveId":"driveId","bitLockerKey":"bitLockerKey","manifestHash":"manifestHash","bytesSucceeded":6,"driveHeaderHash":"driveHeaderHash","manifestUri":"manifestUri","percentComplete":1,"state":"Specified","copyStatus":"copyStatus","errorLogUri":"errorLogUri","verboseLogUri":"verboseLogUri"},{"manifestFile":"manifestFile","driveId":"driveId","bitLockerKey":"bitLockerKey","manifestHash":"manifestHash","bytesSucceeded":6,"driveHeaderHash":"driveHeaderHash","manifestUri":"manifestUri","percentComplete":1,"state":"Specified","copyStatus":"copyStatus","errorLogUri":"errorLogUri","verboseLogUri":"verboseLogUri"}],"backupDriveManifest":True,"state":"state","cancelRequested":True,"returnAddress":{"countryOrRegion":"countryOrRegion","stateOrProvince":"stateOrProvince","city":"city","phone":"phone","postalCode":"postalCode","streetAddress1":"streetAddress1","recipientName":"recipientName","streetAddress2":"streetAddress2","email":"email"}},"tags":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ImportExport/jobs/{job_name}'.format(job_name='job_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_get(client):
    """Test case for locations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ImportExport/locations/{location_name}'.format(location_name='location_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_locations_list(client):
    """Test case for locations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ImportExport/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_operations_list(client):
    """Test case for operations_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ImportExport/operations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

