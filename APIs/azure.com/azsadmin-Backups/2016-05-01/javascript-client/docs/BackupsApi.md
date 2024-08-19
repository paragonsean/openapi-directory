# BackupManagementClient.BackupsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupsGet**](BackupsApi.md#backupsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Backup.Admin/backupLocations/{location}/backups/{backup} | 
[**backupsList**](BackupsApi.md#backupsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Backup.Admin/backupLocations/{location}/backups | 
[**backupsRestore**](BackupsApi.md#backupsRestore) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Backup.Admin/backupLocations/{location}/backups/{backup}/restore | 



## backupsGet

> Backup backupsGet(subscriptionId, resourceGroupName, location, backup, apiVersion)



Returns a backup from a location based on name.

### Example

```javascript
import BackupManagementClient from 'backup_management_client';
let defaultClient = BackupManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BackupManagementClient.BackupsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Name of the backup location.
let backup = "backup_example"; // String | Name of the backup.
let apiVersion = "'2016-05-01'"; // String | Client API version.
apiInstance.backupsGet(subscriptionId, resourceGroupName, location, backup, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Name of the backup location. | 
 **backup** | **String**| Name of the backup. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-01&#39;]

### Return type

[**Backup**](Backup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupsList

> BackupList backupsList(subscriptionId, resourceGroupName, location, apiVersion)



Returns a list of backups from a location.

### Example

```javascript
import BackupManagementClient from 'backup_management_client';
let defaultClient = BackupManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BackupManagementClient.BackupsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let location = "location_example"; // String | Name of the backup location.
let apiVersion = "'2016-05-01'"; // String | Client API version.
apiInstance.backupsList(subscriptionId, resourceGroupName, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **location** | **String**| Name of the backup location. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-01&#39;]

### Return type

[**BackupList**](BackupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupsRestore

> backupsRestore(subscriptionId, location, resourceGroupName, backup, apiVersion)



Restore a backup.

### Example

```javascript
import BackupManagementClient from 'backup_management_client';
let defaultClient = BackupManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BackupManagementClient.BackupsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | Name of the backup location.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group.
let backup = "backup_example"; // String | Name of the backup.
let apiVersion = "'2016-05-01'"; // String | Client API version.
apiInstance.backupsRestore(subscriptionId, location, resourceGroupName, backup, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **location** | **String**| Name of the backup location. | 
 **resourceGroupName** | **String**| Name of the resource group. | 
 **backup** | **String**| Name of the backup. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2016-05-01&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

