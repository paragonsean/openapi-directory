# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_data_attribute_metadata_interface import CustomerDataAttributeMetadataInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_customer_customer_metadata_v1_get_custom_attributes_metadata_get(client):
    """Test case for customer_customer_metadata_v1_get_custom_attributes_metadata_get

    attributeMetadata/customer/custom
    """
    params = [('dataInterfaceName', 'data_interface_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/attributeMetadata/customer/custom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

