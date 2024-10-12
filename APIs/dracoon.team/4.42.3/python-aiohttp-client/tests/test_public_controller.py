# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.active_directory_auth_info import ActiveDirectoryAuthInfo
from openapi_server.models.chunk_upload_response import ChunkUploadResponse
from openapi_server.models.complete_s3_share_upload_request import CompleteS3ShareUploadRequest
from openapi_server.models.create_share_upload_channel_request import CreateShareUploadChannelRequest
from openapi_server.models.create_share_upload_channel_response import CreateShareUploadChannelResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.generate_presigned_urls_request import GeneratePresignedUrlsRequest
from openapi_server.models.open_id_auth_info import OpenIdAuthInfo
from openapi_server.models.presigned_url_list import PresignedUrlList
from openapi_server.models.public_download_share import PublicDownloadShare
from openapi_server.models.public_download_token_generate_request import PublicDownloadTokenGenerateRequest
from openapi_server.models.public_download_token_generate_response import PublicDownloadTokenGenerateResponse
from openapi_server.models.public_upload_share import PublicUploadShare
from openapi_server.models.public_uploaded_file_data import PublicUploadedFileData
from openapi_server.models.s3_share_upload_status import S3ShareUploadStatus
from openapi_server.models.sds_server_time import SdsServerTime
from openapi_server.models.software_version_data import SoftwareVersionData
from openapi_server.models.system_info import SystemInfo
from openapi_server.models.third_party_dependencies_data import ThirdPartyDependenciesData
from openapi_server.models.user_file_key_list import UserFileKeyList


pytestmark = pytest.mark.asyncio

async def test_cancel_file_upload_via_share(client):
    """Test case for cancel_file_upload_via_share

    Cancel file upload
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v4/public/shares/uploads/{access_key}/{upload_id}'.format(access_key='access_key_example', upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_public_download_share_password(client):
    """Test case for check_public_download_share_password

    Check public Download Share password
    """
    params = [('password', 'password_example')]
    headers = { 
    }
    response = await client.request(
        method='HEAD',
        path='/api/v4/public/shares/downloads/{access_key}'.format(access_key='access_key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_file_upload_via_share(client):
    """Test case for complete_file_upload_via_share

    Complete file upload
    """
    body = {"items":[{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0},{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/public/shares/uploads/{access_key}/{upload_id}'.format(access_key='access_key_example', upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_s3_file_upload_via_share(client):
    """Test case for complete_s3_file_upload_via_share

    Complete S3 file upload
    """
    body = {"parts":[{"partEtag":"partEtag","partNumber":0},{"partEtag":"partEtag","partNumber":0}],"userFileKeyList":[{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0},{"fileKey":{"tag":"tag","iv":"iv","version":"version","key":"key"},"userId":0}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v4/public/shares/uploads/{access_key}/{upload_id}/s3'.format(access_key='access_key_example', upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_share_upload_channel(client):
    """Test case for create_share_upload_channel

    Create new file upload channel
    """
    body = {"timestampModification":"2000-01-23T04:56:07.000+00:00","password":"password","size":0,"name":"name","timestampCreation":"2000-01-23T04:56:07.000+00:00","directS3Upload":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/public/shares/uploads/{access_key}'.format(access_key='access_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_file_via_token_public(client):
    """Test case for download_file_via_token_public

    Download file with token
    """
    params = [('generic_mimetype', True),
                    ('inline', True)]
    headers = { 
        'Accept': 'application/octet-stream',
        'range': 'range_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/shares/downloads/{access_key}/{token}'.format(access_key='access_key_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_file_via_token_public1(client):
    """Test case for download_file_via_token_public1

    Download file with token
    """
    params = [('generic_mimetype', True),
                    ('inline', True)]
    headers = { 
        'Accept': 'application/octet-stream',
        'range': 'range_example',
    }
    response = await client.request(
        method='HEAD',
        path='/api/v4/public/shares/downloads/{access_key}/{token}'.format(access_key='access_key_example', token='token_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_download_url_public(client):
    """Test case for generate_download_url_public

    Generate download URL
    """
    body = {"password":"password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/public/shares/downloads/{access_key}'.format(access_key='access_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_presigned_urls_public(client):
    """Test case for generate_presigned_urls_public

    Generate presigned URLs for S3 file upload
    """
    body = {"size":1,"lastPartNumber":6,"firstPartNumber":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='POST',
        path='/api/v4/public/shares/uploads/{access_key}/{upload_id}/s3_urls'.format(access_key='access_key_example', upload_id='upload_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_active_directory_auth_info(client):
    """Test case for request_active_directory_auth_info

    Request Active Directory authentication information
    """
    params = [('is_global_available', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/system/info/auth/ad',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_open_id_auth_info(client):
    """Test case for request_open_id_auth_info

    Request OpenID Connect provider authentication information
    """
    params = [('is_global_available', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/system/info/auth/openid',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_public_download_share_info(client):
    """Test case for request_public_download_share_info

    Request public Download Share information
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/shares/downloads/{access_key}'.format(access_key='access_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_public_upload_share_info(client):
    """Test case for request_public_upload_share_info

    Request public Upload Share information
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_share_password': 'x_sds_share_password_example',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/shares/uploads/{access_key}'.format(access_key='access_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_software_version(client):
    """Test case for request_software_version

    Request software version information
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/software/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_info(client):
    """Test case for request_system_info

    Request system information
    """
    params = [('is_enabled', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/system/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_system_time(client):
    """Test case for request_system_time

    Request system time
    """
    headers = { 
        'Accept': 'application/json',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/time',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_third_party_dependencies(client):
    """Test case for request_third_party_dependencies

    Request third-party software dependencies
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/software/third_party_dependencies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_request_upload_status_public(client):
    """Test case for request_upload_status_public

    Request status of S3 file upload
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v4/public/shares/uploads/{access_key}/{upload_id}'.format(access_key='access_key_example', upload_id='upload_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file_as_multipart_public1(client):
    """Test case for upload_file_as_multipart_public1

    Upload file
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'content_range': 'content_range_example',
        'x_sds_date_format': 'x_sds_date_format_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v4/public/shares/uploads/{access_key}/{upload_id}'.format(access_key='access_key_example', upload_id='upload_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

