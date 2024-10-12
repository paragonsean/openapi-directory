# ApiManagementClient.DiagnosticLoggersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticLoggerCheckEntityExists**](DiagnosticLoggersApi.md#diagnosticLoggerCheckEntityExists) | **HEAD** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers/{loggerid} | 
[**diagnosticLoggerCreateOrUpdate**](DiagnosticLoggersApi.md#diagnosticLoggerCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers/{loggerid} | 
[**diagnosticLoggerDelete**](DiagnosticLoggersApi.md#diagnosticLoggerDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers/{loggerid} | 
[**diagnosticLoggerListByService**](DiagnosticLoggersApi.md#diagnosticLoggerListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/diagnostics/{diagnosticId}/loggers | 



## diagnosticLoggerCheckEntityExists

> diagnosticLoggerCheckEntityExists(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId)



Checks that logger entity specified by identifier is associated with the diagnostics entity.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.DiagnosticLoggersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
let loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.diagnosticLoggerCheckEntityExists(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | 
 **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticLoggerCreateOrUpdate

> DiagnosticLoggerCreateOrUpdate200Response diagnosticLoggerCreateOrUpdate(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId)



Attaches a logger to a diagnostic.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.DiagnosticLoggersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
let loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.diagnosticLoggerCreateOrUpdate(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | 
 **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DiagnosticLoggerCreateOrUpdate200Response**](DiagnosticLoggerCreateOrUpdate200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticLoggerDelete

> diagnosticLoggerDelete(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId)



Deletes the specified Logger from Diagnostic.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.DiagnosticLoggersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
let loggerid = "loggerid_example"; // String | Logger identifier. Must be unique in the API Management service instance.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.diagnosticLoggerDelete(resourceGroupName, serviceName, diagnosticId, loggerid, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | 
 **loggerid** | **String**| Logger identifier. Must be unique in the API Management service instance. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticLoggerListByService

> DiagnosticLoggerListByService200Response diagnosticLoggerListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, diagnosticId, opts)



Lists all loggers associated with the specified Diagnostic of the API Management service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.DiagnosticLoggersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let diagnosticId = "diagnosticId_example"; // String | Diagnostic identifier. Must be unique in the current API Management service instance.
let opts = {
  'filter': "filter_example", // String | | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   |
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.diagnosticLoggerListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, diagnosticId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **diagnosticId** | **String**| Diagnostic identifier. Must be unique in the current API Management service instance. | 
 **filter** | **String**| | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | type        | eq                     |                                   | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**DiagnosticLoggerListByService200Response**](DiagnosticLoggerListByService200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

