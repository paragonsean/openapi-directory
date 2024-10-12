# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.anchore_image import AnchoreImage
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.content_files_response import ContentFilesResponse
from openapi_server.models.content_java_package_response import ContentJAVAPackageResponse
from openapi_server.models.content_malware_response import ContentMalwareResponse
from openapi_server.models.content_package_response import ContentPackageResponse
from openapi_server.models.delete_image_response import DeleteImageResponse
from openapi_server.models.image_analysis_request import ImageAnalysisRequest
from openapi_server.models.metadata_response import MetadataResponse
from openapi_server.models.vulnerability_response import VulnerabilityResponse


pytestmark = pytest.mark.asyncio

async def test_add_image(client):
    """Test case for add_image

    Submit a new image for analysis by the engine
    """
    body = {"dockerfile":"dockerfile","digest":"digest","annotations":"{}","created_at":"2000-01-23T04:56:07.000+00:00","source":{"import":{"local_image_id":"local_image_id","operation_uuid":"operation_uuid","contents":{"parent_manifest":"parent_manifest","manifest":"manifest","dockerfile":"dockerfile","image_config":"image_config","packages":"packages"},"digest":"digest","parent_digest":"parent_digest","tags":["docker.io/library/nginx:latest","docker.io/library/nginx:latest"]},"digest":{"creation_timestamp_override":"2000-01-23T04:56:07.000+00:00","dockerfile":"dockerfile","pullstring":"pullstring","tag":"tag"},"archive":{"digest":"digest"},"tag":{"dockerfile":"dockerfile","pullstring":"pullstring"}},"tag":"tag","image_type":"image_type"}
    params = [('force', True),
                    ('autosubscribe', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='POST',
        path='/images',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image(client):
    """Test case for delete_image

    Delete an image analysis
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/images/{image_digest}'.format(image_digest='image_digest_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_image_by_image_id(client):
    """Test case for delete_image_by_image_id

    Delete image by docker imageId
    """
    params = [('force', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/images/by_id/{image_id}'.format(image_id='image_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_images_async(client):
    """Test case for delete_images_async

    Bulk mark images for deletion
    """
    params = [('imageDigests', ['image_digests_example']),
                    ('force', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='DELETE',
        path='/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image(client):
    """Test case for get_image

    Get image metadata
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_by_image_id(client):
    """Test case for get_image_by_image_id

    Lookup image by docker imageId
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type(client):
    """Test case for get_image_content_by_type

    Get the content of an image by type
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/content/{ctype}'.format(image_digest='image_digest_example', ctype='ctype_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type_files(client):
    """Test case for get_image_content_by_type_files

    Get the content of an image by type files
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/content/files'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type_image_id(client):
    """Test case for get_image_content_by_type_image_id

    Get the content of an image by type
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/content/{ctype}'.format(image_id='image_id_example', ctype='ctype_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type_image_id_files(client):
    """Test case for get_image_content_by_type_image_id_files

    Get the content of an image by type files
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/content/files'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type_image_id_javapackage(client):
    """Test case for get_image_content_by_type_image_id_javapackage

    Get the content of an image by type java
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/content/java'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type_javapackage(client):
    """Test case for get_image_content_by_type_javapackage

    Get the content of an image by type java
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/content/java'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_content_by_type_malware(client):
    """Test case for get_image_content_by_type_malware

    Get the content of an image by type malware
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/content/malware'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_metadata_by_type(client):
    """Test case for get_image_metadata_by_type

    Get the metadata of an image by type
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/metadata/{mtype}'.format(image_digest='image_digest_example', mtype='mtype_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_policy_check(client):
    """Test case for get_image_policy_check

    Check policy evaluation status for image
    """
    params = [('policyId', 'policy_id_example'),
                    ('tag', 'tag_example'),
                    ('detail', True),
                    ('history', True),
                    ('interactive', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/check'.format(image_digest='image_digest_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_policy_check_by_image_id(client):
    """Test case for get_image_policy_check_by_image_id

    Check policy evaluation status for image
    """
    params = [('policyId', 'policy_id_example'),
                    ('tag', 'tag_example'),
                    ('detail', True),
                    ('history', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/check'.format(image_id='image_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_sbom_native(client):
    """Test case for get_image_sbom_native

    Get image sbom in the native Anchore format
    """
    headers = { 
        'Accept': 'application/gzip',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/sboms/native'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_vulnerabilities_by_type(client):
    """Test case for get_image_vulnerabilities_by_type

    Get vulnerabilities by type
    """
    params = [('force_refresh', True),
                    ('vendor_only', True)]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/vuln/{vtype}'.format(image_digest='image_digest_example', vtype='vtype_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_vulnerabilities_by_type_image_id(client):
    """Test case for get_image_vulnerabilities_by_type_image_id

    Get vulnerabilities by type
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/vuln/{vtype}'.format(image_id='image_id_example', vtype='vtype_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_vulnerability_types(client):
    """Test case for get_image_vulnerability_types

    Get vulnerability types
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/vuln'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_image_vulnerability_types_by_image_id(client):
    """Test case for get_image_vulnerability_types_by_image_id

    Get vulnerability types
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/vuln'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_image_content(client):
    """Test case for list_image_content

    List image content types
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/content'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_image_content_by_imageid(client):
    """Test case for list_image_content_by_imageid

    List image content types
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/by_id/{image_id}/content'.format(image_id='image_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_image_metadata(client):
    """Test case for list_image_metadata

    List image metadata types
    """
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/metadata'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_images(client):
    """Test case for list_images

    List all visible images
    """
    params = [('history', True),
                    ('fulltag', 'fulltag_example'),
                    ('image_status', active),
                    ('analysis_status', 'analysis_status_example')]
    headers = { 
        'Accept': 'application/json',
        'x_anchore_account': 'x_anchore_account_example',
    }
    response = await client.request(
        method='GET',
        path='/images',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

