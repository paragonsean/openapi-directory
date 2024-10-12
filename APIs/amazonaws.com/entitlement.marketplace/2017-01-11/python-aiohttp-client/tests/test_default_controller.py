# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_entitlements_request import GetEntitlementsRequest
from openapi_server.models.get_entitlements_result import GetEntitlementsResult
from openapi_server.models.internal_service_error_exception import InternalServiceErrorException
from openapi_server.models.invalid_parameter_exception import InvalidParameterException
from openapi_server.models.throttling_exception import ThrottlingException


pytestmark = pytest.mark.asyncio

async def test_get_entitlements(client):
    """Test case for get_entitlements

    
    """
    body = {"NextToken":"","ProductCode":"","Filter":"","MaxResults":""}
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
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=AWSMPEntitlementService.GetEntitlements',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

