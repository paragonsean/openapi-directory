# BackupRestoreApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupPartition**](BackupRestoreApi.md#backupPartition) | **POST** /Partitions/{partitionId}/$/Backup | Triggers backup of the partition&#39;s state. |
| [**createBackupPolicy**](BackupRestoreApi.md#createBackupPolicy) | **POST** /BackupRestore/BackupPolicies/$/Create | Creates a backup policy. |
| [**deleteBackupPolicy**](BackupRestoreApi.md#deleteBackupPolicy) | **POST** /BackupRestore/BackupPolicies/{backupPolicyName}/$/Delete | Deletes the backup policy. |
| [**disableApplicationBackup**](BackupRestoreApi.md#disableApplicationBackup) | **POST** /Applications/{applicationId}/$/DisableBackup | Disables periodic backup of Service Fabric application. |
| [**disablePartitionBackup**](BackupRestoreApi.md#disablePartitionBackup) | **POST** /Partitions/{partitionId}/$/DisableBackup | Disables periodic backup of Service Fabric partition which was previously enabled. |
| [**disableServiceBackup**](BackupRestoreApi.md#disableServiceBackup) | **POST** /Services/{serviceId}/$/DisableBackup | Disables periodic backup of Service Fabric service which was previously enabled. |
| [**enableApplicationBackup**](BackupRestoreApi.md#enableApplicationBackup) | **POST** /Applications/{applicationId}/$/EnableBackup | Enables periodic backup of stateful partitions under this Service Fabric application. |
| [**enablePartitionBackup**](BackupRestoreApi.md#enablePartitionBackup) | **POST** /Partitions/{partitionId}/$/EnableBackup | Enables periodic backup of the stateful persisted partition. |
| [**enableServiceBackup**](BackupRestoreApi.md#enableServiceBackup) | **POST** /Services/{serviceId}/$/EnableBackup | Enables periodic backup of stateful partitions under this Service Fabric service. |
| [**getAllEntitiesBackedUpByPolicy**](BackupRestoreApi.md#getAllEntitiesBackedUpByPolicy) | **GET** /BackupRestore/BackupPolicies/{backupPolicyName}/$/GetBackupEnabledEntities | Gets the list of backup entities that are associated with this policy. |
| [**getApplicationBackupConfigurationInfo**](BackupRestoreApi.md#getApplicationBackupConfigurationInfo) | **GET** /Applications/{applicationId}/$/GetBackupConfigurationInfo | Gets the Service Fabric application backup configuration information. |
| [**getApplicationBackupList**](BackupRestoreApi.md#getApplicationBackupList) | **GET** /Applications/{applicationId}/$/GetBackups | Gets the list of backups available for every partition in this application. |
| [**getBackupPolicyByName**](BackupRestoreApi.md#getBackupPolicyByName) | **GET** /BackupRestore/BackupPolicies/{backupPolicyName} | Gets a particular backup policy by name. |
| [**getBackupPolicyList**](BackupRestoreApi.md#getBackupPolicyList) | **GET** /BackupRestore/BackupPolicies | Gets all the backup policies configured. |
| [**getBackupsFromBackupLocation**](BackupRestoreApi.md#getBackupsFromBackupLocation) | **POST** /BackupRestore/$/GetBackups | Gets the list of backups available for the specified backed up entity at the specified backup location. |
| [**getPartitionBackupConfigurationInfo**](BackupRestoreApi.md#getPartitionBackupConfigurationInfo) | **GET** /Partitions/{partitionId}/$/GetBackupConfigurationInfo | Gets the partition backup configuration information |
| [**getPartitionBackupList**](BackupRestoreApi.md#getPartitionBackupList) | **GET** /Partitions/{partitionId}/$/GetBackups | Gets the list of backups available for the specified partition. |
| [**getPartitionBackupProgress**](BackupRestoreApi.md#getPartitionBackupProgress) | **GET** /Partitions/{partitionId}/$/GetBackupProgress | Gets details for the latest backup triggered for this partition. |
| [**getPartitionRestoreProgress**](BackupRestoreApi.md#getPartitionRestoreProgress) | **GET** /Partitions/{partitionId}/$/GetRestoreProgress | Gets details for the latest restore operation triggered for this partition. |
| [**getServiceBackupConfigurationInfo**](BackupRestoreApi.md#getServiceBackupConfigurationInfo) | **GET** /Services/{serviceId}/$/GetBackupConfigurationInfo | Gets the Service Fabric service backup configuration information. |
| [**getServiceBackupList**](BackupRestoreApi.md#getServiceBackupList) | **GET** /Services/{serviceId}/$/GetBackups | Gets the list of backups available for every partition in this service. |
| [**restorePartition**](BackupRestoreApi.md#restorePartition) | **POST** /Partitions/{partitionId}/$/Restore | Triggers restore of the state of the partition using the specified restore partition description. |
| [**resumeApplicationBackup**](BackupRestoreApi.md#resumeApplicationBackup) | **POST** /Applications/{applicationId}/$/ResumeBackup | Resumes periodic backup of a Service Fabric application which was previously suspended. |
| [**resumePartitionBackup**](BackupRestoreApi.md#resumePartitionBackup) | **POST** /Partitions/{partitionId}/$/ResumeBackup | Resumes periodic backup of partition which was previously suspended. |
| [**resumeServiceBackup**](BackupRestoreApi.md#resumeServiceBackup) | **POST** /Services/{serviceId}/$/ResumeBackup | Resumes periodic backup of a Service Fabric service which was previously suspended. |
| [**suspendApplicationBackup**](BackupRestoreApi.md#suspendApplicationBackup) | **POST** /Applications/{applicationId}/$/SuspendBackup | Suspends periodic backup for the specified Service Fabric application. |
| [**suspendPartitionBackup**](BackupRestoreApi.md#suspendPartitionBackup) | **POST** /Partitions/{partitionId}/$/SuspendBackup | Suspends periodic backup for the specified partition. |
| [**suspendServiceBackup**](BackupRestoreApi.md#suspendServiceBackup) | **POST** /Services/{serviceId}/$/SuspendBackup | Suspends periodic backup for the specified Service Fabric service. |
| [**updateBackupPolicy**](BackupRestoreApi.md#updateBackupPolicy) | **POST** /BackupRestore/BackupPolicies/{backupPolicyName}/$/Update | Updates the backup policy. |


<a id="backupPartition"></a>
# **backupPartition**
> backupPartition(partitionId, apiVersion, backupTimeout, timeout, backupPartitionDescription)

Triggers backup of the partition&#39;s state.

Creates a backup of the stateful persisted partition&#39;s state. In case the partition is already being periodically backed up, then by default the new backup is created at the same backup storage. One can also override the same by specifying the backup storage details as part of the request body. Once the backup is initiated, its progress can be tracked using the GetBackupProgress operation.  In case, the operation times out, specify a greater backup timeout value in the query parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Integer backupTimeout = 10; // Integer | Specifies the maximum amount of time, in minutes, to wait for the backup operation to complete. Post that, the operation completes with timeout error. However, in certain corner cases it could be that though the operation returns back timeout, the backup actually goes through. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. The default value for the same is 10 minutes.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    BackupPartitionDescription backupPartitionDescription = new BackupPartitionDescription(); // BackupPartitionDescription | Describes the parameters to backup the partition now. If not present, backup operation uses default parameters from the backup policy current associated with this partition.
    try {
      apiInstance.backupPartition(partitionId, apiVersion, backupTimeout, timeout, backupPartitionDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#backupPartition");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **backupTimeout** | **Integer**| Specifies the maximum amount of time, in minutes, to wait for the backup operation to complete. Post that, the operation completes with timeout error. However, in certain corner cases it could be that though the operation returns back timeout, the backup actually goes through. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. The default value for the same is 10 minutes. | [optional] [default to 10] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **backupPartitionDescription** | [**BackupPartitionDescription**](BackupPartitionDescription.md)| Describes the parameters to backup the partition now. If not present, backup operation uses default parameters from the backup policy current associated with this partition. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and backup will be initiated. Use GetPartitionBackupProgress operation to get the status of the backup operation. |  -  |
| **0** | The detailed error response. |  -  |

<a id="createBackupPolicy"></a>
# **createBackupPolicy**
> createBackupPolicy(apiVersion, backupPolicyDescription, timeout)

Creates a backup policy.

Creates a backup policy which can be associated later with a Service Fabric application, service or a partition for periodic backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    BackupPolicyDescription backupPolicyDescription = new BackupPolicyDescription(); // BackupPolicyDescription | Describes the backup policy.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.createBackupPolicy(apiVersion, backupPolicyDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#createBackupPolicy");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **backupPolicyDescription** | [**BackupPolicyDescription**](BackupPolicyDescription.md)| Describes the backup policy. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | A successful operation returns 201 status code and creates a new backup policy. |  -  |
| **0** | The detailed error response. |  -  |

<a id="deleteBackupPolicy"></a>
# **deleteBackupPolicy**
> deleteBackupPolicy(backupPolicyName, apiVersion, timeout)

Deletes the backup policy.

Deletes an existing backup policy. A backup policy must be created before it can be deleted. A currently active backup policy, associated with any Service Fabric application, service or partition, cannot be deleted without first deleting the mapping.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.deleteBackupPolicy(backupPolicyName, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#deleteBackupPolicy");
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
| **backupPolicyName** | **String**| The name of the backup policy. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation returns 200 status code and deletes the backup policy. |  -  |
| **0** | The detailed error response. |  -  |

<a id="disableApplicationBackup"></a>
# **disableApplicationBackup**
> disableApplicationBackup(applicationId, apiVersion, timeout)

Disables periodic backup of Service Fabric application.

Disables periodic backup of Service Fabric application which was previously enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.disableApplicationBackup(applicationId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#disableApplicationBackup");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the request to disable application backup has been accepted. |  -  |
| **0** | The detailed error response. |  -  |

<a id="disablePartitionBackup"></a>
# **disablePartitionBackup**
> disablePartitionBackup(partitionId, apiVersion, timeout)

Disables periodic backup of Service Fabric partition which was previously enabled.

Disables periodic backup of partition which was previously enabled. Backup must be explicitly enabled before it can be disabled.  In case the backup is enabled for the Service Fabric application or service, which this partition is part of, this partition would continue to be periodically backed up as per the policy mapped at the higher level entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.disablePartitionBackup(partitionId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#disablePartitionBackup");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the request to disable partition backup has been accepted. |  -  |
| **0** | The detailed error response. |  -  |

<a id="disableServiceBackup"></a>
# **disableServiceBackup**
> disableServiceBackup(serviceId, apiVersion, timeout)

Disables periodic backup of Service Fabric service which was previously enabled.

Disables periodic backup of Service Fabric service which was previously enabled. Backup must be explicitly enabled before it can be disabled. In case the backup is enabled for the Service Fabric application, which this service is part of, this service would continue to be periodically backed up as per the policy mapped at the application level.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.disableServiceBackup(serviceId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#disableServiceBackup");
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
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the request to disable service backup has been accepted. |  -  |
| **0** | The detailed error response. |  -  |

<a id="enableApplicationBackup"></a>
# **enableApplicationBackup**
> enableApplicationBackup(applicationId, apiVersion, enableBackupDescription, timeout)

Enables periodic backup of stateful partitions under this Service Fabric application.

Enables periodic backup of stateful partitions which are part of this Service Fabric application. Each partition is backed up individually as per the specified backup policy description.  Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    EnableBackupDescription enableBackupDescription = new EnableBackupDescription(); // EnableBackupDescription | Specifies the parameters for enabling backup.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.enableApplicationBackup(applicationId, apiVersion, enableBackupDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#enableApplicationBackup");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **enableBackupDescription** | [**EnableBackupDescription**](EnableBackupDescription.md)| Specifies the parameters for enabling backup. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the request to enable application backup has been accepted. |  -  |
| **0** | The detailed error response. |  -  |

<a id="enablePartitionBackup"></a>
# **enablePartitionBackup**
> enablePartitionBackup(partitionId, apiVersion, enableBackupDescription, timeout)

Enables periodic backup of the stateful persisted partition.

Enables periodic backup of stateful persisted partition. Each partition is backed up as per the specified backup policy description. In case the application or service, which is partition is part of, is already enabled for backup then this operation would override the policy being used to take the periodic backup of this partition. Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    EnableBackupDescription enableBackupDescription = new EnableBackupDescription(); // EnableBackupDescription | Specifies the parameters for enabling backup.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.enablePartitionBackup(partitionId, apiVersion, enableBackupDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#enablePartitionBackup");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **enableBackupDescription** | [**EnableBackupDescription**](EnableBackupDescription.md)| Specifies the parameters for enabling backup. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the request to enable partition backup has been accepted. |  -  |
| **0** | The detailed error response. |  -  |

<a id="enableServiceBackup"></a>
# **enableServiceBackup**
> enableServiceBackup(serviceId, apiVersion, enableBackupDescription, timeout)

Enables periodic backup of stateful partitions under this Service Fabric service.

Enables periodic backup of stateful partitions which are part of this Service Fabric service. Each partition is backed up individually as per the specified backup policy description. In case the application, which the service is part of, is already enabled for backup then this operation would override the policy being used to take the periodic backup for this service and its partitions (unless explicitly overridden at the partition level). Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    EnableBackupDescription enableBackupDescription = new EnableBackupDescription(); // EnableBackupDescription | Specifies the parameters for enabling backup.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.enableServiceBackup(serviceId, apiVersion, enableBackupDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#enableServiceBackup");
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
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **enableBackupDescription** | [**EnableBackupDescription**](EnableBackupDescription.md)| Specifies the parameters for enabling backup. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the request to enable service backup has been accepted. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getAllEntitiesBackedUpByPolicy"></a>
# **getAllEntitiesBackedUpByPolicy**
> PagedBackupEntityList getAllEntitiesBackedUpByPolicy(backupPolicyName, apiVersion, continuationToken, maxResults, timeout)

Gets the list of backup entities that are associated with this policy.

Returns a list of Service Fabric application, service or partition which are associated with this backup policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedBackupEntityList result = apiInstance.getAllEntitiesBackedUpByPolicy(backupPolicyName, apiVersion, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getAllEntitiesBackedUpByPolicy");
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
| **backupPolicyName** | **String**| The name of the backup policy. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedBackupEntityList**](PagedBackupEntityList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of Service Fabric entities that are associated with this policy. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getApplicationBackupConfigurationInfo"></a>
# **getApplicationBackupConfigurationInfo**
> PagedBackupConfigurationInfoList getApplicationBackupConfigurationInfo(applicationId, apiVersion, continuationToken, maxResults, timeout)

Gets the Service Fabric application backup configuration information.

Gets the Service Fabric backup configuration information for the application and the services and partitions under this application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedBackupConfigurationInfoList result = apiInstance.getApplicationBackupConfigurationInfo(applicationId, apiVersion, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getApplicationBackupConfigurationInfo");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedBackupConfigurationInfoList**](PagedBackupConfigurationInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of backup configuration information for the application, and the services and partitions under this application, for which backup configuration has been overridden. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getApplicationBackupList"></a>
# **getApplicationBackupList**
> PagedBackupInfoList getApplicationBackupList(applicationId, apiVersion, timeout, latest, startDateTimeFilter, endDateTimeFilter, continuationToken, maxResults)

Gets the list of backups available for every partition in this application.

Returns a list of backups available for every partition in this Service Fabric application. The server enumerates all the backups available at the backup location configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for every partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    Boolean latest = false; // Boolean | Specifies whether to get only the most recent backup available for a partition for the specified time range.
    OffsetDateTime startDateTimeFilter = OffsetDateTime.now(); // OffsetDateTime | Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
    OffsetDateTime endDateTimeFilter = OffsetDateTime.now(); // OffsetDateTime | Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    try {
      PagedBackupInfoList result = apiInstance.getApplicationBackupList(applicationId, apiVersion, timeout, latest, startDateTimeFilter, endDateTimeFilter, continuationToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getApplicationBackupList");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **latest** | **Boolean**| Specifies whether to get only the most recent backup available for a partition for the specified time range. | [optional] [default to false] |
| **startDateTimeFilter** | **OffsetDateTime**| Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated. | [optional] |
| **endDateTimeFilter** | **OffsetDateTime**| Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup. | [optional] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of backup information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getBackupPolicyByName"></a>
# **getBackupPolicyByName**
> BackupPolicyDescription getBackupPolicyByName(backupPolicyName, apiVersion, timeout)

Gets a particular backup policy by name.

Gets a particular backup policy identified by {backupPolicyName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      BackupPolicyDescription result = apiInstance.getBackupPolicyByName(backupPolicyName, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getBackupPolicyByName");
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
| **backupPolicyName** | **String**| The name of the backup policy. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**BackupPolicyDescription**](BackupPolicyDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and the backup policy description. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getBackupPolicyList"></a>
# **getBackupPolicyList**
> PagedBackupPolicyDescriptionList getBackupPolicyList(apiVersion, continuationToken, maxResults, timeout)

Gets all the backup policies configured.

Get a list of all the backup policies configured.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedBackupPolicyDescriptionList result = apiInstance.getBackupPolicyList(apiVersion, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getBackupPolicyList");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedBackupPolicyDescriptionList**](PagedBackupPolicyDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and paged list of backup policies. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getBackupsFromBackupLocation"></a>
# **getBackupsFromBackupLocation**
> PagedBackupInfoList getBackupsFromBackupLocation(apiVersion, getBackupByStorageQueryDescription, timeout, continuationToken, maxResults)

Gets the list of backups available for the specified backed up entity at the specified backup location.

Gets the list of backups available for the specified backed up entity (Application, Service or Partition) at the specified backup location (FileShare or Azure Blob Storage).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    GetBackupByStorageQueryDescription getBackupByStorageQueryDescription = new GetBackupByStorageQueryDescription(); // GetBackupByStorageQueryDescription | Describes the filters and backup storage details to be used for enumerating backups.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    try {
      PagedBackupInfoList result = apiInstance.getBackupsFromBackupLocation(apiVersion, getBackupByStorageQueryDescription, timeout, continuationToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getBackupsFromBackupLocation");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **getBackupByStorageQueryDescription** | [**GetBackupByStorageQueryDescription**](GetBackupByStorageQueryDescription.md)| Describes the filters and backup storage details to be used for enumerating backups. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of backup information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionBackupConfigurationInfo"></a>
# **getPartitionBackupConfigurationInfo**
> PartitionBackupConfigurationInfo getPartitionBackupConfigurationInfo(partitionId, apiVersion, timeout)

Gets the partition backup configuration information

Gets the Service Fabric Backup configuration information for the specified partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PartitionBackupConfigurationInfo result = apiInstance.getPartitionBackupConfigurationInfo(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getPartitionBackupConfigurationInfo");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PartitionBackupConfigurationInfo**](PartitionBackupConfigurationInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and gets the partition&#39;s backup configuration information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionBackupList"></a>
# **getPartitionBackupList**
> PagedBackupInfoList getPartitionBackupList(partitionId, apiVersion, timeout, latest, startDateTimeFilter, endDateTimeFilter)

Gets the list of backups available for the specified partition.

Returns a list of backups available for the specified partition. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for the partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    Boolean latest = false; // Boolean | Specifies whether to get only the most recent backup available for a partition for the specified time range.
    OffsetDateTime startDateTimeFilter = OffsetDateTime.now(); // OffsetDateTime | Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
    OffsetDateTime endDateTimeFilter = OffsetDateTime.now(); // OffsetDateTime | Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
    try {
      PagedBackupInfoList result = apiInstance.getPartitionBackupList(partitionId, apiVersion, timeout, latest, startDateTimeFilter, endDateTimeFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getPartitionBackupList");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **latest** | **Boolean**| Specifies whether to get only the most recent backup available for a partition for the specified time range. | [optional] [default to false] |
| **startDateTimeFilter** | **OffsetDateTime**| Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated. | [optional] |
| **endDateTimeFilter** | **OffsetDateTime**| Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup. | [optional] |

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of backup information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionBackupProgress"></a>
# **getPartitionBackupProgress**
> BackupProgressInfo getPartitionBackupProgress(partitionId, apiVersion, timeout)

Gets details for the latest backup triggered for this partition.

Returns information about the state of the latest backup along with details or failure reason in case of completion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      BackupProgressInfo result = apiInstance.getPartitionBackupProgress(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getPartitionBackupProgress");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**BackupProgressInfo**](BackupProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation returns 200 status code and backup progress details. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getPartitionRestoreProgress"></a>
# **getPartitionRestoreProgress**
> RestoreProgressInfo getPartitionRestoreProgress(partitionId, apiVersion, timeout)

Gets details for the latest restore operation triggered for this partition.

Returns information about the state of the latest restore operation along with details or failure reason in case of completion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      RestoreProgressInfo result = apiInstance.getPartitionRestoreProgress(partitionId, apiVersion, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getPartitionRestoreProgress");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**RestoreProgressInfo**](RestoreProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation returns 200 status code and restore progress details. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getServiceBackupConfigurationInfo"></a>
# **getServiceBackupConfigurationInfo**
> PagedBackupConfigurationInfoList getServiceBackupConfigurationInfo(serviceId, apiVersion, continuationToken, maxResults, timeout)

Gets the Service Fabric service backup configuration information.

Gets the Service Fabric backup configuration information for the service and the partitions under this service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      PagedBackupConfigurationInfoList result = apiInstance.getServiceBackupConfigurationInfo(serviceId, apiVersion, continuationToken, maxResults, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getServiceBackupConfigurationInfo");
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
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

[**PagedBackupConfigurationInfoList**](PagedBackupConfigurationInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of backup configuration information for the service, and the partitions under this service, for which backup configuration has been overridden. |  -  |
| **0** | The detailed error response. |  -  |

<a id="getServiceBackupList"></a>
# **getServiceBackupList**
> PagedBackupInfoList getServiceBackupList(serviceId, apiVersion, timeout, latest, startDateTimeFilter, endDateTimeFilter, continuationToken, maxResults)

Gets the list of backups available for every partition in this service.

Returns a list of backups available for every partition in this Service Fabric service. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for every partition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    Boolean latest = false; // Boolean | Specifies whether to get only the most recent backup available for a partition for the specified time range.
    OffsetDateTime startDateTimeFilter = OffsetDateTime.now(); // OffsetDateTime | Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
    OffsetDateTime endDateTimeFilter = OffsetDateTime.now(); // OffsetDateTime | Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
    String continuationToken = "continuationToken_example"; // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
    Long maxResults = 0L; // Long | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
    try {
      PagedBackupInfoList result = apiInstance.getServiceBackupList(serviceId, apiVersion, timeout, latest, startDateTimeFilter, endDateTimeFilter, continuationToken, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#getServiceBackupList");
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
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |
| **latest** | **Boolean**| Specifies whether to get only the most recent backup available for a partition for the specified time range. | [optional] [default to false] |
| **startDateTimeFilter** | **OffsetDateTime**| Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated. | [optional] |
| **endDateTimeFilter** | **OffsetDateTime**| Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup. | [optional] |
| **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] |
| **maxResults** | **Long**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0] |

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation will return 200 status code and a paged list of backup information. |  -  |
| **0** | The detailed error response. |  -  |

<a id="restorePartition"></a>
# **restorePartition**
> restorePartition(partitionId, apiVersion, restorePartitionDescription, restoreTimeout, timeout)

Triggers restore of the state of the partition using the specified restore partition description.

Restores the state of a of the stateful persisted partition using the specified backup point. In case the partition is already being periodically backed up, then by default the backup point is looked for in the storage specified in backup policy. One can also override the same by specifying the backup storage details as part of the restore partition description in body. Once the restore is initiated, its progress can be tracked using the GetRestoreProgress operation.  In case, the operation times out, specify a greater restore timeout value in the query parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    RestorePartitionDescription restorePartitionDescription = new RestorePartitionDescription(); // RestorePartitionDescription | Describes the parameters to restore the partition.
    Integer restoreTimeout = 10; // Integer | Specifies the maximum amount of time to wait, in minutes, for the restore operation to complete. Post that, the operation returns back with timeout error. However, in certain corner cases it could be that the restore operation goes through even though it completes with timeout. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. the default value for the same is 10 minutes.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.restorePartition(partitionId, apiVersion, restorePartitionDescription, restoreTimeout, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#restorePartition");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **restorePartitionDescription** | [**RestorePartitionDescription**](RestorePartitionDescription.md)| Describes the parameters to restore the partition. | |
| **restoreTimeout** | **Integer**| Specifies the maximum amount of time to wait, in minutes, for the restore operation to complete. Post that, the operation returns back with timeout error. However, in certain corner cases it could be that the restore operation goes through even though it completes with timeout. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. the default value for the same is 10 minutes. | [optional] [default to 10] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and restore will be initiated. Use GetPartitionRestoreProgress operation to get the status of the restore operation. |  -  |
| **0** | The detailed error response. |  -  |

<a id="resumeApplicationBackup"></a>
# **resumeApplicationBackup**
> resumeApplicationBackup(applicationId, apiVersion, timeout)

Resumes periodic backup of a Service Fabric application which was previously suspended.

The previously suspended Service Fabric application resumes taking periodic backup as per the backup policy currently configured for the same.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.resumeApplicationBackup(applicationId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#resumeApplicationBackup");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and application backup will be resumed. |  -  |
| **0** | The detailed error response. |  -  |

<a id="resumePartitionBackup"></a>
# **resumePartitionBackup**
> resumePartitionBackup(partitionId, apiVersion, timeout)

Resumes periodic backup of partition which was previously suspended.

The previously suspended partition resumes taking periodic backup as per the backup policy currently configured for the same.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.resumePartitionBackup(partitionId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#resumePartitionBackup");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and partition backup will be resumed. |  -  |
| **0** | The detailed error response. |  -  |

<a id="resumeServiceBackup"></a>
# **resumeServiceBackup**
> resumeServiceBackup(serviceId, apiVersion, timeout)

Resumes periodic backup of a Service Fabric service which was previously suspended.

The previously suspended Service Fabric service resumes taking periodic backup as per the backup policy currently configured for the same.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.resumeServiceBackup(serviceId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#resumeServiceBackup");
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
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and service backup will be resumed. |  -  |
| **0** | The detailed error response. |  -  |

<a id="suspendApplicationBackup"></a>
# **suspendApplicationBackup**
> suspendApplicationBackup(applicationId, apiVersion, timeout)

Suspends periodic backup for the specified Service Fabric application.

The application which is configured to take periodic backups, is suspended for taking further backups till it is resumed again. This operation applies to the entire application&#39;s hierarchy. It means all the services and partitions under this application are now suspended for backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.suspendApplicationBackup(applicationId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#suspendApplicationBackup");
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
| **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and application backup will be suspended. |  -  |
| **0** | The detailed error response. |  -  |

<a id="suspendPartitionBackup"></a>
# **suspendPartitionBackup**
> suspendPartitionBackup(partitionId, apiVersion, timeout)

Suspends periodic backup for the specified partition.

The partition which is configured to take periodic backups, is suspended for taking further backups till it is resumed again.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    UUID partitionId = UUID.randomUUID(); // UUID | The identity of the partition.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.suspendPartitionBackup(partitionId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#suspendPartitionBackup");
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
| **partitionId** | **UUID**| The identity of the partition. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and partition backup will be suspended. |  -  |
| **0** | The detailed error response. |  -  |

<a id="suspendServiceBackup"></a>
# **suspendServiceBackup**
> suspendServiceBackup(serviceId, apiVersion, timeout)

Suspends periodic backup for the specified Service Fabric service.

The service which is configured to take periodic backups, is suspended for taking further backups till it is resumed again. This operation applies to the entire service&#39;s hierarchy. It means all the partitions under this service are now suspended for backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.suspendServiceBackup(serviceId, apiVersion, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#suspendServiceBackup");
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
| **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | A 202 status code indicates the operation request was accepted and service backup will be suspended. |  -  |
| **0** | The detailed error response. |  -  |

<a id="updateBackupPolicy"></a>
# **updateBackupPolicy**
> updateBackupPolicy(backupPolicyName, apiVersion, backupPolicyDescription, timeout)

Updates the backup policy.

Updates the backup policy identified by {backupPolicyName}

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupRestoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    BackupRestoreApi apiInstance = new BackupRestoreApi(defaultClient);
    String backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
    String apiVersion = "6.2-preview"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
    BackupPolicyDescription backupPolicyDescription = new BackupPolicyDescription(); // BackupPolicyDescription | Describes the backup policy.
    Long timeout = 60L; // Long | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
    try {
      apiInstance.updateBackupPolicy(backupPolicyName, apiVersion, backupPolicyDescription, timeout);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupRestoreApi#updateBackupPolicy");
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
| **backupPolicyName** | **String**| The name of the backup policy. | |
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to 6.2-preview] [enum: 6.2-preview] |
| **backupPolicyDescription** | [**BackupPolicyDescription**](BackupPolicyDescription.md)| Describes the backup policy. | |
| **timeout** | **Long**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful operation returns 200 status code and updates the backup policy description. |  -  |
| **0** | The detailed error response. |  -  |

