from typing import List, Dict
from aiohttp import web

from openapi_server.models.remote_server_configuration_file_entity import RemoteServerConfigurationFileEntity
from openapi_server.models.remote_server_entity import RemoteServerEntity
from openapi_server import util


async def delete_remote_servers_id(request: web.Request, id) -> web.Response:
    """Delete Remote Server

    Delete Remote Server

    :param id: Remote Server ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_remote_servers(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List Remote Servers

    List Remote Servers

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_remote_servers_id(request: web.Request, id) -> web.Response:
    """Show Remote Server

    Show Remote Server

    :param id: Remote Server ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_remote_servers_id_configuration_file(request: web.Request, id) -> web.Response:
    """Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)

    Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)

    :param id: Remote Server ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_remote_servers_id(request: web.Request, id, aws_access_key=None, aws_secret_key=None, azure_blob_storage_access_key=None, azure_blob_storage_account=None, azure_blob_storage_container=None, azure_blob_storage_sas_token=None, azure_files_storage_access_key=None, azure_files_storage_account=None, azure_files_storage_sas_token=None, azure_files_storage_share_name=None, backblaze_b2_application_key=None, backblaze_b2_bucket=None, backblaze_b2_key_id=None, backblaze_b2_s3_endpoint=None, enable_dedicated_ips=None, filebase_access_key=None, filebase_bucket=None, filebase_secret_key=None, files_agent_permission_set=None, files_agent_root=None, google_cloud_storage_bucket=None, google_cloud_storage_credentials_json=None, google_cloud_storage_project_id=None, hostname=None, max_connections=None, name=None, one_drive_account_type=None, password=None, pin_to_site_region=None, port=None, private_key=None, private_key_passphrase=None, rackspace_api_key=None, rackspace_container=None, rackspace_region=None, rackspace_username=None, reset_authentication=None, s3_bucket=None, s3_compatible_access_key=None, s3_compatible_bucket=None, s3_compatible_endpoint=None, s3_compatible_region=None, s3_compatible_secret_key=None, s3_region=None, server_certificate=None, server_host_key=None, server_type=None, ssl=None, ssl_certificate=None, username=None, wasabi_access_key=None, wasabi_bucket=None, wasabi_region=None, wasabi_secret_key=None) -> web.Response:
    """Update Remote Server

    Update Remote Server

    :param id: Remote Server ID.
    :type id: int
    :param aws_access_key: AWS Access Key.
    :type aws_access_key: str
    :param aws_secret_key: AWS secret key.
    :type aws_secret_key: str
    :param azure_blob_storage_access_key: Azure Blob Storage secret key.
    :type azure_blob_storage_access_key: str
    :param azure_blob_storage_account: Azure Blob Storage Account name
    :type azure_blob_storage_account: str
    :param azure_blob_storage_container: Azure Blob Storage Container name
    :type azure_blob_storage_container: str
    :param azure_blob_storage_sas_token: Shared Access Signature (SAS) token
    :type azure_blob_storage_sas_token: str
    :param azure_files_storage_access_key: Azure File Storage access key.
    :type azure_files_storage_access_key: str
    :param azure_files_storage_account: Azure File Storage Account name
    :type azure_files_storage_account: str
    :param azure_files_storage_sas_token: Shared Access Signature (SAS) token
    :type azure_files_storage_sas_token: str
    :param azure_files_storage_share_name: Azure File Storage Share name
    :type azure_files_storage_share_name: str
    :param backblaze_b2_application_key: Backblaze B2 Cloud Storage applicationKey.
    :type backblaze_b2_application_key: str
    :param backblaze_b2_bucket: Backblaze B2 Cloud Storage Bucket name
    :type backblaze_b2_bucket: str
    :param backblaze_b2_key_id: Backblaze B2 Cloud Storage keyID.
    :type backblaze_b2_key_id: str
    :param backblaze_b2_s3_endpoint: Backblaze B2 Cloud Storage S3 Endpoint
    :type backblaze_b2_s3_endpoint: str
    :param enable_dedicated_ips: &#x60;true&#x60; if remote server only accepts connections from dedicated IPs
    :type enable_dedicated_ips: bool
    :param filebase_access_key: Filebase Access Key.
    :type filebase_access_key: str
    :param filebase_bucket: Filebase Bucket name
    :type filebase_bucket: str
    :param filebase_secret_key: Filebase secret key
    :type filebase_secret_key: str
    :param files_agent_permission_set: Local permissions for files agent. read_only, write_only, or read_write
    :type files_agent_permission_set: str
    :param files_agent_root: Agent local root path
    :type files_agent_root: str
    :param google_cloud_storage_bucket: Google Cloud Storage bucket name
    :type google_cloud_storage_bucket: str
    :param google_cloud_storage_credentials_json: A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey
    :type google_cloud_storage_credentials_json: str
    :param google_cloud_storage_project_id: Google Cloud Project ID
    :type google_cloud_storage_project_id: str
    :param hostname: Hostname or IP address
    :type hostname: str
    :param max_connections: Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible).
    :type max_connections: int
    :param name: Internal name for your reference
    :type name: str
    :param one_drive_account_type: Either personal or business_other account types
    :type one_drive_account_type: str
    :param password: Password if needed.
    :type password: str
    :param pin_to_site_region: If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true.
    :type pin_to_site_region: bool
    :param port: Port for remote server.  Not needed for S3.
    :type port: int
    :param private_key: Private key if needed.
    :type private_key: str
    :param private_key_passphrase: Passphrase for private key if needed.
    :type private_key_passphrase: str
    :param rackspace_api_key: Rackspace API key from the Rackspace Cloud Control Panel.
    :type rackspace_api_key: str
    :param rackspace_container: The name of the container (top level directory) where files will sync.
    :type rackspace_container: str
    :param rackspace_region: Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/
    :type rackspace_region: str
    :param rackspace_username: Rackspace username used to login to the Rackspace Cloud Control Panel.
    :type rackspace_username: str
    :param reset_authentication: Reset authenticated account
    :type reset_authentication: bool
    :param s3_bucket: S3 bucket name
    :type s3_bucket: str
    :param s3_compatible_access_key: S3-compatible Access Key.
    :type s3_compatible_access_key: str
    :param s3_compatible_bucket: S3-compatible Bucket name
    :type s3_compatible_bucket: str
    :param s3_compatible_endpoint: S3-compatible endpoint
    :type s3_compatible_endpoint: str
    :param s3_compatible_region: S3-compatible endpoint
    :type s3_compatible_region: str
    :param s3_compatible_secret_key: S3-compatible secret key
    :type s3_compatible_secret_key: str
    :param s3_region: S3 region
    :type s3_region: str
    :param server_certificate: Remote server certificate
    :type server_certificate: str
    :param server_host_key: Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts
    :type server_host_key: str
    :param server_type: Remote server type.
    :type server_type: str
    :param ssl: Should we require SSL?
    :type ssl: str
    :param ssl_certificate: SSL client certificate.
    :type ssl_certificate: str
    :param username: Remote server username.  Not needed for S3 buckets.
    :type username: str
    :param wasabi_access_key: Wasabi access key.
    :type wasabi_access_key: str
    :param wasabi_bucket: Wasabi Bucket name
    :type wasabi_bucket: str
    :param wasabi_region: Wasabi region
    :type wasabi_region: str
    :param wasabi_secret_key: Wasabi secret key.
    :type wasabi_secret_key: str

    """
    return web.Response(status=200)


async def post_remote_servers(request: web.Request, aws_access_key=None, aws_secret_key=None, azure_blob_storage_access_key=None, azure_blob_storage_account=None, azure_blob_storage_container=None, azure_blob_storage_sas_token=None, azure_files_storage_access_key=None, azure_files_storage_account=None, azure_files_storage_sas_token=None, azure_files_storage_share_name=None, backblaze_b2_application_key=None, backblaze_b2_bucket=None, backblaze_b2_key_id=None, backblaze_b2_s3_endpoint=None, enable_dedicated_ips=None, filebase_access_key=None, filebase_bucket=None, filebase_secret_key=None, files_agent_permission_set=None, files_agent_root=None, google_cloud_storage_bucket=None, google_cloud_storage_credentials_json=None, google_cloud_storage_project_id=None, hostname=None, max_connections=None, name=None, one_drive_account_type=None, password=None, pin_to_site_region=None, port=None, private_key=None, private_key_passphrase=None, rackspace_api_key=None, rackspace_container=None, rackspace_region=None, rackspace_username=None, reset_authentication=None, s3_bucket=None, s3_compatible_access_key=None, s3_compatible_bucket=None, s3_compatible_endpoint=None, s3_compatible_region=None, s3_compatible_secret_key=None, s3_region=None, server_certificate=None, server_host_key=None, server_type=None, ssl=None, ssl_certificate=None, username=None, wasabi_access_key=None, wasabi_bucket=None, wasabi_region=None, wasabi_secret_key=None) -> web.Response:
    """Create Remote Server

    Create Remote Server

    :param aws_access_key: AWS Access Key.
    :type aws_access_key: str
    :param aws_secret_key: AWS secret key.
    :type aws_secret_key: str
    :param azure_blob_storage_access_key: Azure Blob Storage secret key.
    :type azure_blob_storage_access_key: str
    :param azure_blob_storage_account: Azure Blob Storage Account name
    :type azure_blob_storage_account: str
    :param azure_blob_storage_container: Azure Blob Storage Container name
    :type azure_blob_storage_container: str
    :param azure_blob_storage_sas_token: Shared Access Signature (SAS) token
    :type azure_blob_storage_sas_token: str
    :param azure_files_storage_access_key: Azure File Storage access key.
    :type azure_files_storage_access_key: str
    :param azure_files_storage_account: Azure File Storage Account name
    :type azure_files_storage_account: str
    :param azure_files_storage_sas_token: Shared Access Signature (SAS) token
    :type azure_files_storage_sas_token: str
    :param azure_files_storage_share_name: Azure File Storage Share name
    :type azure_files_storage_share_name: str
    :param backblaze_b2_application_key: Backblaze B2 Cloud Storage applicationKey.
    :type backblaze_b2_application_key: str
    :param backblaze_b2_bucket: Backblaze B2 Cloud Storage Bucket name
    :type backblaze_b2_bucket: str
    :param backblaze_b2_key_id: Backblaze B2 Cloud Storage keyID.
    :type backblaze_b2_key_id: str
    :param backblaze_b2_s3_endpoint: Backblaze B2 Cloud Storage S3 Endpoint
    :type backblaze_b2_s3_endpoint: str
    :param enable_dedicated_ips: &#x60;true&#x60; if remote server only accepts connections from dedicated IPs
    :type enable_dedicated_ips: bool
    :param filebase_access_key: Filebase Access Key.
    :type filebase_access_key: str
    :param filebase_bucket: Filebase Bucket name
    :type filebase_bucket: str
    :param filebase_secret_key: Filebase secret key
    :type filebase_secret_key: str
    :param files_agent_permission_set: Local permissions for files agent. read_only, write_only, or read_write
    :type files_agent_permission_set: str
    :param files_agent_root: Agent local root path
    :type files_agent_root: str
    :param google_cloud_storage_bucket: Google Cloud Storage bucket name
    :type google_cloud_storage_bucket: str
    :param google_cloud_storage_credentials_json: A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey
    :type google_cloud_storage_credentials_json: str
    :param google_cloud_storage_project_id: Google Cloud Project ID
    :type google_cloud_storage_project_id: str
    :param hostname: Hostname or IP address
    :type hostname: str
    :param max_connections: Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible).
    :type max_connections: int
    :param name: Internal name for your reference
    :type name: str
    :param one_drive_account_type: Either personal or business_other account types
    :type one_drive_account_type: str
    :param password: Password if needed.
    :type password: str
    :param pin_to_site_region: If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true.
    :type pin_to_site_region: bool
    :param port: Port for remote server.  Not needed for S3.
    :type port: int
    :param private_key: Private key if needed.
    :type private_key: str
    :param private_key_passphrase: Passphrase for private key if needed.
    :type private_key_passphrase: str
    :param rackspace_api_key: Rackspace API key from the Rackspace Cloud Control Panel.
    :type rackspace_api_key: str
    :param rackspace_container: The name of the container (top level directory) where files will sync.
    :type rackspace_container: str
    :param rackspace_region: Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/
    :type rackspace_region: str
    :param rackspace_username: Rackspace username used to login to the Rackspace Cloud Control Panel.
    :type rackspace_username: str
    :param reset_authentication: Reset authenticated account
    :type reset_authentication: bool
    :param s3_bucket: S3 bucket name
    :type s3_bucket: str
    :param s3_compatible_access_key: S3-compatible Access Key.
    :type s3_compatible_access_key: str
    :param s3_compatible_bucket: S3-compatible Bucket name
    :type s3_compatible_bucket: str
    :param s3_compatible_endpoint: S3-compatible endpoint
    :type s3_compatible_endpoint: str
    :param s3_compatible_region: S3-compatible endpoint
    :type s3_compatible_region: str
    :param s3_compatible_secret_key: S3-compatible secret key
    :type s3_compatible_secret_key: str
    :param s3_region: S3 region
    :type s3_region: str
    :param server_certificate: Remote server certificate
    :type server_certificate: str
    :param server_host_key: Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts
    :type server_host_key: str
    :param server_type: Remote server type.
    :type server_type: str
    :param ssl: Should we require SSL?
    :type ssl: str
    :param ssl_certificate: SSL client certificate.
    :type ssl_certificate: str
    :param username: Remote server username.  Not needed for S3 buckets.
    :type username: str
    :param wasabi_access_key: Wasabi access key.
    :type wasabi_access_key: str
    :param wasabi_bucket: Wasabi Bucket name
    :type wasabi_bucket: str
    :param wasabi_region: Wasabi region
    :type wasabi_region: str
    :param wasabi_secret_key: Wasabi secret key.
    :type wasabi_secret_key: str

    """
    return web.Response(status=200)


async def post_remote_servers_id_configuration_file(request: web.Request, id, api_token=None, config_version=None, hostname=None, permission_set=None, port=None, private_key=None, public_key=None, root=None, server_host_key=None, status=None, subdomain=None) -> web.Response:
    """Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)

    Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)

    :param id: Remote Server ID.
    :type id: int
    :param api_token: Files Agent API Token
    :type api_token: str
    :param config_version: agent config version
    :type config_version: str
    :param hostname: 
    :type hostname: str
    :param permission_set: 
    :type permission_set: str
    :param port: Incoming port for files agent connections
    :type port: int
    :param private_key: private key
    :type private_key: str
    :param public_key: public key
    :type public_key: str
    :param root: Agent local root path
    :type root: str
    :param server_host_key: 
    :type server_host_key: str
    :param status: either running or shutdown
    :type status: str
    :param subdomain: 
    :type subdomain: str

    """
    return web.Response(status=200)
