# StorSimple8000SeriesManagementClient.BackupSchedulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupSchedulesCreateOrUpdate**](BackupSchedulesApi.md#backupSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules/{backupScheduleName} | 
[**backupSchedulesDelete**](BackupSchedulesApi.md#backupSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules/{backupScheduleName} | 
[**backupSchedulesGet**](BackupSchedulesApi.md#backupSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules/{backupScheduleName} | 
[**backupSchedulesListByBackupPolicy**](BackupSchedulesApi.md#backupSchedulesListByBackupPolicy) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules | 



## backupSchedulesCreateOrUpdate

> BackupSchedule backupSchedulesCreateOrUpdate(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters)



Creates or updates the backup schedule.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BackupSchedulesApi();
let deviceName = "deviceName_example"; // String | The device name
let backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
let backupScheduleName = "backupScheduleName_example"; // String | The backup schedule name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let parameters = new StorSimple8000SeriesManagementClient.BackupSchedule(); // BackupSchedule | The backup schedule.
apiInstance.backupSchedulesCreateOrUpdate(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters, (error, data, response) => {
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
 **deviceName** | **String**| The device name | 
 **backupPolicyName** | **String**| The backup policy name. | 
 **backupScheduleName** | **String**| The backup schedule name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **parameters** | [**BackupSchedule**](BackupSchedule.md)| The backup schedule. | 

### Return type

[**BackupSchedule**](BackupSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupSchedulesDelete

> backupSchedulesDelete(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the backup schedule.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BackupSchedulesApi();
let deviceName = "deviceName_example"; // String | The device name
let backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
let backupScheduleName = "backupScheduleName_example"; // String | The name the backup schedule.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupSchedulesDelete(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name | 
 **backupPolicyName** | **String**| The backup policy name. | 
 **backupScheduleName** | **String**| The name the backup schedule. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## backupSchedulesGet

> BackupSchedule backupSchedulesGet(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion)



Gets the properties of the specified backup schedule name.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BackupSchedulesApi();
let deviceName = "deviceName_example"; // String | The device name
let backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
let backupScheduleName = "backupScheduleName_example"; // String | The name of the backup schedule to be fetched
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupSchedulesGet(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name | 
 **backupPolicyName** | **String**| The backup policy name. | 
 **backupScheduleName** | **String**| The name of the backup schedule to be fetched | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**BackupSchedule**](BackupSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupSchedulesListByBackupPolicy

> BackupScheduleList backupSchedulesListByBackupPolicy(deviceName, backupPolicyName, subscriptionId, resourceGroupName, managerName, apiVersion)



Gets all the backup schedules in a backup policy.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.BackupSchedulesApi();
let deviceName = "deviceName_example"; // String | The device name
let backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupSchedulesListByBackupPolicy(deviceName, backupPolicyName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The device name | 
 **backupPolicyName** | **String**| The backup policy name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**BackupScheduleList**](BackupScheduleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

