# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.downloadable_data_link_interface import DownloadableDataLinkInterface
from openapi_server.models.downloadable_link_repository_v1_save_post_request import DownloadableLinkRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_downloadable_link_repository_v1_get_list_get(client):
    """Test case for downloadable_link_repository_v1_get_list_get

    products/{sku}/downloadable-links
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/products/{sku}/downloadable-links'.format(sku='sku_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_downloadable_link_repository_v1_save_post(client):
    """Test case for downloadable_link_repository_v1_save_post

    products/{sku}/downloadable-links
    """
    body = openapi_server.DownloadableLinkRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/{sku}/downloadable-links'.format(sku='sku_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

