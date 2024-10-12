# AzureDataMigrationServiceResourceProvider.GETApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList_0**](GETApi.md#operationsList_0) | **GET** /providers/Microsoft.DataMigration/operations | Get available resource provider actions (operations)
[**projectsGet_1**](GETApi.md#projectsGet_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName} | Get project information
[**projectsList_1**](GETApi.md#projectsList_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects | Get projects in a service
[**resourceSkusListSkus_0**](GETApi.md#resourceSkusListSkus_0) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/skus | Get supported SKUs
[**servicesGet_1**](GETApi.md#servicesGet_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName} | Get DMS Service Instance
[**servicesListByResourceGroup_1**](GETApi.md#servicesListByResourceGroup_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services | Get services in resource group
[**servicesListSkus_1**](GETApi.md#servicesListSkus_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/skus | Get compatible SKUs
[**servicesList_1**](GETApi.md#servicesList_1) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/services | Get services in subscription
[**tasksGet_1**](GETApi.md#tasksGet_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName} | Get task information
[**tasksList_1**](GETApi.md#tasksList_1) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks | Get tasks in a service
[**usagesList_0**](GETApi.md#usagesList_0) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/locations/{location}/usages | Get resource quotas and usage information



## operationsList_0

> OperationsList200Response operationsList_0(apiVersion)

Get available resource provider actions (operations)

Lists all available actions exposed by the Data Migration Service resource provider.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.operationsList_0(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API | 

### Return type

[**OperationsList200Response**](OperationsList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGet_1

> ProjectsGet200Response projectsGet_1(subscriptionId, groupName, serviceName, projectName, apiVersion)

Get project information

The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.projectsGet_1(subscriptionId, groupName, serviceName, projectName, apiVersion, (error, data, response) => {
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


## projectsList_1

> ProjectsList200Response projectsList_1(subscriptionId, groupName, serviceName, apiVersion)

Get projects in a service

The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.projectsList_1(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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


## resourceSkusListSkus_0

> ResourceSkusListSkus200Response resourceSkusListSkus_0(subscriptionId, apiVersion)

Get supported SKUs

The skus action returns the list of SKUs that DMS supports.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.resourceSkusListSkus_0(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API | 

### Return type

[**ResourceSkusListSkus200Response**](ResourceSkusListSkus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGet_1

> ServicesGet200Response servicesGet_1(subscriptionId, groupName, serviceName, apiVersion)

Get DMS Service Instance

The services resource is the top-level resource that represents the Data Migration Service. The GET method retrieves information about a service instance.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesGet_1(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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

[**ServicesGet200Response**](ServicesGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListByResourceGroup_1

> ServicesList200Response servicesListByResourceGroup_1(subscriptionId, groupName, apiVersion)

Get services in resource group

The Services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a resource group.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesListByResourceGroup_1(subscriptionId, groupName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API | 

### Return type

[**ServicesList200Response**](ServicesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListSkus_1

> ServicesListSkus200Response servicesListSkus_1(subscriptionId, groupName, serviceName, apiVersion)

Get compatible SKUs

The services resource is the top-level resource that represents the Data Migration Service. The skus action returns the list of SKUs that a service resource can be updated to.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesListSkus_1(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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

[**ServicesListSkus200Response**](ServicesListSkus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesList_1

> ServicesList200Response servicesList_1(subscriptionId, apiVersion)

Get services in subscription

The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of service resources in a subscription.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesList_1(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API | 

### Return type

[**ServicesList200Response**](ServicesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksGet_1

> TasksGet200Response tasksGet_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, opts)

Get task information

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. The GET method retrieves information about a task.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let taskName = "taskName_example"; // String | Name of the Task
let apiVersion = "apiVersion_example"; // String | Version of the API
let opts = {
  'expand': "expand_example" // String | Expand the response
};
apiInstance.tasksGet_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| Expand the response | [optional] 

### Return type

[**TasksGet200Response**](TasksGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksList_1

> TasksList200Response tasksList_1(subscriptionId, groupName, serviceName, projectName, apiVersion, opts)

Get tasks in a service

The services resource is the top-level resource that represents the Data Migration Service. This method returns a list of tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let apiVersion = "apiVersion_example"; // String | Version of the API
let opts = {
  'taskType': "taskType_example" // String | Filter tasks by task type
};
apiInstance.tasksList_1(subscriptionId, groupName, serviceName, projectName, apiVersion, opts, (error, data, response) => {
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
 **taskType** | **String**| Filter tasks by task type | [optional] 

### Return type

[**TasksList200Response**](TasksList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usagesList_0

> UsagesList200Response usagesList_0(subscriptionId, location, apiVersion)

Get resource quotas and usage information

This method returns region-specific quotas and resource usage information for the Data Migration Service.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.GETApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let location = "location_example"; // String | The Azure region of the operation
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.usagesList_0(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **location** | **String**| The Azure region of the operation | 
 **apiVersion** | **String**| Version of the API | 

### Return type

[**UsagesList200Response**](UsagesList200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

