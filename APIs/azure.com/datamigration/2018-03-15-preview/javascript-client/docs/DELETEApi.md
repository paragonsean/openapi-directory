# AzureDataMigrationServiceResourceProvider.DELETEApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsDelete_1**](DELETEApi.md#projectsDelete_1) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Delete project
[**servicesDelete_1**](DELETEApi.md#servicesDelete_1) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Delete DMS Service Instance
[**tasksDelete_1**](DELETEApi.md#tasksDelete_1) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName} | Delete task



## projectsDelete_1

> projectsDelete_1(subscriptionId, groupName, serviceName, projectName, apiVersion, opts)

Delete project

The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.DELETEApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
let opts = {
  'deleteRunningTasks': true // Boolean | Delete the resource even if it contains running tasks
};
apiInstance.projectsDelete_1(subscriptionId, groupName, serviceName, projectName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of the subscription | 
 **groupName** | **String**| Name of the resource group | 
 **serviceName** | **String**| Name of the service | 
 **projectName** | **String**| Name of the project | 
 **apiVersion** | **String**| Version of the API | 
 **deleteRunningTasks** | **Boolean**| Delete the resource even if it contains running tasks | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesDelete_1

> servicesDelete_1(subscriptionId, groupName, serviceName, apiVersion, opts)

Delete DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The DELETE method deletes a service. Any running tasks will be canceled.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.DELETEApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
let opts = {
  'deleteRunningTasks': true // Boolean | Delete the resource even if it contains running tasks
};
apiInstance.servicesDelete_1(subscriptionId, groupName, serviceName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of the subscription | 
 **groupName** | **String**| Name of the resource group | 
 **serviceName** | **String**| Name of the service | 
 **apiVersion** | **String**| Version of the API | 
 **deleteRunningTasks** | **Boolean**| Delete the resource even if it contains running tasks | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksDelete_1

> tasksDelete_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, opts)

Delete task

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The DELETE method deletes a task, canceling it first if it&#39;s running.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.DELETEApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let taskName = "taskName_example"; // String | Name of the Task
let apiVersion = "apiVersion_example"; // String | Version of the API
let opts = {
  'deleteRunningTasks': true // Boolean | Delete the resource even if it contains running tasks
};
apiInstance.tasksDelete_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of the subscription | 
 **groupName** | **String**| Name of the resource group | 
 **serviceName** | **String**| Name of the service | 
 **projectName** | **String**| Name of the project | 
 **taskName** | **String**| Name of the Task | 
 **apiVersion** | **String**| Version of the API | 
 **deleteRunningTasks** | **Boolean**| Delete the resource even if it contains running tasks | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

