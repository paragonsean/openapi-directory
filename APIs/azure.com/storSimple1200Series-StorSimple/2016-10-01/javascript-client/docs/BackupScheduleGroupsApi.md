# StorSimpleManagementClient.BackupScheduleGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupScheduleGroupsCreateOrUpdate**](BackupScheduleGroupsApi.md#backupScheduleGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupScheduleGroups/{scheduleGroupName} | 
[**backupScheduleGroupsDelete**](BackupScheduleGroupsApi.md#backupScheduleGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupScheduleGroups/{scheduleGroupName} | 
[**backupScheduleGroupsGet**](BackupScheduleGroupsApi.md#backupScheduleGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupScheduleGroups/{scheduleGroupName} | 
[**backupScheduleGroupsListByDevice**](BackupScheduleGroupsApi.md#backupScheduleGroupsListByDevice) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupScheduleGroups | 



## backupScheduleGroupsCreateOrUpdate

> BackupScheduleGroup backupScheduleGroupsCreateOrUpdate(deviceName, scheduleGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, scheduleGroup)



Creates or Updates the backup schedule Group.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupScheduleGroupsApi();
let deviceName = "deviceName_example"; // String | The name of the device.
let scheduleGroupName = "scheduleGroupName_example"; // String | The name of the schedule group.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let scheduleGroup = new StorSimpleManagementClient.BackupScheduleGroup(); // BackupScheduleGroup | The schedule group to be created
apiInstance.backupScheduleGroupsCreateOrUpdate(deviceName, scheduleGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, scheduleGroup, (error, data, response) => {
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
 **deviceName** | **String**| The name of the device. | 
 **scheduleGroupName** | **String**| The name of the schedule group. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **scheduleGroup** | [**BackupScheduleGroup**](BackupScheduleGroup.md)| The schedule group to be created | 

### Return type

[**BackupScheduleGroup**](BackupScheduleGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## backupScheduleGroupsDelete

> backupScheduleGroupsDelete(deviceName, scheduleGroupName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the backup schedule group.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupScheduleGroupsApi();
let deviceName = "deviceName_example"; // String | The name of the device.
let scheduleGroupName = "scheduleGroupName_example"; // String | The name of the schedule group.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupScheduleGroupsDelete(deviceName, scheduleGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The name of the device. | 
 **scheduleGroupName** | **String**| The name of the schedule group. | 
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
- **Accept**: application/json


## backupScheduleGroupsGet

> BackupScheduleGroup backupScheduleGroupsGet(deviceName, scheduleGroupName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified backup schedule group name.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupScheduleGroupsApi();
let deviceName = "deviceName_example"; // String | The name of the device.
let scheduleGroupName = "scheduleGroupName_example"; // String | The name of the schedule group.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupScheduleGroupsGet(deviceName, scheduleGroupName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The name of the device. | 
 **scheduleGroupName** | **String**| The name of the schedule group. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**BackupScheduleGroup**](BackupScheduleGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## backupScheduleGroupsListByDevice

> BackupScheduleGroupList backupScheduleGroupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the backup schedule groups in a device.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.BackupScheduleGroupsApi();
let deviceName = "deviceName_example"; // String | The name of the device.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.backupScheduleGroupsListByDevice(deviceName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **deviceName** | **String**| The name of the device. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**BackupScheduleGroupList**](BackupScheduleGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

