# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.remote_server_configuration_file_entity import RemoteServerConfigurationFileEntity
from openapi_server.models.remote_server_entity import RemoteServerEntity


pytestmark = pytest.mark.asyncio

async def test_delete_remote_servers_id(client):
    """Test case for delete_remote_servers_id

    Delete Remote Server
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/remote_servers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_servers(client):
    """Test case for get_remote_servers

    List Remote Servers
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/remote_servers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_servers_id(client):
    """Test case for get_remote_servers_id

    Show Remote Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/remote_servers/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_remote_servers_id_configuration_file(client):
    """Test case for get_remote_servers_id_configuration_file

    Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/remote_servers/{id}/configuration_file'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_patch_remote_servers_id(client):
    """Test case for patch_remote_servers_id

    Update Remote Server
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('aws_access_key', 'aws_access_key_example')
    data.add_field('aws_secret_key', 'aws_secret_key_example')
    data.add_field('azure_blob_storage_access_key', 'azure_blob_storage_access_key_example')
    data.add_field('azure_blob_storage_account', 'azure_blob_storage_account_example')
    data.add_field('azure_blob_storage_container', 'azure_blob_storage_container_example')
    data.add_field('azure_blob_storage_sas_token', 'azure_blob_storage_sas_token_example')
    data.add_field('azure_files_storage_access_key', 'azure_files_storage_access_key_example')
    data.add_field('azure_files_storage_account', 'azure_files_storage_account_example')
    data.add_field('azure_files_storage_sas_token', 'azure_files_storage_sas_token_example')
    data.add_field('azure_files_storage_share_name', 'azure_files_storage_share_name_example')
    data.add_field('backblaze_b2_application_key', 'backblaze_b2_application_key_example')
    data.add_field('backblaze_b2_bucket', 'backblaze_b2_bucket_example')
    data.add_field('backblaze_b2_key_id', 'backblaze_b2_key_id_example')
    data.add_field('backblaze_b2_s3_endpoint', 'backblaze_b2_s3_endpoint_example')
    data.add_field('enable_dedicated_ips', True)
    data.add_field('filebase_access_key', 'filebase_access_key_example')
    data.add_field('filebase_bucket', 'filebase_bucket_example')
    data.add_field('filebase_secret_key', 'filebase_secret_key_example')
    data.add_field('files_agent_permission_set', 'files_agent_permission_set_example')
    data.add_field('files_agent_root', 'files_agent_root_example')
    data.add_field('google_cloud_storage_bucket', 'google_cloud_storage_bucket_example')
    data.add_field('google_cloud_storage_credentials_json', 'google_cloud_storage_credentials_json_example')
    data.add_field('google_cloud_storage_project_id', 'google_cloud_storage_project_id_example')
    data.add_field('hostname', 'hostname_example')
    data.add_field('max_connections', 56)
    data.add_field('name', 'name_example')
    data.add_field('one_drive_account_type', 'one_drive_account_type_example')
    data.add_field('password', 'password_example')
    data.add_field('pin_to_site_region', True)
    data.add_field('port', 56)
    data.add_field('private_key', 'private_key_example')
    data.add_field('private_key_passphrase', 'private_key_passphrase_example')
    data.add_field('rackspace_api_key', 'rackspace_api_key_example')
    data.add_field('rackspace_container', 'rackspace_container_example')
    data.add_field('rackspace_region', 'rackspace_region_example')
    data.add_field('rackspace_username', 'rackspace_username_example')
    data.add_field('reset_authentication', True)
    data.add_field('s3_bucket', 's3_bucket_example')
    data.add_field('s3_compatible_access_key', 's3_compatible_access_key_example')
    data.add_field('s3_compatible_bucket', 's3_compatible_bucket_example')
    data.add_field('s3_compatible_endpoint', 's3_compatible_endpoint_example')
    data.add_field('s3_compatible_region', 's3_compatible_region_example')
    data.add_field('s3_compatible_secret_key', 's3_compatible_secret_key_example')
    data.add_field('s3_region', 's3_region_example')
    data.add_field('server_certificate', 'server_certificate_example')
    data.add_field('server_host_key', 'server_host_key_example')
    data.add_field('server_type', 'server_type_example')
    data.add_field('ssl', 'ssl_example')
    data.add_field('ssl_certificate', 'ssl_certificate_example')
    data.add_field('username', 'username_example')
    data.add_field('wasabi_access_key', 'wasabi_access_key_example')
    data.add_field('wasabi_bucket', 'wasabi_bucket_example')
    data.add_field('wasabi_region', 'wasabi_region_example')
    data.add_field('wasabi_secret_key', 'wasabi_secret_key_example')
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/remote_servers/{id}'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_remote_servers(client):
    """Test case for post_remote_servers

    Create Remote Server
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('aws_access_key', 'aws_access_key_example')
    data.add_field('aws_secret_key', 'aws_secret_key_example')
    data.add_field('azure_blob_storage_access_key', 'azure_blob_storage_access_key_example')
    data.add_field('azure_blob_storage_account', 'azure_blob_storage_account_example')
    data.add_field('azure_blob_storage_container', 'azure_blob_storage_container_example')
    data.add_field('azure_blob_storage_sas_token', 'azure_blob_storage_sas_token_example')
    data.add_field('azure_files_storage_access_key', 'azure_files_storage_access_key_example')
    data.add_field('azure_files_storage_account', 'azure_files_storage_account_example')
    data.add_field('azure_files_storage_sas_token', 'azure_files_storage_sas_token_example')
    data.add_field('azure_files_storage_share_name', 'azure_files_storage_share_name_example')
    data.add_field('backblaze_b2_application_key', 'backblaze_b2_application_key_example')
    data.add_field('backblaze_b2_bucket', 'backblaze_b2_bucket_example')
    data.add_field('backblaze_b2_key_id', 'backblaze_b2_key_id_example')
    data.add_field('backblaze_b2_s3_endpoint', 'backblaze_b2_s3_endpoint_example')
    data.add_field('enable_dedicated_ips', True)
    data.add_field('filebase_access_key', 'filebase_access_key_example')
    data.add_field('filebase_bucket', 'filebase_bucket_example')
    data.add_field('filebase_secret_key', 'filebase_secret_key_example')
    data.add_field('files_agent_permission_set', 'files_agent_permission_set_example')
    data.add_field('files_agent_root', 'files_agent_root_example')
    data.add_field('google_cloud_storage_bucket', 'google_cloud_storage_bucket_example')
    data.add_field('google_cloud_storage_credentials_json', 'google_cloud_storage_credentials_json_example')
    data.add_field('google_cloud_storage_project_id', 'google_cloud_storage_project_id_example')
    data.add_field('hostname', 'hostname_example')
    data.add_field('max_connections', 56)
    data.add_field('name', 'name_example')
    data.add_field('one_drive_account_type', 'one_drive_account_type_example')
    data.add_field('password', 'password_example')
    data.add_field('pin_to_site_region', True)
    data.add_field('port', 56)
    data.add_field('private_key', 'private_key_example')
    data.add_field('private_key_passphrase', 'private_key_passphrase_example')
    data.add_field('rackspace_api_key', 'rackspace_api_key_example')
    data.add_field('rackspace_container', 'rackspace_container_example')
    data.add_field('rackspace_region', 'rackspace_region_example')
    data.add_field('rackspace_username', 'rackspace_username_example')
    data.add_field('reset_authentication', True)
    data.add_field('s3_bucket', 's3_bucket_example')
    data.add_field('s3_compatible_access_key', 's3_compatible_access_key_example')
    data.add_field('s3_compatible_bucket', 's3_compatible_bucket_example')
    data.add_field('s3_compatible_endpoint', 's3_compatible_endpoint_example')
    data.add_field('s3_compatible_region', 's3_compatible_region_example')
    data.add_field('s3_compatible_secret_key', 's3_compatible_secret_key_example')
    data.add_field('s3_region', 's3_region_example')
    data.add_field('server_certificate', 'server_certificate_example')
    data.add_field('server_host_key', 'server_host_key_example')
    data.add_field('server_type', 'server_type_example')
    data.add_field('ssl', 'ssl_example')
    data.add_field('ssl_certificate', 'ssl_certificate_example')
    data.add_field('username', 'username_example')
    data.add_field('wasabi_access_key', 'wasabi_access_key_example')
    data.add_field('wasabi_bucket', 'wasabi_bucket_example')
    data.add_field('wasabi_region', 'wasabi_region_example')
    data.add_field('wasabi_secret_key', 'wasabi_secret_key_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/remote_servers',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_remote_servers_id_configuration_file(client):
    """Test case for post_remote_servers_id_configuration_file

    Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('api_token', 'api_token_example')
    data.add_field('config_version', 'config_version_example')
    data.add_field('hostname', 'hostname_example')
    data.add_field('permission_set', 'permission_set_example')
    data.add_field('port', 56)
    data.add_field('private_key', 'private_key_example')
    data.add_field('public_key', 'public_key_example')
    data.add_field('root', 'root_example')
    data.add_field('server_host_key', 'server_host_key_example')
    data.add_field('status', 'status_example')
    data.add_field('subdomain', 'subdomain_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/remote_servers/{id}/configuration_file'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

