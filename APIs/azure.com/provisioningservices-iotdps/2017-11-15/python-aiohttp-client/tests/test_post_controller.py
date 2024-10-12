# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_response import CertificateResponse
from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.name_availability_info import NameAvailabilityInfo
from openapi_server.models.operation_inputs import OperationInputs
from openapi_server.models.shared_access_signature_authorization_rule_access_rights_description import SharedAccessSignatureAuthorizationRuleAccessRightsDescription
from openapi_server.models.shared_access_signature_authorization_rule_list_result import SharedAccessSignatureAuthorizationRuleListResult
from openapi_server.models.verification_code_request import VerificationCodeRequest
from openapi_server.models.verification_code_response import VerificationCodeResponse


pytestmark = pytest.mark.asyncio

async def test_dps_certificate_generate_verification_code(client):
    """Test case for dps_certificate_generate_verification_code

    
    """
    params = [('certificate.name', 'certificate_name_example'),
                    ('certificate.rawBytes', 'certificate_raw_bytes_example'),
                    ('certificate.isVerified', True),
                    ('certificate.purpose', 'certificate_purpose_example'),
                    ('certificate.created', '2013-10-20T19:20:30+01:00'),
                    ('certificate.lastUpdated', '2013-10-20T19:20:30+01:00'),
                    ('certificate.hasPrivateKey', True),
                    ('certificate.nonce', 'certificate_nonce_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/certificates/{certificate_name}/generateVerificationCode'.format(certificate_name='certificate_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dps_certificate_verify_certificate(client):
    """Test case for dps_certificate_verify_certificate

    Verify certificate's private key possession.
    """
    request = {"certificate":"certificate"}
    params = [('certificate.name', 'certificate_name_example'),
                    ('certificate.rawBytes', 'certificate_raw_bytes_example'),
                    ('certificate.isVerified', True),
                    ('certificate.purpose', 'certificate_purpose_example'),
                    ('certificate.created', '2013-10-20T19:20:30+01:00'),
                    ('certificate.lastUpdated', '2013-10-20T19:20:30+01:00'),
                    ('certificate.hasPrivateKey', True),
                    ('certificate.nonce', 'certificate_nonce_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/certificates/{certificate_name}/verify'.format(certificate_name='certificate_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', provisioning_service_name='provisioning_service_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_check_provisioning_service_name_availability(client):
    """Test case for iot_dps_resource_check_provisioning_service_name_availability

    Check if a provisioning service name is available.
    """
    arguments = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Devices/checkProvisioningServiceNameAvailability'.format(subscription_id='subscription_id_example'),
        headers=headers,
        json=arguments,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_list_keys(client):
    """Test case for iot_dps_resource_list_keys

    Get the security metadata for a provisioning service.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/listkeys'.format(provisioning_service_name='provisioning_service_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_dps_resource_list_keys_for_key_name(client):
    """Test case for iot_dps_resource_list_keys_for_key_name

    Get a shared access policy by name from a provisioning service.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/provisioningServices/{provisioning_service_name}/keys/{key_name}/listkeys'.format(provisioning_service_name='provisioning_service_name_example', key_name='key_name_example', subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

