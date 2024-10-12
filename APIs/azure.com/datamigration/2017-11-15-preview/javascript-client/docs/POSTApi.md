# AzureDataMigrationServiceResourceProvider.POSTApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesCheckChildrenNameAvailability_0**](POSTApi.md#servicesCheckChildrenNameAvailability_0) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/checkNameAvailability | Check nested resource name validity and availability
[**servicesCheckNameAvailability_0**](POSTApi.md#servicesCheckNameAvailability_0) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataMigration/locations/{location}/checkNameAvailability | Check name validity and availability
[**servicesCheckStatus_1**](POSTApi.md#servicesCheckStatus_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/checkStatus | Check service health status
[**servicesStart_1**](POSTApi.md#servicesStart_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/start | Start service
[**servicesStop_1**](POSTApi.md#servicesStop_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/stop | Stop service
[**tasksCancel_1**](POSTApi.md#tasksCancel_1) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}/cancel | Cancel a task



## servicesCheckChildrenNameAvailability_0

> ServicesCheckNameAvailability200Response servicesCheckChildrenNameAvailability_0(subscriptionId, groupName, apiVersion, serviceName, parameters)

Check nested resource name validity and availability

This method checks whether a proposed nested resource name is valid and available.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let apiVersion = "apiVersion_example"; // String | Version of the API
let serviceName = "serviceName_example"; // String | Name of the service
let parameters = new AzureDataMigrationServiceResourceProvider.ServicesCheckNameAvailabilityRequest(); // ServicesCheckNameAvailabilityRequest | Requested name to validate
apiInstance.servicesCheckChildrenNameAvailability_0(subscriptionId, groupName, apiVersion, serviceName, parameters, (error, data, response) => {
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
 **serviceName** | **String**| Name of the service | 
 **parameters** | [**ServicesCheckNameAvailabilityRequest**](ServicesCheckNameAvailabilityRequest.md)| Requested name to validate | 

### Return type

[**ServicesCheckNameAvailability200Response**](ServicesCheckNameAvailability200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesCheckNameAvailability_0

> ServicesCheckNameAvailability200Response servicesCheckNameAvailability_0(subscriptionId, apiVersion, location, parameters)

Check name validity and availability

This method checks whether a proposed top-level resource name is valid and available.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let apiVersion = "apiVersion_example"; // String | Version of the API
let location = "location_example"; // String | The Azure region of the operation
let parameters = new AzureDataMigrationServiceResourceProvider.ServicesCheckNameAvailabilityRequest(); // ServicesCheckNameAvailabilityRequest | Requested name to validate
apiInstance.servicesCheckNameAvailability_0(subscriptionId, apiVersion, location, parameters, (error, data, response) => {
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
 **location** | **String**| The Azure region of the operation | 
 **parameters** | [**ServicesCheckNameAvailabilityRequest**](ServicesCheckNameAvailabilityRequest.md)| Requested name to validate | 

### Return type

[**ServicesCheckNameAvailability200Response**](ServicesCheckNameAvailability200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesCheckStatus_1

> ServicesCheckStatus200Response servicesCheckStatus_1(subscriptionId, groupName, serviceName, apiVersion)

Check service health status

The services resource is the top-level resource that represents the Data Migration Service. This action performs a health check and returns the status of the service and virtual machine size.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesCheckStatus_1(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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

[**ServicesCheckStatus200Response**](ServicesCheckStatus200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesStart_1

> servicesStart_1(subscriptionId, groupName, serviceName, apiVersion)

Start service

The services resource is the top-level resource that represents the Data Migration Service. This action starts the service and the service can be used for data migration.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesStart_1(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesStop_1

> servicesStop_1(subscriptionId, groupName, serviceName, apiVersion)

Stop service

The services resource is the top-level resource that represents the Data Migration Service. This action stops the service and the service cannot be used for data migration. The service owner won&#39;t be billed when the service is stopped.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.servicesStop_1(subscriptionId, groupName, serviceName, apiVersion, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tasksCancel_1

> TasksGet200Response tasksCancel_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion)

Cancel a task

The tasks resource is a nested, proxy-only resource representing work performed by a DMS instance. This method cancels a task if it&#39;s currently queued or running.

### Example

```javascript
import AzureDataMigrationServiceResourceProvider from 'azure_data_migration_service_resource_provider';
let defaultClient = AzureDataMigrationServiceResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDataMigrationServiceResourceProvider.POSTApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of the subscription
let groupName = "groupName_example"; // String | Name of the resource group
let serviceName = "serviceName_example"; // String | Name of the service
let projectName = "projectName_example"; // String | Name of the project
let taskName = "taskName_example"; // String | Name of the Task
let apiVersion = "apiVersion_example"; // String | Version of the API
apiInstance.tasksCancel_1(subscriptionId, groupName, serviceName, projectName, taskName, apiVersion, (error, data, response) => {
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

### Return type

[**TasksGet200Response**](TasksGet200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

