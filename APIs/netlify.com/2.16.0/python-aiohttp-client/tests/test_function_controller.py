# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.function import Function


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_upload_deploy_function(client):
    """Test case for upload_deploy_function

    
    """
    file_body = '/path/to/file'
    params = [('runtime', 'runtime_example'),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'x_nf_retry_count': 56,
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/deploys/{deploy_id}/functions/{name}'.format(deploy_id='deploy_id_example', name='name_example'),
        headers=headers,
        json=file_body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

