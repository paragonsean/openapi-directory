# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.certificate_body_description import CertificateBodyDescription
from openapi_server.models.certificate_description import CertificateDescription
from openapi_server.models.certificate_list_description import CertificateListDescription
from openapi_server.models.certificate_verification_description import CertificateVerificationDescription
from openapi_server.models.certificate_with_nonce_description import CertificateWithNonceDescription
from openapi_server.models.error_details import ErrorDetails


pytestmark = pytest.mark.asyncio

async def test_certificates_create_or_update(client):
    """Test case for certificates_create_or_update

    Upload the certificate to the IoT hub.
    """
    certificate_description = {"certificate":"certificate"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_delete(client):
    """Test case for certificates_delete

    Delete an X509 certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_generate_verification_code(client):
    """Test case for certificates_generate_verification_code

    Generate verification code for proof of possession flow.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/certificates/{certificate_name}/generateVerificationCode'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_get(client):
    """Test case for certificates_get

    Get the certificate.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/certificates/{certificate_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_list_by_iot_hub(client):
    """Test case for certificates_list_by_iot_hub

    Get the certificate list.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/certificates'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_certificates_verify(client):
    """Test case for certificates_verify

    Verify certificate's private key possession.
    """
    certificate_verification_body = {"certificate":"certificate"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/certificates/{certificate_name}/verify'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', certificate_name='certificate_name_example'),
        headers=headers,
        json=certificate_verification_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

