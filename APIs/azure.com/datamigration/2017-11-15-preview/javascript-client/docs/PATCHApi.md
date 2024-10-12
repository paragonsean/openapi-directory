# AzureDataMigrationServiceResourceProvider.PATCHApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsUpdate_1**](PATCHApi.md#projectsUpdate_1) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Update project
[**servicesUpdate_1**](PATCHApi.md#servicesUpdate_1) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Create or update DMS Service Instance
[**tasksUpdate_1**](PATCHApi.md#tasksUpdate_1) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName} | Create or update task



## projectsUpdate_1

> ProjectsGet200Response projectsUpdate_1(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters)

Update project

The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.PATCHApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
let parameters = new AzureDataMigrationServiceResourceProvider.ProjectsGet200Response(); // ProjectsGet200Response | Information about the project
apiInstance.projectsUpdate_1(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of the subscription | 
 **groupName** | **String**| Name of the resource group | 
 **serviceName** | **String**| Name of the service | 
 **projectName** | **String**| Name of the project | 
 **apiVersion** | **String**| Version of the API | 
 **parameters** | [**ProjectsGet200Response**](ProjectsGet200Response.md)| Information about the project | 

### Return type

[**ProjectsGet200Response**](ProjectsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesUpdate_1

> ServicesGet200Response servicesUpdate_1(subscriptionId, groupName, serviceName, apiVersion, parameters)

Create or update DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request (\&quot;ServiceIsBusy\&quot;).

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.PATCHApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
let parameters = new AzureDataMigrationServiceResourceProvider.ServicesGet200Response(); // ServicesGet200Response | Information about the service
apiInstance.servicesUpdate_1(subscriptionId, groupName, serviceName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of the subscription | 
 **groupName** | **String**| Name of the resource group | 
 **serviceName** | **String**| Name of the service | 
 **apiVersion** | **String**| Version of the API | 
 **parameters** | [**ServicesGet200Response**](ServicesGet200Response.md)| Information about the service | 

### Return type

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tasksUpdate_1

> TasksGet200Response tasksUpdate_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, parameters)

Create or update task

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The PATCH method updates an existing task, but since tasks have no mutable custom properties, there is little reason to do so.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.PATCHApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let taskName = "taskName_example"; // String | Name of the Task
let apiVersion = "apiVersion_example"; // String | Version of the API
let parameters = new AzureDataMigrationServiceResourceProvider.TasksGet200Response(); // TasksGet200Response | Information about the task
apiInstance.tasksUpdate_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of the subscription | 
 **groupName** | **String**| Name of the resource group | 
 **serviceName** | **String**| Name of the service | 
 **projectName** | **String**| Name of the project | 
 **taskName** | **String**| Name of the Task | 
 **apiVersion** | **String**| Version of the API | 
 **parameters** | [**TasksGet200Response**](TasksGet200Response.md)| Information about the task | 

### Return type

[**TasksGet200Response**](TasksGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

