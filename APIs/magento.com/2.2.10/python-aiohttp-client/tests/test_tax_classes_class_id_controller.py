# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_tax_class_repository_v1_save_post_request import TaxTaxClassRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_tax_class_repository_v1_save_put(client):
    """Test case for tax_tax_class_repository_v1_save_put

    taxClasses/{classId}
    """
    body = openapi_server.TaxTaxClassRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/taxClasses/{class_id}'.format(class_id='class_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

