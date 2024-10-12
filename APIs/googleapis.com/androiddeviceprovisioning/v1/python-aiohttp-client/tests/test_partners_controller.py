# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.claim_device_request import ClaimDeviceRequest
from openapi_server.models.claim_device_response import ClaimDeviceResponse
from openapi_server.models.claim_devices_request import ClaimDevicesRequest
from openapi_server.models.company import Company
from openapi_server.models.create_customer_request import CreateCustomerRequest
from openapi_server.models.device import Device
from openapi_server.models.device_metadata import DeviceMetadata
from openapi_server.models.find_devices_by_device_identifier_request import FindDevicesByDeviceIdentifierRequest
from openapi_server.models.find_devices_by_device_identifier_response import FindDevicesByDeviceIdentifierResponse
from openapi_server.models.find_devices_by_owner_request import FindDevicesByOwnerRequest
from openapi_server.models.find_devices_by_owner_response import FindDevicesByOwnerResponse
from openapi_server.models.get_device_sim_lock_state_request import GetDeviceSimLockStateRequest
from openapi_server.models.get_device_sim_lock_state_response import GetDeviceSimLockStateResponse
from openapi_server.models.list_customers_response import ListCustomersResponse
from openapi_server.models.list_vendor_customers_response import ListVendorCustomersResponse
from openapi_server.models.list_vendors_response import ListVendorsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.unclaim_device_request import UnclaimDeviceRequest
from openapi_server.models.unclaim_devices_request import UnclaimDevicesRequest
from openapi_server.models.update_device_metadata_in_batch_request import UpdateDeviceMetadataInBatchRequest
from openapi_server.models.update_device_metadata_request import UpdateDeviceMetadataRequest


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_customers_create(client):
    """Test case for androiddeviceprovisioning_partners_customers_create

    
    """
    body = {"customer":{"companyId":"companyId","adminEmails":["adminEmails","adminEmails"],"companyName":"companyName","ownerEmails":["ownerEmails","ownerEmails"],"name":"name","termsStatus":"TERMS_STATUS_UNSPECIFIED","languageCode":"languageCode","skipWelcomeEmail":True,"googleWorkspaceAccount":{"customerId":"customerId","preProvisioningTokens":["preProvisioningTokens","preProvisioningTokens"]}}}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/{parent}/customers'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_customers_list(client):
    """Test case for androiddeviceprovisioning_partners_customers_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v1/partners/{partner_id}/customers'.format(partner_id='partner_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_claim(client):
    """Test case for androiddeviceprovisioning_partners_devices_claim

    
    """
    body = {"preProvisioningToken":"preProvisioningToken","deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"googleWorkspaceCustomerId":"googleWorkspaceCustomerId","deviceMetadata":{"entries":{"key":"entries"}},"customerId":"customerId","configurationId":"configurationId","simlockProfileId":"simlockProfileId","sectionType":"SECTION_TYPE_UNSPECIFIED"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:claim'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_claim_async(client):
    """Test case for androiddeviceprovisioning_partners_devices_claim_async

    
    """
    body = {"claims":[{"preProvisioningToken":"preProvisioningToken","deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"googleWorkspaceCustomerId":"googleWorkspaceCustomerId","deviceMetadata":{"entries":{"key":"entries"}},"customerId":"customerId","configurationId":"configurationId","simlockProfileId":"simlockProfileId","sectionType":"SECTION_TYPE_UNSPECIFIED"},{"preProvisioningToken":"preProvisioningToken","deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"googleWorkspaceCustomerId":"googleWorkspaceCustomerId","deviceMetadata":{"entries":{"key":"entries"}},"customerId":"customerId","configurationId":"configurationId","simlockProfileId":"simlockProfileId","sectionType":"SECTION_TYPE_UNSPECIFIED"}]}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:claimAsync'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_find_by_identifier(client):
    """Test case for androiddeviceprovisioning_partners_devices_find_by_identifier

    
    """
    body = {"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"limit":"limit","pageToken":"pageToken"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:findByIdentifier'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_find_by_owner(client):
    """Test case for androiddeviceprovisioning_partners_devices_find_by_owner

    
    """
    body = {"googleWorkspaceCustomerId":["googleWorkspaceCustomerId","googleWorkspaceCustomerId"],"customerId":["customerId","customerId"],"limit":"limit","pageToken":"pageToken","sectionType":"SECTION_TYPE_UNSPECIFIED"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:findByOwner'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_get(client):
    """Test case for androiddeviceprovisioning_partners_devices_get

    
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
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_get_sim_lock_state(client):
    """Test case for androiddeviceprovisioning_partners_devices_get_sim_lock_state

    
    """
    body = {"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"}}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:getSimLockState'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_metadata(client):
    """Test case for androiddeviceprovisioning_partners_devices_metadata

    
    """
    body = {"deviceMetadata":{"entries":{"key":"entries"}}}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{metadata_owner_id}/devices/{device_id}/metadata'.format(metadata_owner_id='metadata_owner_id_example', device_id='device_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_unclaim(client):
    """Test case for androiddeviceprovisioning_partners_devices_unclaim

    
    """
    body = {"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"sectionType":"SECTION_TYPE_UNSPECIFIED","vacationModeExpireTime":"vacationModeExpireTime","deviceId":"deviceId","vacationModeDays":0}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:unclaim'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_unclaim_async(client):
    """Test case for androiddeviceprovisioning_partners_devices_unclaim_async

    
    """
    body = {"unclaims":[{"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"sectionType":"SECTION_TYPE_UNSPECIFIED","vacationModeExpireTime":"vacationModeExpireTime","deviceId":"deviceId","vacationModeDays":0},{"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"sectionType":"SECTION_TYPE_UNSPECIFIED","vacationModeExpireTime":"vacationModeExpireTime","deviceId":"deviceId","vacationModeDays":0}]}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:unclaimAsync'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_devices_update_metadata_async(client):
    """Test case for androiddeviceprovisioning_partners_devices_update_metadata_async

    
    """
    body = {"updates":[{"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"deviceMetadata":{"entries":{"key":"entries"}},"deviceId":"deviceId"},{"deviceIdentifier":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","meid":"meid","serialNumber":"serialNumber","chromeOsAttestedDeviceId":"chromeOsAttestedDeviceId","imei":"imei","model":"model","manufacturer":"manufacturer"},"deviceMetadata":{"entries":{"key":"entries"}},"deviceId":"deviceId"}]}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/partners/{partner_id}/devices:updateMetadataAsync'.format(partner_id='partner_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_vendors_customers_list(client):
    """Test case for androiddeviceprovisioning_partners_vendors_customers_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/customers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_androiddeviceprovisioning_partners_vendors_list(client):
    """Test case for androiddeviceprovisioning_partners_vendors_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/vendors'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

