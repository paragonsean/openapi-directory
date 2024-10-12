# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.framework_metadata_object_interface import FrameworkMetadataObjectInterface


pytestmark = pytest.mark.asyncio

async def test_rma_rma_attributes_management_v1_get_custom_attributes_metadata_get(client):
    """Test case for rma_rma_attributes_management_v1_get_custom_attributes_metadata_get

    returnsAttributeMetadata/custom
    """
    params = [('dataObjectClassName', 'data_object_class_name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/returnsAttributeMetadata/custom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

