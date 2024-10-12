# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invoke_endpoint_async_output import InvokeEndpointAsyncOutput
from openapi_server.models.invoke_endpoint_output import InvokeEndpointOutput
from openapi_server.models.invoke_endpoint_request import InvokeEndpointRequest


pytestmark = pytest.mark.asyncio

async def test_invoke_endpoint(client):
    """Test case for invoke_endpoint

    
    """
    body = openapi_server.InvokeEndpointRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'content_type': 'content_type_example',
        'accept': 'accept_example',
        'x_amzn_sage_maker_custom_attributes': 'x_amzn_sage_maker_custom_attributes_example',
        'x_amzn_sage_maker_target_model': 'x_amzn_sage_maker_target_model_example',
        'x_amzn_sage_maker_target_variant': 'x_amzn_sage_maker_target_variant_example',
        'x_amzn_sage_maker_target_container_hostname': 'x_amzn_sage_maker_target_container_hostname_example',
        'x_amzn_sage_maker_inference_id': 'x_amzn_sage_maker_inference_id_example',
        'x_amzn_sage_maker_enable_explanations': 'x_amzn_sage_maker_enable_explanations_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/endpoints/{endpoint_name}/invocations'.format(endpoint_name='endpoint_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoke_endpoint_async(client):
    """Test case for invoke_endpoint_async

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amzn_sage_maker_content_type': 'x_amzn_sage_maker_content_type_example',
        'x_amzn_sage_maker_accept': 'x_amzn_sage_maker_accept_example',
        'x_amzn_sage_maker_custom_attributes': 'x_amzn_sage_maker_custom_attributes_example',
        'x_amzn_sage_maker_inference_id': 'x_amzn_sage_maker_inference_id_example',
        'x_amzn_sage_maker_input_location': 'x_amzn_sage_maker_input_location_example',
        'x_amzn_sage_maker_request_ttl_seconds': 56,
        'x_amzn_sage_maker_invocation_timeout_seconds': 56,
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/endpoints/{endpoint_name}/async-invocations#X-Amzn-SageMaker-InputLocation'.format(endpoint_name='endpoint_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

