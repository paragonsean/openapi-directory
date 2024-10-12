# AzureMlWebServicesManagementClient.WebServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webServicesCreateOrUpdate**](WebServicesApi.md#webServicesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} | 
[**webServicesGet**](WebServicesApi.md#webServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} | 
[**webServicesList**](WebServicesApi.md#webServicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearning/webServices | 
[**webServicesListByResourceGroup**](WebServicesApi.md#webServicesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices | 
[**webServicesListKeys**](WebServicesApi.md#webServicesListKeys) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName}/listKeys | 
[**webServicesPatch**](WebServicesApi.md#webServicesPatch) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} | 
[**webServicesRemove**](WebServicesApi.md#webServicesRemove) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearning/webServices/{webServiceName} | 



## webServicesCreateOrUpdate

> WebService webServicesCreateOrUpdate(resourceGroupName, webServiceName, apiVersion, subscriptionId, createOrUpdatePayload)



Create or update a web service. This call will overwrite an existing web service. Note that there is no warning or confirmation. This is a nonrecoverable operation. If your intent is to create a new web service, call the Get operation first to verify that it does not exist.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
let webServiceName = "webServiceName_example"; // String | The name of the web service.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let createOrUpdatePayload = new AzureMlWebServicesManagementClient.WebService(); // WebService | The payload that is used to create or update the web service.
apiInstance.webServicesCreateOrUpdate(resourceGroupName, webServiceName, apiVersion, subscriptionId, createOrUpdatePayload, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | 
 **webServiceName** | **String**| The name of the web service. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **createOrUpdatePayload** | [**WebService**](WebService.md)| The payload that is used to create or update the web service. | 

### Return type

[**WebService**](WebService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## webServicesGet

> WebService webServicesGet(resourceGroupName, webServiceName, apiVersion, subscriptionId)



Gets the Web Service Definition as specified by a subscription, resource group, and name. Note that the storage credentials and web service keys are not returned by this call. To get the web service access keys, call List Keys.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
let webServiceName = "webServiceName_example"; // String | The name of the web service.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
apiInstance.webServicesGet(resourceGroupName, webServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | 
 **webServiceName** | **String**| The name of the web service. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 

### Return type

[**WebService**](WebService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webServicesList

> PaginatedWebServicesList webServicesList(apiVersion, subscriptionId, opts)



Gets the web services in the specified subscription.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.webServicesList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**PaginatedWebServicesList**](PaginatedWebServicesList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webServicesListByResourceGroup

> PaginatedWebServicesList webServicesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Gets the web services in the specified resource group.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let opts = {
  'skiptoken': "skiptoken_example" // String | Continuation token for pagination.
};
apiInstance.webServicesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **skiptoken** | **String**| Continuation token for pagination. | [optional] 

### Return type

[**PaginatedWebServicesList**](PaginatedWebServicesList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webServicesListKeys

> WebServiceKeys webServicesListKeys(resourceGroupName, webServiceName, apiVersion, subscriptionId)



Gets the access keys for the specified web service.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
let webServiceName = "webServiceName_example"; // String | The name of the web service.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
apiInstance.webServicesListKeys(resourceGroupName, webServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | 
 **webServiceName** | **String**| The name of the web service. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 

### Return type

[**WebServiceKeys**](WebServiceKeys.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## webServicesPatch

> WebService webServicesPatch(resourceGroupName, webServiceName, apiVersion, subscriptionId, patchPayload)



Modifies an existing web service resource. The PATCH API call is an asynchronous operation. To determine whether it has completed successfully, you must perform a Get operation.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
let webServiceName = "webServiceName_example"; // String | The name of the web service.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let patchPayload = new AzureMlWebServicesManagementClient.WebService(); // WebService | The payload to use to patch the web service.
apiInstance.webServicesPatch(resourceGroupName, webServiceName, apiVersion, subscriptionId, patchPayload, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | 
 **webServiceName** | **String**| The name of the web service. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **patchPayload** | [**WebService**](WebService.md)| The payload to use to patch the web service. | 

### Return type

[**WebService**](WebService.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## webServicesRemove

> webServicesRemove(resourceGroupName, webServiceName, apiVersion, subscriptionId)



Deletes the specified web service.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.WebServicesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group in which the web service is located.
let webServiceName = "webServiceName_example"; // String | The name of the web service.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
apiInstance.webServicesRemove(resourceGroupName, webServiceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group in which the web service is located. | 
 **webServiceName** | **String**| The name of the web service. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

