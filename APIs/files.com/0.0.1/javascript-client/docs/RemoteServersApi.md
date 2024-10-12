# FilesComApi.RemoteServersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRemoteServersId**](RemoteServersApi.md#deleteRemoteServersId) | **DELETE** /remote_servers/{id} | Delete Remote Server
[**getRemoteServers**](RemoteServersApi.md#getRemoteServers) | **GET** /remote_servers | List Remote Servers
[**getRemoteServersId**](RemoteServersApi.md#getRemoteServersId) | **GET** /remote_servers/{id} | Show Remote Server
[**getRemoteServersIdConfigurationFile**](RemoteServersApi.md#getRemoteServersIdConfigurationFile) | **GET** /remote_servers/{id}/configuration_file | Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)
[**patchRemoteServersId**](RemoteServersApi.md#patchRemoteServersId) | **PATCH** /remote_servers/{id} | Update Remote Server
[**postRemoteServers**](RemoteServersApi.md#postRemoteServers) | **POST** /remote_servers | Create Remote Server
[**postRemoteServersIdConfigurationFile**](RemoteServersApi.md#postRemoteServersIdConfigurationFile) | **POST** /remote_servers/{id}/configuration_file | Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)



## deleteRemoteServersId

> deleteRemoteServersId(id)

Delete Remote Server

Delete Remote Server

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let id = 56; // Number | Remote Server ID.
apiInstance.deleteRemoteServersId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Remote Server ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getRemoteServers

> [RemoteServerEntity] getRemoteServers(opts)

List Remote Servers

List Remote Servers

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getRemoteServers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[RemoteServerEntity]**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRemoteServersId

> RemoteServerEntity getRemoteServersId(id)

Show Remote Server

Show Remote Server

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let id = 56; // Number | Remote Server ID.
apiInstance.getRemoteServersId(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Remote Server ID. | 

### Return type

[**RemoteServerEntity**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRemoteServersIdConfigurationFile

> RemoteServerConfigurationFileEntity getRemoteServersIdConfigurationFile(id)

Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)

Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let id = 56; // Number | Remote Server ID.
apiInstance.getRemoteServersIdConfigurationFile(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Remote Server ID. | 

### Return type

[**RemoteServerConfigurationFileEntity**](RemoteServerConfigurationFileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchRemoteServersId

> RemoteServerEntity patchRemoteServersId(id, opts)

Update Remote Server

Update Remote Server

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let id = 56; // Number | Remote Server ID.
let opts = {
  'awsAccessKey': "awsAccessKey_example", // String | AWS Access Key.
  'awsSecretKey': "awsSecretKey_example", // String | AWS secret key.
  'azureBlobStorageAccessKey': "azureBlobStorageAccessKey_example", // String | Azure Blob Storage secret key.
  'azureBlobStorageAccount': "azureBlobStorageAccount_example", // String | Azure Blob Storage Account name
  'azureBlobStorageContainer': "azureBlobStorageContainer_example", // String | Azure Blob Storage Container name
  'azureBlobStorageSasToken': "azureBlobStorageSasToken_example", // String | Shared Access Signature (SAS) token
  'azureFilesStorageAccessKey': "azureFilesStorageAccessKey_example", // String | Azure File Storage access key.
  'azureFilesStorageAccount': "azureFilesStorageAccount_example", // String | Azure File Storage Account name
  'azureFilesStorageSasToken': "azureFilesStorageSasToken_example", // String | Shared Access Signature (SAS) token
  'azureFilesStorageShareName': "azureFilesStorageShareName_example", // String | Azure File Storage Share name
  'backblazeB2ApplicationKey': "backblazeB2ApplicationKey_example", // String | Backblaze B2 Cloud Storage applicationKey.
  'backblazeB2Bucket': "backblazeB2Bucket_example", // String | Backblaze B2 Cloud Storage Bucket name
  'backblazeB2KeyId': "backblazeB2KeyId_example", // String | Backblaze B2 Cloud Storage keyID.
  'backblazeB2S3Endpoint': "backblazeB2S3Endpoint_example", // String | Backblaze B2 Cloud Storage S3 Endpoint
  'enableDedicatedIps': true, // Boolean | `true` if remote server only accepts connections from dedicated IPs
  'filebaseAccessKey': "filebaseAccessKey_example", // String | Filebase Access Key.
  'filebaseBucket': "filebaseBucket_example", // String | Filebase Bucket name
  'filebaseSecretKey': "filebaseSecretKey_example", // String | Filebase secret key
  'filesAgentPermissionSet': "filesAgentPermissionSet_example", // String | Local permissions for files agent. read_only, write_only, or read_write
  'filesAgentRoot': "filesAgentRoot_example", // String | Agent local root path
  'googleCloudStorageBucket': "googleCloudStorageBucket_example", // String | Google Cloud Storage bucket name
  'googleCloudStorageCredentialsJson': "googleCloudStorageCredentialsJson_example", // String | A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey
  'googleCloudStorageProjectId': "googleCloudStorageProjectId_example", // String | Google Cloud Project ID
  'hostname': "hostname_example", // String | Hostname or IP address
  'maxConnections': 56, // Number | Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible).
  'name': "name_example", // String | Internal name for your reference
  'oneDriveAccountType': "oneDriveAccountType_example", // String | Either personal or business_other account types
  'password': "password_example", // String | Password if needed.
  'pinToSiteRegion': true, // Boolean | If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true.
  'port': 56, // Number | Port for remote server.  Not needed for S3.
  'privateKey': "privateKey_example", // String | Private key if needed.
  'privateKeyPassphrase': "privateKeyPassphrase_example", // String | Passphrase for private key if needed.
  'rackspaceApiKey': "rackspaceApiKey_example", // String | Rackspace API key from the Rackspace Cloud Control Panel.
  'rackspaceContainer': "rackspaceContainer_example", // String | The name of the container (top level directory) where files will sync.
  'rackspaceRegion': "rackspaceRegion_example", // String | Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/
  'rackspaceUsername': "rackspaceUsername_example", // String | Rackspace username used to login to the Rackspace Cloud Control Panel.
  'resetAuthentication': true, // Boolean | Reset authenticated account
  's3Bucket': "s3Bucket_example", // String | S3 bucket name
  's3CompatibleAccessKey': "s3CompatibleAccessKey_example", // String | S3-compatible Access Key.
  's3CompatibleBucket': "s3CompatibleBucket_example", // String | S3-compatible Bucket name
  's3CompatibleEndpoint': "s3CompatibleEndpoint_example", // String | S3-compatible endpoint
  's3CompatibleRegion': "s3CompatibleRegion_example", // String | S3-compatible endpoint
  's3CompatibleSecretKey': "s3CompatibleSecretKey_example", // String | S3-compatible secret key
  's3Region': "s3Region_example", // String | S3 region
  'serverCertificate': "serverCertificate_example", // String | Remote server certificate
  'serverHostKey': "serverHostKey_example", // String | Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts
  'serverType': "serverType_example", // String | Remote server type.
  'ssl': "ssl_example", // String | Should we require SSL?
  'sslCertificate': "sslCertificate_example", // String | SSL client certificate.
  'username': "username_example", // String | Remote server username.  Not needed for S3 buckets.
  'wasabiAccessKey': "wasabiAccessKey_example", // String | Wasabi access key.
  'wasabiBucket': "wasabiBucket_example", // String | Wasabi Bucket name
  'wasabiRegion': "wasabiRegion_example", // String | Wasabi region
  'wasabiSecretKey': "wasabiSecretKey_example" // String | Wasabi secret key.
};
apiInstance.patchRemoteServersId(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Remote Server ID. | 
 **awsAccessKey** | **String**| AWS Access Key. | [optional] 
 **awsSecretKey** | **String**| AWS secret key. | [optional] 
 **azureBlobStorageAccessKey** | **String**| Azure Blob Storage secret key. | [optional] 
 **azureBlobStorageAccount** | **String**| Azure Blob Storage Account name | [optional] 
 **azureBlobStorageContainer** | **String**| Azure Blob Storage Container name | [optional] 
 **azureBlobStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] 
 **azureFilesStorageAccessKey** | **String**| Azure File Storage access key. | [optional] 
 **azureFilesStorageAccount** | **String**| Azure File Storage Account name | [optional] 
 **azureFilesStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] 
 **azureFilesStorageShareName** | **String**| Azure File Storage Share name | [optional] 
 **backblazeB2ApplicationKey** | **String**| Backblaze B2 Cloud Storage applicationKey. | [optional] 
 **backblazeB2Bucket** | **String**| Backblaze B2 Cloud Storage Bucket name | [optional] 
 **backblazeB2KeyId** | **String**| Backblaze B2 Cloud Storage keyID. | [optional] 
 **backblazeB2S3Endpoint** | **String**| Backblaze B2 Cloud Storage S3 Endpoint | [optional] 
 **enableDedicatedIps** | **Boolean**| &#x60;true&#x60; if remote server only accepts connections from dedicated IPs | [optional] 
 **filebaseAccessKey** | **String**| Filebase Access Key. | [optional] 
 **filebaseBucket** | **String**| Filebase Bucket name | [optional] 
 **filebaseSecretKey** | **String**| Filebase secret key | [optional] 
 **filesAgentPermissionSet** | **String**| Local permissions for files agent. read_only, write_only, or read_write | [optional] 
 **filesAgentRoot** | **String**| Agent local root path | [optional] 
 **googleCloudStorageBucket** | **String**| Google Cloud Storage bucket name | [optional] 
 **googleCloudStorageCredentialsJson** | **String**| A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey | [optional] 
 **googleCloudStorageProjectId** | **String**| Google Cloud Project ID | [optional] 
 **hostname** | **String**| Hostname or IP address | [optional] 
 **maxConnections** | **Number**| Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible). | [optional] 
 **name** | **String**| Internal name for your reference | [optional] 
 **oneDriveAccountType** | **String**| Either personal or business_other account types | [optional] 
 **password** | **String**| Password if needed. | [optional] 
 **pinToSiteRegion** | **Boolean**| If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true. | [optional] 
 **port** | **Number**| Port for remote server.  Not needed for S3. | [optional] 
 **privateKey** | **String**| Private key if needed. | [optional] 
 **privateKeyPassphrase** | **String**| Passphrase for private key if needed. | [optional] 
 **rackspaceApiKey** | **String**| Rackspace API key from the Rackspace Cloud Control Panel. | [optional] 
 **rackspaceContainer** | **String**| The name of the container (top level directory) where files will sync. | [optional] 
 **rackspaceRegion** | **String**| Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/ | [optional] 
 **rackspaceUsername** | **String**| Rackspace username used to login to the Rackspace Cloud Control Panel. | [optional] 
 **resetAuthentication** | **Boolean**| Reset authenticated account | [optional] 
 **s3Bucket** | **String**| S3 bucket name | [optional] 
 **s3CompatibleAccessKey** | **String**| S3-compatible Access Key. | [optional] 
 **s3CompatibleBucket** | **String**| S3-compatible Bucket name | [optional] 
 **s3CompatibleEndpoint** | **String**| S3-compatible endpoint | [optional] 
 **s3CompatibleRegion** | **String**| S3-compatible endpoint | [optional] 
 **s3CompatibleSecretKey** | **String**| S3-compatible secret key | [optional] 
 **s3Region** | **String**| S3 region | [optional] 
 **serverCertificate** | **String**| Remote server certificate | [optional] 
 **serverHostKey** | **String**| Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts | [optional] 
 **serverType** | **String**| Remote server type. | [optional] 
 **ssl** | **String**| Should we require SSL? | [optional] 
 **sslCertificate** | **String**| SSL client certificate. | [optional] 
 **username** | **String**| Remote server username.  Not needed for S3 buckets. | [optional] 
 **wasabiAccessKey** | **String**| Wasabi access key. | [optional] 
 **wasabiBucket** | **String**| Wasabi Bucket name | [optional] 
 **wasabiRegion** | **String**| Wasabi region | [optional] 
 **wasabiSecretKey** | **String**| Wasabi secret key. | [optional] 

### Return type

[**RemoteServerEntity**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postRemoteServers

> RemoteServerEntity postRemoteServers(opts)

Create Remote Server

Create Remote Server

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let opts = {
  'awsAccessKey': "awsAccessKey_example", // String | AWS Access Key.
  'awsSecretKey': "awsSecretKey_example", // String | AWS secret key.
  'azureBlobStorageAccessKey': "azureBlobStorageAccessKey_example", // String | Azure Blob Storage secret key.
  'azureBlobStorageAccount': "azureBlobStorageAccount_example", // String | Azure Blob Storage Account name
  'azureBlobStorageContainer': "azureBlobStorageContainer_example", // String | Azure Blob Storage Container name
  'azureBlobStorageSasToken': "azureBlobStorageSasToken_example", // String | Shared Access Signature (SAS) token
  'azureFilesStorageAccessKey': "azureFilesStorageAccessKey_example", // String | Azure File Storage access key.
  'azureFilesStorageAccount': "azureFilesStorageAccount_example", // String | Azure File Storage Account name
  'azureFilesStorageSasToken': "azureFilesStorageSasToken_example", // String | Shared Access Signature (SAS) token
  'azureFilesStorageShareName': "azureFilesStorageShareName_example", // String | Azure File Storage Share name
  'backblazeB2ApplicationKey': "backblazeB2ApplicationKey_example", // String | Backblaze B2 Cloud Storage applicationKey.
  'backblazeB2Bucket': "backblazeB2Bucket_example", // String | Backblaze B2 Cloud Storage Bucket name
  'backblazeB2KeyId': "backblazeB2KeyId_example", // String | Backblaze B2 Cloud Storage keyID.
  'backblazeB2S3Endpoint': "backblazeB2S3Endpoint_example", // String | Backblaze B2 Cloud Storage S3 Endpoint
  'enableDedicatedIps': true, // Boolean | `true` if remote server only accepts connections from dedicated IPs
  'filebaseAccessKey': "filebaseAccessKey_example", // String | Filebase Access Key.
  'filebaseBucket': "filebaseBucket_example", // String | Filebase Bucket name
  'filebaseSecretKey': "filebaseSecretKey_example", // String | Filebase secret key
  'filesAgentPermissionSet': "filesAgentPermissionSet_example", // String | Local permissions for files agent. read_only, write_only, or read_write
  'filesAgentRoot': "filesAgentRoot_example", // String | Agent local root path
  'googleCloudStorageBucket': "googleCloudStorageBucket_example", // String | Google Cloud Storage bucket name
  'googleCloudStorageCredentialsJson': "googleCloudStorageCredentialsJson_example", // String | A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey
  'googleCloudStorageProjectId': "googleCloudStorageProjectId_example", // String | Google Cloud Project ID
  'hostname': "hostname_example", // String | Hostname or IP address
  'maxConnections': 56, // Number | Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible).
  'name': "name_example", // String | Internal name for your reference
  'oneDriveAccountType': "oneDriveAccountType_example", // String | Either personal or business_other account types
  'password': "password_example", // String | Password if needed.
  'pinToSiteRegion': true, // Boolean | If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true.
  'port': 56, // Number | Port for remote server.  Not needed for S3.
  'privateKey': "privateKey_example", // String | Private key if needed.
  'privateKeyPassphrase': "privateKeyPassphrase_example", // String | Passphrase for private key if needed.
  'rackspaceApiKey': "rackspaceApiKey_example", // String | Rackspace API key from the Rackspace Cloud Control Panel.
  'rackspaceContainer': "rackspaceContainer_example", // String | The name of the container (top level directory) where files will sync.
  'rackspaceRegion': "rackspaceRegion_example", // String | Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/
  'rackspaceUsername': "rackspaceUsername_example", // String | Rackspace username used to login to the Rackspace Cloud Control Panel.
  'resetAuthentication': true, // Boolean | Reset authenticated account
  's3Bucket': "s3Bucket_example", // String | S3 bucket name
  's3CompatibleAccessKey': "s3CompatibleAccessKey_example", // String | S3-compatible Access Key.
  's3CompatibleBucket': "s3CompatibleBucket_example", // String | S3-compatible Bucket name
  's3CompatibleEndpoint': "s3CompatibleEndpoint_example", // String | S3-compatible endpoint
  's3CompatibleRegion': "s3CompatibleRegion_example", // String | S3-compatible endpoint
  's3CompatibleSecretKey': "s3CompatibleSecretKey_example", // String | S3-compatible secret key
  's3Region': "s3Region_example", // String | S3 region
  'serverCertificate': "serverCertificate_example", // String | Remote server certificate
  'serverHostKey': "serverHostKey_example", // String | Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts
  'serverType': "serverType_example", // String | Remote server type.
  'ssl': "ssl_example", // String | Should we require SSL?
  'sslCertificate': "sslCertificate_example", // String | SSL client certificate.
  'username': "username_example", // String | Remote server username.  Not needed for S3 buckets.
  'wasabiAccessKey': "wasabiAccessKey_example", // String | Wasabi access key.
  'wasabiBucket': "wasabiBucket_example", // String | Wasabi Bucket name
  'wasabiRegion': "wasabiRegion_example", // String | Wasabi region
  'wasabiSecretKey': "wasabiSecretKey_example" // String | Wasabi secret key.
};
apiInstance.postRemoteServers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **awsAccessKey** | **String**| AWS Access Key. | [optional] 
 **awsSecretKey** | **String**| AWS secret key. | [optional] 
 **azureBlobStorageAccessKey** | **String**| Azure Blob Storage secret key. | [optional] 
 **azureBlobStorageAccount** | **String**| Azure Blob Storage Account name | [optional] 
 **azureBlobStorageContainer** | **String**| Azure Blob Storage Container name | [optional] 
 **azureBlobStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] 
 **azureFilesStorageAccessKey** | **String**| Azure File Storage access key. | [optional] 
 **azureFilesStorageAccount** | **String**| Azure File Storage Account name | [optional] 
 **azureFilesStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] 
 **azureFilesStorageShareName** | **String**| Azure File Storage Share name | [optional] 
 **backblazeB2ApplicationKey** | **String**| Backblaze B2 Cloud Storage applicationKey. | [optional] 
 **backblazeB2Bucket** | **String**| Backblaze B2 Cloud Storage Bucket name | [optional] 
 **backblazeB2KeyId** | **String**| Backblaze B2 Cloud Storage keyID. | [optional] 
 **backblazeB2S3Endpoint** | **String**| Backblaze B2 Cloud Storage S3 Endpoint | [optional] 
 **enableDedicatedIps** | **Boolean**| &#x60;true&#x60; if remote server only accepts connections from dedicated IPs | [optional] 
 **filebaseAccessKey** | **String**| Filebase Access Key. | [optional] 
 **filebaseBucket** | **String**| Filebase Bucket name | [optional] 
 **filebaseSecretKey** | **String**| Filebase secret key | [optional] 
 **filesAgentPermissionSet** | **String**| Local permissions for files agent. read_only, write_only, or read_write | [optional] 
 **filesAgentRoot** | **String**| Agent local root path | [optional] 
 **googleCloudStorageBucket** | **String**| Google Cloud Storage bucket name | [optional] 
 **googleCloudStorageCredentialsJson** | **String**| A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey | [optional] 
 **googleCloudStorageProjectId** | **String**| Google Cloud Project ID | [optional] 
 **hostname** | **String**| Hostname or IP address | [optional] 
 **maxConnections** | **Number**| Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible). | [optional] 
 **name** | **String**| Internal name for your reference | [optional] 
 **oneDriveAccountType** | **String**| Either personal or business_other account types | [optional] 
 **password** | **String**| Password if needed. | [optional] 
 **pinToSiteRegion** | **Boolean**| If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true. | [optional] 
 **port** | **Number**| Port for remote server.  Not needed for S3. | [optional] 
 **privateKey** | **String**| Private key if needed. | [optional] 
 **privateKeyPassphrase** | **String**| Passphrase for private key if needed. | [optional] 
 **rackspaceApiKey** | **String**| Rackspace API key from the Rackspace Cloud Control Panel. | [optional] 
 **rackspaceContainer** | **String**| The name of the container (top level directory) where files will sync. | [optional] 
 **rackspaceRegion** | **String**| Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/ | [optional] 
 **rackspaceUsername** | **String**| Rackspace username used to login to the Rackspace Cloud Control Panel. | [optional] 
 **resetAuthentication** | **Boolean**| Reset authenticated account | [optional] 
 **s3Bucket** | **String**| S3 bucket name | [optional] 
 **s3CompatibleAccessKey** | **String**| S3-compatible Access Key. | [optional] 
 **s3CompatibleBucket** | **String**| S3-compatible Bucket name | [optional] 
 **s3CompatibleEndpoint** | **String**| S3-compatible endpoint | [optional] 
 **s3CompatibleRegion** | **String**| S3-compatible endpoint | [optional] 
 **s3CompatibleSecretKey** | **String**| S3-compatible secret key | [optional] 
 **s3Region** | **String**| S3 region | [optional] 
 **serverCertificate** | **String**| Remote server certificate | [optional] 
 **serverHostKey** | **String**| Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts | [optional] 
 **serverType** | **String**| Remote server type. | [optional] 
 **ssl** | **String**| Should we require SSL? | [optional] 
 **sslCertificate** | **String**| SSL client certificate. | [optional] 
 **username** | **String**| Remote server username.  Not needed for S3 buckets. | [optional] 
 **wasabiAccessKey** | **String**| Wasabi access key. | [optional] 
 **wasabiBucket** | **String**| Wasabi Bucket name | [optional] 
 **wasabiRegion** | **String**| Wasabi region | [optional] 
 **wasabiSecretKey** | **String**| Wasabi secret key. | [optional] 

### Return type

[**RemoteServerEntity**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postRemoteServersIdConfigurationFile

> RemoteServerConfigurationFileEntity postRemoteServersIdConfigurationFile(id, opts)

Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)

Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.RemoteServersApi();
let id = 56; // Number | Remote Server ID.
let opts = {
  'apiToken': "apiToken_example", // String | Files Agent API Token
  'configVersion': "configVersion_example", // String | agent config version
  'hostname': "hostname_example", // String | 
  'permissionSet': "permissionSet_example", // String | 
  'port': 56, // Number | Incoming port for files agent connections
  'privateKey': "privateKey_example", // String | private key
  'publicKey': "publicKey_example", // String | public key
  'root': "root_example", // String | Agent local root path
  'serverHostKey': "serverHostKey_example", // String | 
  'status': "status_example", // String | either running or shutdown
  'subdomain': "subdomain_example" // String | 
};
apiInstance.postRemoteServersIdConfigurationFile(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| Remote Server ID. | 
 **apiToken** | **String**| Files Agent API Token | [optional] 
 **configVersion** | **String**| agent config version | [optional] 
 **hostname** | **String**|  | [optional] 
 **permissionSet** | **String**|  | [optional] 
 **port** | **Number**| Incoming port for files agent connections | [optional] 
 **privateKey** | **String**| private key | [optional] 
 **publicKey** | **String**| public key | [optional] 
 **root** | **String**| Agent local root path | [optional] 
 **serverHostKey** | **String**|  | [optional] 
 **status** | **String**| either running or shutdown | [optional] 
 **subdomain** | **String**|  | [optional] 

### Return type

[**RemoteServerConfigurationFileEntity**](RemoteServerConfigurationFileEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

