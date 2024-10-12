# ServiceFabricClientApis.BackupRestoreApi

All URIs are relative to *http://azure.local:19080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupPartition**](BackupRestoreApi.md#backupPartition) | **POST** /Partitions/{partitionId}/$/Backup | Triggers backup of the partition&#39;s state.
[**createBackupPolicy**](BackupRestoreApi.md#createBackupPolicy) | **POST** /BackupRestore/BackupPolicies/$/Create | Creates a backup policy.
[**deleteBackupPolicy**](BackupRestoreApi.md#deleteBackupPolicy) | **POST** /BackupRestore/BackupPolicies/{backupPolicyName}/$/Delete | Deletes the backup policy.
[**disableApplicationBackup**](BackupRestoreApi.md#disableApplicationBackup) | **POST** /Applications/{applicationId}/$/DisableBackup | Disables periodic backup of Service Fabric application.
[**disablePartitionBackup**](BackupRestoreApi.md#disablePartitionBackup) | **POST** /Partitions/{partitionId}/$/DisableBackup | Disables periodic backup of Service Fabric partition which was previously enabled.
[**disableServiceBackup**](BackupRestoreApi.md#disableServiceBackup) | **POST** /Services/{serviceId}/$/DisableBackup | Disables periodic backup of Service Fabric service which was previously enabled.
[**enableApplicationBackup**](BackupRestoreApi.md#enableApplicationBackup) | **POST** /Applications/{applicationId}/$/EnableBackup | Enables periodic backup of stateful partitions under this Service Fabric application.
[**enablePartitionBackup**](BackupRestoreApi.md#enablePartitionBackup) | **POST** /Partitions/{partitionId}/$/EnableBackup | Enables periodic backup of the stateful persisted partition.
[**enableServiceBackup**](BackupRestoreApi.md#enableServiceBackup) | **POST** /Services/{serviceId}/$/EnableBackup | Enables periodic backup of stateful partitions under this Service Fabric service.
[**getAllEntitiesBackedUpByPolicy**](BackupRestoreApi.md#getAllEntitiesBackedUpByPolicy) | **GET** /BackupRestore/BackupPolicies/{backupPolicyName}/$/GetBackupEnabledEntities | Gets the list of backup entities that are associated with this policy.
[**getApplicationBackupConfigurationInfo**](BackupRestoreApi.md#getApplicationBackupConfigurationInfo) | **GET** /Applications/{applicationId}/$/GetBackupConfigurationInfo | Gets the Service Fabric application backup configuration information.
[**getApplicationBackupList**](BackupRestoreApi.md#getApplicationBackupList) | **GET** /Applications/{applicationId}/$/GetBackups | Gets the list of backups available for every partition in this application.
[**getBackupPolicyByName**](BackupRestoreApi.md#getBackupPolicyByName) | **GET** /BackupRestore/BackupPolicies/{backupPolicyName} | Gets a particular backup policy by name.
[**getBackupPolicyList**](BackupRestoreApi.md#getBackupPolicyList) | **GET** /BackupRestore/BackupPolicies | Gets all the backup policies configured.
[**getBackupsFromBackupLocation**](BackupRestoreApi.md#getBackupsFromBackupLocation) | **POST** /BackupRestore/$/GetBackups | Gets the list of backups available for the specified backed up entity at the specified backup location.
[**getPartitionBackupConfigurationInfo**](BackupRestoreApi.md#getPartitionBackupConfigurationInfo) | **GET** /Partitions/{partitionId}/$/GetBackupConfigurationInfo | Gets the partition backup configuration information
[**getPartitionBackupList**](BackupRestoreApi.md#getPartitionBackupList) | **GET** /Partitions/{partitionId}/$/GetBackups | Gets the list of backups available for the specified partition.
[**getPartitionBackupProgress**](BackupRestoreApi.md#getPartitionBackupProgress) | **GET** /Partitions/{partitionId}/$/GetBackupProgress | Gets details for the latest backup triggered for this partition.
[**getPartitionRestoreProgress**](BackupRestoreApi.md#getPartitionRestoreProgress) | **GET** /Partitions/{partitionId}/$/GetRestoreProgress | Gets details for the latest restore operation triggered for this partition.
[**getServiceBackupConfigurationInfo**](BackupRestoreApi.md#getServiceBackupConfigurationInfo) | **GET** /Services/{serviceId}/$/GetBackupConfigurationInfo | Gets the Service Fabric service backup configuration information.
[**getServiceBackupList**](BackupRestoreApi.md#getServiceBackupList) | **GET** /Services/{serviceId}/$/GetBackups | Gets the list of backups available for every partition in this service.
[**restorePartition**](BackupRestoreApi.md#restorePartition) | **POST** /Partitions/{partitionId}/$/Restore | Triggers restore of the state of the partition using the specified restore partition description.
[**resumeApplicationBackup**](BackupRestoreApi.md#resumeApplicationBackup) | **POST** /Applications/{applicationId}/$/ResumeBackup | Resumes periodic backup of a Service Fabric application which was previously suspended.
[**resumePartitionBackup**](BackupRestoreApi.md#resumePartitionBackup) | **POST** /Partitions/{partitionId}/$/ResumeBackup | Resumes periodic backup of partition which was previously suspended.
[**resumeServiceBackup**](BackupRestoreApi.md#resumeServiceBackup) | **POST** /Services/{serviceId}/$/ResumeBackup | Resumes periodic backup of a Service Fabric service which was previously suspended.
[**suspendApplicationBackup**](BackupRestoreApi.md#suspendApplicationBackup) | **POST** /Applications/{applicationId}/$/SuspendBackup | Suspends periodic backup for the specified Service Fabric application.
[**suspendPartitionBackup**](BackupRestoreApi.md#suspendPartitionBackup) | **POST** /Partitions/{partitionId}/$/SuspendBackup | Suspends periodic backup for the specified partition.
[**suspendServiceBackup**](BackupRestoreApi.md#suspendServiceBackup) | **POST** /Services/{serviceId}/$/SuspendBackup | Suspends periodic backup for the specified Service Fabric service.
[**updateBackupPolicy**](BackupRestoreApi.md#updateBackupPolicy) | **POST** /BackupRestore/BackupPolicies/{backupPolicyName}/$/Update | Updates the backup policy.



## backupPartition

> backupPartition(partitionId, apiVersion, opts)

Triggers backup of the partition&#39;s state.

Creates a backup of the stateful persisted partition&#39;s state. In case the partition is already being periodically backed up, then by default the new backup is created at the same backup storage. One can also override the same by specifying the backup storage details as part of the request body. Once the backup is initiated, its progress can be tracked using the GetBackupProgress operation.  In case, the operation times out, specify a greater backup timeout value in the query parameter.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'backupTimeout': 10, // Number | Specifies the maximum amount of time, in minutes, to wait for the backup operation to complete. Post that, the operation completes with timeout error. However, in certain corner cases it could be that though the operation returns back timeout, the backup actually goes through. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. The default value for the same is 10 minutes.
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'backupPartitionDescription': new ServiceFabricClientApis.BackupPartitionDescription() // BackupPartitionDescription | Describes the parameters to backup the partition now. If not present, backup operation uses default parameters from the backup policy current associated with this partition.
};
apiInstance.backupPartition(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **backupTimeout** | **Number**| Specifies the maximum amount of time, in minutes, to wait for the backup operation to complete. Post that, the operation completes with timeout error. However, in certain corner cases it could be that though the operation returns back timeout, the backup actually goes through. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. The default value for the same is 10 minutes. | [optional] [default to 10]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **backupPartitionDescription** | [**BackupPartitionDescription**](BackupPartitionDescription.md)| Describes the parameters to backup the partition now. If not present, backup operation uses default parameters from the backup policy current associated with this partition. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createBackupPolicy

> createBackupPolicy(apiVersion, backupPolicyDescription, opts)

Creates a backup policy.

Creates a backup policy which can be associated later with a Service Fabric application, service or a partition for periodic backup.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let backupPolicyDescription = new ServiceFabricClientApis.BackupPolicyDescription(); // BackupPolicyDescription | Describes the backup policy.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.createBackupPolicy(apiVersion, backupPolicyDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **backupPolicyDescription** | [**BackupPolicyDescription**](BackupPolicyDescription.md)| Describes the backup policy. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBackupPolicy

> deleteBackupPolicy(backupPolicyName, apiVersion, opts)

Deletes the backup policy.

Deletes an existing backup policy. A backup policy must be created before it can be deleted. A currently active backup policy, associated with any Service Fabric application, service or partition, cannot be deleted without first deleting the mapping.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.deleteBackupPolicy(backupPolicyName, apiVersion, opts, (error, data, response) => {
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
 **backupPolicyName** | **String**| The name of the backup policy. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableApplicationBackup

> disableApplicationBackup(applicationId, apiVersion, opts)

Disables periodic backup of Service Fabric application.

Disables periodic backup of Service Fabric application which was previously enabled.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.disableApplicationBackup(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disablePartitionBackup

> disablePartitionBackup(partitionId, apiVersion, opts)

Disables periodic backup of Service Fabric partition which was previously enabled.

Disables periodic backup of partition which was previously enabled. Backup must be explicitly enabled before it can be disabled.  In case the backup is enabled for the Service Fabric application or service, which this partition is part of, this partition would continue to be periodically backed up as per the policy mapped at the higher level entity.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.disablePartitionBackup(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disableServiceBackup

> disableServiceBackup(serviceId, apiVersion, opts)

Disables periodic backup of Service Fabric service which was previously enabled.

Disables periodic backup of Service Fabric service which was previously enabled. Backup must be explicitly enabled before it can be disabled. In case the backup is enabled for the Service Fabric application, which this service is part of, this service would continue to be periodically backed up as per the policy mapped at the application level.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.disableServiceBackup(serviceId, apiVersion, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableApplicationBackup

> enableApplicationBackup(applicationId, apiVersion, enableBackupDescription, opts)

Enables periodic backup of stateful partitions under this Service Fabric application.

Enables periodic backup of stateful partitions which are part of this Service Fabric application. Each partition is backed up individually as per the specified backup policy description.  Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let enableBackupDescription = new ServiceFabricClientApis.EnableBackupDescription(); // EnableBackupDescription | Specifies the parameters for enabling backup.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.enableApplicationBackup(applicationId, apiVersion, enableBackupDescription, opts, (error, data, response) => {
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
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **enableBackupDescription** | [**EnableBackupDescription**](EnableBackupDescription.md)| Specifies the parameters for enabling backup. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enablePartitionBackup

> enablePartitionBackup(partitionId, apiVersion, enableBackupDescription, opts)

Enables periodic backup of the stateful persisted partition.

Enables periodic backup of stateful persisted partition. Each partition is backed up as per the specified backup policy description. In case the application or service, which is partition is part of, is already enabled for backup then this operation would override the policy being used to take the periodic backup of this partition. Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let enableBackupDescription = new ServiceFabricClientApis.EnableBackupDescription(); // EnableBackupDescription | Specifies the parameters for enabling backup.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.enablePartitionBackup(partitionId, apiVersion, enableBackupDescription, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **enableBackupDescription** | [**EnableBackupDescription**](EnableBackupDescription.md)| Specifies the parameters for enabling backup. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableServiceBackup

> enableServiceBackup(serviceId, apiVersion, enableBackupDescription, opts)

Enables periodic backup of stateful partitions under this Service Fabric service.

Enables periodic backup of stateful partitions which are part of this Service Fabric service. Each partition is backed up individually as per the specified backup policy description. In case the application, which the service is part of, is already enabled for backup then this operation would override the policy being used to take the periodic backup for this service and its partitions (unless explicitly overridden at the partition level). Note only C# based Reliable Actor and Reliable Stateful services are currently supported for periodic backup.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let enableBackupDescription = new ServiceFabricClientApis.EnableBackupDescription(); // EnableBackupDescription | Specifies the parameters for enabling backup.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.enableServiceBackup(serviceId, apiVersion, enableBackupDescription, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **enableBackupDescription** | [**EnableBackupDescription**](EnableBackupDescription.md)| Specifies the parameters for enabling backup. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllEntitiesBackedUpByPolicy

> PagedBackupEntityList getAllEntitiesBackedUpByPolicy(backupPolicyName, apiVersion, opts)

Gets the list of backup entities that are associated with this policy.

Returns a list of Service Fabric application, service or partition which are associated with this backup policy.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getAllEntitiesBackedUpByPolicy(backupPolicyName, apiVersion, opts, (error, data, response) => {
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
 **backupPolicyName** | **String**| The name of the backup policy. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedBackupEntityList**](PagedBackupEntityList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationBackupConfigurationInfo

> PagedBackupConfigurationInfoList getApplicationBackupConfigurationInfo(applicationId, apiVersion, opts)

Gets the Service Fabric application backup configuration information.

Gets the Service Fabric backup configuration information for the application and the services and partitions under this application.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getApplicationBackupConfigurationInfo(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedBackupConfigurationInfoList**](PagedBackupConfigurationInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationBackupList

> PagedBackupInfoList getApplicationBackupList(applicationId, apiVersion, opts)

Gets the list of backups available for every partition in this application.

Returns a list of backups available for every partition in this Service Fabric application. The server enumerates all the backups available at the backup location configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for every partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'latest': false, // Boolean | Specifies whether to get only the most recent backup available for a partition for the specified time range.
  'startDateTimeFilter': new Date("2013-10-20T19:20:30+01:00"), // Date | Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
  'endDateTimeFilter': new Date("2013-10-20T19:20:30+01:00"), // Date | Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0 // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
};
apiInstance.getApplicationBackupList(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **latest** | **Boolean**| Specifies whether to get only the most recent backup available for a partition for the specified time range. | [optional] [default to false]
 **startDateTimeFilter** | **Date**| Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated. | [optional] 
 **endDateTimeFilter** | **Date**| Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup. | [optional] 
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupPolicyByName

> BackupPolicyDescription getBackupPolicyByName(backupPolicyName, apiVersion, opts)

Gets a particular backup policy by name.

Gets a particular backup policy identified by {backupPolicyName}

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getBackupPolicyByName(backupPolicyName, apiVersion, opts, (error, data, response) => {
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
 **backupPolicyName** | **String**| The name of the backup policy. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**BackupPolicyDescription**](BackupPolicyDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupPolicyList

> PagedBackupPolicyDescriptionList getBackupPolicyList(apiVersion, opts)

Gets all the backup policies configured.

Get a list of all the backup policies configured.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getBackupPolicyList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedBackupPolicyDescriptionList**](PagedBackupPolicyDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBackupsFromBackupLocation

> PagedBackupInfoList getBackupsFromBackupLocation(apiVersion, getBackupByStorageQueryDescription, opts)

Gets the list of backups available for the specified backed up entity at the specified backup location.

Gets the list of backups available for the specified backed up entity (Application, Service or Partition) at the specified backup location (FileShare or Azure Blob Storage).

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let getBackupByStorageQueryDescription = new ServiceFabricClientApis.GetBackupByStorageQueryDescription(); // GetBackupByStorageQueryDescription | Describes the filters and backup storage details to be used for enumerating backups.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0 // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
};
apiInstance.getBackupsFromBackupLocation(apiVersion, getBackupByStorageQueryDescription, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **getBackupByStorageQueryDescription** | [**GetBackupByStorageQueryDescription**](GetBackupByStorageQueryDescription.md)| Describes the filters and backup storage details to be used for enumerating backups. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionBackupConfigurationInfo

> PartitionBackupConfigurationInfo getPartitionBackupConfigurationInfo(partitionId, apiVersion, opts)

Gets the partition backup configuration information

Gets the Service Fabric Backup configuration information for the specified partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionBackupConfigurationInfo(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PartitionBackupConfigurationInfo**](PartitionBackupConfigurationInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionBackupList

> PagedBackupInfoList getPartitionBackupList(partitionId, apiVersion, opts)

Gets the list of backups available for the specified partition.

Returns a list of backups available for the specified partition. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for the partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'latest': false, // Boolean | Specifies whether to get only the most recent backup available for a partition for the specified time range.
  'startDateTimeFilter': new Date("2013-10-20T19:20:30+01:00"), // Date | Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
  'endDateTimeFilter': new Date("2013-10-20T19:20:30+01:00") // Date | Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
};
apiInstance.getPartitionBackupList(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **latest** | **Boolean**| Specifies whether to get only the most recent backup available for a partition for the specified time range. | [optional] [default to false]
 **startDateTimeFilter** | **Date**| Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated. | [optional] 
 **endDateTimeFilter** | **Date**| Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup. | [optional] 

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionBackupProgress

> BackupProgressInfo getPartitionBackupProgress(partitionId, apiVersion, opts)

Gets details for the latest backup triggered for this partition.

Returns information about the state of the latest backup along with details or failure reason in case of completion.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionBackupProgress(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**BackupProgressInfo**](BackupProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPartitionRestoreProgress

> RestoreProgressInfo getPartitionRestoreProgress(partitionId, apiVersion, opts)

Gets details for the latest restore operation triggered for this partition.

Returns information about the state of the latest restore operation along with details or failure reason in case of completion.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getPartitionRestoreProgress(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**RestoreProgressInfo**](RestoreProgressInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceBackupConfigurationInfo

> PagedBackupConfigurationInfoList getServiceBackupConfigurationInfo(serviceId, apiVersion, opts)

Gets the Service Fabric service backup configuration information.

Gets the Service Fabric backup configuration information for the service and the partitions under this service.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0, // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.getServiceBackupConfigurationInfo(serviceId, apiVersion, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

[**PagedBackupConfigurationInfoList**](PagedBackupConfigurationInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getServiceBackupList

> PagedBackupInfoList getServiceBackupList(serviceId, apiVersion, opts)

Gets the list of backups available for every partition in this service.

Returns a list of backups available for every partition in this Service Fabric service. The server enumerates all the backups available in the backup store configured in the backup policy. It also allows filtering of the result based on start and end datetime or just fetching the latest available backup for every partition.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60, // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
  'latest': false, // Boolean | Specifies whether to get only the most recent backup available for a partition for the specified time range.
  'startDateTimeFilter': new Date("2013-10-20T19:20:30+01:00"), // Date | Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated.
  'endDateTimeFilter': new Date("2013-10-20T19:20:30+01:00"), // Date | Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup.
  'continuationToken': "continuationToken_example", // String | The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded.
  'maxResults': 0 // Number | The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message.
};
apiInstance.getServiceBackupList(serviceId, apiVersion, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]
 **latest** | **Boolean**| Specifies whether to get only the most recent backup available for a partition for the specified time range. | [optional] [default to false]
 **startDateTimeFilter** | **Date**| Specify the start date time from which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, all backups from the beginning are enumerated. | [optional] 
 **endDateTimeFilter** | **Date**| Specify the end date time till which to enumerate backups, in datetime format. The date time must be specified in ISO8601 format. This is an optional parameter. If not specified, enumeration is done till the most recent backup. | [optional] 
 **continuationToken** | **String**| The continuation token parameter is used to obtain next set of results. A continuation token with a non-empty value is included in the response of the API when the results from the system do not fit in a single response. When this value is passed to the next API call, the API returns next set of results. If there are no further results, then the continuation token does not contain a value. The value of this parameter should not be URL encoded. | [optional] 
 **maxResults** | **Number**| The maximum number of results to be returned as part of the paged queries. This parameter defines the upper bound on the number of results returned. The results returned can be less than the specified maximum results if they do not fit in the message as per the max message size restrictions defined in the configuration. If this parameter is zero or not specified, the paged query includes as many results as possible that fit in the return message. | [optional] [default to 0]

### Return type

[**PagedBackupInfoList**](PagedBackupInfoList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restorePartition

> restorePartition(partitionId, apiVersion, restorePartitionDescription, opts)

Triggers restore of the state of the partition using the specified restore partition description.

Restores the state of a of the stateful persisted partition using the specified backup point. In case the partition is already being periodically backed up, then by default the backup point is looked for in the storage specified in backup policy. One can also override the same by specifying the backup storage details as part of the restore partition description in body. Once the restore is initiated, its progress can be tracked using the GetRestoreProgress operation.  In case, the operation times out, specify a greater restore timeout value in the query parameter.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let restorePartitionDescription = new ServiceFabricClientApis.RestorePartitionDescription(); // RestorePartitionDescription | Describes the parameters to restore the partition.
let opts = {
  'restoreTimeout': 10, // Number | Specifies the maximum amount of time to wait, in minutes, for the restore operation to complete. Post that, the operation returns back with timeout error. However, in certain corner cases it could be that the restore operation goes through even though it completes with timeout. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. the default value for the same is 10 minutes.
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.restorePartition(partitionId, apiVersion, restorePartitionDescription, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **restorePartitionDescription** | [**RestorePartitionDescription**](RestorePartitionDescription.md)| Describes the parameters to restore the partition. | 
 **restoreTimeout** | **Number**| Specifies the maximum amount of time to wait, in minutes, for the restore operation to complete. Post that, the operation returns back with timeout error. However, in certain corner cases it could be that the restore operation goes through even though it completes with timeout. In case of timeout error, its recommended to invoke this operation again with a greater timeout value. the default value for the same is 10 minutes. | [optional] [default to 10]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resumeApplicationBackup

> resumeApplicationBackup(applicationId, apiVersion, opts)

Resumes periodic backup of a Service Fabric application which was previously suspended.

The previously suspended Service Fabric application resumes taking periodic backup as per the backup policy currently configured for the same.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.resumeApplicationBackup(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resumePartitionBackup

> resumePartitionBackup(partitionId, apiVersion, opts)

Resumes periodic backup of partition which was previously suspended.

The previously suspended partition resumes taking periodic backup as per the backup policy currently configured for the same.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.resumePartitionBackup(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resumeServiceBackup

> resumeServiceBackup(serviceId, apiVersion, opts)

Resumes periodic backup of a Service Fabric service which was previously suspended.

The previously suspended Service Fabric service resumes taking periodic backup as per the backup policy currently configured for the same.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.resumeServiceBackup(serviceId, apiVersion, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suspendApplicationBackup

> suspendApplicationBackup(applicationId, apiVersion, opts)

Suspends periodic backup for the specified Service Fabric application.

The application which is configured to take periodic backups, is suspended for taking further backups till it is resumed again. This operation applies to the entire application&#39;s hierarchy. It means all the services and partitions under this application are now suspended for backup.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let applicationId = "applicationId_example"; // String | The identity of the application. This is typically the full name of the application without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the application name is \"fabric:/myapp/app1\", the application identity would be \"myapp~app1\" in 6.0+ and \"myapp/app1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.suspendApplicationBackup(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The identity of the application. This is typically the full name of the application without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the application name is \&quot;fabric:/myapp/app1\&quot;, the application identity would be \&quot;myapp~app1\&quot; in 6.0+ and \&quot;myapp/app1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suspendPartitionBackup

> suspendPartitionBackup(partitionId, apiVersion, opts)

Suspends periodic backup for the specified partition.

The partition which is configured to take periodic backups, is suspended for taking further backups till it is resumed again.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let partitionId = "partitionId_example"; // String | The identity of the partition.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.suspendPartitionBackup(partitionId, apiVersion, opts, (error, data, response) => {
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
 **partitionId** | **String**| The identity of the partition. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## suspendServiceBackup

> suspendServiceBackup(serviceId, apiVersion, opts)

Suspends periodic backup for the specified Service Fabric service.

The service which is configured to take periodic backups, is suspended for taking further backups till it is resumed again. This operation applies to the entire service&#39;s hierarchy. It means all the partitions under this service are now suspended for backup.

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let serviceId = "serviceId_example"; // String | The identity of the service. This ID is typically the full name of the service without the 'fabric:' URI scheme. Starting from version 6.0, hierarchical names are delimited with the \"~\" character. For example, if the service name is \"fabric:/myapp/app1/svc1\", the service identity would be \"myapp~app1~svc1\" in 6.0+ and \"myapp/app1/svc1\" in previous versions.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.suspendServiceBackup(serviceId, apiVersion, opts, (error, data, response) => {
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
 **serviceId** | **String**| The identity of the service. This ID is typically the full name of the service without the &#39;fabric:&#39; URI scheme. Starting from version 6.0, hierarchical names are delimited with the \&quot;~\&quot; character. For example, if the service name is \&quot;fabric:/myapp/app1/svc1\&quot;, the service identity would be \&quot;myapp~app1~svc1\&quot; in 6.0+ and \&quot;myapp/app1/svc1\&quot; in previous versions. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBackupPolicy

> updateBackupPolicy(backupPolicyName, apiVersion, backupPolicyDescription, opts)

Updates the backup policy.

Updates the backup policy identified by {backupPolicyName}

### Example

```javascript
import ServiceFabricClientApis from 'service_fabric_client_apis';

let apiInstance = new ServiceFabricClientApis.BackupRestoreApi();
let backupPolicyName = "backupPolicyName_example"; // String | The name of the backup policy.
let apiVersion = "'6.2-preview'"; // String | The version of the API. This parameter is required and its value must be '6.2-preview'.
let backupPolicyDescription = new ServiceFabricClientApis.BackupPolicyDescription(); // BackupPolicyDescription | Describes the backup policy.
let opts = {
  'timeout': 60 // Number | The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds.
};
apiInstance.updateBackupPolicy(backupPolicyName, apiVersion, backupPolicyDescription, opts, (error, data, response) => {
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
 **backupPolicyName** | **String**| The name of the backup policy. | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.2-preview&#39;. | [default to &#39;6.2-preview&#39;]
 **backupPolicyDescription** | [**BackupPolicyDescription**](BackupPolicyDescription.md)| Describes the backup policy. | 
 **timeout** | **Number**| The server timeout for performing the operation in seconds. This timeout specifies the time duration that the client is willing to wait for the requested operation to complete. The default value for this parameter is 60 seconds. | [optional] [default to 60]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

