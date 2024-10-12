# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.image_import_content_response import ImageImportContentResponse
from openapi_server.models.image_import_operation import ImageImportOperation
from openapi_server.models.image_package_manifest import ImagePackageManifest


pytestmark = pytest.mark.asyncio

async def test_create_operation(client):
    """Test case for create_operation

    Begin the import of an image analyzed by Syft into the system
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/imports/images',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_operation(client):
    """Test case for get_operation

    Get detail on a single import
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images/{operation_id}'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_image_config(client):
    """Test case for import_image_config

    Import a docker or OCI image config to associate with the image
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/imports/images/{operation_id}/image_config'.format(operation_id='operation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain; utf-8 not supported by Connexion")
async def test_import_image_dockerfile(client):
    """Test case for import_image_dockerfile

    Begin the import of an image analyzed by Syft into the system
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain; utf-8',
    }
    response = await client.request(
        method='POST',
        path='/imports/images/{operation_id}/dockerfile'.format(operation_id='operation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_import_image_manifest(client):
    """Test case for import_image_manifest

    Import a docker or OCI distribution manifest to associate with the image
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/vnd.docker.distribution.manifest.v1+json',
    }
    response = await client.request(
        method='POST',
        path='/imports/images/{operation_id}/manifest'.format(operation_id='operation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_image_packages(client):
    """Test case for import_image_packages

    Begin the import of an image analyzed by Syft into the system
    """
    body = {"schema":{"version":"version","url":"url"},"distro":{"idLike":"idLike","name":"name","version":"version"},"descriptor":{"name":"name","version":"version"},"source":{"type":"type","target":{"key":""}},"artifactRelationships":[{"parent":"parent","metadata":{"key":""},"type":"type","child":"child"},{"parent":"parent","metadata":{"key":""},"type":"type","child":"child"}],"artifacts":[{"foundBy":"foundBy","licenses":["licenses","licenses"],"metadata":"{}","cpes":["cpes","cpes"],"name":"name","language":"language","locations":[{"path":"path","layerID":"layerID"},{"path":"path","layerID":"layerID"}],"id":"id","purl":"purl","type":"type","version":"version","metadataType":"metadataType"},{"foundBy":"foundBy","licenses":["licenses","licenses"],"metadata":"{}","cpes":["cpes","cpes"],"name":"name","language":"language","locations":[{"path":"path","layerID":"layerID"},{"path":"path","layerID":"layerID"}],"id":"id","purl":"purl","type":"type","version":"version","metadataType":"metadataType"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/imports/images/{operation_id}/packages'.format(operation_id='operation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_import_image_parent_manifest(client):
    """Test case for import_image_parent_manifest

    Import a docker or OCI distribution manifest list to associate with the image
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/vnd.docker.distribution.manifest.list.v2+json',
    }
    response = await client.request(
        method='POST',
        path='/imports/images/{operation_id}/parent_manifest'.format(operation_id='operation_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invalidate_operation(client):
    """Test case for invalidate_operation

    Invalidate operation ID so it can be garbage collected
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/imports/images/{operation_id}'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_import_dockerfiles(client):
    """Test case for list_import_dockerfiles

    List uploaded dockerfiles
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images/{operation_id}/dockerfile'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_import_image_configs(client):
    """Test case for list_import_image_configs

    List uploaded image configs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images/{operation_id}/image_config'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_import_image_manifests(client):
    """Test case for list_import_image_manifests

    List uploaded image manifests
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images/{operation_id}/manifest'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_import_packages(client):
    """Test case for list_import_packages

    List uploaded package manifests
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images/{operation_id}/packages'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_import_parent_manifests(client):
    """Test case for list_import_parent_manifests

    List uploaded parent manifests (manifest lists for a tag)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images/{operation_id}/parent_manifest'.format(operation_id='operation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_operations(client):
    """Test case for list_operations

    Lists in-progress imports
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/imports/images',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

