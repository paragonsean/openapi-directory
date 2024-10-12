# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.s3_config import S3Config
from openapi_server.models.s3_config_create_request import S3ConfigCreateRequest
from openapi_server.models.s3_config_update_request import S3ConfigUpdateRequest
from openapi_server.models.s3_tag import S3Tag
from openapi_server.models.s3_tag_create_request import S3TagCreateRequest
from openapi_server.models.s3_tag_list import S3TagList


pytestmark = pytest.mark.asyncio

async def test_create_s3_config(client):
    """Test case for create_s3_config

    Create S3 storage configuration
    """
    body = {"bucketName":"bucketName","secretKey":"secretKey","accessKey":"accessKey","bucketUrl":"bucketUrl","endpointUrl":"endpointUrl","region":"region"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/storage/s3',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_s3_tag(client):
    """Test case for create_s3_tag

    Create S3 tag
    """
    body = {"value":"value","isMandatory":False,"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/system/config/storage/s3/tags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_s3_tag(client):
    """Test case for remove_s3_tag

    Remove S3 tag
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/system/config/storage/s3/tags/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request3_config(client):
    """Test case for request3_config

    Request S3 storage configuration
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/storage/s3',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_s3_tag(client):
    """Test case for request_s3_tag

    Request S3 tag
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/storage/s3/tags/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_s3_tag_list(client):
    """Test case for request_s3_tag_list

    Request list of configured S3 tags
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/system/config/storage/s3/tags',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_s3_config(client):
    """Test case for update_s3_config

    Update S3 storage configuration
    """
    body = {"bucketName":"bucketName","secretKey":"secretKey","accessKey":"accessKey","bucketUrl":"bucketUrl","endpointUrl":"endpointUrl","region":"region"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_auth_token': 'x_sds_auth_token_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/system/config/storage/s3',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

