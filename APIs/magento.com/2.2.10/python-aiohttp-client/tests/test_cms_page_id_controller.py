# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cms_data_page_interface import CmsDataPageInterface
from openapi_server.models.cms_page_repository_v1_save_post_request import CmsPageRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_cms_page_repository_v1_save_put(client):
    """Test case for cms_page_repository_v1_save_put

    cmsPage/{id}
    """
    body = openapi_server.CmsPageRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/cmsPage/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

