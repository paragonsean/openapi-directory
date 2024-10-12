# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.generate_data_set_request import GenerateDataSetRequest
from openapi_server.models.generate_data_set_result import GenerateDataSetResult
from openapi_server.models.start_support_data_export_request import StartSupportDataExportRequest
from openapi_server.models.start_support_data_export_result import StartSupportDataExportResult


pytestmark = pytest.mark.asyncio

async def test_generate_data_set(client):
    """Test case for generate_data_set

    
    """
    body = {"dataSetType":"","snsTopicArn":"","destinationS3Prefix":"","customerDefinedValues":"","dataSetPublicationDate":"","destinationS3BucketName":"","roleNameArn":""}
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
        path='/#X-Amz-Target=MarketplaceCommerceAnalytics20150701.GenerateDataSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_support_data_export(client):
    """Test case for start_support_data_export

    
    """
    body = {"fromDate":"","dataSetType":"","snsTopicArn":"","destinationS3Prefix":"","customerDefinedValues":"","destinationS3BucketName":"","roleNameArn":""}
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
        path='/#X-Amz-Target=MarketplaceCommerceAnalytics20150701.StartSupportDataExport',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

