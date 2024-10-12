# RemoteServersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRemoteServersId**](RemoteServersApi.md#deleteRemoteServersId) | **DELETE** /remote_servers/{id} | Delete Remote Server |
| [**getRemoteServers**](RemoteServersApi.md#getRemoteServers) | **GET** /remote_servers | List Remote Servers |
| [**getRemoteServersId**](RemoteServersApi.md#getRemoteServersId) | **GET** /remote_servers/{id} | Show Remote Server |
| [**getRemoteServersIdConfigurationFile**](RemoteServersApi.md#getRemoteServersIdConfigurationFile) | **GET** /remote_servers/{id}/configuration_file | Download configuration file (required for some Remote Server integrations, such as the Files.com Agent) |
| [**patchRemoteServersId**](RemoteServersApi.md#patchRemoteServersId) | **PATCH** /remote_servers/{id} | Update Remote Server |
| [**postRemoteServers**](RemoteServersApi.md#postRemoteServers) | **POST** /remote_servers | Create Remote Server |
| [**postRemoteServersIdConfigurationFile**](RemoteServersApi.md#postRemoteServersIdConfigurationFile) | **POST** /remote_servers/{id}/configuration_file | Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent) |


<a id="deleteRemoteServersId"></a>
# **deleteRemoteServersId**
> deleteRemoteServersId(id)

Delete Remote Server

Delete Remote Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    Integer id = 56; // Integer | Remote Server ID.
    try {
      apiInstance.deleteRemoteServersId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#deleteRemoteServersId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Remote Server ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getRemoteServers"></a>
# **getRemoteServers**
> List&lt;RemoteServerEntity&gt; getRemoteServers(cursor, perPage)

List Remote Servers

List Remote Servers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<RemoteServerEntity> result = apiInstance.getRemoteServers(cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#getRemoteServers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;RemoteServerEntity&gt;**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of RemoteServers objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getRemoteServersId"></a>
# **getRemoteServersId**
> RemoteServerEntity getRemoteServersId(id)

Show Remote Server

Show Remote Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    Integer id = 56; // Integer | Remote Server ID.
    try {
      RemoteServerEntity result = apiInstance.getRemoteServersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#getRemoteServersId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Remote Server ID. | |

### Return type

[**RemoteServerEntity**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RemoteServers object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getRemoteServersIdConfigurationFile"></a>
# **getRemoteServersIdConfigurationFile**
> RemoteServerConfigurationFileEntity getRemoteServersIdConfigurationFile(id)

Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)

Download configuration file (required for some Remote Server integrations, such as the Files.com Agent)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    Integer id = 56; // Integer | Remote Server ID.
    try {
      RemoteServerConfigurationFileEntity result = apiInstance.getRemoteServersIdConfigurationFile(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#getRemoteServersIdConfigurationFile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Remote Server ID. | |

### Return type

[**RemoteServerConfigurationFileEntity**](RemoteServerConfigurationFileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RemoteServers object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchRemoteServersId"></a>
# **patchRemoteServersId**
> RemoteServerEntity patchRemoteServersId(id, awsAccessKey, awsSecretKey, azureBlobStorageAccessKey, azureBlobStorageAccount, azureBlobStorageContainer, azureBlobStorageSasToken, azureFilesStorageAccessKey, azureFilesStorageAccount, azureFilesStorageSasToken, azureFilesStorageShareName, backblazeB2ApplicationKey, backblazeB2Bucket, backblazeB2KeyId, backblazeB2S3Endpoint, enableDedicatedIps, filebaseAccessKey, filebaseBucket, filebaseSecretKey, filesAgentPermissionSet, filesAgentRoot, googleCloudStorageBucket, googleCloudStorageCredentialsJson, googleCloudStorageProjectId, hostname, maxConnections, name, oneDriveAccountType, password, pinToSiteRegion, port, privateKey, privateKeyPassphrase, rackspaceApiKey, rackspaceContainer, rackspaceRegion, rackspaceUsername, resetAuthentication, s3Bucket, s3CompatibleAccessKey, s3CompatibleBucket, s3CompatibleEndpoint, s3CompatibleRegion, s3CompatibleSecretKey, s3Region, serverCertificate, serverHostKey, serverType, ssl, sslCertificate, username, wasabiAccessKey, wasabiBucket, wasabiRegion, wasabiSecretKey)

Update Remote Server

Update Remote Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    Integer id = 56; // Integer | Remote Server ID.
    String awsAccessKey = "awsAccessKey_example"; // String | AWS Access Key.
    String awsSecretKey = "awsSecretKey_example"; // String | AWS secret key.
    String azureBlobStorageAccessKey = "azureBlobStorageAccessKey_example"; // String | Azure Blob Storage secret key.
    String azureBlobStorageAccount = "azureBlobStorageAccount_example"; // String | Azure Blob Storage Account name
    String azureBlobStorageContainer = "azureBlobStorageContainer_example"; // String | Azure Blob Storage Container name
    String azureBlobStorageSasToken = "azureBlobStorageSasToken_example"; // String | Shared Access Signature (SAS) token
    String azureFilesStorageAccessKey = "azureFilesStorageAccessKey_example"; // String | Azure File Storage access key.
    String azureFilesStorageAccount = "azureFilesStorageAccount_example"; // String | Azure File Storage Account name
    String azureFilesStorageSasToken = "azureFilesStorageSasToken_example"; // String | Shared Access Signature (SAS) token
    String azureFilesStorageShareName = "azureFilesStorageShareName_example"; // String | Azure File Storage Share name
    String backblazeB2ApplicationKey = "backblazeB2ApplicationKey_example"; // String | Backblaze B2 Cloud Storage applicationKey.
    String backblazeB2Bucket = "backblazeB2Bucket_example"; // String | Backblaze B2 Cloud Storage Bucket name
    String backblazeB2KeyId = "backblazeB2KeyId_example"; // String | Backblaze B2 Cloud Storage keyID.
    String backblazeB2S3Endpoint = "backblazeB2S3Endpoint_example"; // String | Backblaze B2 Cloud Storage S3 Endpoint
    Boolean enableDedicatedIps = true; // Boolean | `true` if remote server only accepts connections from dedicated IPs
    String filebaseAccessKey = "filebaseAccessKey_example"; // String | Filebase Access Key.
    String filebaseBucket = "filebaseBucket_example"; // String | Filebase Bucket name
    String filebaseSecretKey = "filebaseSecretKey_example"; // String | Filebase secret key
    String filesAgentPermissionSet = "read_write"; // String | Local permissions for files agent. read_only, write_only, or read_write
    String filesAgentRoot = "filesAgentRoot_example"; // String | Agent local root path
    String googleCloudStorageBucket = "googleCloudStorageBucket_example"; // String | Google Cloud Storage bucket name
    String googleCloudStorageCredentialsJson = "googleCloudStorageCredentialsJson_example"; // String | A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey
    String googleCloudStorageProjectId = "googleCloudStorageProjectId_example"; // String | Google Cloud Project ID
    String hostname = "hostname_example"; // String | Hostname or IP address
    Integer maxConnections = 56; // Integer | Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible).
    String name = "name_example"; // String | Internal name for your reference
    String oneDriveAccountType = "personal"; // String | Either personal or business_other account types
    String password = "password_example"; // String | Password if needed.
    Boolean pinToSiteRegion = true; // Boolean | If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true.
    Integer port = 56; // Integer | Port for remote server.  Not needed for S3.
    String privateKey = "privateKey_example"; // String | Private key if needed.
    String privateKeyPassphrase = "privateKeyPassphrase_example"; // String | Passphrase for private key if needed.
    String rackspaceApiKey = "rackspaceApiKey_example"; // String | Rackspace API key from the Rackspace Cloud Control Panel.
    String rackspaceContainer = "rackspaceContainer_example"; // String | The name of the container (top level directory) where files will sync.
    String rackspaceRegion = "rackspaceRegion_example"; // String | Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/
    String rackspaceUsername = "rackspaceUsername_example"; // String | Rackspace username used to login to the Rackspace Cloud Control Panel.
    Boolean resetAuthentication = true; // Boolean | Reset authenticated account
    String s3Bucket = "s3Bucket_example"; // String | S3 bucket name
    String s3CompatibleAccessKey = "s3CompatibleAccessKey_example"; // String | S3-compatible Access Key.
    String s3CompatibleBucket = "s3CompatibleBucket_example"; // String | S3-compatible Bucket name
    String s3CompatibleEndpoint = "s3CompatibleEndpoint_example"; // String | S3-compatible endpoint
    String s3CompatibleRegion = "s3CompatibleRegion_example"; // String | S3-compatible endpoint
    String s3CompatibleSecretKey = "s3CompatibleSecretKey_example"; // String | S3-compatible secret key
    String s3Region = "s3Region_example"; // String | S3 region
    String serverCertificate = "require_match"; // String | Remote server certificate
    String serverHostKey = "serverHostKey_example"; // String | Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts
    String serverType = "ftp"; // String | Remote server type.
    String ssl = "if_available"; // String | Should we require SSL?
    String sslCertificate = "sslCertificate_example"; // String | SSL client certificate.
    String username = "username_example"; // String | Remote server username.  Not needed for S3 buckets.
    String wasabiAccessKey = "wasabiAccessKey_example"; // String | Wasabi access key.
    String wasabiBucket = "wasabiBucket_example"; // String | Wasabi Bucket name
    String wasabiRegion = "wasabiRegion_example"; // String | Wasabi region
    String wasabiSecretKey = "wasabiSecretKey_example"; // String | Wasabi secret key.
    try {
      RemoteServerEntity result = apiInstance.patchRemoteServersId(id, awsAccessKey, awsSecretKey, azureBlobStorageAccessKey, azureBlobStorageAccount, azureBlobStorageContainer, azureBlobStorageSasToken, azureFilesStorageAccessKey, azureFilesStorageAccount, azureFilesStorageSasToken, azureFilesStorageShareName, backblazeB2ApplicationKey, backblazeB2Bucket, backblazeB2KeyId, backblazeB2S3Endpoint, enableDedicatedIps, filebaseAccessKey, filebaseBucket, filebaseSecretKey, filesAgentPermissionSet, filesAgentRoot, googleCloudStorageBucket, googleCloudStorageCredentialsJson, googleCloudStorageProjectId, hostname, maxConnections, name, oneDriveAccountType, password, pinToSiteRegion, port, privateKey, privateKeyPassphrase, rackspaceApiKey, rackspaceContainer, rackspaceRegion, rackspaceUsername, resetAuthentication, s3Bucket, s3CompatibleAccessKey, s3CompatibleBucket, s3CompatibleEndpoint, s3CompatibleRegion, s3CompatibleSecretKey, s3Region, serverCertificate, serverHostKey, serverType, ssl, sslCertificate, username, wasabiAccessKey, wasabiBucket, wasabiRegion, wasabiSecretKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#patchRemoteServersId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Remote Server ID. | |
| **awsAccessKey** | **String**| AWS Access Key. | [optional] |
| **awsSecretKey** | **String**| AWS secret key. | [optional] |
| **azureBlobStorageAccessKey** | **String**| Azure Blob Storage secret key. | [optional] |
| **azureBlobStorageAccount** | **String**| Azure Blob Storage Account name | [optional] |
| **azureBlobStorageContainer** | **String**| Azure Blob Storage Container name | [optional] |
| **azureBlobStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] |
| **azureFilesStorageAccessKey** | **String**| Azure File Storage access key. | [optional] |
| **azureFilesStorageAccount** | **String**| Azure File Storage Account name | [optional] |
| **azureFilesStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] |
| **azureFilesStorageShareName** | **String**| Azure File Storage Share name | [optional] |
| **backblazeB2ApplicationKey** | **String**| Backblaze B2 Cloud Storage applicationKey. | [optional] |
| **backblazeB2Bucket** | **String**| Backblaze B2 Cloud Storage Bucket name | [optional] |
| **backblazeB2KeyId** | **String**| Backblaze B2 Cloud Storage keyID. | [optional] |
| **backblazeB2S3Endpoint** | **String**| Backblaze B2 Cloud Storage S3 Endpoint | [optional] |
| **enableDedicatedIps** | **Boolean**| &#x60;true&#x60; if remote server only accepts connections from dedicated IPs | [optional] |
| **filebaseAccessKey** | **String**| Filebase Access Key. | [optional] |
| **filebaseBucket** | **String**| Filebase Bucket name | [optional] |
| **filebaseSecretKey** | **String**| Filebase secret key | [optional] |
| **filesAgentPermissionSet** | **String**| Local permissions for files agent. read_only, write_only, or read_write | [optional] [enum: read_write, read_only, write_only] |
| **filesAgentRoot** | **String**| Agent local root path | [optional] |
| **googleCloudStorageBucket** | **String**| Google Cloud Storage bucket name | [optional] |
| **googleCloudStorageCredentialsJson** | **String**| A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey | [optional] |
| **googleCloudStorageProjectId** | **String**| Google Cloud Project ID | [optional] |
| **hostname** | **String**| Hostname or IP address | [optional] |
| **maxConnections** | **Integer**| Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible). | [optional] |
| **name** | **String**| Internal name for your reference | [optional] |
| **oneDriveAccountType** | **String**| Either personal or business_other account types | [optional] [enum: personal, business_other] |
| **password** | **String**| Password if needed. | [optional] |
| **pinToSiteRegion** | **Boolean**| If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true. | [optional] |
| **port** | **Integer**| Port for remote server.  Not needed for S3. | [optional] |
| **privateKey** | **String**| Private key if needed. | [optional] |
| **privateKeyPassphrase** | **String**| Passphrase for private key if needed. | [optional] |
| **rackspaceApiKey** | **String**| Rackspace API key from the Rackspace Cloud Control Panel. | [optional] |
| **rackspaceContainer** | **String**| The name of the container (top level directory) where files will sync. | [optional] |
| **rackspaceRegion** | **String**| Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/ | [optional] |
| **rackspaceUsername** | **String**| Rackspace username used to login to the Rackspace Cloud Control Panel. | [optional] |
| **resetAuthentication** | **Boolean**| Reset authenticated account | [optional] |
| **s3Bucket** | **String**| S3 bucket name | [optional] |
| **s3CompatibleAccessKey** | **String**| S3-compatible Access Key. | [optional] |
| **s3CompatibleBucket** | **String**| S3-compatible Bucket name | [optional] |
| **s3CompatibleEndpoint** | **String**| S3-compatible endpoint | [optional] |
| **s3CompatibleRegion** | **String**| S3-compatible endpoint | [optional] |
| **s3CompatibleSecretKey** | **String**| S3-compatible secret key | [optional] |
| **s3Region** | **String**| S3 region | [optional] |
| **serverCertificate** | **String**| Remote server certificate | [optional] [enum: require_match, allow_any] |
| **serverHostKey** | **String**| Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts | [optional] |
| **serverType** | **String**| Remote server type. | [optional] [enum: ftp, sftp, s3, google_cloud_storage, webdav, wasabi, backblaze_b2, one_drive, rackspace, box, dropbox, google_drive, azure, sharepoint, s3_compatible, azure_files, files_agent, filebase] |
| **ssl** | **String**| Should we require SSL? | [optional] [enum: if_available, require, require_implicit, never] |
| **sslCertificate** | **String**| SSL client certificate. | [optional] |
| **username** | **String**| Remote server username.  Not needed for S3 buckets. | [optional] |
| **wasabiAccessKey** | **String**| Wasabi access key. | [optional] |
| **wasabiBucket** | **String**| Wasabi Bucket name | [optional] |
| **wasabiRegion** | **String**| Wasabi region | [optional] |
| **wasabiSecretKey** | **String**| Wasabi secret key. | [optional] |

### Return type

[**RemoteServerEntity**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The RemoteServers object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postRemoteServers"></a>
# **postRemoteServers**
> RemoteServerEntity postRemoteServers(awsAccessKey, awsSecretKey, azureBlobStorageAccessKey, azureBlobStorageAccount, azureBlobStorageContainer, azureBlobStorageSasToken, azureFilesStorageAccessKey, azureFilesStorageAccount, azureFilesStorageSasToken, azureFilesStorageShareName, backblazeB2ApplicationKey, backblazeB2Bucket, backblazeB2KeyId, backblazeB2S3Endpoint, enableDedicatedIps, filebaseAccessKey, filebaseBucket, filebaseSecretKey, filesAgentPermissionSet, filesAgentRoot, googleCloudStorageBucket, googleCloudStorageCredentialsJson, googleCloudStorageProjectId, hostname, maxConnections, name, oneDriveAccountType, password, pinToSiteRegion, port, privateKey, privateKeyPassphrase, rackspaceApiKey, rackspaceContainer, rackspaceRegion, rackspaceUsername, resetAuthentication, s3Bucket, s3CompatibleAccessKey, s3CompatibleBucket, s3CompatibleEndpoint, s3CompatibleRegion, s3CompatibleSecretKey, s3Region, serverCertificate, serverHostKey, serverType, ssl, sslCertificate, username, wasabiAccessKey, wasabiBucket, wasabiRegion, wasabiSecretKey)

Create Remote Server

Create Remote Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    String awsAccessKey = "awsAccessKey_example"; // String | AWS Access Key.
    String awsSecretKey = "awsSecretKey_example"; // String | AWS secret key.
    String azureBlobStorageAccessKey = "azureBlobStorageAccessKey_example"; // String | Azure Blob Storage secret key.
    String azureBlobStorageAccount = "azureBlobStorageAccount_example"; // String | Azure Blob Storage Account name
    String azureBlobStorageContainer = "azureBlobStorageContainer_example"; // String | Azure Blob Storage Container name
    String azureBlobStorageSasToken = "azureBlobStorageSasToken_example"; // String | Shared Access Signature (SAS) token
    String azureFilesStorageAccessKey = "azureFilesStorageAccessKey_example"; // String | Azure File Storage access key.
    String azureFilesStorageAccount = "azureFilesStorageAccount_example"; // String | Azure File Storage Account name
    String azureFilesStorageSasToken = "azureFilesStorageSasToken_example"; // String | Shared Access Signature (SAS) token
    String azureFilesStorageShareName = "azureFilesStorageShareName_example"; // String | Azure File Storage Share name
    String backblazeB2ApplicationKey = "backblazeB2ApplicationKey_example"; // String | Backblaze B2 Cloud Storage applicationKey.
    String backblazeB2Bucket = "backblazeB2Bucket_example"; // String | Backblaze B2 Cloud Storage Bucket name
    String backblazeB2KeyId = "backblazeB2KeyId_example"; // String | Backblaze B2 Cloud Storage keyID.
    String backblazeB2S3Endpoint = "backblazeB2S3Endpoint_example"; // String | Backblaze B2 Cloud Storage S3 Endpoint
    Boolean enableDedicatedIps = true; // Boolean | `true` if remote server only accepts connections from dedicated IPs
    String filebaseAccessKey = "filebaseAccessKey_example"; // String | Filebase Access Key.
    String filebaseBucket = "filebaseBucket_example"; // String | Filebase Bucket name
    String filebaseSecretKey = "filebaseSecretKey_example"; // String | Filebase secret key
    String filesAgentPermissionSet = "read_write"; // String | Local permissions for files agent. read_only, write_only, or read_write
    String filesAgentRoot = "filesAgentRoot_example"; // String | Agent local root path
    String googleCloudStorageBucket = "googleCloudStorageBucket_example"; // String | Google Cloud Storage bucket name
    String googleCloudStorageCredentialsJson = "googleCloudStorageCredentialsJson_example"; // String | A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey
    String googleCloudStorageProjectId = "googleCloudStorageProjectId_example"; // String | Google Cloud Project ID
    String hostname = "hostname_example"; // String | Hostname or IP address
    Integer maxConnections = 56; // Integer | Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible).
    String name = "name_example"; // String | Internal name for your reference
    String oneDriveAccountType = "personal"; // String | Either personal or business_other account types
    String password = "password_example"; // String | Password if needed.
    Boolean pinToSiteRegion = true; // Boolean | If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true.
    Integer port = 56; // Integer | Port for remote server.  Not needed for S3.
    String privateKey = "privateKey_example"; // String | Private key if needed.
    String privateKeyPassphrase = "privateKeyPassphrase_example"; // String | Passphrase for private key if needed.
    String rackspaceApiKey = "rackspaceApiKey_example"; // String | Rackspace API key from the Rackspace Cloud Control Panel.
    String rackspaceContainer = "rackspaceContainer_example"; // String | The name of the container (top level directory) where files will sync.
    String rackspaceRegion = "rackspaceRegion_example"; // String | Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/
    String rackspaceUsername = "rackspaceUsername_example"; // String | Rackspace username used to login to the Rackspace Cloud Control Panel.
    Boolean resetAuthentication = true; // Boolean | Reset authenticated account
    String s3Bucket = "s3Bucket_example"; // String | S3 bucket name
    String s3CompatibleAccessKey = "s3CompatibleAccessKey_example"; // String | S3-compatible Access Key.
    String s3CompatibleBucket = "s3CompatibleBucket_example"; // String | S3-compatible Bucket name
    String s3CompatibleEndpoint = "s3CompatibleEndpoint_example"; // String | S3-compatible endpoint
    String s3CompatibleRegion = "s3CompatibleRegion_example"; // String | S3-compatible endpoint
    String s3CompatibleSecretKey = "s3CompatibleSecretKey_example"; // String | S3-compatible secret key
    String s3Region = "s3Region_example"; // String | S3 region
    String serverCertificate = "require_match"; // String | Remote server certificate
    String serverHostKey = "serverHostKey_example"; // String | Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts
    String serverType = "ftp"; // String | Remote server type.
    String ssl = "if_available"; // String | Should we require SSL?
    String sslCertificate = "sslCertificate_example"; // String | SSL client certificate.
    String username = "username_example"; // String | Remote server username.  Not needed for S3 buckets.
    String wasabiAccessKey = "wasabiAccessKey_example"; // String | Wasabi access key.
    String wasabiBucket = "wasabiBucket_example"; // String | Wasabi Bucket name
    String wasabiRegion = "wasabiRegion_example"; // String | Wasabi region
    String wasabiSecretKey = "wasabiSecretKey_example"; // String | Wasabi secret key.
    try {
      RemoteServerEntity result = apiInstance.postRemoteServers(awsAccessKey, awsSecretKey, azureBlobStorageAccessKey, azureBlobStorageAccount, azureBlobStorageContainer, azureBlobStorageSasToken, azureFilesStorageAccessKey, azureFilesStorageAccount, azureFilesStorageSasToken, azureFilesStorageShareName, backblazeB2ApplicationKey, backblazeB2Bucket, backblazeB2KeyId, backblazeB2S3Endpoint, enableDedicatedIps, filebaseAccessKey, filebaseBucket, filebaseSecretKey, filesAgentPermissionSet, filesAgentRoot, googleCloudStorageBucket, googleCloudStorageCredentialsJson, googleCloudStorageProjectId, hostname, maxConnections, name, oneDriveAccountType, password, pinToSiteRegion, port, privateKey, privateKeyPassphrase, rackspaceApiKey, rackspaceContainer, rackspaceRegion, rackspaceUsername, resetAuthentication, s3Bucket, s3CompatibleAccessKey, s3CompatibleBucket, s3CompatibleEndpoint, s3CompatibleRegion, s3CompatibleSecretKey, s3Region, serverCertificate, serverHostKey, serverType, ssl, sslCertificate, username, wasabiAccessKey, wasabiBucket, wasabiRegion, wasabiSecretKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#postRemoteServers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **awsAccessKey** | **String**| AWS Access Key. | [optional] |
| **awsSecretKey** | **String**| AWS secret key. | [optional] |
| **azureBlobStorageAccessKey** | **String**| Azure Blob Storage secret key. | [optional] |
| **azureBlobStorageAccount** | **String**| Azure Blob Storage Account name | [optional] |
| **azureBlobStorageContainer** | **String**| Azure Blob Storage Container name | [optional] |
| **azureBlobStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] |
| **azureFilesStorageAccessKey** | **String**| Azure File Storage access key. | [optional] |
| **azureFilesStorageAccount** | **String**| Azure File Storage Account name | [optional] |
| **azureFilesStorageSasToken** | **String**| Shared Access Signature (SAS) token | [optional] |
| **azureFilesStorageShareName** | **String**| Azure File Storage Share name | [optional] |
| **backblazeB2ApplicationKey** | **String**| Backblaze B2 Cloud Storage applicationKey. | [optional] |
| **backblazeB2Bucket** | **String**| Backblaze B2 Cloud Storage Bucket name | [optional] |
| **backblazeB2KeyId** | **String**| Backblaze B2 Cloud Storage keyID. | [optional] |
| **backblazeB2S3Endpoint** | **String**| Backblaze B2 Cloud Storage S3 Endpoint | [optional] |
| **enableDedicatedIps** | **Boolean**| &#x60;true&#x60; if remote server only accepts connections from dedicated IPs | [optional] |
| **filebaseAccessKey** | **String**| Filebase Access Key. | [optional] |
| **filebaseBucket** | **String**| Filebase Bucket name | [optional] |
| **filebaseSecretKey** | **String**| Filebase secret key | [optional] |
| **filesAgentPermissionSet** | **String**| Local permissions for files agent. read_only, write_only, or read_write | [optional] [enum: read_write, read_only, write_only] |
| **filesAgentRoot** | **String**| Agent local root path | [optional] |
| **googleCloudStorageBucket** | **String**| Google Cloud Storage bucket name | [optional] |
| **googleCloudStorageCredentialsJson** | **String**| A JSON file that contains the private key. To generate see https://cloud.google.com/storage/docs/json_api/v1/how-tos/authorizing#APIKey | [optional] |
| **googleCloudStorageProjectId** | **String**| Google Cloud Project ID | [optional] |
| **hostname** | **String**| Hostname or IP address | [optional] |
| **maxConnections** | **Integer**| Max number of parallel connections.  Ignored for S3 connections (we will parallelize these as much as possible). | [optional] |
| **name** | **String**| Internal name for your reference | [optional] |
| **oneDriveAccountType** | **String**| Either personal or business_other account types | [optional] [enum: personal, business_other] |
| **password** | **String**| Password if needed. | [optional] |
| **pinToSiteRegion** | **Boolean**| If true, we will ensure that all communications with this remote server are made through the primary region of the site.  This setting can also be overridden by a sitewide setting which will force it to true. | [optional] |
| **port** | **Integer**| Port for remote server.  Not needed for S3. | [optional] |
| **privateKey** | **String**| Private key if needed. | [optional] |
| **privateKeyPassphrase** | **String**| Passphrase for private key if needed. | [optional] |
| **rackspaceApiKey** | **String**| Rackspace API key from the Rackspace Cloud Control Panel. | [optional] |
| **rackspaceContainer** | **String**| The name of the container (top level directory) where files will sync. | [optional] |
| **rackspaceRegion** | **String**| Three letter airport code for Rackspace region. See https://support.rackspace.com/how-to/about-regions/ | [optional] |
| **rackspaceUsername** | **String**| Rackspace username used to login to the Rackspace Cloud Control Panel. | [optional] |
| **resetAuthentication** | **Boolean**| Reset authenticated account | [optional] |
| **s3Bucket** | **String**| S3 bucket name | [optional] |
| **s3CompatibleAccessKey** | **String**| S3-compatible Access Key. | [optional] |
| **s3CompatibleBucket** | **String**| S3-compatible Bucket name | [optional] |
| **s3CompatibleEndpoint** | **String**| S3-compatible endpoint | [optional] |
| **s3CompatibleRegion** | **String**| S3-compatible endpoint | [optional] |
| **s3CompatibleSecretKey** | **String**| S3-compatible secret key | [optional] |
| **s3Region** | **String**| S3 region | [optional] |
| **serverCertificate** | **String**| Remote server certificate | [optional] [enum: require_match, allow_any] |
| **serverHostKey** | **String**| Remote server SSH Host Key. If provided, we will require that the server host key matches the provided key. Uses OpenSSH format similar to what would go into ~/.ssh/known_hosts | [optional] |
| **serverType** | **String**| Remote server type. | [optional] [enum: ftp, sftp, s3, google_cloud_storage, webdav, wasabi, backblaze_b2, one_drive, rackspace, box, dropbox, google_drive, azure, sharepoint, s3_compatible, azure_files, files_agent, filebase] |
| **ssl** | **String**| Should we require SSL? | [optional] [enum: if_available, require, require_implicit, never] |
| **sslCertificate** | **String**| SSL client certificate. | [optional] |
| **username** | **String**| Remote server username.  Not needed for S3 buckets. | [optional] |
| **wasabiAccessKey** | **String**| Wasabi access key. | [optional] |
| **wasabiBucket** | **String**| Wasabi Bucket name | [optional] |
| **wasabiRegion** | **String**| Wasabi region | [optional] |
| **wasabiSecretKey** | **String**| Wasabi secret key. | [optional] |

### Return type

[**RemoteServerEntity**](RemoteServerEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The RemoteServers object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postRemoteServersIdConfigurationFile"></a>
# **postRemoteServersIdConfigurationFile**
> RemoteServerConfigurationFileEntity postRemoteServersIdConfigurationFile(id, apiToken, configVersion, hostname, permissionSet, port, privateKey, publicKey, root, serverHostKey, status, subdomain)

Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)

Post local changes, check in, and download configuration file (used by some Remote Server integrations, such as the Files.com Agent)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RemoteServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RemoteServersApi apiInstance = new RemoteServersApi(defaultClient);
    Integer id = 56; // Integer | Remote Server ID.
    String apiToken = "apiToken_example"; // String | Files Agent API Token
    String configVersion = "configVersion_example"; // String | agent config version
    String hostname = "hostname_example"; // String | 
    String permissionSet = "permissionSet_example"; // String | 
    Integer port = 56; // Integer | Incoming port for files agent connections
    String privateKey = "privateKey_example"; // String | private key
    String publicKey = "publicKey_example"; // String | public key
    String root = "root_example"; // String | Agent local root path
    String serverHostKey = "serverHostKey_example"; // String | 
    String status = "status_example"; // String | either running or shutdown
    String subdomain = "subdomain_example"; // String | 
    try {
      RemoteServerConfigurationFileEntity result = apiInstance.postRemoteServersIdConfigurationFile(id, apiToken, configVersion, hostname, permissionSet, port, privateKey, publicKey, root, serverHostKey, status, subdomain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RemoteServersApi#postRemoteServersIdConfigurationFile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Remote Server ID. | |
| **apiToken** | **String**| Files Agent API Token | [optional] |
| **configVersion** | **String**| agent config version | [optional] |
| **hostname** | **String**|  | [optional] |
| **permissionSet** | **String**|  | [optional] |
| **port** | **Integer**| Incoming port for files agent connections | [optional] |
| **privateKey** | **String**| private key | [optional] |
| **publicKey** | **String**| public key | [optional] |
| **root** | **String**| Agent local root path | [optional] |
| **serverHostKey** | **String**|  | [optional] |
| **status** | **String**| either running or shutdown | [optional] |
| **subdomain** | **String**|  | [optional] |

### Return type

[**RemoteServerConfigurationFileEntity**](RemoteServerConfigurationFileEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The RemoteServers object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

