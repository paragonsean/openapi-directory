# AzureDataMigrationServiceResourceProvider.ProjectResourceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projectsCreateOrUpdate**](ProjectResourceApi.md#projectsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Create or update project
[**projectsDelete**](ProjectResourceApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Delete project
[**projectsGet**](ProjectResourceApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Get project information
[**projectsList**](ProjectResourceApi.md#projectsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects | Get projects in a service
[**projectsUpdate**](ProjectResourceApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Update project



## projectsCreateOrUpdate

> ProjectsGet200Response projectsCreateOrUpdate(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters)

Create or update project

The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.ProjectResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
let parameters = new AzureDataMigrationServiceResourceProvider.ProjectsGet200Response(); // ProjectsGet200Response | Information about the project
apiInstance.projectsCreateOrUpdate(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters, (error, data, response) => {
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


## projectsDelete

> projectsDelete(subscriptionId, groupName, serviceName, projectName, apiVersion, opts)

Delete project

The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.ProjectResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
let opts = {
  'deleteRunningTasks': true // Boolean | Delete the resource even if it contains running tasks
};
apiInstance.projectsDelete(subscriptionId, groupName, serviceName, projectName, apiVersion, opts, (error, data, response) => {
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


## projectsGet

> ProjectsGet200Response projectsGet(subscriptionId, groupName, serviceName, projectName, apiVersion)

Get project information

The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.ProjectResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.projectsGet(subscriptionId, groupName, serviceName, projectName, apiVersion, (error, data, response) => {
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

### Return type

[**ProjectsGet200Response**](ProjectsGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsList

> ProjectsList200Response projectsList(subscriptionId, groupName, serviceName, apiVersion)

Get projects in a service

The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.ProjectResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.projectsList(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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

### Return type

[**ProjectsList200Response**](ProjectsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsUpdate

> ProjectsGet200Response projectsUpdate(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters)

Update project

The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.ProjectResourceApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
let parameters = new AzureDataMigrationServiceResourceProvider.ProjectsGet200Response(); // ProjectsGet200Response | Information about the project
apiInstance.projectsUpdate(subscriptionId, groupName, serviceName, projectName, apiVersion, parameters, (error, data, response) => {
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

