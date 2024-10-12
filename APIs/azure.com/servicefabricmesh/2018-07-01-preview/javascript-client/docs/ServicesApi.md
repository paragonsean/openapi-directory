# SeaBreezeManagementClient.ServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceGet**](ServicesApi.md#serviceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services/{serviceName} | Gets the properties of the service.
[**serviceListByApplicationName**](ServicesApi.md#serviceListByApplicationName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationName}/services | Gets services of a given application.



## serviceGet

> ServiceResourceDescription serviceGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName)

Gets the properties of the service.

The operation returns the properties of the service.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationName = "applicationName_example"; // String | The identity of the application.
let serviceName = "serviceName_example"; // String | The identity of the service.
apiInstance.serviceGet(subscriptionId, apiVersion, resourceGroupName, applicationName, serviceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationName** | **String**| The identity of the application. | 
 **serviceName** | **String**| The identity of the service. | 

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceListByApplicationName

> ServiceList serviceListByApplicationName(subscriptionId, apiVersion, resourceGroupName, applicationName)

Gets services of a given application.

Gets the information about all services of a given service of an application. The information includes the runtime properties of the service instance.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-07-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-07-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationName = "applicationName_example"; // String | The identity of the application.
apiInstance.serviceListByApplicationName(subscriptionId, apiVersion, resourceGroupName, applicationName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-07-01-preview&#x60;. | [default to &#39;2018-07-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationName** | **String**| The identity of the application. | 

### Return type

[**ServiceList**](ServiceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

