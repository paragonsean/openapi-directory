# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_attribute_metadata_interface import CustomerDataAttributeMetadataInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_rma_rma_attributes_management_v1_get_all_attributes_metadata_get(client):
    """Test case for rma_rma_attributes_management_v1_get_all_attributes_metadata_get

    returnsAttributeMetadata
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/returnsAttributeMetadata',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

