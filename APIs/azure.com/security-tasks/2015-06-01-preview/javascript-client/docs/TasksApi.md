# SecurityCenter.TasksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasksGetResourceGroupLevelTask**](TasksApi.md#tasksGetResourceGroupLevelTask) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName} | 
[**tasksGetSubscriptionLevelTask**](TasksApi.md#tasksGetSubscriptionLevelTask) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName} | 
[**tasksList**](TasksApi.md#tasksList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/tasks | 
[**tasksListByHomeRegion**](TasksApi.md#tasksListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks | 
[**tasksListByResourceGroup**](TasksApi.md#tasksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks | 
[**tasksUpdateResourceGroupLevelTaskState**](TasksApi.md#tasksUpdateResourceGroupLevelTaskState) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType} | 
[**tasksUpdateSubscriptionLevelTaskState**](TasksApi.md#tasksUpdateSubscriptionLevelTaskState) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/tasks/{taskName}/{taskUpdateActionType} | 



## tasksGetResourceGroupLevelTask

> SecurityTask tasksGetResourceGroupLevelTask(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let taskName = "taskName_example"; // String | Name of the task object, will be a GUID
apiInstance.tasksGetResourceGroupLevelTask(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **taskName** | **String**| Name of the task object, will be a GUID | 

### Return type

[**SecurityTask**](SecurityTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksGetSubscriptionLevelTask

> SecurityTask tasksGetSubscriptionLevelTask(apiVersion, subscriptionId, ascLocation, taskName)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let taskName = "taskName_example"; // String | Name of the task object, will be a GUID
apiInstance.tasksGetSubscriptionLevelTask(apiVersion, subscriptionId, ascLocation, taskName, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **taskName** | **String**| Name of the task object, will be a GUID | 

### Return type

[**SecurityTask**](SecurityTask.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksList

> SecurityTaskList tasksList(apiVersion, subscriptionId, opts)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let opts = {
  'filter': "filter_example" // String | OData filter. Optional.
};
apiInstance.tasksList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **filter** | **String**| OData filter. Optional. | [optional] 

### Return type

[**SecurityTaskList**](SecurityTaskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksListByHomeRegion

> SecurityTaskList tasksListByHomeRegion(apiVersion, subscriptionId, ascLocation, opts)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let opts = {
  'filter': "filter_example" // String | OData filter. Optional.
};
apiInstance.tasksListByHomeRegion(apiVersion, subscriptionId, ascLocation, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **filter** | **String**| OData filter. Optional. | [optional] 

### Return type

[**SecurityTaskList**](SecurityTaskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksListByResourceGroup

> SecurityTaskList tasksListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, ascLocation, opts)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let opts = {
  'filter': "filter_example" // String | OData filter. Optional.
};
apiInstance.tasksListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, ascLocation, opts, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **filter** | **String**| OData filter. Optional. | [optional] 

### Return type

[**SecurityTaskList**](SecurityTaskList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksUpdateResourceGroupLevelTaskState

> tasksUpdateResourceGroupLevelTaskState(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName, taskUpdateActionType)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let taskName = "taskName_example"; // String | Name of the task object, will be a GUID
let taskUpdateActionType = "taskUpdateActionType_example"; // String | Type of the action to do on the task
apiInstance.tasksUpdateResourceGroupLevelTaskState(apiVersion, subscriptionId, resourceGroupName, ascLocation, taskName, taskUpdateActionType, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **taskName** | **String**| Name of the task object, will be a GUID | 
 **taskUpdateActionType** | **String**| Type of the action to do on the task | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksUpdateSubscriptionLevelTaskState

> tasksUpdateSubscriptionLevelTaskState(apiVersion, subscriptionId, ascLocation, taskName, taskUpdateActionType)



Recommended tasks that will help improve the security of the subscription proactively

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.TasksApi();
let apiVersion = "apiVersion_example"; // String | API version for the operation
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let taskName = "taskName_example"; // String | Name of the task object, will be a GUID
let taskUpdateActionType = "taskUpdateActionType_example"; // String | Type of the action to do on the task
apiInstance.tasksUpdateSubscriptionLevelTaskState(apiVersion, subscriptionId, ascLocation, taskName, taskUpdateActionType, (error, data, response) => {
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
 **apiVersion** | **String**| API version for the operation | 
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **taskName** | **String**| Name of the task object, will be a GUID | 
 **taskUpdateActionType** | **String**| Type of the action to do on the task | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

