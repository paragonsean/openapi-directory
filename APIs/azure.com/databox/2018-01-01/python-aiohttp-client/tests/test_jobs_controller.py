# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancellation_reason import CancellationReason
from openapi_server.models.job_resource import JobResource
from openapi_server.models.job_resource_list import JobResourceList
from openapi_server.models.job_resource_update_parameter import JobResourceUpdateParameter
from openapi_server.models.shipment_pick_up_request import ShipmentPickUpRequest
from openapi_server.models.shipment_pick_up_response import ShipmentPickUpResponse
from openapi_server.models.unencrypted_credentials_list import UnencryptedCredentialsList


pytestmark = pytest.mark.asyncio

async def test_jobs_book_shipment_pick_up(client):
    """Test case for jobs_book_shipment_pick_up

    
    """
    shipment_pick_up_request = {"shipmentLocation":"shipmentLocation","startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}/bookShipmentPickUp'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        json=shipment_pick_up_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_cancel(client):
    """Test case for jobs_cancel

    
    """
    cancellation_reason = {"reason":"reason"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}/cancel'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        json=cancellation_reason,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_create(client):
    """Test case for jobs_create

    
    """
    job_resource = {"name":"name","id":"id","type":"type","properties":{"isDeletable":True,"cancellationReason":"cancellationReason","isCancellable":True,"details":{"preferences":{"preferredDataCenterRegion":["preferredDataCenterRegion","preferredDataCenterRegion"]},"destinationAccountDetails":[{"accountId":"accountId","dataDestinationType":"UnknownType"},{"accountId":"accountId","dataDestinationType":"UnknownType"}],"contactDetails":{"emailList":["emailList","emailList"],"phone":"phone","contactName":"contactName","phoneExtension":"phoneExtension","mobile":"mobile","notificationPreference":[{"stageName":"DevicePrepared","sendNotification":True},{"stageName":"DevicePrepared","sendNotification":True}]},"returnPackage":{"carrierName":"carrierName","trackingUrl":"trackingUrl","trackingId":"trackingId"},"chainOfCustodySasKey":"chainOfCustodySasKey","deliveryPackage":{"carrierName":"carrierName","trackingUrl":"trackingUrl","trackingId":"trackingId"},"expectedDataSizeInTeraBytes":6,"jobDetailsType":"DataBox","reverseShipmentLabelSasKey":"reverseShipmentLabelSasKey","shippingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","zipExtendedCode":"zipExtendedCode","addressType":"None","companyName":"companyName","postalCode":"postalCode","streetAddress1":"streetAddress1","streetAddress2":"streetAddress2","streetAddress3":"streetAddress3"},"copyLogDetails":[{"copyLogDetailsType":"DataBox"},{"copyLogDetailsType":"DataBox"}],"errorDetails":[{"recommendedAction":"recommendedAction","errorMessage":"errorMessage","errorCode":0,"exceptionMessage":"exceptionMessage"},{"recommendedAction":"recommendedAction","errorMessage":"errorMessage","errorCode":0,"exceptionMessage":"exceptionMessage"}],"jobStages":[{"stageStatus":"None","stageName":"DeviceOrdered","displayName":"displayName","stageTime":"2000-01-23T04:56:07.000+00:00","jobStageDetails":"{}","errorDetails":[{"recommendedAction":"recommendedAction","errorMessage":"errorMessage","errorCode":0,"exceptionMessage":"exceptionMessage"},{"recommendedAction":"recommendedAction","errorMessage":"errorMessage","errorCode":0,"exceptionMessage":"exceptionMessage"}]},{"stageStatus":"None","stageName":"DeviceOrdered","displayName":"displayName","stageTime":"2000-01-23T04:56:07.000+00:00","jobStageDetails":"{}","errorDetails":[{"recommendedAction":"recommendedAction","errorMessage":"errorMessage","errorCode":0,"exceptionMessage":"exceptionMessage"},{"recommendedAction":"recommendedAction","errorMessage":"errorMessage","errorCode":0,"exceptionMessage":"exceptionMessage"}]}]},"isShippingAddressEditable":True,"startTime":"2000-01-23T04:56:07.000+00:00","error":{"code":"code","message":"message"},"status":"DeviceOrdered"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        json=job_resource,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_delete(client):
    """Test case for jobs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_get(client):
    """Test case for jobs_get

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list(client):
    """Test case for jobs_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataBox/jobs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_by_resource_group(client):
    """Test case for jobs_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_list_credentials(client):
    """Test case for jobs_list_credentials

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}/listCredentials'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_update(client):
    """Test case for jobs_update

    
    """
    job_resource_update_parameter = {"properties":{"destinationAccountDetails":[{"accountId":"accountId","dataDestinationType":"UnknownType"},{"accountId":"accountId","dataDestinationType":"UnknownType"}],"details":{"shippingAddress":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","zipExtendedCode":"zipExtendedCode","addressType":"None","companyName":"companyName","postalCode":"postalCode","streetAddress1":"streetAddress1","streetAddress2":"streetAddress2","streetAddress3":"streetAddress3"},"contactDetails":{"emailList":["emailList","emailList"],"phone":"phone","contactName":"contactName","phoneExtension":"phoneExtension","mobile":"mobile","notificationPreference":[{"stageName":"DevicePrepared","sendNotification":True},{"stageName":"DevicePrepared","sendNotification":True}]}}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataBox/jobs/{job_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', job_name='job_name_example'),
        headers=headers,
        json=job_resource_update_parameter,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

