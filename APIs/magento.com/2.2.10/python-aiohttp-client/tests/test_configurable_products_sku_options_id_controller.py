# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.configurable_product_data_option_interface import ConfigurableProductDataOptionInterface
from openapi_server.models.configurable_product_option_repository_v1_save_post_request import ConfigurableProductOptionRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_configurable_product_option_repository_v1_delete_by_id_delete(client):
    """Test case for configurable_product_option_repository_v1_delete_by_id_delete

    configurable-products/{sku}/options/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/configurable-products/{sku}/options/{id}'.format(sku='sku_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configurable_product_option_repository_v1_get_get(client):
    """Test case for configurable_product_option_repository_v1_get_get

    configurable-products/{sku}/options/{id}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/configurable-products/{sku}/options/{id}'.format(sku='sku_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_configurable_product_option_repository_v1_save_put(client):
    """Test case for configurable_product_option_repository_v1_save_put

    configurable-products/{sku}/options/{id}
    """
    body = openapi_server.ConfigurableProductOptionRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/configurable-products/{sku}/options/{id}'.format(sku='sku_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

