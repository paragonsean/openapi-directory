# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.eav_attribute_set_repository_v1_save_put_request import EavAttributeSetRepositoryV1SavePutRequest
from openapi_server.models.eav_data_attribute_set_interface import EavDataAttributeSetInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_eav_attribute_set_repository_v1_delete_by_id_delete(client):
    """Test case for eav_attribute_set_repository_v1_delete_by_id_delete

    eav/attribute-sets/{attributeSetId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/eav/attribute-sets/{attribute_set_id}'.format(attribute_set_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eav_attribute_set_repository_v1_get_get(client):
    """Test case for eav_attribute_set_repository_v1_get_get

    eav/attribute-sets/{attributeSetId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/eav/attribute-sets/{attribute_set_id}'.format(attribute_set_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_eav_attribute_set_repository_v1_save_put(client):
    """Test case for eav_attribute_set_repository_v1_save_put

    eav/attribute-sets/{attributeSetId}
    """
    body = openapi_server.EavAttributeSetRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/eav/attribute-sets/{attribute_set_id}'.format(attribute_set_id='attribute_set_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

